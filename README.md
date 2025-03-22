# Image-Reader

## Overview
Image-Reader is a web-based Optical Character Recognition (OCR) tool that extracts text from images using **Tesseract OCR** and **OpenCV**. It provides a simple and interactive interface to upload images and retrieve their textual content.

## Features
- 🖼️ **Upload Images**: Users can upload images to extract text.
- 📄 **OCR Extraction**: Uses Tesseract OCR to process images and extract text.
- 🌐 **Web Interface**: Built with Flask, HTML, and CSS for a smooth user experience.
- 🔄 **Preprocessing**: Utilizes OpenCV for image enhancements to improve OCR accuracy.
- 📂 **Secure File Handling**: Supports multiple image formats with size constraints.

## Tech Stack
- **Backend**: Flask, Python
- **OCR Engine**: Tesseract OCR, OpenCV
- **Frontend**: HTML, CSS

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/DYNOSuprovo/Image-Reader.git
   cd Image-Reader
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install Tesseract OCR:
   - **Windows**: Download and install from [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
   - **Linux/macOS**:
     ```bash
     sudo apt install tesseract-ocr  # Ubuntu
     brew install tesseract  # macOS
     ```

## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```
3. Upload an image and view the extracted text.

## Project Structure
```
Image-Reader/
│── static/        # CSS & assets
│── templates/     # HTML files
│── uploads/       # Uploaded images
│── app.py         # Main Flask application
│── requirements.txt  # Dependencies
│── README.md      # Project documentation
```

## Future Improvements
- ✅ Improve text extraction accuracy using image pre-processing techniques.
- ✅ Implement multi-language OCR support.
- ✅ Add API support for automated text extraction.

## License
This project is open-source and available under the **MIT License**.

---
💡 Contributions are welcome! Feel free to fork, modify, and improve the project. 🚀

