import pickle
import streamlit as st

model = pickle.load(open('estimasi_covid19.sav', 'rb'))

st.title('Estimasi Jumlah Kematian Covid-19 Di Berbagai Negara')
Confirmed = st.number_input('Input Jumlah Manusia yang Terkonfirmasi Covid-19')
Active = st.number_input('Input Total yang Aktif')
Recovered = st.number_input('Input Jumlah yang sudah Pulih')

predict = ''

if st.button('Estimasi Deaths'):
    predict = model.predict(
        [[Confirmed, Active, Recovered]]
        )
    st.write ('Estimasi Jumlah Kematian Covid-19 : ', predict)