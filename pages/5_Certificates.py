import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text { font-family: 'Agdasima', sans-serif; font-size: 45px;color:cyan }
                    </style>
                    <p class="custom-text">Certications </p>
                    """, unsafe_allow_html=True)

st.divider()
col1004, col1005 = st.columns([30,30])
with col1004:
   st.markdown(':orange[MASTER DATA SCIENCE PROGRAM FROM GUVI, IIT MADRAS]')
with col1005:
   st.image('Final.png')

st.write('')
st.write('')
col1004, col1005 = st.columns([30,30])
with col1004:
   st.markdown(':orange[PYTHON COURSE ON MULTIPLE LANGUAGES FROM IIT MADRAS]')
with col1005:
   st.image('1.jpg')

st.write('')
st.write('')
col1004, col1005 = st.columns([30,30])
with col1004:
   st.markdown(':orange[DATA ANALYTICS USING PANDAS FROM GUVI, IIT MADRAS]')
with col1005:
   st.image('2.jpg')

st.write('')
st.write('')
col1004, col1005 = st.columns([30,30])
with col1004:
   st.markdown(':orange[MACHINE LEARNING 101 FROM GUVI, IIT MADRAS]')
with col1005:
   st.image('3.jpg')

st.write('')
st.write('')
col1004, col1005 = st.columns([30,30])
with col1004:
   st.markdown(':orange[POWERBI FROM GUVI, IIT MADRAS]')
with col1005:
   st.image('4.jpg')

st.write('')
st.write('')
col1004, col1005 = st.columns([30,30])
with col1004:
   st.markdown(':orange[AMAZON WEB SERVICES FROM GUVI, IIT MADRAS]')
with col1005:
   st.image('5.jpg')

st.write('')
st.write('')
col1004, col1005 = st.columns([30,30])
with col1004:
   st.markdown(':orange[MACHINE LEARNING, DATA SCIENCE AND DEEP LEARNING WITH PYTHON FROM UDEMY]')
with col1005:
   st.image('6.jpg')



