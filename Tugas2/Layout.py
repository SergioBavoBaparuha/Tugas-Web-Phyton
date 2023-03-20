import streamlit as st

st.header('Layout')

st.write("by Sergio Bavo Baparuha_32200077")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Silahkan Pilih sidebar",
    ("Homepage", "Jelajah", "About")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Pilih Tema",
        ("Tema Gelap", "Tema Terang")
    )