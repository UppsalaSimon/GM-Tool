import os
from character_model import Character
from docx import Document

def importera_karaktär_fil(filväg):
    """
    Importerar en karaktär från en .docx- eller .txt-fil.
    Exempel på filstruktur:
    Namn: Boromir
    Beskrivning: En stolt människa från Gondor...
    Dialekt: Brittisk
    Taggar: krigare, adelsman
    """
    if filväg.endswith(".docx"):
        doc = Document(filväg)
        text = "\n".join([p.text for p in doc.paragraphs])
    elif filväg.endswith(".txt"):
        with open(filväg, encoding="utf-8-sig") as f:   # UTF-8 with BOM (signature)
            text = f.read()
    else:
        raise ValueError("Endast .docx eller .txt stöds just nu.")

    data = {}
    for rad in text.split("\n"):
        if ":" in rad:
            nyckel, värde = rad.split(":", 1)
            data[nyckel.strip().lower()] = värde.strip()
    namn = data.get("namn", "Okänd")
    beskrivning = data.get("beskrivning", "")
    dialekt = data.get("dialekt", "")
    taggar = [t.strip() for t in data.get("taggar", "").split(",") if t.strip()]

    return Character(namn, beskrivning, dialekt, taggar)