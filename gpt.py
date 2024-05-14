from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"),)


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": ("You are a tool helping to determine the greatest Quarterback" 
                                   "of all time for different nfl teams. When asked, you must" 
                                   "respond with ONLY the name of the quarterback and nothing else")},
    {"role": "user", "content": "Who is the greatest quarterback of the pittsburght stealers."}
  ]
)

print(completion.choices[0].message.content)