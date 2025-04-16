import streamlit as st
import webbrowser 
from PIL import Image

if __name__ == '__main__':
    st.set_page_config(layout="wide")

    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Agdasima');
            
            /* Title styling */
            .custom-title {
                font-family: 'Agdasima', sans-serif; 
                font-size: 45px; 
                color: cyan;
            }
    
            /* Section headers */
            .section-header {
                font-size: 25px; 
                color: #FFA500; /* Orange color */
                margin-top: 15px;
            }
    
            /* Content paragraphs */
            .section-content {
                text-align: justify; 
                margin-bottom: 20px;
                line-height: 1.5em;
            }
            
            /* Subheader styling */
            .project-subheader {
                color: orange; 
                font-size: 28px;
                font-weight: bold;
                margin-bottom: 10px;
            }
        </style>
        
        <h1 class="custom-title"> Work related projects </h1>
    """, unsafe_allow_html=True)
    
    # 1) Sales KPI Analysis
    st.markdown('<div class="project-subheader">Sales KPI Analysis</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-content">
        <span class="section-header">Project Description:</span><br>
        Analyzed CRM sales KPIs to classify sales representatives into performance tiers and uncover key drivers of success.
    </div>
    <div class="section-content">
        <span class="section-header">Goal:</span><br>
        Classify sales representatives into distinct performance tiers to enable targeted coaching and improve overall sales effectiveness.
    </div>
    <div class="section-content">
        <span class="section-header">Solution:</span><br>
        - Combined multiple datasets (e.g., Opportunity, Revenue, Gong, Salesforce, LinkedIn) and conducted extensive data cleaning.<br>
        - Built a data manipulation pipeline using Kedro to streamline the exploratory data analysis (EDA) process.<br>
        - Performed EDA to identify KPIs that drive customer and revenue retention.<br>
        - Developed dynamic Power BI visualizations to communicate actionable insights.
    </div>
    <div class="section-content">
        <span class="section-header">Results:</span><br>
        - Classified representatives into Top, Medium, and Low performers, enabling managers to tailor coaching effectively.<br>
        - Provided a business-centric view of KPIs that enhanced strategic decision-making.
    </div>
    <div class="section-content">
        <span class="section-header">Learning:</span><br>
        - Improved data munging and analytical techniques in CRM analytics.<br>
        - Demonstrated the value of integrating multiple data sources and effective visualization in driving business outcomes.
    </div>
    """, unsafe_allow_html=True)
    st.write('---')
    
    # 2) Effort and Cost Prediction Using Ensemble ML Models
    st.markdown('<div class="project-subheader">Effort and Cost Prediction Using Ensemble ML Models</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-content">
        <span class="section-header">Project Description:</span><br>
        Developed a machine learning model to predict unit effort and cost for new projects, utilizing historical data and advanced ensemble techniques.
    </div>
    <div class="section-content">
        <span class="section-header">Goal:</span><br>
        Predict the effort and cost required for new projects to enable realistic planning and resource allocation.
    </div>
    <div class="section-content">
        <span class="section-header">Solution:</span><br>
        - Converted the prediction problem into a classification task for better outcome control.<br>
        - Extracted raw data from PostgreSQL and conducted extensive data cleaning, standardization, and feature engineering.<br>
        - Balanced the dataset using SMOTE to address class imbalance.<br>
        - Utilized grid search to determine optimal model parameters and built an ensemble model to improve accuracy.<br><br>
        Data visualizations with Seaborn and Matplotlib were employed to highlight trends and detect outliers.
    </div>
    <div class="section-content">
        <span class="section-header">Results:</span><br>
        - Delivered more reliable and realistic estimates of effort and cost, aiding in project planning.<br>
        - Enhanced model accuracy and consistency through effective data preprocessing and ensemble methods.
    </div>
    <div class="section-content">
        <span class="section-header">Learning:</span><br>
        - Validated that class-balancing can prevent skewed predictions.<br>
        - Showcased the benefits of reframing regression into classification for improved control over outcomes.<br>
        - Sharpened skills in end-to-end machine learning pipelines—from data ingestion to model evaluation.
    </div>
    """, unsafe_allow_html=True)
    st.write('---')
    
    # 3) RAG-based Chatbot
    st.markdown('<div class="project-subheader">RAG-based Chatbot</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-content">
        <span class="section-header">Project Description:</span><br>
        Developed a Retrieval-Augmented Generation (RAG) based chatbot to intelligently answer user queries related to plans, offers, and discounts.
    </div>
    <div class="section-content">
        <span class="section-header">Goal:</span><br>
        Provide detailed information on various plans, offers, and discounts while reducing calls to customer support.
    </div>
    <div class="section-content">
        <span class="section-header">Solution:</span><br>
        - Converted HTML data into CSV to preserve hierarchical table structures containing the necessary details.<br>
        - Created manageable chunks from the CSV and generated text embeddings along with associated metadata.<br>
        - Ingested the vectorized chunks into a VectorStore for efficient hybrid search (combining keyword and semantic approaches).<br>
        - On user query, employed cosine similarity to select the top 5 relevant chunks, which were then passed to an LLM to generate responses with supporting source links.<br><br>
        The end-to-end pipeline leverages Generative AI, Natural Language Processing, and prompt engineering for accurate and transparent responses.
    </div>
    <div class="section-content">
        <span class="section-header">Results:</span><br>
        - Reduced customer support calls by enabling accurate self-service responses.<br>
        - Improved response accuracy and system transparency through source-linked answers.
    </div>
    <div class="section-content">
        <span class="section-header">Learning:</span><br>
        - Enhanced expertise in Langchain Agents and advanced prompt engineering techniques.<br>
        - Learned to balance retrieval depth with response latency, boosting overall system performance.
    </div>
    """, unsafe_allow_html=True)
    st.write('---')
    
    # 4) RAPTOR: AI-Powered Tree-Based Retrieval System
    st.markdown('<div class="project-subheader">RAPTOR: AI-Powered Tree-Based Retrieval System</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-content">
        <span class="section-header">Project Description:</span><br>
        Spearheaded the implementation of RAPTOR—a state-of-the-art tree-based information retrieval system designed to outperform traditional RAG methods.
    </div>
    <div class="section-content">
        <span class="section-header">Goal:</span><br>
        Improve retrieval accuracy by structuring data into hierarchical trees for enhanced abstraction and relevance.
    </div>
    <div class="section-content">
        <span class="section-header">Solution:</span><br>
        - Ingested data followed by specialized RAPTOR processing to organize content into hierarchical structures.<br>
        - Applied hierarchical clustering algorithms (GMM) and dimensionality reduction techniques (UMAP) to create an optimized retrieval pipeline.<br>
        - Reduced retrieval noise with iterative summarization and context-aware knowledge extraction.<br>
        - Employed Bayesian Information Criterion (BIC) for optimal model selection and used PGvector for scalable vector storage.<br>
        - Orchestrated the entire pipeline using Langchain to streamline integration.
    </div>
    <div class="section-content">
        <span class="section-header">Results:</span><br>
        - Significantly enhanced answer relevance and reduced retrieval noise, surpassing conventional RAG performance.<br>
        - Enabled more precise decision-making with a well-structured hierarchical data retrieval framework.
    </div>
    <div class="section-content">
        <span class="section-header">Learning:</span><br>
        - Developed expertise in constructing hierarchical tree structures for improved search and data abstraction.<br>
        - Explored advanced clustering and dimensionality reduction techniques for large-scale vector retrieval.<br>
        - Expanded knowledge in orchestrating complex AI pipelines using tools like Langchain.
    </div>
    """, unsafe_allow_html=True)
    st.write('---')
