from machine import Pin
import time
from servo import Servo  # si tu as sauvegardé la classe dans un fichier servo.py
# ou si la classe est dans le même fichier, pas besoin d'importer

# Initialisation des pins
capteur_pin = Pin(28, Pin.IN)
led_verte = Pin(17, Pin.OUT)
led_rouge = Pin(18, Pin.OUT)

# Initialisation du servo sur GPIO16
servo = Servo(16)

while True:
    if capteur_pin.value() == 1:
        led_verte.on()
        led_rouge.off()
        
        # Déplacer le servo à 180°
        servo.move(180)
        time.sleep(5)  # Attendre 5 secondes
        servo.move(0)  # Revenir à 0°
        
        # Attendre que le capteur repasse à 0 avant de réagir à nouveau
        while capteur_pin.value() == 1:
            time.sleep(0.1)
        
    else:
        led_verte.off()
        led_rouge.on()
    
    time.sleep(0.1)
