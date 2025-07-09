import streamlit as st
import os
import sqlite3
import dotenv
dotenv.load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


def get_sql_query_from_text(user_query):
    groq_sys_prompt = ChatPromptTemplate.from_template("""
        You are an expert at turning plain-English questions into SQL.

        The database is called CRICKET and has one table, CRICKETER, with columns:
        ▸ PLAYER_NAME
        ▸ TEAM
        ▸ ROLE        -- e.g. Batsman, Bowler, All-rounder
        ▸ RUNS
        ▸ WICKETS

        Example 1 – “How many players are in the table?”
            SELECT COUNT(*) FROM CRICKETER;

        Example 2 – “List all bowlers from India.”
            SELECT * FROM CRICKETER
            WHERE TEAM = 'India' AND ROLE = 'Bowler';

        Rules:
          • No ``` fences.
          • Don’t include the word “sql”.
          • Output only a valid SQL query.

        Now convert this question to SQL: {user_query}
    """)

    model="gemma2-9b-it"
    llm = ChatGroq(
        groq_api_key=os.environ.get("GROQ_API_KEY"),
        model_name=model
    )
    chain=groq_sys_prompt | llm | StrOutputParser()
    sql_query=chain.invoke({"user_query": user_query})


    return sql_query


def get_data_from_database(sql_query):
    database="cricket.db"
    with sqlite3.connect(database) as connection:
        return connection.execute(sql_query).fetchall()


def main():
    st.set_page_config(page_title="Natural Language to SQL")
    st.header("Talk to your database")

    user_query=st.text_input("Input:")
    submit=st.button("Enter")
    if submit:
        sql_query = get_sql_query_from_text(user_query)
        retrived_data=get_data_from_database(sql_query)
        st.header(f"Retriveing data fromt he databse with the query: [{sql_query}]")
        for row in retrived_data:
            st.header(row)

if __name__=='__main__':
    main()