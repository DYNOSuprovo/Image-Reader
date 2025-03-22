import streamlit as st
from PIL import Image
import pytesseract
import io
from langchain_community.llms import Ollama

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.title("Image Text Analysis with LLM")

# Upload Image
uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Convert uploaded file to Image
    img = Image.open(io.BytesIO(uploaded_file.getvalue()))
    
    # Extract text using Tesseract
    extracted_text = pytesseract.image_to_string(img).strip()
    
    st.subheader("Extracted Text:")
    st.write(extracted_text)

    if extracted_text:
        # Process with LLM
        prompt_text =prompt_text =  f"Extract the text from the image, even if it appears disorganized or poorly formatted. Your task is to refine and present it in a clear, structured, and human-friendly manner. Focus on improving readability and coherence without altering the original meaning.\n\nText: {extracted_text}"

        try:
            llm = Ollama(model="llama3")
            result = llm.invoke(prompt_text)
            st.subheader("LLM Analysis:")
            st.write(result if result.strip() else "No response from LLM.")
        except Exception as e:
            st.error(f"LLM Error: {str(e)}")
    else:
        st.error("No text extracted to analyze.")
