from agents import Agent
from my_config.my_data_config import MODEL
from guardrails.guardrails import input_guardrial_function, guardrail_output_function

basic_agent= Agent(
    name="basic_agent",
    model= MODEL,
    instructions="Help users with there basic quries",
    input_guardrails=[input_guardrial_function],
    output_guardrails=[guardrail_output_function]
)