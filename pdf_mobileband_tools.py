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

def summarize_mobile_bands(text, ollama_url="http://localhost:11434/api/chat", model="llama2"):
    prompt = (
        "Extract and summarize all mobile frequency bands (Mobilfunkgassen) mentioned in the following text. "
        "List them in a concise way, grouped if possible. Text: " + text
    )
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }
    try:
        resp = requests.post(ollama_url, json=payload, timeout=600)
        resp.raise_for_status()
        result = resp.json()
        return result.get("message", {}).get("content", "")
    except Exception as e:
        print(f"Fehler bei der KI-Zusammenfassung: {e}")
        return None
