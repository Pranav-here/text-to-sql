import streamlit as st

def main():
    st.set_page_config(page_title="Natural Language to SQL")
    st.header("Talk to your database")

    user_query=st.text_input("Input:")
    submit=st.button("Enter")
    if submit:
        st.header("Hi, I'm your assitant")

if __name__=='__main__':
    main()