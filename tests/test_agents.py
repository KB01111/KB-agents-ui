import pytest
from agents import Agent, InputGuardrail, GuardrailFunctionOutput, Runner
from pydantic import BaseModel
import asyncio

# Define agents for math and history tutoring
math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
)

history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
)

# Define a triage agent with handoffs to math and history agents
triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[history_tutor_agent, math_tutor_agent]
)

# Define a guardrail agent and a guardrail function
class HomeworkOutput(BaseModel):
    is_homework: bool
    reasoning: str

guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking about homework.",
    output_type=HomeworkOutput,
)

async def homework_guardrail(ctx, agent, input_data):
    result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
    final_output = result.final_output_as(HomeworkOutput)
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_homework,
    )

# Implement the main function to run the agent orchestration
triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[history_tutor_agent, math_tutor_agent],
    input_guardrails=[
        InputGuardrail(guardrail_function=homework_guardrail),
    ],
)

async def main():
    result = await Runner.run(triage_agent, "who was the first president of the united states?")
    print(result.final_output)

    result = await Runner.run(triage_agent, "what is life")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

# Test functions to verify the functionality of the agents and the agent orchestration
@pytest.mark.asyncio
async def test_math_tutor_agent():
    result = await Runner.run(math_tutor_agent, "What is 2 + 2?")
    assert "4" in result.final_output

@pytest.mark.asyncio
async def test_history_tutor_agent():
    result = await Runner.run(history_tutor_agent, "Who was the first president of the United States?")
    assert "George Washington" in result.final_output

@pytest.mark.asyncio
async def test_trige_agent_routing():
    result = await Runner.run(triage_agent, "What is 2 + 2?")
    assert "4" in result.final_output

    result = await Runner.run(triage_agent, "Who was the first president of the United States?")
    assert "George Washington" in result.final_output

@pytest.mark.asyncio
async def test_guardrail_function():
    result = await homework_guardrail(None, None, "Is this a homework question?")
    assert result.tripwire_triggered is False
