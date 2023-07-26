import streamlit as st
st. set_page_config(layout="wide")
st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text { font-family: 'Agdasima', sans-serif; font-size: 45px;color:cyan }
                    </style>
                    <p class="custom-text">Developer contact details</p>
                    """, unsafe_allow_html=True)
st.divider()
col301, col302 = st.columns([10,20])
with col301:
  st.markdown(":orange[email id:]")
  st.write('')
with col302:
  st.markdown(":yellow[gururaj008@gmail.com]")
  st.write('')

col301, col302 = st.columns([10,20])
with col301:
  st.markdown(":orange[Personal webpage hosting other Datascience projects :]")
  st.write('')
with col302:
  st.markdown(":yellow[http://gururaj008.pythonanywhere.com/]")
  st.write('')

col301, col302 = st.columns([10,20])
with col301:
  st.markdown(":orange[LinkedIn profile :]")
  st.write('')
with col302:
  st.markdown(":yellow[https://www.linkedin.com/in/gururaj-hc-data-science-enthusiast/]")
  st.write('')


col301, col302 = st.columns([10,20])
with col301:
  st.markdown(":orange[Github link:]")
  st.write('')
with col302:
  st.markdown(":yellow[https://github.com/Gururaj008]")
  st.write('')


st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
col901, col902, col903 = st.columns(3)
with col903:
    st.markdown('_An_ _effort_ _by_ : :red[**MAVERICK_GR**]')
