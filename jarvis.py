import os
import sys
import webbrowser
import pyttsx3
from datetime import datetime
import requests

# --- CONFIGURATION VOIX ---
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 

def parler(texte):
    try:
        print(f"[JARVIS] : {texte}")
        engine.say(texte)
        engine.runAndWait((
    except:
        pass

# --- MISE À JOUR AUTO ---
def mise_a_jour():
    # Ton lien direct vers GitHub
    Lien_Raw = "https://raw.githubusercontent.com/evancornu474-collab/jarvis-/main/jarvis.py" 
    
    if not Lien_Raw or "http" not in Lien_Raw:
        return

    try:
        # On vérifie s'il y a du nouveau sur GitHub
        r = requests.get(Lien_Raw, timeout=5)
        if r.status_code == 200:
            with open(__file__, "r", encoding="utf-8") as f:
                actuel = f.read()
            
            # Si le code sur GitHub est différent du code sur le PC
            if r.text != actuel:
                parler("Mise à jour système détectée. Synchronisation avec le serveur...")
                with open(__file__, "w", encoding="utf-8") as f:
                    f.write(r.text)
                parler("Mise à jour installée. Redémarrage immédiat.")
                os.execv(sys.executable, ['python'] + sys.argv)
    except Exception as e:
        # En cas d'erreur internet, on lance le programme normalement
        pass

# --- INTERFACE ---
os.system("cls")
print(r"""
  .d8888b.  8888888b.  888     888 d888888b .d8888b. 
 d88P  Y88b 888   Y88b 888     888   `888'  d88P  Y88b 
 Y88b.      888    888 888     888    888   Y88b.     
  "Y888b.   888   d88P Y88b   d88P    888    "Y888b.   
     "Y88b. 8888888P"   "Y88b d88P"    888       "Y88b. 
       888  888  T88b     "Y8888P"     888         888 
 Y88b  d88P 888   T88b      888       .888.  Y88b  d88P 
  "Y8888P"  888    T88b     888     d888888b  "Y8888P"  
                                                       
          [ J.A.R.V.I.S  -  S Y S T E M  V 5.2 ]
          ======================================
""")

# Identification
auth = input("IDENTIFICATION : ").lower().strip()
if auth != "stark":
    print("Accès refusé.")
    sys.exit()

# Lancement de la mise à jour auto au démarrage
mise_a_jour()

parler("Mise à jour réussie. Je suis prêt, Monsieur Stark.")

while True:
    ordre = input("\n[JARVIS] > ").lower().strip()
    
    if not ordre:
        continue

    # --- COMMANDES ---
    if "éteindre" in ordre or "eteindre" in ordre or "stop pc" in ordre:
        parler("Extinction programmée dans 60 secondes.")
        os.system("shutdown -s -t 60")
    
    elif "annuler" in ordre or "stop arrêt" in ordre:
        os.system("shutdown -a")
        parler("Procédure d'arrêt interrompue.")

    elif "quitter" in ordre or "fermer" in ordre:
        parler("Déconnexion. Bonne fin de journée.")
        sys.exit()

    elif "fortnite" in ordre or "fortn" in ordre:
        parler("Lancement de Fortnite.")
        os.system("start com.epicgames.launcher://apps/Fortnite?action=launch&silent=true")

    elif "gta" in ordre:
        parler("Initialisation de GTA.")
        os.system("start com.epicgames.launcher://apps/9d2d0eb64d544454bc5d6a461100293b?action=launch&silent=true")

    elif "anime" in ordre or "sama" in ordre:
        parler("Accès à Anime-Sama.")
        webbrowser.open("https://anime-sama.fr")

    elif "youtube" in ordre:
        parler("Ouverture de YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "heure" in ordre:
        parler(f"Il est précisément {datetime.now().strftime('%H:%M')}.")

    elif "note" in ordre or "bloc" in ordre:
        parler("Ouverture du Bloc-notes.")
        os.system("notepad.exe")

    elif "nettoyer" in ordre or "cls" in ordre:
        os.system("cls")
        parler("Interface réinitialisée.")

    else:
        parler(f"Recherche Google pour : {ordre}")
        webbrowser.open(f"https://www.google.com/search?q={ordre}")
