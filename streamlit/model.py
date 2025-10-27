import streamlit as st
import pandas as pd
import requests

url="https://linear-regression-project-3w1u.onrender.com/predict"
st.title("welcome to my Linear Reression prediction model")
st.subheader("below enter fill the value user")


age=st.number_input("enter your age")
service=st.number_input("enter your service[1 t0 3]")
arrival_year=st.number_input("enter your arrival_year")
arrival_month=st.number_input("enter your arrival_month")
arrival_day=st.number_input("enter your arrival_day")
departure_year=st.number_input("enter your departure_year")
departure_month=st.number_input("enter your departure_month")
departure_day=st.number_input("enter your departure_day")

if st.button("pridict satification score"):
    if age and service and arrival_year:
        user_input={
            "age":age,
     "service":service,
     "arrival_year":arrival_year,
     "arrival_month":arrival_month,
     "arrival_day":arrival_day,
     "departure_year":departure_year,
     "departure_month":departure_month,
     "departure_day":departure_day }
        
    st.dataframe(user_input)
    responce=requests.post(url,json=user_input)
    if responce.status_code==200:
        responce.json()
        result=st.json(responce.json())
        st.write("my predict satisfaction",result)


