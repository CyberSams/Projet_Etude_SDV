from colorama import Fore, Back, Style, init
import requests

def checkusername(username):

    url = ['https://www.reddit.com/user/',
    'https://www.youtube.com/@',
    'https://github.com/',
    'https://instagram.com/',
    'https://www.twitch.tv/']
    
    displayInfos = f"\n\n===================================\n"
    displayInfos+= f"Account for user "+username
    displayInfos+= f"\n===================================\n"

    

    for i in range(len(url)):
        r = requests.get(url[i]+username)
        text = r.text
        status = r.status_code
        
        if url[i] == 'https://instagram.com/':
           
            if 'Instagram photos' in text:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"

        elif url[i] == 'https://github.com/':

            if status == 404:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
        
        elif url[i] == 'https://www.reddit.com/user/':

            if 'pseudo ' in text:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"

        elif url[i] == 'https://www.youtube.com/@':

            if '404' in text:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"

        elif url[i] == 'https://www.twitch.tv/':

            if 'og:video:width' in text:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"

    return displayInfos