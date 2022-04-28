from time import sleep

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
M1_Vitesse = GPIO.PWM(M1_En, 100)

M1_Vitesse.start(100)


def sens1(moteurNum):
    GPIO.output(Pins[moteurNum - 1][1], GPIO.HIGH)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.LOW)


def sens2(moteurNum):
    GPIO.output(Pins[moteurNum - 1][1], GPIO.LOW)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.HIGH)


def arret(moteurNum):
    GPIO.output(Pins[moteurNum - 1][1], GPIO.LOW)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.LOW)
    print("Moteur", moteurNum, "arret.")


def arretComplet():
    GPIO.output(Pins[0][1], GPIO.LOW)
    GPIO.output(Pins[0][2], GPIO.LOW)
    print("Moteurs arretes.")


arretComplet()

print("Moteur 1 tourne dans le sens 1.")
sens1(1)
sleep(3)
arretComplet()
sleep(3)
print("Moteur 1 tourne dans le sens 2.")
sens2(1)
sleep(2)
arret(1)
sleep(1)

print("Moteur 1 tourne dans le sens 1.")
while True:
    sens1(1)

# je dois recup le flux video de la camera pr comme ca quand je lui montre un objet avec le code de romeo elle fait
# bouger le servomoteur en fonction sachant que romeo (il est plus la ce soir il re dm ) ma dit que quand il montrre un
# objet a la cam de son ordi l'ia arr a savoir c quoi ducoup je me demande comment faire les liens
# car pr le moment c je tape python3 et le prog du servo
