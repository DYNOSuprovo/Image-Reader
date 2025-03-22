from PIL import Image
import pytesseract
import cv2
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path
from IPython.display import display


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_path = Path("image.png")

if image_path.exists():
    img_original = Image.open(image_path)
    display(img_original)

    img_cv = cv2.imread(str(image_path))
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    img_new = Image.fromarray(gray)
    display(img_new)

    ocr_text = pytesseract.image_to_string(img_original)
    print("OCR result from the original image:")
    print(ocr_text)

    ocr_text_processed = pytesseract.image_to_string(Image.fromarray(gray))
    print("\nOCR result from the processed (grayscale) image:")
    print(ocr_text_processed)
else:
    print(f"Image not found: {image_path}")
