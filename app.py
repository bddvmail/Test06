import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Demonstrateur')

### --- LOAD DATAFRAME
excel_file = 'Book1.xlsx'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:B',
                   header=0)

# --- STREAMLIT SELECTION
offre = df['Offre'].unique().tolist()

offre_selection = st.multiselect('Offre:',
                                    offre,
                                    default=offre)

# --- FILTER DATAFRAME BASED ON SELECTION
mask = (df['Offre'].isin(offre_selection))
df_filtered = df[mask]

# --- PLOT BAR CHART
bar_chart = px.bar(df_filtered,
                   x='Offre',
                   y='Montant',
                   text='Montant',
                   color_discrete_sequence = ['#3395f6']*len(df_filtered),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)
