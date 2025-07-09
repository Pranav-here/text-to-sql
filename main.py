import os
import sqlite3

import streamlit as st
import pandas as pd
import dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ─── Load environment variables ───────────────────────────────────────────────
dotenv.load_dotenv()  # expects GROQ_API_KEY in your .env

# ─── Build the system prompt for translating English → SQL ───────────────────
groq_sys_prompt = ChatPromptTemplate.from_template("""
You are an expert at turning plain-English questions into SQL.

The database is called CRICKET and has one table, CRICKETER, with columns:
  • PLAYER_NAME
  • TEAM
  • ROLE        -- e.g. Batsman, Bowler, All-rounder
  • RUNS
  • WICKETS

Examples:
  “How many players are in the table?”
    SELECT COUNT(*) FROM CRICKETER;

  “List all bowlers from India.”
    SELECT * FROM CRICKETER
    WHERE TEAM = 'India' AND ROLE = 'Bowler';

Rules:
  • No ``` fences.
  • Don’t include the word “sql”.
  • Output only a valid SQL query.

Convert this question to SQL: {user_query}
""")

def get_sql_query_from_text(user_query: str) -> str:
    """Call Groq LLM to get a pure SQL string from a user question."""
    llm = ChatGroq(
        groq_api_key=os.environ["GROQ_API_KEY"],
        model_name="gemma2-9b-it"
    )
    chain = groq_sys_prompt | llm | StrOutputParser()
    return chain.invoke({"user_query": user_query})

def get_data_from_database(sql_query: str):
    """Run the generated SQL against cricket.db and return (cols, rows)."""
    with sqlite3.connect("cricket.db") as conn:
        cursor = conn.execute(sql_query)
        cols = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
    return cols, rows

def main():
    st.set_page_config(page_title="Text to SQL", layout="wide")
    st.title("Natural-Language → SQL")

    # 1️⃣  Get user input
    query = st.text_input("Ask a question about your CRICKETER table:")
    if st.button("Run Query"):
        with st.spinner("Translating to SQL…"):
            try:
                sql = get_sql_query_from_text(query)
            except Exception as e:
                st.error(f"Failed to generate SQL: {e}")
                return

        # 2️⃣  Show the generated SQL
        st.subheader("Generated SQL")
        st.code(sql, language="sql")

        # 3️⃣  Execute the SQL and fetch results
        try:
            cols, rows = get_data_from_database(sql)
        except Exception as e:
            st.error(f"Database error: {e}")
            return

        # 4️⃣  Display results as a pandas DataFrame
        st.subheader("Query Results")
        if rows:
            df = pd.DataFrame(rows, columns=cols)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No rows returned.")

if __name__ == "__main__":
    main()