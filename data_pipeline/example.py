from loader import validate_file, save_file
from ocr import extract_text_from_image, extract_text_from_pdf
from preprocess import clean_text

def process_file(uploaded_file, save_dir="uploads"):
    """
    Process the uploaded file: validate, save, extract text, and clean it.
    
    Args:
        uploaded_file: The file uploaded by the user.
        save_dir: Directory where the file will be saved.
    
    Returns:
        str: The cleaned text extracted from the file.
    """
    # Validate the file
    filename = validate_file(uploaded_file)
    
    # Save the file
    file_path = save_file(uploaded_file, save_dir)
    
    # Extract text based on file type
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        raw_text = extract_text_from_image(file_path)
    elif filename.lower().endswith('.pdf'):
        raw_text = extract_text_from_pdf(file_path)
    else:
        raise ValueError("Unsupported file type.")
    
    # Clean the extracted text
    cleaned_text = clean_text(raw_text)
    
    return cleaned_text

with open("../SampleHealthReport.pdf", "rb") as file:
    class MockFile:
        filename = "SampleHealthReport.pdf"
        file = file

    processed_text = process_file(MockFile())
    print(processed_text)