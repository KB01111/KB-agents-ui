<script>
  import { writable } from 'svelte/store';
  export let agents;
  
  let selectedAgentIndex = 0;
  let userPrompt = '';
  let response = writable('');
  let isLoading = writable(false);
  
  async function testAgent() {
    if ($agents.length === 0) {
      response.set('Please create an agent first');
      return;
    }
    
    if (!userPrompt) {
      response.set('Please enter a prompt');
      return;
    }
    
    isLoading.set(true);
    response.set('Processing...');
    
    // Simulate API call
    setTimeout(() => {
      const agent = $agents[selectedAgentIndex];
      response.set(`Response from ${agent.name}: This is a simulated response since we can't make actual API calls in this demo.`);
      isLoading.set(false);
    }, 2000);
  }
</script>

<div class="mb-4 p-4 border rounded bg-gray-50">
  <h2 class="text-xl font-bold mb-2">Test Your Agent</h2>
  
  {#if $agents.length === 0}
  <div class="p-4 border rounded bg-gray-100">Create an agent first to test it.</div>
  {:else}
  <div class="mb-4">
    <label class="block mb-2">Select Agent:</label>
    <select bind:value={selectedAgentIndex} class="w-full p-2 border rounded">
      {#each $agents as agent, i}
      <option value={i}>{agent.name}</option>
      {/each}
    </select>
  </div>
  
  <div class="mb-4">
    <label class="block mb-2">Your Prompt:</label>
    <textarea bind:value={userPrompt} class="w-full p-2 border rounded h-20" placeholder="Enter your prompt here..."></textarea>
  </div>
  
  <button on:click={testAgent} class="bg-green-500 text-white p-2 rounded mb-4" disabled={$isLoading}>
    {$isLoading ? 'Processing...' : 'Test Agent'}
  </button>
  
  {#if $response}
  <div class="p-4 border rounded bg-white">
    <h3 class="font-bold mb-2">Response:</h3>
    <p class="whitespace-pre-wrap">{$response}</p>
  </div>
  {/if}
  {/if}
</div>
