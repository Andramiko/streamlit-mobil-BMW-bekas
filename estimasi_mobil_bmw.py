import pickle
import streamlit as st

model = pickle.load(open("estimasi_mobil_bmw.sav", "rb"))

st.title("Estimasi Haga Mobil BMW Bekas")

year = st.number_input("Input Tahun Mobil")
mileage = st.number_input("Input Jarak Tempuh Mobil")
tax = st.number_input("Input Pajak Mobil")
mpg = st.number_input("Input Konsumsi BBM Mobil")
engineSize = st.number_input("Input Engine Size")

predict = ""

if st.button("Estimasi Harga"):
    predict = model.predict([[year, mileage, tax, mpg, engineSize]])
    st.write("Estimasi harga mobil BMW bekas dalam Pounds : ", predict)
    st.write("Estimasi harga mobil BMW bekas dalam IDR (Juta)", predict * 19000)
