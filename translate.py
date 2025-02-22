from fastapi import FastAPI, Request
from deep_translator import GoogleTranslator

app = FastAPI()

@app.post("/process_message")
async def process_message(request: Request):
    data = await request.json()  # Get message from Telex
    text = data.get("text", "")

    # Translate message to French
    translated_text = GoogleTranslator(source='auto', target='fr').translate(text)

    return {"text": translated_text}  # Return translated message
