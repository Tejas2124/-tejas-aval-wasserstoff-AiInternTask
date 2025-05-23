import fitz  # PyMuPDF
from pdf2image import convert_from_bytes
import pytesseract
from pdf2image import convert_from_path
from pytesseract import image_to_string
import pdfplumber

def extract_text_from_pdf_bytes(pdf_bytes):
    try:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        full_text = ""
        for page in doc:
            text = page.get_text()
            full_text += text
        if full_text.strip():
            return full_text
    except Exception:
        pass
    # fallback to OCR
    images = convert_from_bytes(pdf_bytes)
    ocr_text = ""
    for image in images:
        ocr_text += pytesseract.image_to_string(image)
    return ocr_text