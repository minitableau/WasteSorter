from time import sleep

import RPi.GPIO as GPIO

# Definition des pins
M1_En = 21
M1_In1 = 20
M1_In2 = 16

M2_En = 18
M2_In1 = 23
M2_In2 = 24

# Creation d'une liste des pins pour chaque moteur pour compacter la suite du code
Pins = [[M1_En, M1_In1, M1_In2], [M2_En, M2_In1, M2_In2]]

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(M1_En, GPIO.OUT)
GPIO.setup(M1_In1, GPIO.OUT)
GPIO.setup(M1_In2, GPIO.OUT)

GPIO.setup(M2_En, GPIO.OUT)
GPIO.setup(M2_In1, GPIO.OUT)
GPIO.setup(M2_In2, GPIO.OUT)

# Voir aide dans le tuto

M2_Vitesse = GPIO.PWM(M2_En, 100)

# Initialisation
M1_Vitesse = GPIO.PWM(M1_En, 100)
M1_Vitesse.start(5)  # On entre ici un rapport cyclique entre 0 et 100 (pourcentages) # inutile ?

# Changement des valeurs
M1_Vitesse.ChangeFrequency(100)  # inutile ?
M1_Vitesse.ChangeDutyCycle(5)  # inutile ?

M1_Vitesse.start(100)
M2_Vitesse.start(100)


def sens1(moteurNum):
    GPIO.output(Pins[moteurNum - 1][1], GPIO.HIGH)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.LOW)
    print("Moteur", moteurNum, "tourne dans le sens 1.")


def sens2(moteurNum):
    GPIO.output(Pins[moteurNum - 1][1], GPIO.LOW)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.HIGH)
    print("Moteur", moteurNum, "tourne dans le sens 2.")


def arret(moteurNum):
    GPIO.output(Pins[moteurNum - 1][1], GPIO.LOW)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.LOW)
    print("Moteur", moteurNum, "arret.")


def arretComplet():
    GPIO.output(Pins[0][1], GPIO.LOW)
    GPIO.output(Pins[0][2], GPIO.LOW)
    GPIO.output(Pins[1][1], GPIO.LOW)
    GPIO.output(Pins[1][2], GPIO.LOW)
    print("Moteurs arretes.")


arretComplet()

sens1(1)
sleep(3)
arretComplet()
sleep(3)
sens2(1)
sleep(2)
arret(1)
sleep(1)

while True:
    sens1(1)

# je dois recup le flux video de la camera pr comme ca quand je lui montre un objet avec le code de romeo elle fait
# bouger le servomoteur en fonction sachant que romeo (il est plus la ce soir il re dm ) ma dit que quand il montrre un
# objet a la cam de son ordi l'ia arr a savoir c quoi ducoup je me demande comment faire les liens
# car pr le moment c je tape python3 et le prog du servo
