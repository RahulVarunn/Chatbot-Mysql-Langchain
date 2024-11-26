import streamlit as st
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from sqlalchemy import create_engine
from langchain_groq import ChatGroq
from streamlit_js_eval import streamlit_js_eval




st.set_page_config(page_title="Chat with SQL DB")
st.title("Chat with SQL DataBase")
st.subheader("LangChain Application")
st.markdown("<br><br>", unsafe_allow_html=True)



MYSQL="USE_MYSQL"
db_uri=MYSQL
import streamlit as st
api_key=st.sidebar.text_input(label="GRoq API Key",type="password")

st.sidebar.markdown("<br><br>", unsafe_allow_html=True)


options=["localhost", "Custom"]
host_option = st.sidebar.selectbox("Choose MySQL Host",options)

if host_option == "localhost":
    mysql_host = "localhost" 
else:
    mysql_host = st.sidebar.text_input("Enter MySQL Host Address")
    
mysql_user=st.sidebar.text_input("MYSQL User")
mysql_password=st.sidebar.text_input("MYSQL password",type="password")
mysql_db=st.sidebar.text_input("MySQL database")

if not db_uri:
    st.info("Please enter the database information and uri")

if not api_key:
    st.info("Please add the groq api key")

## LLM model
if api_key:
    llm=ChatGroq(groq_api_key=api_key,model_name="Llama3-8b-8192",streaming=True)
    
   
   
 

@st.cache_resource(ttl="2h")
def configure_db(db_uri,mysql_host=None,mysql_user=None,mysql_password=None,mysql_db=None):
    
        if not (mysql_host and mysql_user  and mysql_db):
            st.error("Please provide all MySQL connection details.")
            st.stop()
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"))   
    
if db_uri==MYSQL:
    
    db=configure_db(db_uri,mysql_host,mysql_user,mysql_password,mysql_db)
else:
    db=configure_db(db_uri)

## toolkit
toolkit=SQLDatabaseToolkit(db=db,llm=llm)

agent=create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True
)



if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_query=st.chat_input(placeholder="Ask anything from the database")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        streamlit_callback=StreamlitCallbackHandler(st.container())
        response=agent.run(user_query,callbacks=[streamlit_callback])
        st.session_state.messages.append({"role":"assistant","content":response})
        st.write(response)

        


