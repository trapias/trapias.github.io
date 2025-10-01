#!/usr/bin/env python3
"""
Script per estrarre l'elenco dei campionati dalla pagina FIH
usando un browser headless per gestire il JavaScript
"""

import json
import re
from playwright.sync_api import sync_playwright

def estrai_campionati():
    """
    Estrae l'elenco completo dei campionati dalla pagina principale FIH
    """
    url = "https://fih.mps-service.it/main/tutti_i_campionati/SAN00"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print(f"Navigazione a {url}...")
        page.goto(url, wait_until="domcontentloaded")

        # Attendi che la pagina sia completamente caricata
        page.wait_for_timeout(5000)

        # Stampa il contenuto per debug
        print("Cercando link...")

        # Estrai tutti i link ai campionati
        links = page.query_selector_all('a[href*="/main/gare_girone/"]')
        print(f"Trovati {len(links)} link")

        elenco_gare = {
            "Maschile": [],
            "Femminile": []
        }

        for i, link in enumerate(links):
            href = link.get_attribute("href")
            if not href:
                print(f"Link {i}: nessun href")
                continue

            # Estrai il titolo (h4)
            h4 = link.query_selector("h4")
            if not h4:
                print(f"Link {i}: nessun h4 trovato per {href}")
                continue

            titolo = h4.inner_text().strip()
            if not titolo:
                print(f"Link {i}: h4 vuoto per {href}")
                continue

            url_gara = "https://fih.mps-service.it" + href

            # Determina il genere
            genere = "Femminile" if any(x in titolo for x in ["Femminile", "Allieve", "Ragazze"]) else "Maschile"

            # Genera filename
            filename = titolo.lower()
            filename = filename.replace(" - outdoor", "")
            filename = filename.replace(" - ", "_")
            filename = filename.replace(" ", "_")
            filename = re.sub(r'[^a-z0-9_]', '', filename)

            gara = {
                "titolo": titolo,
                "filename": filename,
                "url": url_gara
            }

            # Evita duplicati
            already_exists = False
            for existing in elenco_gare[genere]:
                if existing["url"] == gara["url"]:
                    already_exists = True
                    break

            if not already_exists:
                elenco_gare[genere].append(gara)
                print(f"✓ {titolo}")

        browser.close()

        print(f"\n📊 Totale campionati trovati:")
        print(f"   Maschile: {len(elenco_gare['Maschile'])}")
        print(f"   Femminile: {len(elenco_gare['Femminile'])}")

        # Salva in un file JSON
        with open("campionati.json", "w", encoding="utf-8") as f:
            json.dump(elenco_gare, f, indent=2, ensure_ascii=False)

        print(f"\n💾 Salvato in campionati.json")

        return elenco_gare


if __name__ == "__main__":
    estrai_campionati()
