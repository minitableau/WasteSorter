import time

import cv2

from artificial_intelligence.detection import detect
from servomotor import servomotor, beltmotor

cam = cv2.VideoCapture(2)


def start():
    print("Démarrage du programme WasteSorter !")
    # servomotor.start()
    time.sleep(2)
    beltmotor.sens1(1)
    time.sleep(2)
    beltmotor.stop()
    time.sleep(2)
    beltmotor.sens2(1)
    time.sleep(3)
    beltmotor.stop()
    time.sleep(2)

    while True:
        ret, image = cam.read()

        if not ret:
            continue

        beltmotor.sens1(1)

        classname, confidence = detect(image)
        print("Détection d'un", classname, "avec une confiance de", confidence)

        if classname != "boite" and confidence > 67:
            definedAngle = servomotor.object_to_angle[classname]
            if definedAngle:
                servomotor.rotate(definedAngle)
                time.sleep(10)
                servomotor.rotate(75)

    servomotor.stop()
    beltmotor.stop()


if __name__ == '__main__':
    start()
