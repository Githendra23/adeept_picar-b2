import CapteurUltrason
import LEDAvant
import Moteur

import time

moteur = Moteur.Moteur()
capteurUltrason = CapteurUltrason.CapteurUltrason()
ledAvant = LEDAvant.LEDAvant()

if __name__ == "__main__" :
    vitesse = 50
    try :
        while True :
            moteur.avancer(vitesse)
            capteurUltrason.afficher_distance()
            if(capteurUltrason.distance() <= 250) :
                moteur.stop()
                ledAvant.warning()
            time.sleep(0.01)
    except KeyboardInterrupt :
        print("Programme interrompu via le clavier.")
    finally :
        moteur.destroy()