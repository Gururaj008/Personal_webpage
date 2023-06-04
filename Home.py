import streamlit as st
import webbrowser 
from PIL import Image






if __name__ == "__main__":
    st.set_page_config(page_title='Gururaj\'s webpage')
    col1,col2,col3 = st.columns([1,3,1])
    with col2:
        st.header(':blue[Welcome to my webpage]')
    st.divider()
    col4, col5 = st.columns([1,5], gap='medium')
    with col4:
        st.write('')
        st.write('')
        st.write('')
        image = Image.open('C:\MLCourse\Learning\Home_page\GR.jpg')
        st.image(image)
        
    with col5:
        st.markdown('<div style="text-align: justify">Hey! This is Gururaj. I possess work experience with both IT industry and academia. Currently pursuing “IIT-Madras Certified Advanced Programmer with Data Science Mastery Program” course as a part of my learning journey.  </div>', unsafe_allow_html=True)
        st.write('')
        st.markdown('<div style="text-align: justify">After completing my Master of Technology in “Renewable energy” in 2019, I was looking for a way to further my research in “wind energy”, it was then I stumbled upon the field of Data science. I was fascinated by its real world applications and kindled the desire to be a "Data Scientist".  </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> I have consistently excelled in my academic pursuits throughout my life. Project work carried out in the final semester of my bachelor\'s was recognized and funded by the premier research institute “Indian Institute of Science, Bengaluru” . Abstract of my master\'s dissertation was awarded runner-up at National seminar on “Innovation in Science and Engineering “ held by “National Academy of Science, India”.  <div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> While working as Senior Consultant at CapGemini consulting India Pvt. Ltd. for Alcatel-Lucent client based out of US my diligence at work was recognized and received the following - Pride of the team award, Bravo team award , Spot recognition award. Currently working as Lecturer, Department of Electrical & Electronics Engineering, Government polytechic. Seeking a comeback into the IT industry.  <div>', unsafe_allow_html=True)
    st.write('')
    #st.markdown('<div style="text-align: justify"> <div>', unsafe_allow_html=True)
    #st.write('')
    st.markdown('<div style="text-align: justify"> As a part of my research have authored "06 technical papers" which are published with reputed journals like "SPRINGER and IEEE", have also reviewed the manuscripts submitted for pulication with the likes of IEEE. <div>', unsafe_allow_html=True)
    
    st.write('')
    st.markdown('<div style="text-align: justify"> Other than my passion for data, I love to drive and being by the beach (they both soothe my soul). I would love to travel around the world, meet new people, learn different languages and experience new cultures.  I also enjoy watching sci-fi movies. My favourite superhero is "Ironman". I m a highly motivated and diligent individual with a desire to learn, grow and excel. </div>', unsafe_allow_html=True)
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
        image2 = Image.open('C:\MLCourse\Learning\Home_page\pic1.jpg')
        st.image(image2)
    with col202:
        text1 = "<div style='text-align: center;'>It is Not About How Much We have Lost,</div>"
        st.markdown(text1, unsafe_allow_html=True)
        text2 = "<div style='text-align: center;'>It is About How Much We Have Left</div>"
        st.markdown(text2, unsafe_allow_html=True)
    with col203:
        image3 = Image.open('C:\MLCourse\Learning\Home_page\pic2.jpg')
        st.image(image3)
    with col204:
        text3 = "<div style='text-align: center;'>Sometimes You Gotta Run Before You Can Walk</div>"
        st.markdown(text3, unsafe_allow_html=True)
    with col205:
        image4 = Image.open('C:\MLCourse\Learning\Home_page\pic3.jpg')
        width = 750  # Desired width in pixels
        height = 720  # Desired height in pixels
        resized_image = image4.resize((width, height))
        st.image(resized_image)



    
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
        st.markdown('_An_ _effort_ _by_ : :blue[**MAVERICK_GR**]')        
    