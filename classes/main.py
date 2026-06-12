import CapteurSuiviLigne
import Moteur


import time



if __name__ == '__main__':
    try:
        moteur = Moteur()
        moteur.avancer(30)
        capteur_ligne = CapteurSuiviLigne()

        while True:
            capteur_ligne.printState()
            time.sleep(0.2)

    except KeyboardInterrupt:
        print("Fin du programme via le clavier.")