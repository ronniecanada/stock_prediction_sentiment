import os
from azure.storage.blob import BlobServiceClient

# === CONFIGURATION ===
ticker = "AAPL"
local_file = f"{ticker}_news_sentiment.csv"

# Replace below with your actual connection string
connect_str = "DefaultEndpointsProtocol=https;AccountName=aidiml11373989641;AccountKey=I4NXkqAe84FrICTcG7R6+dvKS1hjNjFhoKU3qpf7bLsP/hx0cjW/QyerOWusi9EHbV89sZCjY33v+AStPJISIg==;EndpointSuffix=core.windows.net"
container_name = "sentimentdata"
blob_name = f"{ticker}_sentiment/{local_file}"

# === VALIDATION ===
if not os.path.exists(local_file):
    raise FileNotFoundError(f"❌ File not found: {local_file}")

# === UPLOAD LOGIC ===
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

with open(local_file, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print(f"✅ Uploaded to Azure Blob Storage: {blob_name}")