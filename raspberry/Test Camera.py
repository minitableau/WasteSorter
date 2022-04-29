import cv2

# On accède à la webcam
cam = cv2.VideoCapture(0)

# On prend une photo
ret, image = cam.read()

# Paramètre pour définir la fenêtre
nom_fenetre = "video_cam"

largeur_image = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
hauteur_image = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

cv2.namedWindow(nom_fenetre, cv2.WND_PROP_FULLSCREEN)

# Tout le temps
while True:
    # On prend une photo, ahh c'est pas en temps réel ?
    ret, image = cam.read()
    if ret:

        # On afffiche la fenêtre avec notre image
        cv2.imshow(nom_fenetre, image)

        # On ajoute un temps d'attente
        # et on arrête la boucle si on appuie sur la touche 'q'
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

