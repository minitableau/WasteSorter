# Initialisation
M1_Vitesse = GPIO.PWM(M1_En, 1000)
M1_Vitesse.start(50)  # On entre ici un rapport cyclique entre 0 et 100 (pourcentages)

# Changement des valeurs
M1_Vitesse.ChangeFrequency(1000)
M1_Vitesse.ChangeDutyCycle(50)

# Arret de la modulation
M1_Vitesse.stop()
