import streamlit as st
import pandas as pd
import plotly.express as px

# ===============================
# 1. Konfigurasi halaman
# ===============================
st.set_page_config(
    page_title="Dashboard KDD",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard KDD")
st.caption("Visualisasi hasil Knowledge Discovery in Databases")

# ===============================
# 2. Load dataset
# ===============================
df = pd.read_csv("hasil_kdd.csv")

# ===============================
# 3. SIDEBAR FILTER
# ===============================
st.sidebar.header("🔍 Filter Data")

tahun = st.sidebar.selectbox(
    "Pilih Tahun",
    sorted(df["tahun"].unique())
)

# filter data
df = df[df["tahun"] == tahun]

# ===============================
# 4. METRIC (COLUMNS)
# ===============================
st.subheader("📌 Ringkasan Data")

col1, col2 = st.columns(2)

with col1:
    st.metric("Jumlah Data", len(df))

with col2:
    st.metric("Rata-rata Nilai", round(df["nilai"].mean(), 2))

st.divider()

# ===============================
# 5. VISUALISASI
# ===============================
fig = px.line(
    df,
    x="bulan",
    y="nilai",
    title="Tren Nilai per Bulan"
)

st.plotly_chart(fig, use_container_width=True)
