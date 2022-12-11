import streamlit as st
import pandas as pd
import numpy as np
import prices as pr
from time import sleep


def view_price(a):
	if  a/1000000 > 0:
		return str(int(a) / 1000000) + str(,)+ str((a%1000000)/1000) + str(,) + str(a%1000)
	elif a/1000>0:
		return str(a/1000) + str(,) + str(a%1000)
	else return str(a)


st.set_page_config(
    
    page_icon="📈",
    page_title="Dream of Ape",
    layout="wide",
)

st.header("Welcome to Dream of Ape")

if st.button('Update price', key='update_button'):
    pr.turn = pr.turn + 1
    temp = np.array([[int(int(pr.prices[pr.turn - 1][0] + (float(pr.ss)/100.0 * pr.prices[pr.turn - 1][0])) / 100000 * 100000),
                     int(int(pr.prices[pr.turn - 1][1] + (float(pr.gc)/100.0 * pr.prices[pr.turn - 1][1])) / 100000 * 100000),
                     int(int(pr.prices[pr.turn - 1][2] + (float(pr.mc)/100.0 * pr.prices[pr.turn - 1][2])) / 100000 * 100000),
                     int(int(pr.prices[pr.turn - 1][3] + (float(pr.kk)/100.0 * pr.prices[pr.turn - 1][3])) / 100000 * 100000),
                     int(int(pr.prices[pr.turn - 1][4] + (float(pr.dt)/100.0 * pr.prices[pr.turn - 1][4])) / 100000 * 100000),
                     ]])
    pr.prices = np.r_[pr.prices, temp]
if st.button("Reset"):
    pr.prices = np.zeros(shape=(1,5),dtype=np.intc)
    pr.prices[0][0] = 800000
    pr.prices[0][1] = 1000000
    pr.prices[0][2] = 1000000
    pr.prices[0][3] = 800000
    pr.prices[0][4] = 500000
    pr.turn = 0
cols = st.columns((1,1,2))
cols[0].metric("SAM SMITH", view_price(pr.prices[pr.turn][0]), pr.ss)
cols[0].metric("GG CHEMICAL", view_price(pr.prices[pr.turn][1]), pr.gc)
cols[0].metric("MUSCAR", view_price(pr.prices[pr.turn][2]), pr.mc)
cols[1].metric("KOKOa", view_price(pr.prices[pr.turn][3]), pr.kk)
cols[1].metric("DTD", view_price(pr.prices[pr.turn][4]), pr.dt)
chart_data = pd.DataFrame(
    pr.prices,
    columns=['SAM SMITH','GG CHEMICAL','MUSCAR', 'KOKOa', 'DTD']
)
cols[2].line_chart(chart_data)
pr.ss = st.number_input("SAM SMITH", -1000, 1000, 0, 10)
pr.gc = st.number_input("GG CHEMICAL", -1000, 1000, 0, 10)
pr.mc = st.number_input("MUSCAR", -1000, 1000, 0, 10)
pr.kk = st.number_input("KOKOa", -1000, 1000, 0, 10)
pr.dt = st.number_input("DTD", -1000, 1000, 0, 10)
    
