import logging
import azure.functions as func
import yfinance as yf
from azure.storage.blob import BlobServiceClient
import os
import pandas as pd
from datetime import datetime

# Use the new Python programming model V2
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="stocksdata")
def stocksdata(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    ticker = req.params.get('ticker')
    if not ticker:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            ticker = req_body.get('ticker')

    if ticker:
        try:
            # Fetch data
            stock = yf.Ticker(ticker)
            # Fetch last 1 month of data
            hist = stock.history(period="1mo")

            if hist.empty:
                return func.HttpResponse(
                    f"Could not fetch data for ticker: {ticker}. It might be invalid or no data available.",
                    status_code=400
                )

            # Convert to CSV string, including the index (Date)
            csv_data = hist.to_csv(index=True)

            # Get connection string from application settings
            # Using os.environ.get is safer as it won't raise KeyError if not found
            connect_str = os.environ.get("AzureWebJobsStorage")
            if not connect_str:
                logging.error("AzureWebJobsStorage environment variable not set.")
                return func.HttpResponse(
                    "Azure Storage connection string is missing from application settings.",
                    status_code=500
                )

            blob_service_client = BlobServiceClient.from_connection_string(connect_str)
            container_name = "stock-data" # Ensure this container exists in your storage account
            
            # Create the container if it doesn't exist
            try:
                container_client = blob_service_client.get_container_client(container_name)
                if not container_client.exists():
                    container_client.create_container()
                    logging.info(f"Container '{container_name}' created.")
            except Exception as e:
                logging.error(f"Error checking/creating container '{container_name}': {e}")
                # This error might prevent function from working, so return 500
                return func.HttpResponse(
                    f"Failed to ensure storage container exists: {e}",
                    status_code=500
                )

            # Define blob path: ticker/ticker_YYYYMMDD_HHMMSS.csv
            blob_name = f"{ticker}/{ticker}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

            blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
            blob_client.upload_blob(csv_data, overwrite=True)
            logging.info(f"Successfully uploaded {blob_name} to blob storage.")

            return func.HttpResponse(
                f"Successfully fetched and uploaded data for {ticker} to blob storage.",
                status_code=200
            )
        except Exception as e:
            logging.error(f"An unexpected error occurred for ticker {ticker}: {e}", exc_info=True)
            # Return a generic 500 error to the client, details logged internally
            return func.HttpResponse(
                f"An internal server error occurred. Please check function logs for details.",
                status_code=500
            )
    else:
        return func.HttpResponse(
            "Please pass a 'ticker' in the query string or in the request body.",
            status_code=400
        )