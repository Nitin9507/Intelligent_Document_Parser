from fastapi import APIRouter, File, UploadFile, HTTPException
from app.utils.process_documents import process_pdf
from app.services.extraction import extract_data
import os 


router = APIRouter()

# Define the directory where files will be saved
UPLOAD_DIR = "uploaded_pdfs"

# Ensure the directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF")

    # Save the uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Process the saved file
    text =  process_pdf(file_path)
    extracted_data =  extract_data(text)
    return extracted_data
