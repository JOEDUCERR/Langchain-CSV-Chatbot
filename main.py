import streamlit as st
from langchain_experimental.agents import create_csv_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

def main():

    # load_dotenv()
    openai_key = st.secrets["OPENAI_API_KEY"]
    os.environ["OPENAI_API_KEY"] = openai_key

    st.set_page_config(
        page_title="Ask your CSV"
    )
    st.header("Ask your CSV")

    user_csv = st.file_uploader("Upload your CSV", type="csv")

    if user_csv is not None:
        user_question = st.text_input("Ask a question about your CSV")

        llm = ChatOpenAI(
            # model="gpt-3.5-turbo",
            temperature=0
            )
        agent = create_csv_agent(
            llm,
            user_csv,
            #agent_type="openai-tools",
            verbose=True,
            allow_dangerous_code=True
        )

        if user_question is not None and user_question != "":
            response = agent.run(user_question)
            st.write(response)

if  __name__ == "__main__":
    main()