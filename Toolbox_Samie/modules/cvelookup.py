from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests


def CVELookUp(id, htmlRender=False):

    # Rechercher des infos sur une CVE
    URL = "https://cvedetails.com"
    HEADERS = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "cookie": "cvedconsent=1; _ga=GA1.1.660489098.1715345918; _ga_3404JT2267=GS1.1.1715345917.1.1.1715345967.0.0.0",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }

    cveQuery = requests.get(URL + "/cve/" + id, headers=HEADERS)
    status = True

    if cveQuery.status_code != 200:
        print("Vérifiez l'état du site https://cvedetails.com")
        status = False
    
    if "Unknown CVE ID" in cveQuery.text:
        print("Cette CVE n'est pas référencée ou n'existe pas")
        status = False

    if status:
        if htmlRender:
            spacing = "<br>" 
        else:
            spacing = "\n"

        html = cveQuery.content
        soup = BeautifulSoup(html,"html.parser")
        displayInfos = ""
        

        displayInfos+= f"{spacing}==================================={spacing}"
        displayInfos+= f"Informations sur la "+id
        displayInfos+= f"{spacing}==================================={spacing}"

        summary = soup.find(id='cvedetailssummary').text.strip()
        
        displayInfos+= f"{spacing}"+summary

        return displayInfos
