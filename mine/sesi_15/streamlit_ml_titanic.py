import streamlit as st
import pickle
import pandas as pd

with open('model/titanic_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Aplikasi Pengecekan Penumpang Titanic")

pclass=st.number_input("Passenger Class")
age=st.number_input("Passenger Age")
gender=st.selectbox("Gender",('male','female'))
sibsp=st.number_input("Sibling / Spouse")
parch=st.number_input("Parent / Child")
fare=st.number_input("Ticket Fare")

target=['Not Survived',"Survived"]
columns=['Pclass','Sex','Age','SibSp','Parch','Fare']
new_data=[pclass,gender,age,sibsp,parch,fare]
new_data=pd.DataFrame([new_data],columns=columns)

res = model.predict(new_data)
st.title(target[res[0]])