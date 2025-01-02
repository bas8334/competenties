import streamlit as st

# Maak een dropdown-menu met de niveaus
niveau = st.selectbox('Kies een niveau:', ['niveau 1', 'niveau 2', 'niveau 3'])

# Toon verschillende invulvelden afhankelijk van het geselecteerde niveau
if niveau == 'niveau 1':
    advies = st.text_input('Advies')
    rekenen = st.text_input('Rekenen')
    taal = st.text_input('Taal')
elif niveau == 'niveau 2':
    denken = st.text_input('Denken')
    leren = st.text_input('Leren')
    spelen = st.text_input('Spelen')
elif niveau == 'niveau 3':
    schaken = st.text_input('Schaken')
    dammen = st.text_input('Dammen')
    voetballen = st.text_input('Voetballen')
