# Chatbot-Mysql-Langchain

## Project Overview

The project uses LangChain to integrate a chatbot with a SQL database. This enables non-technical users to conduct queries of relational databases just through natural language. With AI and NLP at the core, user queries are translated into SQL commands by the chatbot for seamless data retrieval.

## Technology Required

	•	Programming Language: Python 3.9 or later
	•	Frontend Framework: Streamlit
	•	Database: MySQL
	•	AI Model: Large Language Model (LLM) - Groq Llama3-8b-8192
	•	Libraries/Frameworks: LangChain, SQLAlchemy

 ## Libraries Used

	1.	LangChain: For building AI-powered applications and connecting LLMs with databases.
	2.	SQLAlchemy: For Object-Relational Mapping (ORM) and executing SQL commands.
	3.	Streamlit: For creating an interactive web-based frontend.
	4.	LangChain Community Toolkit: Specifically, the SQLDatabaseToolkit for seamless database integration.
	5.	MySQL Connector: For database communication.

 ## How to Run the app.py Streamlit File

 ### Clone the Repository
 
> git clone https://github.com/RahulVarunn/Chatbot-Mysql-Langchain.git
> cd Chatbot-Mysql-Langchain

### Install Dependencies

> pip install -r requirements.txt

### Run Streamlit File
> streamlit run app.py
