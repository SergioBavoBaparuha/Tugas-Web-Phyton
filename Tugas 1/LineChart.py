import streamlit as st
import pandas as pd
import numpy as np

st.header('Line Chart')

st.write("by Sergio Bavo Baparuha_32200077")
chart_data = pd.DataFrame(
    {
    'first column': [0, 30, 55, 10],
    'second column': [10, 70, 20, 50],
    'third column': [45, 15, 100, 65]

    },
     columns=['first column', 'second column', 'third column'])
st.line_chart(chart_data)