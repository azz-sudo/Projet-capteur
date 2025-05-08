from machine import Pin
import time
from servo import Servo  # si ta classe est dans un fichier séparé

# Configuration du capteur
capteur_pin = Pin(28, Pin.IN, Pin.PULL_UP)

# Configuration des broches RGB (anode commune : LOW = allumé)
led_rouge = Pin(13, Pin.OUT)
led_verte = Pin(12, Pin.OUT)
led_bleue = Pin(11, Pin.OUT)  # non utilisé, mais tu peux ajouter une couleur

# Configuration du servo (GPIO16)
servo = Servo(16)

# Fonction pour contrôler les couleurs de la LED
def set_rgb(r, g, b):
    led_rouge.value(0 if r else 1)
    led_verte.value(0 if g else 1)
    led_bleue.value(0 if b else 1)

while True:

    print(capteur_pin.value())

    if capteur_pin.value() == 1:
        # Capteur actif → LED rouge, servo active
        set_rgb(0, 0, 1)  # rouge
        servo.move(180)
        time.sleep(5)
        servo.move(0)

        # Attendre que le capteur repasse à 0
        #while capteur_pin.value() == 1:
         #   time.sleep(0.1)

    else:
        # Capteur inactif → LED verte, pas d'action
        set_rgb(0, 1, 0)  # vert

    time.sleep(0.1)
