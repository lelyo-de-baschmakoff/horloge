import time

def afficher_heure(heure, mode):
    heures, minutes, secondes = heure
    if mode == 12:
        am_pm = "AM" if heures < 12 else "PM"
        heures %= 12
        heures = 12 if heures == 0 else heures
        print(f"{heures:02d}:{minutes:02d}:{secondes:02d} {am_pm}")
    elif mode == 24:
        print(f"{heures:02d}:{minutes:02d}:{secondes:02d}")

def actualiser_heure(heure_initiale, heure_alarme, mode):
    while True:
        afficher_heure(heure_initiale, mode)
        verifier_alarme(heure_initiale, heure_alarme)
        heure_initiale = incrementer_seconde(heure_initiale)
        time.sleep(1)

def incrementer_seconde(heure):
    heures, minutes, secondes = heure
    secondes += 1
    if secondes == 60:
        secondes = 0
        minutes += 1
        if minutes == 60:
            minutes = 0
            heures += 1
            if heures == 24:
                heures = 0
    return heures, minutes, secondes

def regler_alarme(heure):
    print(f"Alarme réglée pour {heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}")

def verifier_alarme(heure_actuelle, heure_alarme):
    if heure_actuelle == heure_alarme:
        print("Réveillez-vous ! L'alarme sonne.")

def choisir_mode():
    while True:
        print("Choisissez le mode d'affichage :")
        print("1. 12 heures")
        print("2. 24 heures")
        choix = input("Entrez 1 ou 2 pour sélectionner le mode : ")
        if choix == '1':
            return 12
        elif choix == '2':
            return 24
        else:
            print("Choix invalide. Veuillez sélectionner 1 ou 2.")

heure_initiale = (16, 30, 0)
heure_alarme = (16, 30, 10)

mode = choisir_mode()

afficher_heure(heure_initiale, mode)

regler_alarme(heure_alarme)

actualiser_heure(heure_initiale, heure_alarme, mode)
