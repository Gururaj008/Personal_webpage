import streamlit as st
import webbrowser 
from PIL import Image

if __name__ == '__main__':
    st.set_page_config(layout="wide")
    col8, col9, col10 = st.columns([1,5,1])
    with col9:
        st.subheader(':orange[**Diabetes prediction using health indicators**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> Diabetes is a chronic medical condition characterized by elevated blood sugar levels due to either insufficient insulin production or ineffective use of insulin by the body. It has a significant global impact, with an estimated 463 million adults living with diabetes worldwide. The condition can lead to various complications, including cardiovascular disease, kidney damage, nerve damage, and vision impairment. Diabetes can affect the quality of life by requiring daily management, including monitoring blood sugar levels, taking medication or insulin, and following a healthy diet and exercise regimen. It poses a risk for long-term health complications and can increase the likelihood of premature death. Furthermore, the economic burden of diabetes is substantial, with healthcare costs, lost productivity, and reduced quality of life affecting individuals, families, and healthcare systems globally. Early detection, proper management, and lifestyle modifications are crucial in preventing complications and improving the overall well-being of individuals with diabetes.</div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> Detecting diabetes at an early stage is crucial as it allows for timely intervention and management, helping to prevent or delay complications and improve long-term health outcomes. Hence, developed a machine learning model using SVC, KNN classifier, Bagging classifier, Gradient boosting classifier and Random forest classifier and used a voting classifier on top of them to aggregate the result. </div>', unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')
    col11, col12 = st.columns([2,8])
    with col11:
        st.markdown(':orange[Available at: ]')
    with col12:
        st.markdown('https://gururaj008-diabetes-prediction-diabetes-pred-5sop4d.streamlit.app/')
        
    st.divider()
    
    st.subheader(':orange[**Suggesting customer where to buy a specific product(Flipkart or Amazon)**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> The Indian e-commerce industry has been driven by increasing mobile phone adoption and is estimated to be $75 billion in 2022 and has the potential to expand up to $111 billion by 2024 and $200 billion by 2026. Amazon and Flipkart account for more than 60 percent of the Indian e-commerce market. The offers and discounts offered by each of them vary based on the festive season and special sale on specific date and time. </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> The primary aim of this project is to help customer buy a specific product from the e-commerce market places like Flipkart and Amazon. The suggestion made is based on the selling price of the product and the amount of discount offered so that the customer ends up spending less on buying the product. </div>', unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')
    col11, col12 = st.columns([2,8])
    with col11:
        st.markdown(':orange[Available at: ]')
    with col12:
        st.markdown('https://gururaj008-flipkart-or-amazon-fa-kxnbd3.streamlit.app/')
        
    st.divider()

    col16, col17, col18 = st.columns([3,8,3])
    with col17:
        st.subheader(':orange[**Phonepe pulse data visualization**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> PhonePe Private Limited is a leading e-commerce payment platform in India. The digital wallet company was founded in December 2015. This platform offers services in over 11 Indian regional languages. As a user, you can use the app and book cabs, book hotel services, order food online, pay for your Redbus tickets, and also pay for your flight tickets. You can carry out transactions in the PhonPe app by following any of these methods: UPI Debit Card, UPI Credit Card, Via linked Bank account and using PhonePe Wallet. </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> This project explores the phonepe pulse data to help audience understand how ( Net banking/ Debit card payment/ Credit card payment ), where, when and who( using which device ) does the UPI transactions. </div>', unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')
    col11, col12 = st.columns([2,8])
    with col11:
        st.markdown(':orange[Available at: ]')
    with col12:
        st.markdown('https://gururaj008-phonepe-deploy-p-s-ycgqnz.streamlit.app/')
    st.divider()

    col13, col14, col15 = st.columns([3,8,3])
    with col14:
        st.subheader(':orange[**Youtube Data harvesting and warehousing**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> YouTube is a widely popular online video-sharing platform owned by Google, allowing users to upload, watch, and share videos. With over 2 billion logged-in monthly active users, YouTube has a global reach and supports multiple languages. It receives an astonishing amount of video content, with approximately 500 hours of video uploaded per minute, resulting in over 1 billion hours of daily video views. YouTube\'s influence on culture and society is significant, providing a platform for content creators to share knowledge, entertainment, and diverse perspectives. It has enabled individuals to build successful careers and monetize their content through ads, sponsorships, and partnerships. YouTube has also played a crucial role in supporting educational initiatives, activism, and community engagement. Additionally, YouTube offers a premium subscription service called YouTube Premium, which provides ad-free viewing, offline access, and exclusive original content. Overall, YouTube continues to shape the digital landscape, impacting how we consume and interact with video content. </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> Data harvesting, in simple terms, refers to the process of collecting or gathering large amounts of data from various sources, often using automated methods or tools. It involves extracting, compiling, and storing data from different websites, databases, or digital platforms. Data harvesting can be performed for various purposes, such as market research, data analysis, creating databases, or building machine learning models. The collected data may include information like text, images, videos, user profiles, product details, or any other relevant data points depending on the objective. </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> Data warehousing refers to the process of collecting, organizing, and storing large volumes of structured and/or unstructured data from various sources into a centralized repository. It involves combining data from different operational systems, databases, and external sources to create a comprehensive and integrated view of an organization\'s data. The purpose of a data warehouse is to provide a unified, consistent, and historical view of data that can be used for business intelligence, analytics, reporting, and decision-making. It serves as a central repository where data from multiple sources is extracted, transformed, and loaded (ETL) to ensure consistency, quality, and accessibility. </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> The objective of this project is to make API calls to YouTube and fetch channels, videos and comments information. User is provided with 15 different channel ids, out of which he/she can choose upto 10 channel ids for information retrieval.  The data retrieved is in NoSQL format, which is displayed and user is provided with option to push the data to MongDB and PostgreSQL. Later, SQL queries are made to retrieve, display and visualize some interesting facts about the channels, videos and comments. </div>', unsafe_allow_html=True)
    st.write('')
    st.write('')
    col16, col17 = st.columns([2,8])
    with col16:
        st.markdown(':orange[Code available at: ]')
    with col17:
        st.markdown('https://github.com/Gururaj008/Youtube_project/tree/main')
    st.divider()
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
    
    
    st.markdown('<div style="text-align: justify">  </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify">  </div>', unsafe_allow_html=True)
    st.write('')
