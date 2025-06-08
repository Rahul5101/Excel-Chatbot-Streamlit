import streamlit as st
import pandas as pd
from utils.parser import clean_column_names
from utils.charts import plot_chart
from llm.query_handler import Extract_dataset

st.set_page_config(page_title="Excel Chat Assistant", layout="wide")
st.title("📊 Excel-Based Chat Assistant")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    df.columns = clean_column_names(df.columns)
    st.subheader("Data Preview")
    st.dataframe(df.head(10))

    user_question = st.text_input("Ask a question about the data")

    if user_question:
        with st.spinner("Thinking..."):
            result = Extract_dataset(user_question, df)

        if result["type"] == "text":
            st.markdown(f"**Answer:** {result['content']}")

        elif result["type"] == "table":
            st.dataframe(result["content"])

        elif result["type"] == "chart":
            fig = plot_chart(df, result)
            st.pyplot(fig)

        else:
            st.error("Sorry, I didn't understand the query.")
