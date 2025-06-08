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
    
        small_data = data.head(501).to_markdown(index=False)

        prompt = f"""
You are a great data Scientist. You are going to help me in analyzing the dataset that I provided to you in the tabular format.If the question 
implies a trend, comparison, or distribuƟon, generate appropriate charts (e.g. bar chart, histograms, line chart). Ensure the charts are readable 
and labelled clearly.

If someone ask any question then analyze the code and you have the code execution capability and then write the answer, and don't write the code until you have been explictly asked and also draw the plots,chart and 
table if you have been asked.you have access to code execution capabilities and you can perform any operation on the dataset to answer the question.

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

    except Exception as error:
        return {
            "type": "text",
            "content": f"Failed to process the response. {str(error)}"
        }
