import google.generativeai as genai

genai.configure(api_key="AIzaSyBbIKT2sXtrP_uMMdmglcxTBf47JHQlRcQ")

models = genai.list_models()
for model in models:
    print(model.name, "-", model.supported_generation_methods)