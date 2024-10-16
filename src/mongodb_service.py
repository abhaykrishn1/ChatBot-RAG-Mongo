import pymongo
from config import MONGO_URI, DATABASE_NAME


def get_mongo_client():
    """
    Returns a MongoDB client.
    """
    return pymongo.MongoClient(MONGO_URI)

def fetch_data_from_collection(db_name, collection_name, batch_size, skip=0):
    """
    Fetches documents from a MongoDB collection in batch
    """
    client = get_mongo_client()
    db = client[db_name]
    collection = db[collection_name]
    data = collection.find().skip(skip).limit(batch_size)
    return list(data)

def update_document_with_embedding(db_name, collection_name, document_id, embedding):
    """
    Update the document with the given embedding in the collection
    """
    client = get_mongo_client()
    db = client[db_name]
    collection = db[collection_name]
    collection.update_one({"_id": document_id}, {"$set": {"embedded_msg_preview": embedding}})
