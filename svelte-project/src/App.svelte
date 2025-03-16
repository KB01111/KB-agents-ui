<script>
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';
  import AgentFormModal from './AgentFormModal.svelte';
  import AgentList from './AgentList.svelte';
  import AgentErrorHandling from './AgentErrorHandling.svelte';
  import AgentAPIKey from './AgentAPIKey.svelte';
  import AgentTest from './AgentTest.svelte';
  import AgentTraceViewer from './AgentTraceViewer.svelte';

  let apiKey = '';
  let agentName = '';
  let agentInstructions = '';
  let agents = writable([]);
  let showModal = writable(false);
  let selectedAgentIndex = writable(null);
  let errorMessage = writable('');

  function createAgent() {
    if (!apiKey || !agentName || !agentInstructions) {
      errorMessage.set('All fields are required');
      return;
    }

    agents.update(currentAgents => {
      const newAgent = { name: agentName, instructions: agentInstructions };
      return [...currentAgents, newAgent];
    });

    agentName = '';
    agentInstructions = '';
    showModal.set(false);
  }

  function updateAgent(index) {
    if (!agentInstructions) {
      errorMessage.set('Agent instructions are required');
      return;
    }

    agents.update(currentAgents => {
      const updatedAgents = [...currentAgents];
      updatedAgents[index].instructions = agentInstructions;
      return updatedAgents;
    });

    agentInstructions = '';
    showModal.set(false);
  }

  function deleteAgent(index) {
    agents.update(currentAgents => {
      const updatedAgents = [...currentAgents];
      updatedAgents.splice(index, 1);
      return updatedAgents;
    });
  }

  function openModal(index = null) {
    selectedAgentIndex.set(index);
    showModal.set(true);
  }

  function closeModal() {
    showModal.set(false);
    errorMessage.set('');
  }
</script>

<main class="p-4">
  <h1 class="text-2xl font-bold mb-4">AI Agent Manager</h1>

  <AgentAPIKey bind:apiKey={apiKey} />

  <div class="mb-4">
    <button on:click={() => openModal()} class="bg-blue-500 text-white p-2 rounded">Create Agent</button>
  </div>

  <AgentList {agents} {openModal} {deleteAgent} />

  <AgentFormModal {showModal} {selectedAgentIndex} {agentName} {agentInstructions} {createAgent} {updateAgent} {closeModal} {errorMessage} />

  <AgentErrorHandling {errorMessage} />

  <AgentTest {agents} />

  <AgentTraceViewer {agents} />
</main>
