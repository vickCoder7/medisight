import re

def clean_text(raw_text: str) -> str:
    """
    Preprocesses the raw text by removing unwanted characters and normalizing whitespace.

    Args:
        raw_text (str): The raw text to preprocess.

    Returns:
        str: The preprocessed text.
    """
    # Remove non-printable characters
    cleaned_text = re.sub(r'[^\x20-\x7E]', ' ', raw_text)
    
    # Normalize whitespace (replace multiple spaces with a single space)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text