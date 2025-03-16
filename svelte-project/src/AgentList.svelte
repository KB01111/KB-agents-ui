<script>
  export let agents;
  export let openModal;
  export let deleteAgent;
</script>

<div class="mb-4">
  <h2 class="text-xl font-bold mb-2">Your Agents</h2>
  
  {#if $agents.length === 0}
  <div class="p-4 border rounded bg-gray-100">No agents created yet.</div>
  {:else}
  <ul class="space-y-2">
    {#each $agents as agent, i}
    <li class="p-4 border rounded hover:bg-gray-50">
      <div class="flex justify-between items-center">
        <div>
          <h3 class="font-bold">{agent.name}</h3>
          <p class="text-sm text-gray-600">{agent.instructions.substring(0, 100)}...</p>
        </div>
        <div class="space-x-2">
          <button on:click={() => openModal(i)} class="bg-yellow-500 text-white p-1 rounded">Edit</button>
          <button on:click={() => deleteAgent(i)} class="bg-red-500 text-white p-1 rounded">Delete</button>
        </div>
      </div>
    </li>
    {/each}
  </ul>
  {/if}
</div>
