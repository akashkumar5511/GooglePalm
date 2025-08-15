# langchain_utils.py
import streamlit as st
from langchain_helper import get_few_shots_db_chain
st.title("Atliq T-shirts: Database QNA ")

question=st.text_input("question: ")
if question:
  chain = get_few_shots_db_chain()
  answer =chain.run(question)
  st.header("Answer: ")
  st.write(answer)













