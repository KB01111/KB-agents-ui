<script>
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';

  let apiKey = '';
  let agentName = '';
  let agentInstructions = '';
  let agents = writable([]);

  function createAgent() {
    if (!apiKey || !agentName || !agentInstructions) {
      alert('All fields are required');
      return;
    }

    agents.update(currentAgents => {
      const newAgent = { name: agentName, instructions: agentInstructions };
      return [...currentAgents, newAgent];
    });

    agentName = '';
    agentInstructions = '';
  }

  function updateAgent(index) {
    if (!agentInstructions) {
      alert('Agent instructions are required');
      return;
    }

    agents.update(currentAgents => {
      const updatedAgents = [...currentAgents];
      updatedAgents[index].instructions = agentInstructions;
      return updatedAgents;
    });

    agentInstructions = '';
  }

  function deleteAgent(index) {
    agents.update(currentAgents => {
      const updatedAgents = [...currentAgents];
      updatedAgents.splice(index, 1);
      return updatedAgents;
    });
  }
</script>

<main class="p-4">
  <h1 class="text-2xl font-bold mb-4">AI Agent Manager</h1>

  <div class="mb-4">
    <label class="block mb-2">OpenAI API Key:</label>
    <input type="password" bind:value={apiKey} class="border p-2 w-full" />
  </div>

  <div class="mb-4">
    <label class="block mb-2">Agent Name:</label>
    <input type="text" bind:value={agentName} class="border p-2 w-full" />
  </div>

  <div class="mb-4">
    <label class="block mb-2">Agent Instructions:</label>
    <input type="text" bind:value={agentInstructions} class="border p-2 w-full" />
  </div>

  <div class="mb-4">
    <button on:click={createAgent} class="bg-blue-500 text-white p-2 rounded">Create Agent</button>
  </div>

  <ul>
    {#each $agents as agent, index}
      <li class="mb-2">
        <div class="flex items-center justify-between">
          <div>
            <strong>{agent.name}</strong>: {agent.instructions}
          </div>
          <div>
            <button on:click={() => updateAgent(index)} class="bg-yellow-500 text-white p-2 rounded mr-2">Update</button>
            <button on:click={() => deleteAgent(index)} class="bg-red-500 text-white p-2 rounded">Delete</button>
          </div>
        </div>
      </li>
    {/each}
  </ul>
</main>
