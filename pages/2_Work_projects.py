import streamlit as st

st.set_page_config(layout="wide")

# Custom CSS for title style
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
        .custom-title { font-family: 'Agdasima', sans-serif; font-size: 45px; color: cyan; }
        .section-header { font-size: 25px; color: #FFA500; } /* Orange color for section headers */
        .section-content { text-align: justify; margin-bottom: 20px; }
    </style>
    <h1 class="custom-title">Data Science Projects Portfolio</h1>
    """, unsafe_allow_html=True)

# ---------- Sales KPI Analysis ----------
st.subheader(':orange[**Sales KPI Analysis**]')
st.markdown("""
<div class="section-content">
    <span class="section-header">Project:</span><br>
    Conducted an in-depth analysis of CRM sales KPIs to classify representatives into performance tiers.
</div>
<div class="section-content">
    <span class="section-header">Goal:</span><br>
    Uncover key success factors and inform targeted coaching strategies to boost overall sales effectiveness.
</div>
<div class="section-content">
    <span class="section-header">Solution:</span><br>
    Used Pandas to perform comprehensive exploratory data analysis (EDA) on revenue, customer, and regional retention metrics. Leveraged PostgreSQL for reliable data storage and built dynamic Power BI visualizations to communicate actionable insights.
</div>
<div class="section-content">
    <span class="section-header">Results:</span><br>
    Enabled strategic decision-making by classifying performance tiers, ultimately boosting sales effectiveness through informed coaching.
</div>
<div class="section-content">
    <span class="section-header">Learning:</span><br>
    Honed skills in data munging, manipulation, statistical analysis, and CRM analytics while mastering effective data visualization.
</div>
""", unsafe_allow_html=True)

st.write('---')

# ---------- Effort and Blended Rate Prediction ----------
st.subheader(':orange[**Effort and Blended Rate Prediction**]')
st.markdown("""
<div class="section-content">
    <span class="section-header">Project:</span><br>
    Developed a machine learning model to predict unit effort and blended rate for new projects.
</div>
<div class="section-content">
    <span class="section-header">Goal:</span><br>
    Use historical client data to forecast project effort and pricing metrics reliably.
</div>
<div class="section-content">
    <span class="section-header">Solution:</span><br>
    Extracted raw data from PostgreSQL, performed extensive data cleaning and preprocessing, engineered features, and reframed the task as a classification problem. Applied SMOTE, grid search, and ensemble methods to optimize the model.
</div>
<div class="section-content">
    <span class="section-header">Results:</span><br>
    Achieved improved model accuracy and performance, with effective visualizations using Seaborn and Matplotlib to highlight key trends and outliers.
</div>
<div class="section-content">
    <span class="section-header">Learning:</span><br>
    Enhanced expertise in feature engineering, model tuning, evaluation, and data visualization, deepening overall machine learning proficiency.
</div>
""", unsafe_allow_html=True)

st.write('---')

# ---------- RAG-based Chatbot ----------
st.subheader(':orange[**RAG-based Chatbot**]')
st.markdown("""
<div class="section-content">
    <span class="section-header">Project:</span><br>
    Developed a Retrieval-Augmented Generation (RAG) based chatbot for handling user queries related to plans and offers.
</div>
<div class="section-content">
    <span class="section-header">Goal:</span><br>
    Provide an intelligent chatbot solution that delivers accurate, context-rich responses with clear source support.
</div>
<div class="section-content">
    <span class="section-header">Solution:</span><br>
    Ingested HTML user data through a specialized LLM ingestion service and chunked the content, which was then vectorized and stored in Elasticsearch. Upon receiving a query, cosine similarity was computed to retrieve the top five relevant content chunks, which were then fed to an LLM to generate responses with supporting source links.
</div>
<div class="section-content">
    <span class="section-header">Results:</span><br>
    Delivered a scalable chatbot solution supporting both Google Cloud and API-based deployments, enhancing transparency, trust, and user experience.
</div>
<div class="section-content">
    <span class="section-header">Learning:</span><br>
    Gained practical experience in generative AI, natural language processing, and prompt engineering, while mastering the integration of semantic search with LLMs.
</div>
""", unsafe_allow_html=True)

st.write('---')

# ---------- RAPTOR: AI-Powered Tree-Based Retrieval System ----------
st.subheader(':orange[**RAPTOR: AI-Powered Tree-Based Retrieval System**]')
st.markdown("""
<div class="section-content">
    <span class="section-header">Project:</span><br>
    Spearheaded the development of RAPTOR—a state-of-the-art, tree-based information retrieval system.
</div>
<div class="section-content">
    <span class="section-header">Goal:</span><br>
    Outperform traditional RAG methods by significantly enhancing search relevance and decision-making.
</div>
<div class="section-content">
    <span class="section-header">Solution:</span><br>
    Integrated hierarchical clustering algorithms (GMM) and dimensionality reduction techniques (UMAP) to structure data in an optimized retrieval pipeline. Employed iterative summarization, context-aware knowledge extraction, Bayesian model selection (BIC), and scalable vector storage (PGvector), all orchestrated with Langchain.
</div>
<div class="section-content">
    <span class="section-header">Results:</span><br>
    Delivered an AI-powered search experience that markedly improved question-answering accuracy and relevance for advanced decision-making scenarios.
</div>
<div class="section-content">
    <span class="section-header">Learning:</span><br>
    Deepened understanding of clustering, text embeddings, and orchestration of advanced AI search pipelines, reinforcing skills in context-aware data structuring and retrieval.
</div>
""", unsafe_allow_html=True)

st.write('---')
