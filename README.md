# Excel-Chatbot-Streamlit
This project showcases an intelligent Streamlit-based chatbot that leverages Google's Gemini Pro API to analyze Excel datasets using natural language queries. It simplifies data analysis by allowing users to ask questions like "How many people are above age 25?" and get instant answers with text, tables, or visual charts.


System Architecture
Frontend: Streamlit Interface

    The user uploads an Excel file (.xlsx).

    The interface accepts questions like:

    “How many people are older than 25?”
    “Show a bar chart of age by gender.”

Data Processing Layer

    The uploaded Excel file is parsed using Pandas.

    Column names, types, and sample rows are extracted.

    A dynamic prompt is prepared using LangChain’s PromptTemplate.

LLM Communication (Gemini Pro)

    The user’s question and context about the dataset are passed to Gemini via LLMChain.

    The model responds with:

    Direct answers (text)

    Table-style summaries

    Python code for chart generation (e.g., bar plot, pie chart)

Execution and Output

    The generated Python code (if any) is safely executed in the backend.

    Charts are plotted using Matplotlib and shown instantly.

    Text responses and tables are rendered cleanly via Streamlit.



 Features
✅ Upload and parse Excel (.xlsx) datasets

💬 Chatbot interface powered by Gemini Pro (via LangChain)

📈 Auto-generates:

    Textual insights

    Data summaries

    Bar charts, pie charts, and more (via Matplotlib)

🔄 Dynamic prompt handling with PromptTemplate and LLMChain

🧠 Understands column names, types, and data distribution.



🛠️ Tech Stack
Python

Streamlit

Gemini Pro API

LangChain

Matplotlib / Seaborn / Pandas

HOW TO RUN
1. clone this repository:
   git clone https://github.com/Rahul5101/Excel-Chatbot-Streamlit.git
   cd excel-chatbot-gemini

2. install dependicies:
   pip install -r requirements.txt

3. create a .env file and add api key:
   GEMINI_API_KEY=your_api_key_here

4. start the streamlit app:
   streamlit run app.py


