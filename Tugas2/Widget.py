import streamlit as st

st.header('Widget')

st.write("by Sergio Bavo Baparuha_32200077")

option = st.selectbox(
    'Silahkan Pilih Makanan?',
    ('Nasi Goreng', 'Bakso', 'Mie'))

st.write('You selected:', option)