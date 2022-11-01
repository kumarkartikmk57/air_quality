import streamlit as st
import pickle
import sklearn
import xgboost
st.title("Air quality prediction")
pm = st.text_input("PM2.5")
pm10 = st.text_input("PM10")
no = st.text_input("Nitric oxide")
no2 = st.text_input("Nitrogen oxide")
nox = st.text_input("NOX Nitogren gases from automobile")
co = st.text_input("Carbon Monoxide")
so = st.text_input("Sulfur dioxide")
o3 = st.text_input("ozone")
benzene = st.text_input("Benzene")
Toluene = st.text_input("Toluene")
Xylene = st.text_input("Xylene")
dic = {
    0:"Good",
    1:"Moderate",
    2:"Poor",
    3:"Satisfactory",
    4:"Severe",
    5:"Very Poor"
}
md = pickle.load("xg_air.pkl","rb")
hh = md.predict([[pm,pm10,no,no2,nox,co,so,o3,benzene,Toluene,Xylene]])
if st.button('Predict'):
    st.success("you can purchase laptop for {}".format(dic[hh]))