import RPi.GPIO as GPIO
import CapteurSuiviLigne

if __name__ == '__main__':
    try:
        while True:
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Fin de programme par Ctrl-C")
    finally:
        GPIO.cleanup()  # réinitialise les ports GPIO (ou celle de gpiozero)
        # ou appeler une fonction perso adaptée au robot
        print("Nettoyage final réalisé")
