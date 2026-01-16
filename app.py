import streamlit as st
import pandas as pd
import plotly.express as px

# ===============================
# 1. Konfigurasi Halaman
# ===============================
st.set_page_config(
    page_title="Dashboard KDD",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard KDD")
st.caption("Visualisasi hasil Knowledge Discovery in Databases")

# ===============================
# 2. Load Dataset
# ===============================
try:
    df = pd.read_csv("hasil_kdd.csv")
except FileNotFoundError:
    st.error("File hasil_kdd.csv tidak ditemukan.")
    st.stop()

# ===============================
# 3. Normalisasi Kolom
# ===============================
df.columns = df.columns.str.lower().str.strip()

# ===============================
# 4. Sidebar Filter
# ===============================
st.sidebar.header("🔍 Filter Data")

country = st.sidebar.selectbox(
    "Pilih Country",
    sorted(df["country"].unique())
)

product = st.sidebar.selectbox(
    "Pilih Product",
    sorted(df["product"].unique())
)

df_filtered = df[
    (df["country"] == country) &
    (df["product"] == product)
]

# ===============================
# 5. METRIC
# ===============================
st.subheader("📌 Ringkasan Penjualan")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sales", f"{df_filtered['sales'].sum():,.0f}")

with col2:
    st.metric("Total Profit", f"{df_filtered['profit'].sum():,.0f}")

with col3:
    st.metric("Units Sold", f"{df_filtered['units sold'].sum():,.0f}")

st.divider()

# ===============================
# 6. VISUALISASI
# ===============================
st.subheader("📊 Perbandingan Sales & Profit")

fig = px.bar(
    df_filtered,
    x="segment",
    y=["sales", "profit"],
    barmode="group",
    title=f"Sales vs Profit ({country} - {product})"
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# 7. TABEL DATA
# ===============================
with st.expander("📄 Lihat Data Lengkap"):
    st.dataframe(df_filtered, use_container_width=True)
