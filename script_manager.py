import random
import numpy as np
import TopTwitter
import TopInstagram
import TopYouTube
import Pichichi
import Zamora
from files_manager import get_valor
from datetime import datetime


def script_response(script):
    if script == "script_hora":
        return f"Son las {datetime.now().hour}:{datetime.now().minute}"

    if script == "script_numero_aleatorio":
        return str(random.randrange(100))

    if script == "script_estado_animico":
        sentimiento = get_valor("sentimientos")

        if sentimiento > 0:
            return (
                f"Si por como estoy te refieres a en que % se encuentra mi variable, me encuentro un {sentimiento}% alegre")
        if sentimiento == 0:
            return (
                f"Si por como estoy te refieres a en que % se encuentra mi variable, me encuentro en un estado neutro")
        if sentimiento < 0:
            return (
                f"Si por como estoy te refieres a en que % se encuentra mi variable, me encuentro un {abs(sentimiento)}% enfadada")

    if script == "script_busquedaTwitter":
        salto = ' '
        aux2 =  TopTwitter.twitter()
        for element in range (len(aux2["Nombre"])):
            salto += f'<p>{aux2["Nombre"][element]} {aux2["Usuario"][element]} {aux2["Seguidores"][element]}</p>'
        return f"Estas son las cuentas con mas seguidores en Twitter: <br> {salto}" 
    
    if script == "script_busquedaInstagram":
        salto1 = ' '
        aux2 =  TopInstagram.instagram()
        for element in range (len(aux2["Nombre"])):
            salto1 += f'<p>{aux2["Nombre"][element]} {aux2["Usuario"][element]} {aux2["Seguidores"][element]}</p>'        
        return f"Estas son las cuentas con mas seguidores en Instagram: <br> {salto1}"

    if script == "script_pichichi":  
        return f"Estos son los maximos goleadores: <br> {Pichichi.pichichi()}"  

    if script == "script_youtube": 
        salto3 = ' '
        aux2 =  TopYouTube.youtube()
        for element in range (len(aux2["Nombre"])):
            salto3 += f'<p>{aux2["Nombre"][element]} {aux2["Nombre del canal"][element]} {aux2["Seguidores"][element]}</p>'       
        return f"Estas son las cuentas mas seguidas en youtube: <br> {salto3}" 
    
    if script == "script_zamora":      
        return f"Estos son los porteros menos goleados: <br> {Zamora.zamora()}" 