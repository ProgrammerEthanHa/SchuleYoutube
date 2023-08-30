import streamlit as st
import pandas as pd
import altair as alt

st.header("Für viele gehören YouTube und Schule zusammen")
st.subheader("Wie wichtig sind YouTube Videos für Themen, die in der Schule behandelt werden?")

source = pd.DataFrame({
        'Anteil(%)': [10, 37, 35, 17, 1],
        'Wichtig': ['Sehr wichtig', 'Wichtig', 'Eher unwichtig', 'Völlig unwichtig', 'Weiß nicht']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Wichtig:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis: 520 Befragte; (12 bis 19 Jahre) in Deutschland; 2019
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle:  Rat für Kulturelle Bildung")