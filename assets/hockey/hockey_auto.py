import json
from datetime import datetime
import argparse
import os
import requests
from bs4 import BeautifulSoup
from ics import Calendar, Event
import locale
import pytz
from geopy.geocoders import Nominatim
import webbrowser
import markdown
import diskcache as dc
import re

class Location:
    address = ""
    latitude = 0
    longitude = 0



def create_ics_file(titolo, filename, url):
    locale.setlocale(locale.LC_ALL, 'it_IT')
    print(locale.getlocale())
    geolocator = Nominatim(user_agent="hcvc")

    print("URL: ", url)
    response = requests.get(url)
    print("Response: ", response)

    soup = BeautifulSoup(response.content, "html.parser")
    tabelle = soup.find_all("div", class_="gare-wrap")
    c = Calendar()

    nTabelle = 0
    markdownStr = ""
    htmlHead = '<html>' + '<head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous"><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script></head>' + '<body><div class="row py-5"><div class="col-md-12 text-center"><h1>Hockey Prato Val Chisone</h1><h2>Calendari gare 2025/2026</h2></div></div>'
    htmlHead += '<style>.Maschile {background-color: #f0f0f0; border: solid 2px #06862D; color: #06862D;}.Femminile {background-color: #f0f0f0; border: solid 2px #FE0193; color: #FE0193;}</style>'
    htmlHead += '<script> \
            var _paq = window._paq = window._paq || []; \
            _paq.push([\'trackPageView\']); \
            _paq.push([\'enableLinkTracking\']); \
            (function () { \
                var u="https:////m.trapias.it/"; \
                _paq.push([\'setTrackerUrl\', u + \'matomo.php\']); \
                _paq.push([\'setSiteId\', \'1\']); \
                var d = document, g = d.createElement(\'script\'), s = d.getElementsByTagName(\'script\')[0]; \
                g.async = true; g.src = u + \'matomo.js\'; s.parentNode.insertBefore(g, s); \
            })(); \
        </script>'
    htmlFoot = "</div></body></html>"

    for tabella in tabelle:
        nTabelle += 1
        # if nTabelle == 3:
        #     break
        #print("Tabella: ", nTabelle)
        # print(tabella)

        girone = tabella.find_all(class_="h3-wrap")
        if girone:
            markdownStr += ("# " + girone[0].text)

        risultati = tabella.find_all(class_="risultati")
        for risultato in risultati:

            if 'id' in risultato.attrs:

                #print("RISULTATO " + risultato.attrs['id'])

                ssquadre=""
                nsq=0
                isVALCHISONE = False
                squadre = risultato.find_all(class_="sq-nLong")
                for squadra in squadre:
                    nsq += 1
                    if nsq == 1:
                        ssquadre += squadra.text
                        if squadra.text == "HOCKEY SU PRATO VALCHISONE" or squadra.text == "HOCKEY PRATO VALCHISONE FEMMINILE" or squadra.text == "HP VALCHISONE":
                            isVALCHISONE = True
                    else:
                        ssquadre += " - " + squadra.text
                        if squadra.text == "HOCKEY SU PRATO VALCHISONE" or squadra.text == "HOCKEY PRATO VALCHISONE FEMMINILE" or squadra.text == "HP VALCHISONE":
                            isVALCHISONE = True

                infogara = risultato.find_all(class_="info-gara")
                for gara in infogara:

                    # crea markdown con tutte le gare
                    datagara = gara.find_all(class_="info-gara-data")
                    markdownStr += "\r\n## " + datagara[0].text

                    markdownStr += "\n**" + ssquadre + "**\r\n"

                    giornata = gara.find_all(class_="info-gara-giornata")
                    markdownStr += "\r\nGiornata: " + giornata[0].text + "\r\n"

                    indirizzocampo = gara.find_all(class_="info-gara-campo-desc")
                    nomecampo = indirizzocampo[0].text
                    pnomecampo = nomecampo.index('-')
                    if pnomecampo > 0:
                        nomecampo = indirizzocampo[0].text[0:pnomecampo]
                    soloindirizzocampo = indirizzocampo[0].text[pnomecampo + 1:]

                    citta = gara.find_all(class_="info-gara-campo-loc")
                    markdownStr += "\r\nCampo: " + nomecampo + "\r\n" #indirizzocampo[0].text +" - " + citta[0].text
                    markdownStr += "\r\nIndirizzo Campo: " + soloindirizzocampo + " - " + citta[0].text + "\r\n"

                # aggiungi evento a calendario solo per le gare del Val Chisone
                if isVALCHISONE:
                    evento = Event()
                    evento.name = girone[0].text + " - " + ssquadre
                    evento.description = girone[0].text + "\n" + giornata[0].text + "\n" + indirizzocampo[0].text + " " + citta[0].text + "\n" + ssquadre

                    try:
                        location = None
                        ck = soloindirizzocampo + " " + citta[0].text
                        ck = ck.replace("'", "_").replace(",", "_").replace(" ", "_").replace("-", "_")
                        if ck.startswith("_"):
                            ck = ck[1:]
                        if ck in cache:
                            location = Location()
                            location.address = cache[ck]
                            location.latitude = cache[ck + '_latitude']
                            location.longitude = cache[ck + '_longitude']
                    except Exception as ex:
                        print("Errore location " + str(ex))
                    try:
                        if location is None:
                            location = geolocator.geocode(soloindirizzocampo + " " + citta[0].text)
                        if location is not None:
                            evento.location = location.address # indirizzocampo[0].text + " " + citta[0].text
                            evento.geo = (location.latitude, location.longitude)

                            cache[ck] = location.address
                            cache[ck + '_latitude'] = location.latitude
                            cache[ck + '_longitude'] = location.longitude

                            markdownStr += "\r\nLocation: " + evento.location
                            markdownStr += "\r\nGeo: " + str(evento.geo)
                            # aps =  "geo:" + str(location.latitude) + "," + str(location.longitude),
                            # parameters={
                            #     "VALUE": "URI",
                            #     "X-ADDRESS": location.address,
                            #     "X-APPLE-RADIUS": "72",
                            #     "X-TITLE": location.address
                            # }
                            # e['X-Apple-Structured-Location'] =  aps

                            # print(location.address)
                            # print((location.latitude, location.longitude))
                        else:
                            # e.location = indirizzocampo[0].text + " " + citta[0].text
                            evento.location = soloindirizzocampo + " " + citta[0].text
                            markdownStr += "\r\nLocation: " + evento.location
                    except Exception as ex:
                        print("Errore location " + str(ex))

                    # markdown += "\r\nLocation: " + e.location
                    # markdown += "\r\nGeo: " + str(e.geo)

                    #Dom 22/09/2024 11.30
                    rome_tz = pytz.timezone('Europe/Rome')
                    date_format = '%a %d/%m/%Y %H.%M'

                    if datagara.__len__() == 0:
                        print("Errore nella data: " + datagara)
                        continue
                    try:
                        data = datetime.strptime(datagara[0].text, date_format)
                    #data = datetime.strptime(datagara[0].text, date_format)
                        datalocale = rome_tz.localize(data)
                        evento.begin = datalocale
                        # c.events.add(e)
                    except:# Exception as e:
                        # if e is not None:
                        #     print("Errore nella data " + datagara[0].text + ": " + str(e))
                        # else:
                            print("Errore nella data " + datagara[0].text)
                            # print(datagara[0])

                            # if not datagara[0] is None and not datagara[0].text is None and datagara[0].text != "-":
                            #     date_format = '%d/%m/%Y %H.%M'
                            #     # Dom 13/10/2024 13.00
                            #     try:
                            #         data = datetime.strptime(datagara[0].text, date_format)
                            #         datalocale = rome_tz.localize(data)
                            #         evento.begin = datalocale
                            #     except:
                            #         print("Errore2 nella data " + datagara[0].text)

                    # print(evento.begin)
                    if not  evento is None and not evento.begin is None:
                        c.events.add(evento)
                    else:
                        print("Evento non creato!")

            markdownStr += ("\r\n")

    print('saving ' + filename + '.md')
    with open(filename + ".md", "w") as text_file:
        text_file.write(markdownStr)
    html = markdown.markdown(markdownStr)

    print('saving ' + filename + '.html')
    with open(filename + ".html", "w") as text_file:
        html=html.replace("\r\n","<br />\n")
        output = htmlHead + html + htmlFoot
        text_file.write(output)

        # [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
    print('saving ' + filename + '.ics')
    with open(filename + '.ics', 'w') as ics_file:
        ics_file.writelines(c.serialize_iter())

    print('Done')


