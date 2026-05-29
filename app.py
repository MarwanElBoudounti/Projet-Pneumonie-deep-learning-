import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Interface
st.set_page_config(page_title="Détecteur de Pneumonie", page_icon="🫁")
st.title("Analyseur de Radiographies 🫁")

# Chargement du modèle
@st.cache_resource
def load_my_model():
    # Vérifie que le fichier .h5 est bien dans le même dossier
    return tf.keras.models.load_model('modele_pneumonie_v1.h5')

model = load_my_model()

# Upload
uploaded_file = st.file_uploader("Charger une radio (JPG, PNG)...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Radio chargée", use_container_width=True)
    
    # Prétraitement
    img = image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Prédiction
    if st.button("Analyser"):
        prediction = model.predict(img_array)
        resultat = prediction[0][0]
        
        if resultat > 0.5:
            st.error(f"⚠️ PNEUMONIE DÉTECTÉE ({resultat*100:.2f}%)")
        else:
            st.success(f"✅ NORMAL ({(1-resultat)*100:.2f}%)")