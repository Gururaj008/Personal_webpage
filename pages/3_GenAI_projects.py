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
                    <h1 class="custom-text"> GenAI projects carried out </h1>
                    """, unsafe_allow_html=True)

    st.write('')
    st.write('')
    # col33, col34, col35 = st.columns([3,100,3])
    # with col34:
    st.subheader(':orange[**SmartText Insight**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> The SmartText Insight project is an AI-powered tool designed to enhance document interaction by transforming static text files into dynamic, conversational resources. With support for PDF, DOCX, and TXT file formats, this application allows users to upload one or multiple documents, which are then processed using advanced natural language processing (NLP) techniques. The platform leverages the powerful Google DeepMind “Gemini-Pro” model to interpret context, while GoogleGenerativeAIEmbeddings create robust document embeddings that convert text into vectors, facilitating efficient and accurate information retrieval. To further improve performance, SmartText Insight utilizes the FAISS (Facebook AI Similarity Search) vector store, an indexing system known for its speed and scalability, making it suitable for large volumes of text. </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> The application’s interface is user-friendly, offering step-by-step guidance for uploading files, processing text, and generating responses to user queries. Once the documents are indexed, users can input questions to receive contextually relevant and detailed responses in bullet points, enhancing readability and comprehension. The project is a practical application of generative AI and vector-based search, aimed at making document exploration more accessible, interactive, and insightful. This powerful solution streamlines the process of extracting information from lengthy or complex documents, enabling users to navigate large amounts of content and find relevant answers effortlessly. </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify">  </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify">  </div>', unsafe_allow_html=True)
    st.write('')
    
    col44, col45 = st.columns([2,8])
    with col44:
        st.markdown(':orange[Hosted online at: ]')
    with col45:
        st.markdown('https://talk-to-your-data-by-gururaj-hc.streamlit.app/')
    st.divider() 

    st.write('')
    st.write('')
    # col33, col34, col35 = st.columns([3,100,3])
    # with col34:
    st.subheader(':orange[**Transforming Data into Conversational Wisdom**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> This Streamlit application facilitates an interactive, conversational exploration of data stored in CSV files, allowing users to ask questions about the dataset and receive AI-driven insights in response. After uploading a CSV file, the user provides their OpenAI API key, which the app validates by attempting a test interaction. If the key is verified, the application initializes a conversational agent using OpenAI\'s language model to process user queries. The app also tracks conversation history, allowing the context of previous interactions to enhance the continuity of responses.</div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> The code includes a unique approach to data queries, integrating regular expressions to parse questions for specific column references, ensuring the agent considers user-defined columns in its analysis. If no column is specified, it defaults to the last selected one, fostering a smooth and intuitive question-answer experience. The app\'s responses are presented in a markdown format, using tables whenever possible for better readability. The code dynamically updates the conversation history and selected column, preserving context and refining responses based on prior interactions.</div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> To enhance usability, the application is styled with custom fonts and colors, providing a visually engaging and branded experience. The app guides users step-by-step—from data upload, API key entry, and question submission, to the iterative conversational query process—making data analysis accessible even for non-technical users.  </div>', unsafe_allow_html=True)
    st.write('')
     
    col46, col47 = st.columns([2,8])
    with col46:
        st.markdown(':orange[Hosted online at: ]')
    with col47:
        st.markdown('https://talk-to-your-csv-by-gururaj-hc.streamlit.app/')
    st.divider() 

    st.write('')
    st.write('')
    # col33, col34, col35 = st.columns([3,100,3])
    # with col34:
    st.subheader(':orange[**Youtube assistant using Langchain and OPENAI**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> This code creates a Streamlit application that serves as a YouTube content assistant by allowing users to ask questions about the content of a YouTube video and receive AI-generated responses based solely on the video\'s transcript. It uses Langchain and OpenAI\’s language model to process the video transcript, breaking it down into manageable text chunks that are transformed into vector embeddings and stored in a FAISS vector database. This database enables efficient similarity search, so when a user poses a question, the application can find the most relevant transcript chunks to construct an accurate answer.</div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> The application\’s workflow begins with the user providing a YouTube URL, an OpenAI API key, and a question. Using the YoutubeLoader class from Langchain, it loads the video transcript, which is then split into chunks by RecursiveCharacterTextSplitter. Each chunk is converted into embeddings via OpenAI\’s embedding model, and these embeddings are stored in a FAISS vector database. When a user asks a question, the app performs a similarity search on this database to locate the most pertinent transcript segments. These are passed to an OpenAI language model (text-davinci-003) in a prompt, formulated through PromptTemplate and executed with the LLMChain class, which generates a response based exclusively on the identified transcript chunks.</div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> The app\’s interface, designed with Streamlit, is styled for clarity and user-friendliness. It includes sections for entering the API key, YouTube URL, and user question, along with a button to initiate the answer retrieval process. Once the question is processed, the application presents the AI’s response in a text-wrapped format, making it easy to read. This design enables users to quickly extract specific information from YouTube videos, offering a practical tool for obtaining insights without needing to watch entire videos.</div>', unsafe_allow_html=True)
    st.write('')
    
    col50, col51 = st.columns([2,8])
    with col50:
        st.markdown(':orange[Hosted online at: ]')
    with col51:
        st.markdown('https://youtube-assistant-hc-gururaj.streamlit.app/')
    st.divider() 

    st.write('')
    st.write('')
    # col33, col34, col35 = st.columns([3,100,3])
    # with col34:
    st.subheader(':orange[**Q&A generation using LLM**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> Creating multiple-choice questions based on a given paragraph offers students a multifaceted approach to learning. It not only deepens comprehension by requiring them to distil key concepts and main ideas, but also engages them actively in the material, fostering a stronger grasp of the subject matter. This process encourages critical thinking as students formulate plausible distracters that challenge their own understanding and uncover potential misconceptions. Moreover, the skill of crafting questions cultivates the practical application of acquired knowledge, bridging the gap between theory and real-world scenarios. </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> As students compare their questions to model answers, they engage in meaningful self-assessment, identifying areas of strength and those in need of review. This exercise mirrors the format of assessments, thus aiding in effective test preparation. Beyond assessment, the act of generating questions prompts students to organize information logically, strengthening their ability to structure thoughts coherently. Collaborative sharing of questions with peers and educators initiates a valuable feedback loop, refining their understanding and enhancing communication skills. </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> This practice also nurtures vocabulary enrichment as students carefully select appropriate terminology. Ultimately, the process empowers students to take charge of their learning journey, cultivating autonomy and honing higher-order thinking skills. The lasting impact of question generation on long-term retention solidifies its role as a holistic tool for comprehensive understanding, effective study strategies, and academic growth. </div>', unsafe_allow_html=True)
    st.write('')
    # st.markdown('<div style="text-align: justify"> .</div>', unsafe_allow_html=True)
    # st.write('')
    #st.divider()
    
    col42, col43 = st.columns([2,8])
    with col42:
        st.markdown(':orange[Hosted online at: ]')
    with col43:
        st.markdown('https://gururaj-hc-questionandanswer-generation.streamlit.app/')
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
        st.markdown('_An_ _effort_ _by_ : :orange[**MAVERICK_GR**]')
    
    
    # st.markdown('<div style="text-align: justify">  </div>', unsafe_allow_html=True)
    # st.write('')
    # st.markdown('<div style="text-align: justify">  </div>', unsafe_allow_html=True)
    # st.write('')
