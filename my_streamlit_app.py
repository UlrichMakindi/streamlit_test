
#importer les librairies python travailler dans streamlite localhost : 8501 http://192.168.1.98:8501 #

# Données de la quête 1

import pandas as pd # type: ignore
import streamlit as st # type: ignore
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore

# QUETE STREAMLIT "CARS"
# definition du titre de la quête importation du jeu de données et affichage.
st.title(" # Quête streamlit : cars")
st.header('Table de données')
df = pd.read_csv("cars.csv")
df['continent'] = df['continent'].str.replace('.', '')
df

# matrice de corrélation en supprimant la colonne 'continent' quie st stockée en chaine de caractères.
st.header('Matrice de corrélation entre les variables continues')
st.write('ici on remarque une forte corrélation positive entre plusieurs variables : cylinders, cubicinches, hp, et weightlbs au centre de la matrice')
plt.figure(figsize = (10,5))
matrice = sns.heatmap(df.drop(columns = 'continent').corr(), 
								center = 0, annot = True,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(matrice.figure)

# liste déroulante avec st.selectbox prend en argument le nom de la liste et la liste en second argument
liste_region = df['continent'].unique()
selection_region = st.selectbox('Selectionnez le Pays', liste_region)

# filtrage de la base de données correspondante
df_filtre = df[df['continent'].str.contains(selection_region)]

#évolution de la puissance 'hp' (horse power) dans le temps
st.header('Evolution de la puissance des véhicules HP au fil des années')
st.bar_chart(df_filtre, x = 'year', y = 'hp', color = 'continent')

st.header('Evolution du time to 60 au fil des années')
st.line_chart(df_filtre, x = 'year', y = 'time-to-60', color = 'continent')