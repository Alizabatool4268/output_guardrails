from agents import Agent
from my_config.my_data_config import MODEL
from data_schema.my_data_schema import Mydataclass

guardrial_agent= Agent(
    name="guardrial_agent",
    model= MODEL,
    instructions="check quries for store Exclusive",
    output_type=Mydataclass
)