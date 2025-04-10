import streamlit as st
import webbrowser 
from PIL import Image

if __name__ == '__main__':
    st.set_page_config(layout="wide")
    st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text { font-family: 'Agdasima', sans-serif; font-size: 45px;color:cyan }
                    </style>
                    <h1 class="custom-text"> Work related projects </h1>
                    """, unsafe_allow_html=True)



    # col33, col34, col35 = st.columns([3,100,3])
    # with col34:
    st.subheader(':orange[**Sales KPI analysis**]')
    st.write('')
    st.markdown(
    '''
    <div style="text-align: justify">
        I conducted an in-depth analysis of CRM sales KPIs to classify representatives into performance tiers, which helped uncover key success factors and informed targeted coaching strategies that ultimately boosted sales effectiveness.<br><br>
        Using Pandas, I performed comprehensive exploratory data analysis (EDA) on revenue, customer, and regional retention metrics, ensuring a detailed understanding of performance trends.<br><br>
        I leveraged PostgreSQL for reliable data storage and built dynamic Power BI visualizations to effectively communicate actionable insights to stakeholders.<br><br>
        This project enabled me to hone my skills in data munging, data manipulation, statistical analysis, and CRM analytics, while also showcasing my ability to generate and present strategic insights through data visualization.
    </div>
    ''',
    unsafe_allow_html=True
    )
    st.write('')

    st.subheader(':orange[**Effort and Blended Rate Prediction**]')
    st.write('')
    st.markdown(
        '''
        <div style="text-align: justify">
            Developed a machine learning model to predict unit effort and blended rate for new projects using historical client data. Extracted raw data from PostgreSQL and performed extensive data cleaning and preprocessing.<br><br>
            Engineered relevant features and reframed the task as a classification problem to improve modeling effectiveness. Applied SMOTE to handle class imbalance, used grid search for hyperparameter tuning, and implemented ensemble methods to boost model accuracy.<br><br>
            Evaluated model performance using classification metrics, and leveraged Seaborn and Matplotlib to visualize patterns, highlight key trends, and detect outliers throughout the data pipeline.
        </div>
        ''',
        unsafe_allow_html=True
    )
    st.write('')


