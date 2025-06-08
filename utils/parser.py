import re

def clean_column(columns):
    cleaned=[]
    for column in columns:
        column = column.strip().lower()
        column = ''.join(col if col.isalnum() else ' ' for col in column)
        cleaned.append(column)
    return cleaned




