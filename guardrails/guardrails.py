from agents import  Agent,  GuardrailFunctionOutput,RunContextWrapper, Runner, TResponseInputItem,input_guardrail,output_guardrail
from my_agents.guardrial_agent import guardrial_agent

@input_guardrail
async def input_guardrial_function(ctx: RunContextWrapper, agent: Agent, input: str | list[TResponseInputItem])->GuardrailFunctionOutput:
     
     result = await Runner.run(guardrial_agent, input ,context = ctx.context["name"])
     
     return GuardrailFunctionOutput(
         output_info=result.final_output,
        tripwire_triggered= result.final_output.is_querry_related_to_math
        )
     
@output_guardrail
async def guardrail_output_function(ctx: RunContextWrapper, agent: Agent, output) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrial_agent, output, context=ctx.context)     
    
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered= result.final_output.is_querry_related_to_politics_or_political_figures,
    )