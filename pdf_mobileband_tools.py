import requests
import pdfplumber

def extract_text_from_pdf(url, temp_pdf_path='temp.pdf'):
    """
    Lädt ein PDF von einer URL herunter und extrahiert den Text.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(temp_pdf_path, 'wb') as f:
            f.write(response.content)
        with pdfplumber.open(temp_pdf_path) as pdf:
            text = "\n".join(page.extract_text() or '' for page in pdf.pages)
        return text
    except Exception as e:
        print(f"Fehler beim PDF-Download/Extraktion: {e}")
        return None