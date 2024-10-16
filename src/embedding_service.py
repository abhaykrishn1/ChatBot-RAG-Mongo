import requests
import json
from config import AZURE_API_URL, AZURE_API_KEY

headers = {
    "Content-Type": "application/json",
    "api-key": AZURE_API_KEY,
}

def get_embedding_from_azure(content_preview):
    """
    Sends content to Azure API to retrieve the embedding.
    """
    payload = {
        "input": content_preview
    }

    response = requests.post(AZURE_API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()["data"][0]["embedding"]
    else:
        raise Exception(f"Azure API failed with status code {response.status_code}: {response.text}")
    
def embed_data_batch(data_batch):
    """
    Embeds a batch of documents using the Azure API.
    """
    embeddings = []
    for item in data_batch:
        content_preview = item.get("content_preview", "")
        if content_preview:
            embedding = get_embedding_from_azure(content_preview)
            embeddings.append((item["_id"], embedding))
    return embeddings
