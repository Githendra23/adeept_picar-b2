import time
import Roues
import ServoController
import CapteurSuiviLigne

ETAT_0, ETAT_1, ETAT_2, ETAT_3, ETAT_4 = range(5)

TRANSITIONS = {
    ETAT_0: {(0,1,1): ETAT_1, (1,1,0): ETAT_3},
    ETAT_1: {(1,1,1): ETAT_0, (0,0,1): ETAT_2},
    ETAT_2: {(1,1,1): ETAT_3, (0,1,1): ETAT_1},
    ETAT_3: {(1,1,1): ETAT_0, (1,0,0): ETAT_4},
    ETAT_4: {(1,1,1): ETAT_1, (1,1,0): ETAT_3},
}

ANGLES_RELATIFS = {
    ETAT_0:  0,
    ETAT_1: +30,
    ETAT_2: +60,
    ETAT_3: -30,
    ETAT_4: -60,
}

def suivi_ligne():
    capteur = CapteurSuiviLigne.CapteurSuiviLigne()
    roues = Roues.Roues(ServoController())
    centre = roues.getAngleCenter()
    etat = ETAT_0

    print("ICI 1")

    while True:

        print("ICI 2")
        statut = capteur.statut()
        nouvel_etat = TRANSITIONS.get(etat, {}).get(statut, etat)

        if nouvel_etat != etat:
            etat = nouvel_etat
            print(f"État -> {etat}, capteurs={statut}")

        delta = ANGLES_RELATIFS.get(etat, 0)
        angle = max(roues.getAngleMin(), min(centre + delta, roues.getAngleMax()))
        roues.turn(angle)

        time.sleep(0.05)


if __name__ == "__main__" :
    suivi_ligne()
