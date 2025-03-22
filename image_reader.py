from PIL import Image
import pytesseract
import cv2
import numpy as np
from pathlib import Path
from pdf2image import convert_from_path
from IPython.display import display

# Set Tesseract Path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Take user input for file path
file_path = Path(input("Enter the image or PDF file path: ").strip())

def process_image(image):
    """Process and perform OCR on a single image."""
    display(image)

    # Convert to grayscale
    img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    img_new = Image.fromarray(img_cv)
    display(img_new)

    # Perform OCR
    ocr_text = pytesseract.image_to_string(image)
    print("\nOCR result from the original image:")
    print(ocr_text)

    ocr_text_processed = pytesseract.image_to_string(img_new)
    print("\nOCR result from the processed (grayscale) image:")
    print(ocr_text_processed)

if file_path.exists():
    if file_path.suffix.lower() in [".png", ".jpg", ".jpeg", ".bmp", ".tiff"]:
        # Process image files directly
        img_original = Image.open(file_path)
        process_image(img_original)

    elif file_path.suffix.lower() == ".pdf":
        # Convert PDF to images
        pages = convert_from_path(str(file_path))
        print(f"PDF contains {len(pages)} pages. Processing each page...\n")

        for i, page in enumerate(pages):
            print(f"\n--- Processing Page {i+1} ---")
            process_image(page)

    else:
        print("Unsupported file format! Please use an image (.png, .jpg) or PDF (.pdf).")
else:
    print(f"Error: File not found at '{file_path}'")
