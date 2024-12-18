import pytesseract
from pdf2image import convert_from_path
from PIL import ImageOps

# Path to the PDF file
pdf_path = "../resource/Klingon_lexicon - FrathWiki.pdf"

# Convert PDF to images (one image per page)
images = convert_from_path(pdf_path)

# Extract text from each image using Tesseract OCR
extracted_text = []
for page_number, image in enumerate(images):
    image = ImageOps.grayscale(image)
    try:
        text = pytesseract.image_to_string(image)
        extracted_text.append(f"Page {page_number + 1}:\n{text}\n")
    except Exception as e:
        print(f"Error processing page {page_number + 1}: {e}")

combined_text_file_path = "../klingon-dictionary.txt"

with open(combined_text_file_path, "w") as combined_text_file:
    for text in extracted_text:
        combined_text_file.write(text)