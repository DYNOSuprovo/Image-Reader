# OCR Image Processing with Tesseract and OpenCV

## Overview

This project utilizes **Tesseract OCR** and **OpenCV** to extract text from images. It processes an image in both its original and grayscale forms to improve text recognition accuracy.

## Features

- Reads an image (`image.png`) and displays it.
- Converts the image to grayscale for better OCR results.
- Extracts text from both the original and processed images using Tesseract OCR.

## Requirements

Make sure you have the following installed:

### **Python Packages**

Install dependencies using:

```bash
pip install pytesseract opencv-python numpy matplotlib pillow
```

### **Tesseract OCR**

#### **Windows**:

1. Download and install Tesseract from [this link](https://github.com/UB-Mannheim/tesseract/wiki).
2. Ensure Tesseract is added to your system PATH (usually `C:\Program Files\Tesseract-OCR\tesseract.exe`).

#### **Linux (Ubuntu/Debian)**:

```bash
sudo apt install tesseract-ocr -y
```

#### **macOS**:

```bash
brew install tesseract
```

## Usage

1. Place your image file (`image.png`) in the project directory.
2. Run the script:
   ```bash
   python script.py
   ```
3. The extracted text will be printed in the terminal.

## Expected Output

```plaintext
OCR result from the original image:
[Extracted text]

OCR result from the processed (grayscale) image:
[Improved extracted text]
```

## Notes

- If OCR output is inaccurate, try improving image quality or applying additional preprocessing techniques like thresholding.
- For mathematical notations, consider using `tessdata_best` trained models from [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tessdata_best).

## License

This project is open-source

