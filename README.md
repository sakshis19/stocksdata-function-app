# 📊 End-to-End Stock Data Ingestion Pipeline

This project demonstrates a robust, automated pipeline for fetching historical stock data for multiple tickers and storing it efficiently in Azure Blob Storage. It showcases skills in data ingestion, cloud storage, serverless computing, and Continuous Integration/Continuous Deployment (CI/CD).

---

## 🚀 Project Overview

An end-to-end system to:

- 🔎 Fetch historical stock data using `yfinance`
- ⚙️ Process and store it in Azure Blob Storage
- 🧠 Deploy using Azure Function App (Python V2)
- 🔁 Automate deployment with GitHub Actions

---

## 🔧 Key Features & Components

### 📈 Stock Data Acquisition
- Utilizes the `yfinance` library to reliably fetch daily historical stock data for a given set of ticker symbols.

### ⚙️ Serverless Processing
- An Azure Function (Python V2 Programming Model) serves as the core compute unit.
- Triggered via HTTP requests to process ticker symbols, retrieve data, and handle storage operations.

### ☁️ Scalable Cloud Storage
- Integrated with Azure Blob Storage for persistent and scalable storage.
- Data is organized into folders by ticker symbol:
  ```
  stock-data/MSFT/MSFT_20250724_114451.csv
  ```

### 🔁 Automated Deployment (CI/CD)
- GitHub Actions automates build and deployment.
- Every push to the `main` branch triggers the workflow to deploy the latest version to Azure.

---

## 🧰 Technologies Used

| Category       | Tools/Technologies                              |
|----------------|--------------------------------------------------|
| Language       | Python 3.12                                      |
| Serverless     | Azure Functions (V4 Runtime, Python V2 Model)    |
| Storage        | Azure Blob Storage                               |
| Libraries      | yfinance, pandas, azure-functions, azure-storage-blob |
| CI/CD          | GitHub Actions                                   |

---

## 📁 Project Structure

```
.
├── .github/
│   └── workflows/
│       └── main_stocksdatafunction.yml  # GitHub Actions workflow for CI/CD
├── .vscode/             # VS Code settings (optional)
├── venv/                # Python Virtual Environment (excluded from deployment)
├── function_app.py      # Main Azure Function application code
├── host.json            # Azure Functions host configuration
├── local.settings.json  # Local settings for development (sensitive info)
├── requirements.txt     # Python dependencies
├── tickers.txt          # List of stock tickers for local batch processing
└── README.md            # This README file
```

---

## 💻 How to Run Locally (Batch Processing)

You can run the data ingestion logic locally to fetch data for multiple stocks and upload them directly to Azure Blob Storage.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/sakshis19/stocksdata-function-app.git
cd stocksdata-function-app
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Prepare `tickers.txt`
Create a file named `tickers.txt` in the root directory.  
List each stock ticker on a new line:
```
MSFT
GOOG
AAPL
```

### 6️⃣ Configure Azure Storage Connection String

Open `function_app.py` and locate:
```python
os.environ["AzureWebJobsStorage"] = "YOUR_AZURE_STORAGE_CONNECTION_STRING"
```

Replace `"YOUR_AZURE_STORAGE_CONNECTION_STRING"` with your actual connection string from the Azure Portal.

### 7️⃣ Run the Script
```bash
python function_app.py
```

✅ The script will log progress to the console, and new CSV files will appear in your Azure Blob Storage container.

---

## ☁️ Deployment to Azure

### 🔧 Azure Setup

- Azure Function App (Consumption Plan, Python 3.12, Linux)
- Azure Storage Account
- App Setting: `AzureWebJobsStorage` with your connection string
- GitHub Secret: `AZUREAPPSERVICE_PUBLISHPROFILE_...`

### 🚀 GitHub Actions Workflow

**Path:** `.github/workflows/main_stocksdatafunction.yml`

**Workflow Steps:**

1. ✅ Checkout the code  
2. 🐍 Set up Python  
3. 📦 Install dependencies  
4. 🗜️ Zip the application (excluding `venv`, `.git`, etc.)  
5. 🚀 Deploy to Azure Function App

---

## 🔮 Future Enhancements

- ⏱️ Add timer trigger to fetch data on a daily schedule
- ❌ Add error handling for invalid ticker symbols
- 🔐 Integrate Azure Key Vault for secret management
- 🧹 Add data validation and transformation logic
- 📈 Enable Azure Monitor & Application Insights
- 🔄 Dynamically fetch tickers from a DB or external API

---

## 🙋‍♀️ Author

**Sakshi Shastri**  
📧 sakshishastri72@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/sakshi-shastri)

---

## 🏷️ Tags

`#Azure` `#AzureFunctions` `#GitHubActions` `#CI/CD` `#Python`  
`#BlobStorage` `#Serverless` `#yfinance` `#Automation` `#DataEngineering`
```
