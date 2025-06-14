from PIL import Image
import pytesseract
import pdfplumber

def extract_text_from_image(image_path: str) -> str:
    """
    Extracts text from an image using Tesseract OCR.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The extracted text.
    """
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Use pytesseract to do OCR on the image
            text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error processing image: {e}"
    
def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts text from a PDF file using pdfplumber.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text.
    """
    try:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error processing PDF: {e}"