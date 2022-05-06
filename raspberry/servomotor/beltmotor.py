import RPi.GPIO as GPIO

# Definition des pins
M1_En = 21
M1_In1 = 20
M1_In2 = 16

# Creation d'une liste des pins pour chaque moteur pour compacter la suite du code
Pins = [[M1_En, M1_In1, M1_In2]]

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(M1_En, GPIO.OUT)
GPIO.setup(M1_In1, GPIO.OUT)
GPIO.setup(M1_In2, GPIO.OUT)


# Initialisation

def start():
    M1_Vitesse = GPIO.PWM(M1_En, 100)

    M1_Vitesse.start(100)


def sens1(moteurNum):
    GPIO.output(Pins[moteurNum - 1][1], GPIO.HIGH)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.LOW)


def sens2(moteurNum):
    GPIO.output(Pins[moteurNum - 1][1], GPIO.LOW)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.HIGH)


def pause(moteurNum):
    GPIO.output(Pins[moteurNum - 1][1], GPIO.LOW)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.LOW)
    print("Moteur", moteurNum, "arrêt.")


def stop():
    GPIO.output(Pins[0][1], GPIO.LOW)
    GPIO.output(Pins[0][2], GPIO.LOW)
    print("Moteurs arrêtés.")

# stop()
#
# print("Moteur 1 tourne dans le sens 1.")
# sens1(1)
# sleep(3)
# stop()
# sleep(3)
# print("Moteur 1 tourne dans le sens 2.")
# sens2(1)
# sleep(2)
# pause(1)
# sleep(1)
#
# print("Moteur 1 tourne dans le sens 1.")
# while True:
#     sens1(1)
