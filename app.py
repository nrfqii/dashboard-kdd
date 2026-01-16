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
    st.error("File hasil_kdd.csv tidak ditemukan. Pastikan sudah di-upload ke GitHub.")
    st.stop()

# ===============================
# 3. Normalisasi Nama Kolom (ANTI ERROR)
# ===============================
df.columns = df.columns.str.lower().str.strip()

# Cek kolom wajib
kolom_wajib = {"tahun", "bulan", "nilai"}
if not kolom_wajib.issubset(df.columns):
    st.error(
        f"Dataset harus memiliki kolom: {kolom_wajib}\n\n"
        f"Kolom yang terdeteksi: {list(df.columns)}"
    )
    st.stop()

# ===============================
# 4. Sidebar Filter
# ===============================
st.sidebar.header("🔍 Filter Data")

tahun = st.sidebar.selectbox(
    "Pilih Tahun",
    sorted(df["tahun"].unique())
)

df_filtered = df[df["tahun"] == tahun]

# ===============================
# 5. Ringkasan Data (METRIC)
# ===============================
st.subheader("📌 Ringkasan Data")

col1, col2 = st.columns(2)

with col1:
    st.metric("Jumlah Data", len(df_filtered))

with col2:
    st.metric(
        "Rata-rata Nilai",
        round(df_filtered["nilai"].mean(), 2)
    )

st.divider()

# ===============================
# 6. Visualisasi
# ===============================
st.subheader("📈 Tren Nilai per Bulan")

fig = px.line(
    df_filtered,
    x="bulan",
    y="nilai",
    markers=True,
    title=f"Tren Nilai Tahun {tahun}"
)

fig.update_layout(
    xaxis_title="Bulan",
    yaxis_title="Nilai",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# 7. Tabel Data (Opsional)
# ===============================
with st.expander("📄 Lihat Data"):
    st.dataframe(df_filtered, use_container_width=True)
