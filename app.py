import streamlit as st
from datetime import datetime

st.title("locadora de carros 🏎️")
st.sidebar.image("logo.png")
carro = st.sidebar.selectbox("selecione o carro que deseja alugar",["Gol","Uno","Lancer","Bmw x7","GTR-skyline"])

valores_diaria = {"Gol":250,"Uno":100,"Lancer":450,"Bmw x7":1200,"GTR-skyline":2000}

st.image(f"{carro}.png",width=750)

st.subheader(f"valor da diaria: R$ {valores_diaria[carro]}")
data_retirada = st.date_input("selecione a data de retirada", datetime.now())
data_devolucao = st.date_input("selecione a data de devolução", data_retirada)
if st.button("alugar"):
    dias = data_devolucao - data_retirada
    total = dias * valores_diaria[carro]
    st.success(f"alugando carros por{dias}dias de custo total é: R$ {total}")