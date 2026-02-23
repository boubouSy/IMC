import streamlit as st

#PARTIE SIDEBAR
with st.sidebar:
    with st.container(border=True):
        st.image("ah.jpg")
    for _ in range(18):
        st.write("")
    st.success("De la part de votre serviteur Boubou SY ! 👋")

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
