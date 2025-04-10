import streamlit as st

st.set_page_config(layout="wide")

# Title of your page
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
    .custom-text { font-family: 'Agdasima', sans-serif; font-size: 45px; color: cyan; }
    </style>
    <h1 class="custom-text">Data Science Projects Portfolio</h1>
    """, unsafe_allow_html=True)

# Example layout: using columns for headings defined in your Excel sheet
# Adjust the column names and layout as needed according to your Excel structure

# You might have columns such as: 'Project Title', 'Description', and 'Technologies'
projects = [
    {
        "Project Title": "Sales KPI Analysis",
        "Description": """
I conducted an in-depth analysis of CRM sales KPIs to classify representatives into performance tiers, uncover key success factors, and inform coaching strategies that boosted sales effectiveness. Using Pandas for detailed EDA on revenue, customer, and regional retention metrics, I leveraged PostgreSQL for robust data storage and built dynamic Power BI visualizations to communicate actionable insights.
        """,
    },
    {
        "Project Title": "Effort and Blended Rate Prediction",
        "Description": """
Developed a machine learning model to predict unit effort and blended rate for new projects using historical client data. After extracting raw data from PostgreSQL and performing extensive cleaning and feature engineering, I reframed the task as a classification problem. SMOTE, grid search, and ensemble methods were applied to boost accuracy, while Seaborn and Matplotlib visualized key trends and detected outliers.
        """,
    },
    {
        "Project Title": "RAG-based Chatbot",
        "Description": """
Developed a Retrieval-Augmented Generation (RAG) based chatbot to intelligently answer user queries on plans and offers. The solution ingests HTML user data, vectors it for semantic retrieval in Elasticsearch, and employs cosine similarity to fetch the top five relevant chunks. These are then processed by a large language model (LLM) to generate responses with source links, ensuring transparency and trust.
        """,
    },
    {
        "Project Title": "RAPTOR: AI-Powered Tree-Based Retrieval System",
        "Description": """
Spearheaded the development of RAPTOR—a state-of-the-art information retrieval system using hierarchical clustering (GMM) and dimensionality reduction (UMAP) to structure data for optimal search relevance. With iterative summarization, context-aware knowledge extraction, and advanced orchestration using Langchain, RAPTOR significantly enhances decision-making over traditional methods.
        """,
    }
]

# Loop through projects and display them in columns or expanders
for project in projects:
    st.markdown(f"### :orange[**{project['Project Title']}**]")
    st.markdown(
        f"""
        <div style="text-align: justify">
            {project['Description'].strip()}
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write('---')  # Separator between projects
