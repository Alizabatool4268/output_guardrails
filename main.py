from agents import Runner,set_tracing_disabled,InputGuardrailTripwireTriggered,OutputGuardrailTripwireTriggered
from my_agents.my_agent import basic_agent

prompt = input("what is your question: ")

set_tracing_disabled(True)
try:
    result = Runner.run_sync(
        starting_agent=basic_agent,
        input = prompt,
        context={"name":"basic_agent", "role":"userHelp"},
    )
    print(result.final_output)
except InputGuardrailTripwireTriggered as e:
    print(e)
except OutputGuardrailTripwireTriggered as e:
    print(e)    