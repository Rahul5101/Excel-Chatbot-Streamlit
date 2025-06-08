import re

def clean_column_names(columns):
    return [re.sub(r'\W+', '_', col.strip().lower()) for col in columns]
