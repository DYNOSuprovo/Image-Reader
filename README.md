# OCR Image Text Extraction and Analysis

## Overview
This project provides multiple implementations for Optical Character Recognition (OCR) using Tesseract and enhances text processing with an LLM model. The project includes:
- A **Flask-based web app** for image text extraction.
- A **Streamlit-based interface** with LLM-powered text refinement.
- A **command-line tool** to process images and PDFs.

## Features
- Extracts text from images using Tesseract OCR.
- Supports multiple formats: PNG, JPG, JPEG, BMP, TIFF, and PDFs.
- Provides a **Flask web interface** to upload images and view extracted text.
- **Streamlit integration** for enhanced text processing with an LLM.
- Uses **OpenCV preprocessing** to improve OCR accuracy.

## Project Structure
```
📂 Project Folder
├── app.py             # Flask Web App for OCR
├── check.py           # Duplicate Flask App (can be removed)
├── image_reader.py    # Command-line OCR tool for images and PDFs
├── streamlitonly.py   # Streamlit-based OCR with LLM
├── templates/
│   ├── index.html     # Frontend HTML for Flask app
├── static/
│   ├── style.css      # CSS for web styling
│   ├── uploads/       # Folder for uploaded images
```

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) (Set the correct path in code)
- Required Python Libraries:
  ```sh
  pip install flask streamlit pytesseract pillow opencv-python numpy pdf2image langchain_community
  ```

## Usage
### Flask Web App
Run the Flask application:
```sh
python app.py
```
Open `http://127.0.0.1:5000/` in your browser to upload images and extract text.

### Streamlit Interface
Run the Streamlit application:
```sh
streamlit run streamlitonly.py
```
Upload an image, extract text, and process it with an LLM.

### Command-line OCR Tool
Process an image or PDF via the terminal:
```sh
python image_reader.py
```
Enter the file path when prompted.

## Configuration
Ensure Tesseract is installed and update the path in the scripts:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

## Future Improvements
- Improve OCR accuracy with better preprocessing.
- Add multilingual OCR support.
- Integrate more advanced LLM models.

## License
This project is open-source and available under the MIT License.

