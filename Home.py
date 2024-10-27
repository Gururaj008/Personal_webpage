import streamlit as st
import webbrowser 
from PIL import Image

if __name__ == "__main__":
    st. set_page_config(layout="wide")
    st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text { font-family: 'Agdasima', sans-serif; font-size: 45px;color:cyan }
                    </style>
                    <p class="custom-text">Welcome to Gururaj's webpage</p>
                    """, unsafe_allow_html=True)
    st.divider()
    col4, col5 = st.columns([1,5], gap='medium')
    with col4:
        st.write('')
        st.write('')
        st.write('')
        image = Image.open('GR.jpg')
        st.image(image)
        
    with col5:
        st.markdown('<div style="text-align: justify">Hey! This is Gururaj. Currently, I am working as an Associate Data Scientist at Emplay, where I bring together my expertise in Generative AI (GenAI) and traditional Machine Learning (ML) to deliver impactful solutions across multiple domains. At Emplay, I focus on creating advanced, intelligent chatbots and cutting-edge tools that redefine human-technology interaction. I’m involved throughout the data science lifecycle—from data extraction and transformation to modeling and implementation. This role allows me to work on a range of projects, addressing complex regression and classification challenges that drive business insights and process efficiencies. </div>', unsafe_allow_html=True)
        st.write('')
        st.markdown('<div style="text-align: justify"> My journey into data science began with the IIT Madras Certified Advanced Programmer with Data Science Mastery Program, at GUVI,IIT-Madras, a comprehensive course that honed my skills and allowed me to dive deep into advanced analytics and machine learning techniques. This rigorous certification played a pivotal role in helping me secure my role at Emplay, equipping me with the expertise needed to excel in high-impact, data-driven projects. </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> Prior to my current role, I served as a Lecturer in the Department of Electrical & Electronics Engineering at several Government Polytechnics across the state of Karnataka, where I combined my passion for technology with education. Teaching allowed me to mentor future engineers, imparting both theoretical knowledge and practical applications of data and electrical engineering. This experience solidified my foundation in technical concepts, and further fueled my interest in transitioning to a data-centric career in the IT industry <div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> While working as Consultant at CapGemini consulting India Pvt. Ltd. for Alcatel-Lucent client based out of US my diligence at work was recognized and awarded. Currently working as Lecturer, Department of Electrical & Electronics Engineering, Government polytechic. Seeking a comeback into the IT industry. Throughout my academic journey, I have consistently excelled, with achievements such as having my undergraduate project funded and receiving runner-up recognition at a National Seminar for the abstract of my master\’s dissertation on renewable energy. My passion for research has led me to author six technical papers published in reputed journals like Springer and IEEE, where I\’ve also reviewed manuscripts. <div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> In my earlier experience as a Consultant at CapGemini Consulting India Pvt. Ltd., I supported the Alcatel-Lucent client, based out of the U.S., where my dedication and work ethic were recognized with an award. This role exposed me to consulting at scale, managing data-driven insights to support decision-making and enhance client outcomes. It provided valuable experience working in a high-paced environment and collaborating with global teams, skills that have greatly benefited my journey in data science. <div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> Beyond data and technology, I\’m passionate about driving and spending time by the beach, both of which bring a sense of calm to my life. I love traveling, learning about new cultures, meeting new people, and exploring different languages. Watching sci-fi movies is one of my favorite pastimes, and my favorite superhero is Ironman—a character who mirrors my own drive to innovate and excel. I\'m a highly motivated and diligent individual, always seeking new opportunities to learn, grow, and make a meaningful impact. <div>', unsafe_allow_html=True)
    
    #st.write('')
    #st.markdown('<div style="text-align: justify"> Other than my passion for data, I love to drive and being by the beach (they both soothe my soul). I would love to travel around the world, meet new people, learn different languages and experience new cultures.  I also enjoy watching sci-fi movies. My favourite superhero is "Ironman". I m a highly motivated and diligent individual with a desire to learn, grow and excel. </div>', unsafe_allow_html=True)
    col6, col7, col8 = st.columns([1,5,1])
    with col7:
        st.write('')
        st.write('')
        st.write('')
        st.markdown('I believe in :green[**"No dream is too big and no dreamer is too small"**]')
        st.write('')
        st.write('')
        st.write('')
    












    st.divider()
    col201,col202,col203,col204,col205 = st.columns([1,4,1,4,1])
    with col201:
        image2 = Image.open('pic1.jpg')
        st.image(image2)
    with col202:
        text1 = "<div style='text-align: center;'>It is Not About How Much We have Lost,</div>"
        st.markdown(text1, unsafe_allow_html=True)
        text2 = "<div style='text-align: center;'>It is About How Much We Have Left</div>"
        st.markdown(text2, unsafe_allow_html=True)
    with col203:
        image3 = Image.open('pic2.jpg')
        st.image(image3)
    with col204:
        text3 = "<div style='text-align: center;'>Sometimes You Gotta Run Before You Can Walk</div>"
        st.markdown(text3, unsafe_allow_html=True)
    with col205:
        image4 = Image.open('pic3.jpg')
        width = 750  # Desired width in pixels
        height = 720  # Desired height in pixels
        resized_image = image4.resize((width, height))
        st.image(resized_image)



    #<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
    #<div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="gururaj-hc-data-science-enthusiast" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/gururaj-hc-data-science-enthusiast?trk=profile-badge">Gururaj H C</a></div>
          
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
    
