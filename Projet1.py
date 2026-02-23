import streamlit as st

#Configuration de la page
st.set_page_config(
    page_title = "IMC by Boubou SY",
    layout = "centered"
)

#PARTIE SIDEBAR
with st.sidebar:
    with st.container(border=True):
        st.image("ah.jpg")
    for _ in range(16):
        st.write("")
    st.success("🏥 Votre santé est votre bien le plus précieux. Ne l'oubliez jamais ! ❤️‍🩹")

with st.container(border=True):
    st.title("Calcul des IMC")

poids = st.number_input("Entrez votre poids")
taille = st.number_input("Entrez votre taille")

if st.button("Calculer"):
    
    IMC=poids/(taille**2)
    st.write("L'IMC est de", IMC)
    
    if IMC < 18.5:
        st.warning("Vous étes maigre.")
        
    elif 18.5 < IMC < 25:
        st.success("Vous avez un poids normal.")
        
    elif 25 < IMC < 30:
        st.warning("Attention ! Vous étes en surpoids.")

    else :
        st.write("Votre catégorie n'est pas prise en compte.")
