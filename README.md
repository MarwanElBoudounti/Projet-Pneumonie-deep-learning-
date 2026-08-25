# 🫁 Détection de pneumonie par Deep Learning

Application web interactive capable d'analyser une radiographie thoracique et d'estimer si elle correspond à une image **NORMALE** ou compatible avec une **PNEUMONIE**.

Le projet combine un modèle de vision par ordinateur basé sur **MobileNetV2** et une interface **Streamlit** simple à utiliser. Il a été réalisé dans le cadre d'un projet académique en Deep Learning.

> ⚠️ **Avertissement important :** ce projet est expérimental et pédagogique. Il ne constitue pas un dispositif médical, ne remplace pas l'avis d'un professionnel de santé et ne doit pas être utilisé pour établir un diagnostic.

## ✨ Fonctionnalités

- Import d'une radiographie au format `JPG`, `JPEG` ou `PNG`.
- Prévisualisation de l'image chargée.
- Prétraitement automatique : conversion RGB, redimensionnement en `224 × 224` et normalisation des pixels.
- Classification binaire par modèle TensorFlow/Keras.
- Affichage d'une estimation pour les classes **PNEUMONIE** ou **NORMAL**.
- Mise en cache du modèle pour éviter de le recharger à chaque interaction.

## 🧠 Modèle de Deep Learning

Le modèle a été construit dans le notebook [`Copie_de_Untitled1.ipynb`](Copie_de_Untitled1.ipynb) à partir de **MobileNetV2** pré-entraîné sur ImageNet :

```text
MobileNetV2 (poids ImageNet, base gelée)
    ↓
GlobalAveragePooling2D
    ↓
Dense(128, activation="relu")
    ↓
Dropout(0.5)
    ↓
Dense(1, activation="sigmoid")
```

### Préparation des données

- Taille cible : `224 × 224` pixels.
- Normalisation : valeurs des pixels ramenées entre `0` et `1`.
- Augmentation sur l'ensemble d'entraînement : rotation par cisaillement, zoom et retournement horizontal.
- Validation et test : normalisation uniquement, sans augmentation.
- Fonction de perte : `binary_crossentropy`.
- Optimiseur : `Adam`.
- Entraînement prévu dans le notebook : `10` époques avec une taille de lot de `32`.

Le modèle entraîné est stocké dans [`modele_pneumonie_v1.h5`](modele_pneumonie_v1.h5). La sortie sigmoid est interprétée avec un seuil de `0,5` dans l'application.

## 🏗️ Architecture du projet

```text
Projet_Pneumonie/
├── app.py                              # Interface Streamlit et prédiction
├── Copie_de_Untitled1.ipynb             # Téléchargement des données et entraînement
├── modele_pneumonie_v1.h5               # Modèle Keras entraîné
├── images_test/
│   └── test/
│       ├── NORMAL/                      # Images de test normales
│       └── PNEUMONIA/                   # Images de test avec pneumonie
├── Présentation pptx.pptx              # Présentation du projet
├── Rapport projet deep learning ...pdf  # Rapport académique
└── terminale pour projet marche sur vs code.txt
```

## ⚙️ Installation locale

### Prérequis

- Python 3.9 ou version ultérieure.
- Un environnement virtuel Python recommandé.
- TensorFlow, NumPy, Pillow et Streamlit.

### Installation sous Windows

```bash
python -m venv venv
.\venv\Scripts\activate
python -m pip install --upgrade pip
pip install streamlit tensorflow numpy pillow
```

### Lancement de l'application

Depuis le dossier du projet :

```bash
streamlit run app.py
```

L'application sera accessible à l'adresse suivante : `http://localhost:8501`.

## 🧪 Utilisation

1. Ouvrir l'application Streamlit.
2. Cliquer sur le sélecteur de fichier.
3. Importer une radiographie au format `JPG`, `JPEG` ou `PNG`.
4. Cliquer sur **Analyser**.
5. Consulter la classe prédite et le score affiché.

Le fichier [`images_test/`](images_test/) contient des exemples organisés selon les deux classes utilisées par le projet.

## 🔬 Reproduire l'entraînement

Le notebook contient les étapes suivantes :

1. Téléchargement du dataset `chest-xray-pneumonia` depuis Kaggle.
2. Exploration des dossiers `train`, `val` et `test`.
3. Création des générateurs d'images avec augmentation.
4. Construction et entraînement du modèle MobileNetV2.
5. Évaluation sur l'ensemble de test.
6. Visualisation de l'évolution de l'accuracy et de la loss.
7. Sauvegarde du modèle au format `.h5`.

Pour reproduire cette étape, configurez vos identifiants Kaggle dans l'environnement d'exécution ou utilisez un fichier `kaggle.json` local. **Ne publiez jamais une clé Kaggle dans un notebook ou un dépôt GitHub.**

## 📊 Évaluation

Le notebook calcule l'accuracy sur le dossier de test et trace les courbes d'apprentissage pour l'entraînement et la validation. Les résultats peuvent varier selon la version de TensorFlow, la préparation des données et l'environnement d'exécution ; aucune métrique fixe n'est déclarée ici comme résultat officiel du dépôt.

Pour une évaluation sérieuse, il est recommandé de compléter le projet avec une matrice de confusion, la précision, le rappel, le F1-score, l'AUC-ROC et une analyse des faux négatifs.

## 🛠️ Technologies

| Domaine | Technologies |
| --- | --- |
| Langage | Python |
| Deep Learning | TensorFlow, Keras |
| Modèle | MobileNetV2, transfert d'apprentissage |
| Traitement d'images | Pillow, NumPy |
| Interface web | Streamlit |
| Données | Chest X-Ray Pneumonia, Kaggle |
| Exploration | Jupyter Notebook |

## 🔐 Sécurité et bonnes pratiques

- Ne commitez pas de clés API, mots de passe ou fichiers de credentials.
- Si une clé Kaggle a déjà été publiée, révoquez-la et générez-en une nouvelle.
- Le modèle et les prédictions doivent être utilisés uniquement dans un contexte de recherche ou d'apprentissage.
- Vérifiez la licence et les conditions d'utilisation du dataset avant toute redistribution.

## 👤 Auteur
El Boudounti Marwan , 
Projet académique de détection de pneumonie par analyse de radiographies thoraciques.

---

