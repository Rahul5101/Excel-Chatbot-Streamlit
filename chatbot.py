import streamlit as st
import pandas as pd
from utils.parser import clean_column
from utils.charts import plot_chart
from llm.query_handler import Extract_dataset

st.set_page_config(page_title="Excel Chat Assistant", layout="wide")
st.title("📊 Excel Chat Assistant")

excel_file = st.file_uploader("Please Upload your Excel file for further questioning", type=["xlsx"])

if excel_file:
    data = pd.read_excel(excel_file)
    data.columns = clean_column(data.columns)
    st.subheader("Data Trailer")
    st.dataframe(data.head(10))

    user_ques = st.text_input("Ask a question about the data")

    if user_ques:
        with st.spinner("Thinking..."):
            outcome = Extract_dataset(user_ques, data)

        if outcome["type"] == "text":
            st.markdown(f"**Answer:** {outcome['content']}")

        elif outcome["type"] == "table":
            st.dataframe(outcome["content"])

        elif outcome["type"] == "chart":
            fig = plot_chart(data, outcome)
            st.pyplot(fig)

        else:
            st.error("Sorry, I didn't have the knowledge about the query.")
