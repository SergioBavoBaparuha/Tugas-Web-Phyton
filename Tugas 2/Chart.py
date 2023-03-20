import streamlit as st
import pandas as pd
import numpy as np

st.header('Chart')

st.write("by Sergio Bavo Baparuha_32200077")

chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)