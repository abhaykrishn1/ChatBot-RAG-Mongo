from mongodb_service import fetch_data_from_collection, update_document_with_embedding
from embedding_service import embed_data_batch
from config import BATCH_SIZE

def process_batches_for_old_data():
    """
    Process older data in the car_dealership_content_preview_sample collection in batches.
    """
    collection_name = "car_dealership_content_preview_sample"
    db_name = "cox_comm_sample"
    skip = 0
    while True:
        # Fetch batch of documents from the collection
        data_batch = fetch_data_from_collection(db_name, collection_name, BATCH_SIZE, skip)
        if not data_batch:
            break
        
        # Embed the content preview for the batch
        embeddings = embed_data_batch(data_batch)
        
        # Update MongoDB with the new embeddings
        for document_id, embedding in embeddings:
            update_document_with_embedding(db_name, collection_name, document_id, embedding)
        
        skip += BATCH_SIZE
        print(f"Processed {skip} records...")
