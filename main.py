from fastapi import FastAPI
import string
from pydantic import BaseModel
 
app = FastAPI()
 
@app.get("/")
def health_check():
    return {"status": "API is running"}
 
class InputString(BaseModel):
    input_string: str
 
@app.post("/check-alphabet/")
def check_alphabet(data: InputString):
   
    alphabet_set = set(string.ascii_lowercase)
    filtered_input = ''.join(filter(str.isalpha, data.input_string)).lower()
    input_set = set(filtered_input)
       
    return {"contains_all_letters": alphabet_set.issubset(input_set)}
