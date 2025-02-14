import streamlit as st

def calcul_potentiel_cartes(population, entreprises, agents_municipaux, commerces,
                            taux_adoption_b2c, valeur_carte_b2c,
                            taux_adoption_b2b, valeur_carte_b2b,
                            taux_adoption_b2g, valeur_carte_b2g,
                            taux_adhesion_commerces):
    # Calcul du potentiel B2C
    potentiel_b2c = population * taux_adoption_b2c * valeur_carte_b2c
    
    # Calcul du potentiel B2B
    potentiel_b2b = entreprises * taux_adoption_b2b * valeur_carte_b2b
    
    # Calcul du potentiel B2G
    potentiel_b2g = agents_municipaux * taux_adoption_b2g * valeur_carte_b2g
    
    # Nombre de commerçants acceptant la carte
    commercants_acceptant = commerces * taux_adhesion_commerces
    
    # Potentiel total
    potentiel_total = potentiel_b2c + potentiel_b2b + potentiel_b2g
    
    return potentiel_b2c, potentiel_b2b, potentiel_b2g, potentiel_total, commercants_acceptant

# Interface utilisateur avec Streamlit
st.title("Calculateur du Potentiel de Vente des Cartes Cadeaux Locales")

# Entrées utilisateur
population = st.number_input("Population locale", min_value=0, value=50000)
entreprises = st.number_input("Nombre d'entreprises locales", min_value=0, value=2000)
agents_municipaux = st.number_input("Nombre d'agents municipaux", min_value=0, value=500)
commerces = st.number_input("Nombre de commerces locaux", min_value=0, value=100)

taux_adoption_b2c = st.slider("Taux d'adoption B2C (%)", 0.0, 10.0, 2.0) / 100
valeur_carte_b2c = st.number_input("Valeur moyenne d'une carte cadeau B2C (€)", min_value=1, value=30)

taux_adoption_b2b = st.slider("Taux d'adoption B2B (%)", 0.0, 50.0, 10.0) / 100
valeur_carte_b2b = st.number_input("Valeur moyenne d'une carte cadeau B2B (€)", min_value=1, value=50)

taux_adoption_b2g = st.slider("Taux d'adoption B2G (%)", 0.0, 100.0, 50.0) / 100
valeur_carte_b2g = st.number_input("Valeur moyenne d'une carte cadeau B2G (€)", min_value=1, value=50)

taux_adhesion_commerces = st.slider("Taux d'adhésion des commerces (%)", 0.0, 100.0, 50.0) / 100

# Calculs
if st.button("Calculer le potentiel"):
    potentiel_b2c, potentiel_b2b, potentiel_b2g, potentiel_total, commercants_acceptant = calcul_potentiel_cartes(
        population, entreprises, agents_municipaux, commerces,
        taux_adoption_b2c, valeur_carte_b2c,
        taux_adoption_b2b, valeur_carte_b2b,
        taux_adoption_b2g, valeur_carte_b2g,
        taux_adhesion_commerces
    )
    
    st.subheader("Résultats")
    st.write(f"💰 Potentiel B2C : {potentiel_b2c:,.2f} €")
    st.write(f"🏢 Potentiel B2B : {potentiel_b2b:,.2f} €")
    st.write(f"🏛️ Potentiel B2G : {potentiel_b2g:,.2f} €")
    st.write(f"🔹 Potentiel Total : {potentiel_total:,.2f} €")
    st.write(f"🏪 Nombre de commerçants acceptant la carte : {commercants_acceptant:.0f}")
