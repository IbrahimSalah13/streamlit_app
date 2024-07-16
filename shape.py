import streamlit as st
import time
st.header("Shapes Calculations")

st.sidebar.title("Configurations")
with st.sidebar:
    shape = st.selectbox('choose shape :', options=['Circle', 'Rectangle'])

if shape=='Circle':
    radius = st.number_input("Radius:", min_value=0, max_value=100, step=1)
    area = radius*radius*3.14
    perimeter = 2*3.14*radius
if shape=='Rectangle':
    height = st.number_input("Height:", 0., step=0.1)
    width = st.number_input("Width : ", 0., step=0.1)
    area = height*width
    perimeter = 2*(height+width)
    
compute_btn = st.button("compute area and perimeter")
if compute_btn:
    with st.spinner("Computing..."):
        time.sleep(2)
        st.write("Area : ", area)
        st.write("Perimeter  :", perimeter)
    