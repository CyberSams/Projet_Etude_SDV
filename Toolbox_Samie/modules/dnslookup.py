import requests
import json

def DNSLookUp(domain, htmlRender=False):

    domainName = str(domain)
    URL = "https://networkcalc.com/api/dns/lookup/"+domainName
    query = requests.get(URL)
    displayInfos = ""
    sp = "&nbsp;" * 15
    maxLen = 8

    if htmlRender:
        spacing = "<br>" 
    else:
        spacing = "\n"
    
    if query.status_code != 200:
        displayInfos = f"{spacing}Check your domain name or the API website (https://networkcalc.com/api/)" 
    
    else:
        
        data = json.loads(query.text)
        status = data['status']
        
        if status == 'OK':
            if not htmlRender:
                displayInfos = f"\n\n========================================\n"
                displayInfos+= f"DNS Informations about "+data['hostname']
                displayInfos+= f"\n==========================================\n\n"
            else:
                displayInfos+=f"""
                +-----------------+-------------------------------------------------------------------------+<br>
                | <strong>Record name</strong> |{sp}{sp}<strong>Informations and data</strong>{sp}{sp} |<br>
                +-----------------+-------------------------------------------------------------------------+<br>
                """

            records = data['records']

            for record in records:
                newSpace = maxLen - len(record)
                spaceTag = "&nbsp;" * newSpace

                if not records[record]:
                    if htmlRender:
                        displayInfos+=f"| {spaceTag}{record}{spaceTag} \tNo record found{spacing}"
                        displayInfos+=f"+--------------------------------------------------------------------------------------------+<br>"
                    else:
                         displayInfos+=f"{record} : \tNo record found\n"


                else:
                    if htmlRender:
                            displayInfos+=f"| {spaceTag}{record}{spaceTag}{spaceTag} {records[record]}|{spacing}"
                            displayInfos+=f"+--------------------------------------------------------------------------------------------+<br>"
                    else:
                        displayInfos+=f"{record} : {records[record]}\n"


        else:
            if status == 'NO_RECORDS':
                displayInfos = f"{spacing}No records. Check if the domain is reachable.{spacing}"
            else:
                displayInfos = "Error with the API, check https://networkcalc.com/api/dns/lookup/"

    return displayInfos