def verifica_valchisone(url):
    """
    Verifica se in un campionato partecipa la Val Chisone
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Cerca tutte le squadre
        squadre = soup.find_all(class_="sq-nLong")
        for squadra in squadre:
            nome_squadra = squadra.text.strip()
            if nome_squadra in ["HOCKEY SU PRATO VALCHISONE", "HOCKEY PRATO VALCHISONE FEMMINILE", "HP VALCHISONE"]:
                return True

        return False
    except Exception as ex:
        print(f"Errore verifica Val Chisone per {url}: {ex}")
        return False


def estrai_elenco_gare_da_url(url_pagina_principale):
    """
    Estrae automaticamente l'elenco dei campionati dalla pagina principale
    Nota: questa funzione estrae solo dalle sezioni visibili all'apertura della pagina
    """
    print(f"Caricamento della pagina principale: {url_pagina_principale}")
    response = requests.get(url_pagina_principale)
    soup = BeautifulSoup(response.content, "html.parser")

    elencoGare = {}

    # La pagina usa liste con titoli h2 e link alle gare
    # Troviamo tutti i container con classe che contengono i campionati
    containers = soup.find_all("ul", class_="nav nav-tabs nav-stacked")

    current_category = "Maschile"

    for container in containers:
        # Trova tutti i link nel container
        items = container.find_all("li")

        for item in items:
            link = item.find("a")
            if link and link.get("href"):
                href = link.get("href")

                # Se è un link a Stagione, skippa
                if "stagione" in href.lower() or href == "#":
                    continue

                # Se contiene un #numero, è un link a una sezione
                if href.startswith("#"):
                    # È un titolo di sezione, ignora
                    continue

        # Prova un altro approccio: cerca i link direttamente nel body
        scripts = soup.find_all("script")
        for script in scripts:
            if script.string and "gare_girone" in script.string:
                # Estrai gli ID dei gironi dallo script
                matches = re.findall(r'/main/gare_girone/(\d+)', script.string)
                for match in matches:
                    print(f"Trovato girone ID: {match}")

    # Fallback: hardcoded per i campionati principali se non troviamo nulla
    if not elencoGare or (len(elencoGare.get("Maschile", [])) == 0 and len(elencoGare.get("Femminile", [])) == 0):
        print("ATTENZIONE: impossibile estrarre automaticamente i campionati dalla pagina.")
        print("La pagina potrebbe usare JavaScript per caricare dinamicamente i contenuti.")
        print("Usando lista hardcoded dei campionati principali...")

        elencoGare = {
            "Maschile": [
                {
                    "titolo": "Juniores Maschile - OUTDOOR - Girone A",
                    "filename": "juniores_maschile_outdoor_girone_a",
                    "url": "https://fih.mps-service.it/main/gare_girone/1024"
                }
            ],
            "Femminile": []
        }

    return elencoGare


# =o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=
#                                   MAIN PROGRAM
# =o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=
cache = dc.Cache('./cache')

parser = argparse.ArgumentParser(description='Converti calendari Hockey in ICS')
parser.add_argument('scarica', help='Scarica?')
args = parser.parse_args()
scarica = args.scarica

# Carica l'elenco delle gare da file JSON
with open("campionati.json", "r", encoding="utf-8") as f:
    elencoGare = json.load(f)

print(f"Campionati caricati: {len(elencoGare.get('Maschile', []))} maschili, {len(elencoGare.get('Femminile', []))} femminili")

# Verifica presenza Val Chisone nei campionati
print("\nVerifica partecipazione Val Chisone...")
aggiornato = False
for genere in elencoGare:
    for gara in elencoGare[genere]:
        # Se il campo valchisone non esiste o è None, verifica
        if "valchisone" not in gara or gara["valchisone"] is None:
            print(f"Verifico {gara['titolo']}...", end=" ")
            gara["valchisone"] = verifica_valchisone(gara["url"])
            if gara["valchisone"]:
                print("✓ VAL CHISONE PRESENTE")
            else:
                print("✗ non presente")
            aggiornato = True

# Salva il file aggiornato
if aggiornato:
    print("\nSalvataggio configurazione aggiornata...")
    with open("campionati.json", "w", encoding="utf-8") as f:
        json.dump(elencoGare, f, indent=2, ensure_ascii=False)
    print("✓ campionati.json aggiornato")

# Costruzione della pagina HTML con link a tutti i file
html = '<html>' + '<head><title>Hockey Prato Val Chisone - Calendari gare 2025/2026</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous"><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script></head>' + '<body><div class="row py-5"><div class="col-md-12 text-center"><h1>Hockey Prato Val Chisone</h1><h2>Calendari gare 2025/2026</h2></div></div>'
html += '<style>.Maschile {background-color: #f0f0f0; border: solid 2px #06862D; color: #06862D;}.Femminile {background-color: #f0f0f0; border: solid 2px #FE0193; color: #FE0193;}.valchisone-row {background-color: #fffacd; border-left: 4px solid #ff6b00; font-weight: bold;}</style>'
html += '<script> \
		var _paq = window._paq = window._paq || []; \
		_paq.push([\'trackPageView\']); \
		_paq.push([\'enableLinkTracking\']); \
		(function () { \
			var u="https:////m.trapias.it/"; \
			_paq.push([\'setTrackerUrl\', u + \'matomo.php\']); \
			_paq.push([\'setSiteId\', \'1\']); \
			var d = document, g = d.createElement(\'script\'), s = d.getElementsByTagName(\'script\')[0]; \
			g.async = true; g.src = u + \'matomo.js\'; s.parentNode.insertBefore(g, s); \
		})(); \
	</script>'
html += '<script> function copy(id) { navigator.clipboard.writeText(id); alert("Link copiato negli appunti"); return false;}</script><div class="container-fluid">'
html += '<div class="row"><div class="col-md-12 text-center p-4"><a class="matomo_download" style="font-size:1.5rem" href="HPVC_Calendari_Manuale.pdf">MANUALE ISTRUZIONI iPhone e Android</a></div></div>'

for genere in elencoGare:
    print(genere)
    html += f'<div class="row"><div class="col-md-12 text-center p-2 {genere}"><h2>' + genere + '</h2></div></div>'
    for gara in elencoGare[genere]:
        print(gara["titolo"], gara["url"])
        if scarica == "1":
            create_ics_file(gara["titolo"], gara["filename"], gara["url"])

        # Evidenzia le righe con partecipazione Val Chisone
        row_class = 'valchisone-row' if gara.get("valchisone", False) else ''
        valchisone_badge = ' <span class="badge bg-warning text-dark">⭐ Val Chisone</span>' if gara.get("valchisone", False) else ''

        html += f'<div class="row {row_class}">'
        html += '<div class="col-md-8 text-center p-2">'
        html += f'<h3>{gara["titolo"]}{valchisone_badge}</h3>'
        #html += f'<a class="matomo_download" href="https://trapias.github.io/assets/hockey/{gara['filename']}.html">Tutte le gare</a>'
        html += f'<a class="matomo_download" href="{gara["filename"]}.html">Tutte le gare</a>'
        html += '</div>'
        html += f'<div class="col-md-2 text-center p-2"><a id=\'{gara["filename"]}.ics\' class="btn btn-secondary matomo_download" href="javascript:copy(\'https://trapias.github.io/assets/hockey/{gara["filename"]}.ics\')">COPIA LINK</a></div>'
        html += f'<div class="col-md-2 text-center p-2"><a class="btn btn-primary matomo_download" href="{gara["filename"]}.ics">APRI</a></div>'
        html += '</div>'

html += '</div>'

html += '<div class="row"><div class="col-md-12 text-center p-2"><br><br><h3>Istruzioni</h3></div></div>'
html += '<div class="row"><div class="col-md-12 text-center p-2">'
html += '<a href="https://support.microsoft.com/it-it/office/importare-o-sottoscrivere-un-calendario-in-outlook-com-o-outlook-sul-web-cff1429c-5af6-41ec-a5b4-74f2c278e98c">Outlook</a>'
html += '&nbsp;&nbsp;&nbsp;'
html += '<a href="https://support.google.com/calendar/answer/37118?hl=it">Google Calendar</a>'
html += '&nbsp;&nbsp;&nbsp;'
html += '<a href="https://support.apple.com/it-it/guide/calendar/icl1023/mac">Apple Calendar</a>'
html += '&nbsp;&nbsp;&nbsp;'
html += '<a href="https://support.apple.com/it-it/guide/iphone/iph3d1110d4/18.0/ios/18.0">iPhone</a>'

#html += '<video controls width="320" height="480"><source src="istruzioni.mp4" type="video/mp4">Your browser does not support the video tag.</video>'
html += '</div></div>'
html += '</div></body></html>'

# Salva la pagina HTML su un file
with open('index.html', 'w') as file:
    file.write(html)

# Apre il browser con la pagina HTML generata
webbrowser.open('file://' + os.path.realpath('index.html'))
print("Fine")
