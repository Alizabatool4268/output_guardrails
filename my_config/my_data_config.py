import os 
from agents import OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)
my_key = os.getenv("GEMINI_API_KEY")
my_base_url =os.getenv("BASE_URL")

client = AsyncOpenAI(
    api_key= my_key,
    base_url= my_base_url
)    
MODEL = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client,
)