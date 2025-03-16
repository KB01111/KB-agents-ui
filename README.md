# OpenAI Agents SDK

The OpenAI Agents SDK is a lightweight and easy-to-use package for building agentic AI applications. It offers a small set of primitives and built-in features to help you create complex relationships between tools and agents. Here are the main features of the SDK:

* Agents: LLMs equipped with instructions and tools.
* Handoffs: Allow agents to delegate tasks to other agents.
* Guardrails: Enable input validation for agents.
* Agent loop: Built-in loop that handles calling tools, sending results to the LLM, and looping until the LLM is done.
* Python-first: Use built-in language features to orchestrate and chain agents.
* Function tools: Turn any Python function into a tool with automatic schema generation and Pydantic-powered validation.
* Tracing: Built-in tracing to visualize, debug, and monitor workflows, as well as use OpenAI's evaluation, fine-tuning, and distillation tools.

## Quickstart

To get started with the OpenAI Agents SDK, follow these steps:

* Create a project and virtual environment:
  ```sh
  mkdir my_project
  cd my_project
  python -m venv .venv
  ```

* Activate the virtual environment (do this every time you start a new terminal session):
  ```sh
  source .venv/bin/activate
  ```

* Install the Agents SDK:
  ```sh
  pip install openai-agents
  ```

* Set an OpenAI API key (if you don't have one, follow the instructions to create an OpenAI API key):
  ```sh
  export OPENAI_API_KEY=sk-...
  ```

## Creating and Running Agents

* Create your first agent:
  ```python
  from agents import Agent

  agent = Agent(
      name="Math Tutor",
      instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
  )
  ```

* Add a few more agents:
  ```python
  from agents import Agent

  history_tutor_agent = Agent(
      name="History Tutor",
      handoff_description="Specialist agent for historical questions",
      instructions="You provide assistance with historical queries. Explain important events and context clearly.",
  )

  math_tutor_agent = Agent(
      name="Math Tutor",
      handoff_description="Specialist agent for math questions",
      instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
  )
  ```

* Define your handoffs:
  ```python
  triage_agent = Agent(
      name="Triage Agent",
      instructions="You determine which agent to use based on the user's homework question",
      handoffs=[history_tutor_agent, math_tutor_agent]
  )
  ```

* Run the agent orchestration:
  ```python
  from agents import Runner

  async def main():
      result = await Runner.run(triage_agent, "What is the capital of France?")
      print(result.final_output)
  ```

## Adding Guardrails

* Add a guardrail:
  ```python
  from agents import GuardrailFunctionOutput, Agent, Runner
  from pydantic import BaseModel

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
  ```

* Put it all together and run the entire workflow, using handoffs and the input guardrail:
  ```python
  from agents import Agent, InputGuardrail, GuardrailFunctionOutput, Runner
  from pydantic import BaseModel
  import asyncio

  class HomeworkOutput(BaseModel):
      is_homework: bool
      reasoning: str

  guardrail_agent = Agent(
      name="Guardrail check",
      instructions="Check if the user is asking about homework.",
      output_type=HomeworkOutput,
  )

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

  async def homework_guardrail(ctx, agent, input_data):
      result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
      final_output = result.final_output_as(HomeworkOutput)
      return GuardrailFunctionOutput(
          output_info=final_output,
          tripwire_triggered=not final_output.is_homework,
      )

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
  ```

## Viewing Traces and Next Steps

* View your traces:
  To review what happened during your agent run, navigate to the Trace viewer in the OpenAI Dashboard to view traces of your agent runs.

* Next steps:
  Learn how to build more complex agentic flows. 

## Testing the Functionality

* Use the provided test functions to verify the functionality of the agents and the agent orchestration:
  ```python
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
  ```
