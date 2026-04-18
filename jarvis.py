import os
import sys
import webbrowser
import pyttsx3
from datetime import datetime
import requests

# --- CONFIGURATION VOIX ---
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Si la voix ne te plaît pas, change 0 par 1 ci-dessous
engine.setProperty('voice', voices[0].id) 

def parler(texte):
    try:
        print(f"[JARVIS] : {texte}")
        engine.say(texte)
        engine.runAndWait()
    except:
        pass

# --- MISE À JOUR AUTO (GITHUB) ---
def mise_a_jour():
    # Ton lien direct vers ton dépôt GitHub
    Lien_Raw = "https://raw.githubusercontent.com/evancornu474-collab/jarvis-/main/jarvis.py" 
    
    try:
        r = requests.get(Lien_Raw, timeout=5)
        if r.status_code == 200:
            with open(__file__, "r", encoding="utf-8") as f:
                actuel = f.read()
            
            # Comparaison du code local et du code GitHub
            if r.text.strip() != actuel.strip():
                parler("Mise à jour système détectée. Synchronisation en cours...")
                with open(__file__, "w", encoding="utf-8") as f:
                    f.write(r.text)
                parler("Mise à jour installée. Redémarrage du noyau.")
                
                # Relance le script automatiquement
                os.execv(sys.executable, ['python'] + sys.argv)
    except:
        # Si pas d'internet ou erreur, JARVIS continue normalement
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

# Vérification de la mise à jour dès l'identification réussie
mise_a_jour()

parler("bonjour mr stark")

while True:
    ordre = input("\n[JARVIS] > ").lower().strip()
    
    if not ordre:
        continue

    # --- COMMANDES ---
    if "éteindre" in ordre or "eteindre" in ordre or "stop pc" in ordre:
        parler("Extinction du PC dans 60 secondes.")
        os.system("shutdown -s
