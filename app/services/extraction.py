import os
import instructor

from groq import Groq
from pydantic import BaseModel
from app.core.setting import Settings



client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# By default, the patch function will patch the ChatCompletion.create and ChatCompletion.create methods to support the response_model parameter
client = instructor.from_groq(client, mode=instructor.Mode.TOOLS)


# Now, we can use the response_model parameter using only a base model
# rather than having to use the OpenAISchema class
class UserExtract(BaseModel):
    bill_to: str
   

def extract_data(content):
    prompt =  f"""
            You are a professional data extractor  . You are provided with content . Extract the mentioned data .
            {content}
"""
    response = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        response_model=UserExtract,
        messages=[
            {"role": "user", "content": prompt},
        ],
        temperature  = 0
    )
    return response

