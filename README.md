# **OCR Image Processing Web App with Flask, Tesseract, and OpenCV**

## **📌 Overview**

This project provides a **web-based OCR (Optical Character Recognition) tool** using **Flask**, **Tesseract OCR**, and **OpenCV**.  
Users can **upload an image**, and the app extracts text from it, displaying results in an elegant and responsive UI.

## **🚀 Features**

✅ **Web-based UI** for uploading images  
✅ **Tesseract OCR** for text extraction  
✅ **OpenCV preprocessing** (grayscale conversion)  
✅ **Mobile-friendly & responsive**  
✅ **Dynamic file preview** before submission  

## **🛠️ Requirements**

Make sure you have the following installed:

### **🔹 Python Packages**

Install dependencies using:

```bash
pip install flask pytesseract opencv-python numpy pillow
```

### **🔹 Tesseract OCR Installation**

#### **Windows**:
1. Download and install Tesseract from [this link](https://github.com/UB-Mannheim/tesseract/wiki).
2. Ensure Tesseract is added to your system PATH (`C:\Program Files\Tesseract-OCR\tesseract.exe`).

#### **Linux (Ubuntu/Debian)**:
```bash
sudo apt install tesseract-ocr -y
```

#### **macOS**:
```bash
brew install tesseract
```

---

## **📂 Project Structure**
```
OCR-Image-Processing/
│── static/
│   ├── style.css         # Styles for the UI
│── templates/
│   ├── index.html        # Main HTML file
│── uploads/              # Stores uploaded images
│── app.py                # Flask application
│── README.md             # Project documentation
```

---

## **🖥️ Usage**

1️⃣ **Run the Flask app**:
```bash
python app.py
```

2️⃣ **Open the browser and go to**:
```
http://127.0.0.1:5000/
```

3️⃣ **Upload an image** and click "Extract Text".

4️⃣ **View the extracted text** on the same page.

---

## **📌 Expected Output**

🔹 **Uploaded Image Preview**  
🔹 **Extracted Text Displayed in a Textbox**  

```
Extracted Text:
[Recognized text from the image]
```

---

## **🛠️ Notes & Enhancements**
- If OCR accuracy is **low**, try improving image quality or apply **thresholding**.
- For **better OCR accuracy**, use Tesseract’s `tessdata_best` models from [here](https://github.com/tesseract-ocr/tessdata_best).
- Customize the UI further in `static/style.css`.

---

## **📝 License**
This project is **open-source** and free to use. 🚀

