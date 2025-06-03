import sys
import os
import json

print("Startar character_manager.py")
try:
    from character_model import Character
    print("Importerat character_model")
    from import_character import importera_karaktär_fil
    print("Importerat import_character")
except Exception as e:
    print("Fel vid import:", e)
    input("Tryck Enter för att avsluta...")
    sys.exit(1)

# Ange absolut sökväg för datafilen, så den alltid sparas i din GM_Tool_ver1-mapp
DATAFIL = os.path.join(os.path.dirname(__file__), "karaktärer.json")

def ladda_alla_karaktärer():
    if not os.path.exists(DATAFIL):
        return []
    with open(DATAFIL, encoding="utf-8-sig") as f:
        data = json.load(f)
    return [Character.från_dict(d) for d in data]

def spara_alla_karaktärer(karaktärer):
    with open(DATAFIL, "w", encoding="utf-8-sig") as f:
        json.dump([k.till_dict() for k in karaktärer], f, ensure_ascii=False, indent=2)

def sök_karaktärer(karaktärer, sökterm):
    return [k for k in karaktärer if sökterm.lower() in k.namn.lower()]

def visa_karaktär(k):
    print("="*40)
    print(f"Namn: {k.namn}")
    print(f"Beskrivning: {k.beskrivning}")
    print(f"Dialekt: {k.dialekt}")
    print(f"Taggar: {', '.join(k.taggar)}")
    print(f"Relationer: {k.relationer}")
    print(f"Viktiga händelser: {k.viktiga_händelser}")
    print(f"Exempelrepliker: {k.exempelrepliker}")
    print(f"Anteckningar: {k.anteckningar}")
    print("="*40)

def main():
    print("Programmet startar!")
    karaktärer = ladda_alla_karaktärer()
    while True:
        print("\nVälj ett alternativ:")
        print("1. Importera karaktär från fil")
        print("2. Lista alla karaktärer")
        print("3. Sök karaktär på namn")
        print("4. Avsluta")
        val = input("> ").strip()
        if val == "1":
            filnamn = input("Ange sökväg till .txt eller .docx: ").strip()
            if not os.path.isfile(filnamn):
                print("Filen hittades inte. Ange full sökväg, t.ex. C:\\Users\\saker\\Desktop\\Programmering\\GM_Tool_ver1\\minfil.txt")
                continue
            try:
                ny_k = importera_karaktär_fil(filnamn)
                karaktärer.append(ny_k)
                spara_alla_karaktärer(karaktärer)
                print(f"Importerade {ny_k.namn}!")
            except Exception as e:
                print("Fel vid import:", e)
        elif val == "2":
            for idx, k in enumerate(karaktärer):
                print(f"{idx+1}. {k.namn}")
            detalj = input("Visa detaljer om någon? Ange nummer eller tryck Enter för att hoppa: ").strip()
            if detalj.isdigit():
                idx = int(detalj)-1
                if 0 <= idx < len(karaktärer):
                    visa_karaktär(karaktärer[idx])
        elif val == "3":
            term = input("Ange sökterm: ").strip()
            träffar = sök_karaktärer(karaktärer, term)
            if not träffar:
                print("Inga karaktärer hittades.")
            for k in träffar:
                visa_karaktär(k)
        elif val == "4":
            print("Avslutar.")
            break
        else:
            print("Ogiltigt val.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Fel i programmet:", e)
        input("Tryck Enter för att avsluta...")