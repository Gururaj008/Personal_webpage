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
                    <p class="custom-text"> Data Science projects carried out</p>
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
    st.markdown('<div style="text-align: justify"> This Streamlit application facilitates an interactive, conversational exploration of data stored in CSV files, allowing users to ask questions about the dataset and receive AI-driven insights in response. After uploading a CSV file, the user provides their OpenAI API key, which the app validates by attempting a test interaction. If the key is verified, the application initializes a conversational agent using OpenAI's language model to process user queries. The app also tracks conversation history, allowing the context of previous interactions to enhance the continuity of responses.</div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> The code includes a unique approach to data queries, integrating regular expressions to parse questions for specific column references, ensuring the agent considers user-defined columns in its analysis. If no column is specified, it defaults to the last selected one, fostering a smooth and intuitive question-answer experience. The app's responses are presented in a markdown format, using tables whenever possible for better readability. The code dynamically updates the conversation history and selected column, preserving context and refining responses based on prior interactions.</div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> To enhance usability, the application is styled with custom fonts and colors, providing a visually engaging and branded experience. The app guides users step-by-step—from data upload, API key entry, and question submission, to the iterative conversational query process—making data analysis accessible even for non-technical users.  </div>', unsafe_allow_html=True)
    st.write('')
     
    col46, col47 = st.columns([2,8])
    with col46:
        st.markdown(':orange[Hosted online at: ]')
    with col47:
        st.markdown('https://https://talk-to-your-csv-by-gururaj-hc.streamlit.app/')
    st.divider() 

    st.write('')
    st.write('')
    # col33, col34, col35 = st.columns([3,100,3])
    # with col34:
    st.subheader(':orange[**Youtube assistant using Langchain and OPENAI**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> This code creates a Streamlit application that serves as a YouTube content assistant by allowing users to ask questions about the content of a YouTube video and receive AI-generated responses based solely on the video's transcript. It uses Langchain and OpenAI’s language model to process the video transcript, breaking it down into manageable text chunks that are transformed into vector embeddings and stored in a FAISS vector database. This database enables efficient similarity search, so when a user poses a question, the application can find the most relevant transcript chunks to construct an accurate answer.</div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> The application’s workflow begins with the user providing a YouTube URL, an OpenAI API key, and a question. Using the YoutubeLoader class from Langchain, it loads the video transcript, which is then split into chunks by RecursiveCharacterTextSplitter. Each chunk is converted into embeddings via OpenAI’s embedding model, and these embeddings are stored in a FAISS vector database. When a user asks a question, the app performs a similarity search on this database to locate the most pertinent transcript segments. These are passed to an OpenAI language model (text-davinci-003) in a prompt, formulated through PromptTemplate and executed with the LLMChain class, which generates a response based exclusively on the identified transcript chunks.</div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> The app’s interface, designed with Streamlit, is styled for clarity and user-friendliness. It includes sections for entering the API key, YouTube URL, and user question, along with a button to initiate the answer retrieval process. Once the question is processed, the application presents the AI’s response in a text-wrapped format, making it easy to read. This design enables users to quickly extract specific information from YouTube videos, offering a practical tool for obtaining insights without needing to watch entire videos.</div>', unsafe_allow_html=True)
    st.write('')
    
    col50, col51 = st.columns([2,8])
    with col44:
        st.markdown(':orange[Hosted online at: ]')
    with col45:
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

    
    # col33, col34, col35 = st.columns([3,100,3])
    # with col34:
    st.subheader(':orange[**Crop recommendation engine**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> Farmers play a pivotal role in India, where agriculture has been the backbone of the nation\'s economy and culture for centuries. Their significance cannot be overstated, as they are the primary source of food production for a vast and diverse population. India\'s agrarian sector not only provides sustenance but also contributes significantly to the country\'s GDP and employment. Farmers are custodians of the land, responsible for its fertility and sustainability. They embrace traditional wisdom while also adopting modern agricultural practices, striving to meet the growing demands of a burgeoning population. Their resilience in the face of various challenges, including adverse weather conditions and market fluctuations, is commendable. Moreover, they are the custodians of India\'s rich biodiversity, preserving countless indigenous crops and varieties. The importance of farmers in India extends beyond economic contributions, encompassing social and cultural dimensions, making them the backbone of the nation\'s identity and progress. Recognizing and supporting their efforts is crucial for ensuring food security, economic stability, and the overall well-being of the country.  </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> Artificial Intelligence (AI) holds immense potential to revolutionize agriculture and significantly benefit farmers. Through AI-powered technologies, farmers can access valuable insights and data-driven solutions that enhance crop management, optimize resource allocation, and improve overall productivity. AI can analyze vast amounts of data, including weather patterns, soil quality, and crop health, to provide precise recommendations on when to plant, irrigate, and harvest. Machine learning models can predict disease outbreaks and pest infestations, enabling early intervention and reducing crop losses. Moreover, AI-driven automation can streamline tasks such as harvesting and sorting, reducing labor costs and ensuring efficiency. AI-powered drones and sensors can monitor fields in real-time, helping farmers make informed decisions promptly. In essence, AI empowers farmers with the tools and knowledge needed to make agriculture more sustainable, efficient, and resilient in the face of the evolving challenges of modern farming.  </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> Recommending crop choices for farmers based on soil and weather conditions is of paramount importance in modern agriculture. These recommendations not only optimize crop yield and quality but also contribute significantly to sustainable and efficient farming practices. Soil quality and composition can vary widely even within a single region, and selecting the right crop that matches the soil\'s characteristics ensures optimal growth and reduces the need for excessive fertilizers or chemicals. Weather conditions, including rainfall patterns and temperature fluctuations, play a crucial role in determining crop success. Providing farmers with accurate and timely recommendations based on these factors helps mitigate risks associated with adverse weather events and climate change. Ultimately, tailoring crop choices to local soil and weather conditions not only boosts agricultural productivity but also promotes resource conservation and environmental sustainability, making it a key component of modern, responsible farming practices. </div>', unsafe_allow_html=True)
    st.write('')
    
    # st.markdown('<div style="text-align: justify"> .</div>', unsafe_allow_html=True)
    # st.write('')
    #st.divider()
    
    col40, col41 = st.columns([2,8])
    with col40:
        st.markdown(':orange[Hosted online at: ]')
    with col41:
        st.markdown('https://crop-recommendation-engine-by-gururaj-hc.streamlit.app/')
    st.divider() 






    
    
    
    # col33, col34, col35 = st.columns([3,100,3])
    # with col34:
    st.subheader(':orange[**Industrial Copper Modelling**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> This project involves sales and pricing prediction pertaining to Copper manufacturing industry. the data suffers from issues such as skewness and noise which can affect the accuracy of manual predictions. Dealing with these challenges manually can be time-consuming and may not result in optimal pricing decisions. A machine learning regression model can address these issues by utilizing advanced techniques such as data normalization, feature scaling, and outlier detection, and leveraging algorithms that are robust to skewed and noisy data.</div>', unsafe_allow_html=True)
    st.write('')
    # st.markdown('<div style="text-align: justify"> .</div>', unsafe_allow_html=True)
    # st.write('')
    # st.markdown('<div style="text-align: justify"> .</div>', unsafe_allow_html=True)
    # st.write('')
    # st.markdown('<div style="text-align: justify"> .</div>', unsafe_allow_html=True)
    # st.write('')
    #st.divider()
    
    col38, col39 = st.columns([2,8])
    with col38:
        st.markdown(':orange[Hosted online at: ]')
    with col39:
        st.markdown('https://gururaj-hc-industrial-copper-modelling.streamlit.app/')
    st.divider()
    
    
    
    
    
    
    
    
    
    
    
    
    
    # col33, col34, col35 = st.columns([3,100,3])
    # with col34:
    st.subheader(':orange[**Exploratory Data Analysis on wind data for Chitradurga,India**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> Being born and raised in Chitradurga which is one the largest wind energy producers in all of India, right from my early childhood had the inclination and passion towards wind energy. Following the passion pursued my Bachelors in "Electrical & Electronics Engineering" and my Masters in "Renewable Energy" leading to 06 technical publications with Springer, IEEE and other Scopus indexed journals.</div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> After finishing my Masters in 2019, I was looking for ways to further my research in "Wind Energy", that is when I stumbled upon the field of "Data Science" and have fallen in love with it ever since.</div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> The dataset to carry out this research activity was taken from MERRA-2 meteorological data. The timeframe considered is 2002-2022 in which there is one data point for every 10 minutes accounting for total of more than 1 Million data points. Each data point consists of information regarding pertaining weather conditions-Timestamp, Temperature, Solar irradiation, Relative humidity, Pressure, Snowfall, Snow depth, Wind direction and finally Wind speed. </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify">The only thing that is constant with wind is change hence; we need to analyze the effect of prevailing weather conditions on wind speed season-wise, month-wise, day-wise and hour-wise. This is exactly what I have tried to achieve in this project by plotting 80 different plots capturing every minute detail present in the dataset, clearly indicating what effect each weather condition has on wind speed.  </div>', unsafe_allow_html=True)
    st.write('')
    st.write('')
    col36, col37 = st.columns([2,8])
    with col36:
        st.markdown(':orange[Hosted online at: ]')
    with col37:
        st.markdown('https://gururaj008-cta-wind-data-eda.streamlit.app/')
    st.divider()

    # col23, col24, col25 = st.columns([1,150,1])
    # with col24:
    st.subheader(':orange[**Predicting Breast Cancer in a patient using SVM,ensemble techniques**]')
    st.write('')    
    st.subheader(':orange[**Problem statement**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> Given the details of cell nuclei taken from breast mass, predict whether or not a patient has breast cancer using the Ensembling Techniques. Perform necessary exploratory data analysis before building the model and evaluate the model based on performance metrics other than model accuracy. </div>', unsafe_allow_html=True)
    st.write('')
    col26, col27 = st.columns([20,20])
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    with col26:
        st.markdown(':orange[Jupyter notebook and a comprehensive report on the project available at: ]')
    with col27:
        st.markdown('https://github.com/Gururaj008/IITMDSA_DW42DW43_Final-Projects/tree/main/Projects/Predicting%20Breast%20Cancer%20in%20a%20patient')
    st.divider()

    # col29, col30, col31 = st.columns([15,80,15])
    # with col30:
    st.subheader(':orange[**Predicting Term deposit subscription by a client**]')
    st.write('')
    st.subheader(':orange[**Problem statement**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> Predict if a customer subscribes to a term deposits or not, when contacted by a marketing agent, by understanding the different features and performing predictive analytics </div>', unsafe_allow_html=True)
    st.write('')
    col32, col33 = st.columns([15,30])
    with col32:
        st.markdown(':orange[Jupyter notebook and a comprehensive report on the project available at: ]')
    with col33:
        st.markdown('https://github.com/Gururaj008/IITMDSA_DW42DW43_Final-Projects/tree/main/Projects/Predicting%20Term%20Deposit%20Subscription')
    st.divider()

    # col19, col20, col21 = st.columns([15,50,15])
    # with col20:
    st.subheader(':orange[**Extracting Business card data with OCR**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> A business card is a small printed card that typically contains an individual\'s or a company\'s contact information, such as name, job title, address, phone number, email address, and website. It serves as a tangible representation of professional identity and acts as a convenient networking tool.</div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> OCR stands for Optical Character Recognition. It is a technology that enables the conversion of printed or handwritten text into digital form by scanning and analyzing images or documents. The significance of OCR lies in its ability to automate and streamline various processes that involve the extraction and interpretation of textual information. </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> EasyOCR is an open-source Python library that provides a simple yet powerful Optical Character Recognition (OCR) solution. It allows developers to extract text from images or scanned documents effortlessly. EasyOCR supports more than 80 languages, making it a versatile tool for various applications and industries. One of the key advantages of EasyOCR is its ease of use. It offers a straightforward API, enabling developers to integrate OCR functionality into their applications with minimal coding effort. The library handles the complexities of text recognition, including text localization, character segmentation, and recognition, simplifying the overall development process. </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify">  Objective of this project is to leverage the abilities of EasyOCR to extract the information from business card, store it in a database for future retreival and usage. Hence, avoiding manual data entry.</div>', unsafe_allow_html=True)
    st.write('')
    st.write('')
    col21, col22 = st.columns([2,8])
    with col21:
        st.markdown(':orange[Code available at: ]')
    with col22:
        st.markdown('https://github.com/Gururaj008/Business_card_data/')
    st.divider()

    # col16, col17, col18 = st.columns([3,8,3])
    # with col17:
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
        st.markdown(':orange[Hosted online at: ]')
    with col12:
        st.markdown('https://gururaj008-phonepe-deploy-p-s-ycgqnz.streamlit.app/')
    st.divider()

    # col13, col14, col15 = st.columns([3,15,3])
    # with col14:
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
        st.markdown('https://github.com/Gururaj008/Youtube_project/')
    st.divider()
    
    # col8, col9, col10 = st.columns([1,5,1])
    # with col9:
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
        st.markdown(':orange[Hosted online at: ]')
    with col12:
        st.markdown('https://gururaj008-diabetes-prediction-diabetes-pred-5sop4d.streamlit.app/') 
    st.divider()
    
    # col1008, col1009, col1010 = st.columns([5,130,5])
    # with col1009:
    st.subheader(':orange[**Suggesting customer where to buy a specific product(Flipkart or Amazon)**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> The Indian e-commerce industry has been driven by increasing mobile phone adoption and is estimated to be $75 billion in 2022 and has the potential to expand up to $111 billion by 2024 and $200 billion by 2026. Amazon and Flipkart account for more than 60 percent of the Indian e-commerce market. The offers and discounts offered by each of them vary based on the festive season and special sale on specific date and time. </div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div style="text-align: justify"> The primary aim of this project is to help customer buy a specific product from the e-commerce market places like Flipkart and Amazon. The suggestion made is based on the selling price of the product and the amount of discount offered so that the customer ends up spending less on buying the product. </div>', unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')
    col1011, col1012 = st.columns([2,8])
    with col1011:
        st.markdown(':orange[Hosted online at: ]')
    with col1012:
        st.markdown('https://gururaj008-flipkart-or-amazon-fa-kxnbd3.streamlit.app/')
    st.divider()

    
    
   
    

    # col18, col19, col20 = st.columns([3,15,3])
    # with col19:
    #     st.subheader(':orange[**Extracting Business card data with OCR**]')
    # st.write('')
    # st.markdown('<div style="text-align: justify"> </div>', unsafe_allow_html=True)
    # st.write('')
    # st.markdown('<div style="text-align: justify"> </div>', unsafe_allow_html=True)
    # st.write('')
    # st.markdown('<div style="text-align: justify">  </div>', unsafe_allow_html=True)
    # st.write('')
    # st.markdown('<div style="text-align: justify">  </div>', unsafe_allow_html=True)
    # st.write('')
    # st.write('')
    # col16, col17 = st.columns([2,8])
    # with col16:
    #     st.markdown(':orange[Code available at: ]')
    # with col17:
    #     st.markdown('https://github.com/Gururaj008/Youtube_project/tree/main')
    # st.divider()

    # col18, col19, col20 = st.columns([3,15,3])
    # with col19:
    #     st.subheader(':orange[**Extracting Business card data with OCR**]')
    # st.write('')
    # st.markdown('<div style="text-align: justify"> </div>', unsafe_allow_html=True)
    # st.write('')
    # st.markdown('<div style="text-align: justify"> </div>', unsafe_allow_html=True)
    # st.write('')
    # st.markdown('<div style="text-align: justify">  </div>', unsafe_allow_html=True)
    # st.write('')
    # st.markdown('<div style="text-align: justify">  </div>', unsafe_allow_html=True)
    # st.write('')
    # st.write('')
    # col16, col17 = st.columns([2,8])
    # with col16:
    #     st.markdown(':orange[Code available at: ]')
    # with col17:
    #     st.markdown('https://github.com/Gururaj008/Youtube_project/tree/main')
    # st.divider()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
        st.markdown('_An_ _effort_ _by_ : :green[**MAVERICK_GR**]')
    
    
    # st.markdown('<div style="text-align: justify">  </div>', unsafe_allow_html=True)
    # st.write('')
    # st.markdown('<div style="text-align: justify">  </div>', unsafe_allow_html=True)
    # st.write('')
