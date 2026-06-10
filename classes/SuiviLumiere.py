import CapteurUltrason
import LEDAvant
import Moteur
#import CapteurLumiere

import sys
import time
import threading

moteur = Moteur.Moteur()
capteurUltrason = CapteurUltrason.CapteurUltrason()
ledAvant = LEDAvant.LEDAvant()
# capteurLumiere = CapteurLumiere.CapteurLumiere()

caractere = '0'
programme_actif = True

def lire_clavier():
    global caractere, programme_actif

    while programme_actif:
        caractere = input("M pour avancer")
        print(f"Caractère reçu : {caractere}")

if __name__ == "__main__":
    vitesse = 30

    try:
        threading.Thread(target=lire_clavier, daemon=True).start()

        while True:
            distance = capteurUltrason.distance()
            capteurUltrason.afficherDistance()

            if caractere == 'A' or caractere == 'a' or distance <= 200:
                moteur.stop()
                ledAvant.warning()
                time.sleep(1)
                moteur.reculer(vitesse)
                time.sleep(5)
            elif caractere == 'M' or caractere == 'm':
                moteur.avancer(vitesse)
            elif caractere == 'S' or caractere == 's':
                moteur.reculer(vitesse)
            elif caractere == 'Q' or caractere == 'q':
                print("Arrêt demandé.")
                break

            time.sleep(0.01)
    except KeyboardInterrupt:
        print("Programme interrompu via le clavier.")
    finally:
        programme_actif = False
        moteur.stop()
        moteur.destroy()