import requests
import os

# Configuration
DOCUGENIE_API_URL = os.getenv("DOCUGENIE_API_URL", "http://localhost:8000")
RESUME_PATH = "/Users/tribhangind/Documents/GitHub/My-portfolio/src/assets/Tribhangin_Resume.pdf"

def ingest_resume():
    if not os.path.exists(RESUME_PATH):
        print(f"Error: Resume not found at {RESUME_PATH}")
        return

    print(f"Ingesting resume from {RESUME_PATH}...")
    
    files = [
        ('files', ('Tribhangin_Resume.pdf', open(RESUME_PATH, 'rb'), 'application/pdf'))
    ]
    
    try:
        response = requests.post(f"{DOCUGENIE_API_URL}/ingest", files=files)
        if response.status_code == 200:
            print("Successfully ingested resume!")
            print(response.json())
        else:
            print(f"Failed to ingest resume. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    ingest_resume()
