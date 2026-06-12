from gpiozero import InputDevice
import time

class CapteurSuiviLigne:
    _broche_ligne_gauche = 22
    _broche_ligne_milieu = 27
    _broche_ligne_droite = 17

    def __init__(self):
        self._capteur_gauche = InputDevice(pin=self._broche_ligne_gauche)
        self._capteur_milieu = InputDevice(pin=self._broche_ligne_milieu)
        self._capteur_droite = InputDevice(pin=self._broche_ligne_droite)

    def statut_gauche(self):
        return self._capteur_gauche.value

    def statut_milieu(self):
        return self._capteur_milieu.value

    def statut_droite(self):
        return self._capteur_droite.value

    def state(self) :
        return (
            self._capteur_gauche,
            self._capteur_milieu,
            self._capteur_droite
        )

    def printState(self) :
        print(f"Capteur gauche : {self.statut_gauche()}")
        print(f"Capteur central : {self.statut_milieu()}")
        print(f"Capteur droit : {self.statut_droite()}")