# 🌍 Station Automatisée de Tri des Déchets / Automated Waste Sorting Station  

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)  
[![Raspberry Pi](https://img.shields.io/badge/RaspberryPi-4-red.svg)](https://www.raspberrypi.com/)  
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)  

## 📌 À propos du projet / About the project  

### 🔹 Français 🇫🇷  
Le tri des déchets est un enjeu écologique majeur. Ce projet vise à **automatiser le tri des déchets** en utilisant l’intelligence artificielle et un système embarqué. Grâce à un **réseau de neurones entraîné** sur des images de déchets, une caméra et un **Raspberry Pi 4**, notre station détecte et trie automatiquement différents types de déchets.  

### 🔹 English 🇬🇧  
Waste sorting is a major environmental challenge. This project aims to **automate waste sorting** using artificial intelligence and an embedded system. Thanks to a **trained neural network** on waste images, a camera, and a **Raspberry Pi 4**, our station automatically detects and sorts different types of waste.  

---

## 🌟 Fonctionnalités clés / Key Features  

✅ **Détection automatique** des déchets grâce à un réseau de neurones 🎯  
✅ **Utilisation d’un Raspberry Pi 4** pour l'analyse et le contrôle mécanique 🖥️  
✅ **Tapis roulant fait maison** pour transporter les déchets 🚀  
✅ **Tri via servomoteur** pour rediriger les déchets vers la bonne poubelle ♻️  
✅ **Extensible** : possibilité d'ajouter de nouveaux types de déchets 📈  

✅ **Automatic waste detection** via a neural network 🎯  
✅ **Raspberry Pi 4** for analysis and mechanical control 🖥️  
✅ **Custom conveyor belt** for waste transport 🚀  
✅ **Servo-controlled sorting** to direct waste to the correct bin ♻️  
✅ **Extensible**: can be trained for more waste categories 📈  

---

## 🛠️ Technologies utilisées / Technologies Used  

### 🔹 Français 🇫🇷  
- 🔬 **IA & Machine Learning** : TensorFlow / Keras pour la reconnaissance des déchets  
- 📷 **Traitement d’image** : OpenCV pour l'analyse du flux vidéo  
- 🖥️ **Systèmes embarqués** : Raspberry Pi 4 (8Go)  
- 🛠️ **Mécanique** : Servomoteur, moteur et tapis roulant DIY  

### 🔹 English 🇬🇧  
- 🔬 **AI & Machine Learning**: TensorFlow / Keras for waste recognition  
- 📷 **Image Processing**: OpenCV for video analysis  
- 🖥️ **Embedded Systems**: Raspberry Pi 4 (8GB RAM)  
- 🛠️ **Hardware**: Servo motor, DC motor, and a DIY conveyor belt  

---

## 📸 Aperçu du projet / Project Overview  

Example:  
![Tri des déchets en action](./images/waste_sorting_demo.gif)  

---

## 📂 Structure du projet / Project Structure  

```bash
📂 WasteSorter/
    │──📂 raspberry/
        │── 📁 artificial_intelligence/
        │── 📁 servomotor/            
        │── 📜 Test Camera.py 
        │── 📜 main.py
        │── 📜 requirements.txt                  
    │── 📜 README.md                       
    │── 📜 Poster TIPE - CORREC & TABLEAU (2).pdf
    │── 📜 Rapport_TIPE_CORREC_TABLEAU.pdf
```

## 🚀 Installation & Utilisation / Installation & Usage  

### 🛠️ Prérequis / Requirements  

#### 🇫🇷 Français  
- Un **Raspberry Pi 4** avec **Raspberry Pi OS** installé  
- **Python 3.x** et les bibliothèques nécessaires (voir `requirements.txt`)  

#### 🇬🇧 English  
- A **Raspberry Pi 4** with **Raspberry Pi OS** installed  
- **Python 3.x** and required libraries (see `requirements.txt`)  

---

### 🔧 Installation  

#### 1️⃣ Cloner le projet / Clone the project  
```bash
git clone https://github.com/minitableau/WasteSorter.git
cd WasteSorter
```

#### 2️⃣ Installer les dépendances / Install dependencies
```bash
pip install -r raspberry/requirements.txt
```
#### 3️⃣ Lancer l’entraînement du modèle IA / Train the AI model (optionnel / optional)
```bash
python raspberry/artificial_intelligence/training.py.py
```
#### 4️⃣ Démarrer la station de tri / Start the sorting station
```bash
python raspberry/main.py
```

## 📌 Améliorations & Perspectives / Future Improvements  

### 🇫🇷 Français  
- ✔️ **Ajouter plus de classes de déchets** pour un tri plus précis  
- ✔️ **Optimiser la consommation énergétique** pour une utilisation continue  

### 🇬🇧 English  
- ✔️ **Add more waste categories** for better sorting  
- ✔️ **Optimize energy consumption** for continuous operation  

---

## 👨‍💻 À propos de moi / About Me  

### 🇫🇷 Français  
Je suis passionné par **l’intelligence artificielle et l’automatisation**.  
📫 **Contact** : minitableau2002@gmail.com 

Si ce projet t’intéresse ou que tu veux en discuter, **n’hésite pas à me contacter !** 🚀  

### 🇬🇧 English  
I am passionate about **artificial intelligence and automation**.  
📫 **Contact**: minitableau2002@gmail.com  

If this project interests you or if you want to discuss it, **feel free to reach out!** 🚀  

---

## ⭐ Support  

Si ce projet t’a aidé ou t’intéresse, **laisse une ⭐ sur GitHub !** 😊  
If you found this project helpful or interesting, **leave a ⭐ on GitHub!** 😊  

