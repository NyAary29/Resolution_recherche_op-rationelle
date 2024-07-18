from dotenv import load_dotenv
import os
import google.generativeai as genai
from PIL import Image
import streamlit as st

# Charger les variables d'environnement depuis un fichier .env
load_dotenv()

# Configurer l'API Google avec la clé API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Fonction pour obtenir une réponse de Gemini
def get_gemini_response(input_text, image_data, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input_text, image_data[0], prompt])
    return response.candidates[0].content.parts[0].text

# Fonction pour configurer l'image téléchargée
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }]
        return image_parts
    else:
        raise FileNotFoundError("Pas de photo")

# Configurer la page Streamlit
st.set_page_config(page_title="Gemini image demo")
st.header("Gemini application")

# Texte de l'invite pour Gemini
input_text = """
Please analyze the provided image and respond strictly in the following format:

### Solution
**Objective:** Maximize Z = a1*x1 + a2*x2 + ... + an*xn

**Constraints:**
- c1: a1*x1 + a2*x2 <= b1
- c2: a1*x1 + a2*x2 <= b2
- ...

**Solution :**
1. Steps of the simplex method
2. Optimal values: x1 = v1, x2 = v2, ...
3. Optimal value of the objective function: Z = v

Do not include any additional information or commentary outside this format.
"""

# Fonction pour télécharger un fichier image
uploaded_file = st.file_uploader("Choisis une image ...", type=["jpg", "png", "jpeg"])

# Afficher l'image téléchargée
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Bouton pour soumettre l'image
submit = st.button("Décris-moi l'image")

# Texte de l'invite pour l'expert en recherche opérationnelle
input_prompt = """
You are an expert in operations research and mathematical expert
"""

# Actions à effectuer lors du clic sur le bouton
if submit:
    try:
        # Configurer l'image pour l'envoi à Gemini
        image_data = input_image_setup(uploaded_file)
        
        # Obtenir la réponse de Gemini
        response = get_gemini_response(input_prompt, image_data, input_text)
        
        # Afficher la réponse de Gemini
        st.subheader("La réponse de Gemini :")
        st.write(response)
    except FileNotFoundError as e:
        st.error(str(e))
    except Exception as e:
        st.error(f"Une erreur est survenue : {str(e)}")
