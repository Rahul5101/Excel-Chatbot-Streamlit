import os
import google.generativeai as genai
from google.generativeai import GenerativeModel, GenerationConfig
import pandas as pd
import json
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = GenerativeModel(
    model_name = "models/gemini-1.5-flash-latest",
    generation_config=GenerationConfig(temperature=0.5)
)

def Extract_dataset(ques, data: pd.DataFrame):
    try:
        
        normalize_col=[]
        for col in data.columns:
            normalize_col.append(col.strip().lower().replace(" ","_"))
        data.columns=normalize_col
    
        small_data = data.to_markdown(index=False)

        prompt = f"""
You are a great data Scientist. You are going to help me in analyzing the dataset that I provided to you in the tabular format.If the question 
implies a trend, comparison, or distribuƟon, generate appropriate charts (e.g. bar chart, histograms, line chart). Ensure the charts are readable 
and labelled clearly.
The assistant should support natural language queries like:
1 Statistically summaries (e.g. What is the average income?)
2 Filtered queries (e.g. How many customers are under 30?)
3 Comparisons or groupings (e.g. Compare loan defaults by gender)
4 Visual insights (e.g. Show a bar chart of transacƟon count by job)
If someone ask any question then write the answer only, don't write the code until you have been explictly asked and also draw the plots,chart and 
table if you have been asked.
the dataset is provided in the markdown format below.
{small_data}

The column names may be lowercased and underscored for processing.

Now, answer the following question based on the provided data:

Q: {ques}
A:"""

        
        answer = model.generate_content(prompt)

        
        finalAnswer = answer.text.strip()

        return {
            "type": "text",
            "content": finalAnswer
        }

    except Exception as e:
        return {
            "type": "text",
            "content": f"Failed to process Gemini response. {str(e)}"
        }
