import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard KDD", layout="wide")

st.title("📊 Dashboard Knowledge Discovery in Database (KDD)")

# Load data
df = pd.read_csv("hasil_kdd.csv")

st.subheader("Preview Dataset")
st.dataframe(df.head())

st.subheader("Statistik Deskriptif")
st.write(df.describe())

st.subheader("Visualisasi Data")

num_cols = df.select_dtypes(include="number").columns

x_col = st.selectbox("Pilih sumbu X", num_cols)
y_col = st.selectbox("Pilih sumbu Y", num_cols)

fig = px.scatter(df, x=x_col, y=y_col, title="Scatter Plot Interaktif")
st.plotly_chart(fig, use_container_width=True)
