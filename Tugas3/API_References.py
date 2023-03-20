import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.header('10 API References')
st.write('by Sergio Bavo Baparuha_32200077')
st.write(' ')

st.subheader('1. Write & Magic')
st.write('Write')
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))

('Magic')
('ini contoh magic')
(' ')


st.subheader('2. Text Element')
st.markdown(':red[ini contoh text elemen yang mengubah warna tulisan]')
st.write(' ')


st.subheader('3. Data Display Element')
df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.table(df)
st.write(' ')


st.subheader('4. Chart Element')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.write(' ')


st.subheader('5. Input Widget')
genre = st.radio(
    "What\'s your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")
    st.write(' ')


st.subheader('6. Media Element')
image = Image.open("./Tugas3/CintaSegitiga.jpg")

st.image(image, caption='Drinking Wine, Because you will never be mine')
st.write(' ')

st.subheader('7. Layout & Container')
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
st.write('Output dapat di lihat di sidebar sebelah kiri')
st.write(' ')

st.subheader('8. Status Element')
st.snow()
st.write('Dapat dilihat dari efek salju di atas')
st.write(' ')

st.subheader('9. Control Flow')
form = st.form("my_form")
form.slider("Inside the form")
st.slider("Outside the form")
form.form_submit_button("Submit")
st.write(' ')

st.subheader('10. Utilities')
with st.echo():
    st.write('This code will be printed')
st.write(' ')
