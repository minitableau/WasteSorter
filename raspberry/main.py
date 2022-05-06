import time

import cv2

import raspberry.servomotor.beltmotor as beltmotor
import raspberry.servomotor.servomotor as servomotor
from raspberry.artificial_intelligence.detection import detect

cam = cv2.VideoCapture(0)


def start():
    print("Démarrage du programme WasteSorter !")
    servomotor.start()
    time.sleep(2)
    beltmotor.start()

    while True:
        ret, image = cam.read()

        if not ret:
            continue

        classname, confidence = detect(image)
        print("Détection d'un", classname, "avec une confiance de", confidence)

        if classname != "boite" and confidence > 0.6:
            definedAngle = servomotor.object_to_angle[classname]
            if definedAngle:
                servomotor.rotate(definedAngle)

        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    servomotor.stop()
    beltmotor.stop()


if __name__ == '__main__':
    start()
