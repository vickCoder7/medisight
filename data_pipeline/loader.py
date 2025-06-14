import os
from fastapi import UploadFile, HTTPException

supported_extensions = ('.pdf', '.jpg', '.jpeg', '.png')

def validate_file(uploaded_file: UploadFile) -> str:
    """
    Validate the uploaded file's extension.
    """
    if not uploaded_file.filename.lower().endswith(supported_extensions):
        raise HTTPException(status_code=400, detail="Unsupported file type.")
    
    return uploaded_file.filename

def save_file(uploaded_file: UploadFile, save_dir: str) -> str:
    """
    Save the uploaded file to the specified directory.
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    file_path = os.path.join(save_dir, uploaded_file.filename)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.file.read())
    
    return file_path