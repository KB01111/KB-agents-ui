import tkinter as tk
from tkinter import messagebox
from agents import Agent, Runner

class AgentManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Agent Manager")

        self.api_key_label = tk.Label(root, text="OpenAI API Key:")
        self.api_key_label.pack()
        self.api_key_entry = tk.Entry(root, show="*")
        self.api_key_entry.pack()

        self.agent_name_label = tk.Label(root, text="Agent Name:")
        self.agent_name_label.pack()
        self.agent_name_entry = tk.Entry(root)
        self.agent_name_entry.pack()

        self.agent_instructions_label = tk.Label(root, text="Agent Instructions:")
        self.agent_instructions_label.pack()
        self.agent_instructions_entry = tk.Entry(root)
        self.agent_instructions_entry.pack()

        self.create_agent_button = tk.Button(root, text="Create Agent", command=self.create_agent)
        self.create_agent_button.pack()

        self.update_agent_button = tk.Button(root, text="Update Agent", command=self.update_agent)
        self.update_agent_button.pack()

        self.delete_agent_button = tk.Button(root, text="Delete Agent", command=self.delete_agent)
        self.delete_agent_button.pack()

        self.agent_listbox = tk.Listbox(root)
        self.agent_listbox.pack()

        self.agents = {}

    def create_agent(self):
        api_key = self.api_key_entry.get()
        agent_name = self.agent_name_entry.get()
        agent_instructions = self.agent_instructions_entry.get()

        if not api_key or not agent_name or not agent_instructions:
            messagebox.showerror("Error", "All fields are required")
            return

        agent = Agent(name=agent_name, instructions=agent_instructions)
        self.agents[agent_name] = agent
        self.agent_listbox.insert(tk.END, agent_name)
        messagebox.showinfo("Success", f"Agent '{agent_name}' created successfully")

    def update_agent(self):
        selected_agent_index = self.agent_listbox.curselection()
        if not selected_agent_index:
            messagebox.showerror("Error", "No agent selected")
            return

        agent_name = self.agent_listbox.get(selected_agent_index)
        agent_instructions = self.agent_instructions_entry.get()

        if not agent_instructions:
            messagebox.showerror("Error", "Agent instructions are required")
            return

        agent = self.agents[agent_name]
        agent.instructions = agent_instructions
        messagebox.showinfo("Success", f"Agent '{agent_name}' updated successfully")

    def delete_agent(self):
        selected_agent_index = self.agent_listbox.curselection()
        if not selected_agent_index:
            messagebox.showerror("Error", "No agent selected")
            return

        agent_name = self.agent_listbox.get(selected_agent_index)
        del self.agents[agent_name]
        self.agent_listbox.delete(selected_agent_index)
        messagebox.showinfo("Success", f"Agent '{agent_name}' deleted successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgentManagerApp(root)
    root.mainloop()
