# Resolution_recherche_op-rationelle
# Résolution de Problèmes de Recherche Opérationnelle avec Google AI et Streamlit

Ce projet utilise l'API Google AI Gemini-Pro et Streamlit pour résoudre des problèmes de recherche opérationnelle à partir d'une image. Le projet est conçu pour extraire les informations pertinentes d'une image contenant un problème de recherche opérationnelle et les résoudre en utilisant la méthode du simplexe.

## Fonctionnalités

- Extraction automatique de la fonction objectif, des variables de décision et des contraintes à partir d'une image.
- Résolution de problèmes de maximisation et de minimisation en utilisant la méthode du simplexe.
- Affichage de toutes les étapes de la résolution de manière mathématique.
- Interface utilisateur interactive avec Streamlit.

## Prérequis

- Python 3.8 ou plus récent
- Compte Google Cloud avec accès à l'API Google AI Gemini-Pro
- Bibliothèques Python : `streamlit`, `pyomo`, `google-api-python-client`, `PIL` (Pillow)

## Installation

1. Clonez ce dépôt :

    ```bash
    git clone https://github.com/votre_nom_utilisateur/votre_projet.git
    cd votre_projet
    ```

2. Créez un environnement virtuel et activez-le :

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
    ```

3. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

4. Configurez vos informations d'authentification Google Cloud pour accéder à l'API Google AI Gemini-Pro.

## Utilisation

1. Lancez l'application Streamlit :

    ```bash
    streamlit run app.py
    ```

2. Téléchargez une image contenant un problème de recherche opérationnelle.

3. Cliquez sur le bouton `Décris-moi l'image` pour extraire les informations pertinentes.

4. Cliquez sur le bouton `Résoudre` pour obtenir la solution du problème et afficher toutes les étapes.

## Structure du Projet

- `app.py` : Fichier principal de l'application Streamlit.
- `extractor.py` : Module pour l'extraction des informations à partir de l'image.
- `solver.py` : Module pour la résolution du problème de recherche opérationnelle.
- `requirements.txt` : Liste des dépendances Python.

## Contribution

Les contributions sont les bienvenues ! Veuillez soumettre une demande de tirage (pull request) avec une description des modifications.

## Auteurs
NyAary29


