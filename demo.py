"""
Demo script for KB-agents-ui

This script simulates the functionality of the agent system without requiring
the actual OpenAI API or agents library. It's useful for understanding the
behavior and interaction patterns of the system.

Usage:
python demo.py
"""

import time
import random

def simulate_agent_response(agent_name, query):
    """Simulate an agent responding to a query"""
    print(f"\n🔄 {agent_name} is processing: '{query}'")
    
    # Simulate thinking time
    time.sleep(1)
    
    if agent_name == "Math Tutor":
        if "2+2" in query or "2 + 2" in query:
            return "2 + 2 = 4. This is a simple addition operation where we add 2 and 2 together."
        elif any(x in query.lower() for x in ["add", "sum", "plus", "+"]):
            return "To add numbers, you simply combine their values. For example, 5 + 3 = 8."
        else:
            return "I can help with math problems. Can you provide a specific math question?"
    
    elif agent_name == "History Tutor":
        if "president" in query.lower() and "united states" in query.lower():
            return "George Washington was the first president of the United States, serving from 1789 to 1797."
        elif "france" in query.lower() and "capital" in query.lower():
            return "The capital of France is Paris. It has been the country's capital since 987 CE."
        else:
            return "I can help with historical questions. What period or event are you interested in?"
    
    elif agent_name == "Triage Agent":
        if any(x in query.lower() for x in ["math", "add", "sum", "plus", "+", "2+2"]):
            print("⤷ Delegating to Math Tutor")
            time.sleep(0.5)
            return simulate_agent_response("Math Tutor", query)
        elif any(x in query.lower() for x in ["history", "president", "capital", "war", "when"]):
            print("⤷ Delegating to History Tutor")
            time.sleep(0.5)
            return simulate_agent_response("History Tutor", query)
        else:
            # Make random choice if unclear
            choice = random.choice(["Math Tutor", "History Tutor"])
            print(f"⤷ Query is unclear, trying {choice}")
            time.sleep(0.5)
            return simulate_agent_response(choice, query)
    
    return "I'm not sure how to help with that query."

def main():
    """Main function to run the demo"""
    print("=" * 50)
    print("🤖 KB-agents-ui Demo")
    print("=" * 50)
    print("\nThis demo simulates the agent system without requiring actual OpenAI API access.")
    print("\nAvailable agents:")
    print("- Triage Agent (delegates to specialists)")
    print("- Math Tutor")
    print("- History Tutor")
    
    while True:
        print("\n" + "-" * 50)
        query = input("\n🔍 Enter your query (or 'exit' to quit): ")
        
        if query.lower() in ["exit", "quit", "q"]:
            print("\nThank you for trying the KB-agents-ui demo!")
            break
        
        # Process with main triage agent
        response = simulate_agent_response("Triage Agent", query)
        print(f"\n✅ Response: {response}")

if __name__ == "__main__":
    main()