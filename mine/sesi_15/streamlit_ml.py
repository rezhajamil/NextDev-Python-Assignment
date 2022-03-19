import streamlit as st
import pickle

with open('model/sms_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Aplikasi Pengecekan Penumpang Titanic")

sms = st.text_input("Masukkan SMS yang akan dicek:")
res = model.predict([sms])

if sms:
    st.title(res[0])