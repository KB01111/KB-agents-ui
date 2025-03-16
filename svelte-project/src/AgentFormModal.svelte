<script>
  export let showModal;
  export let selectedAgentIndex;
  export let agentName;
  export let agentInstructions;
  export let createAgent;
  export let updateAgent;
  export let closeModal;
  export let errorMessage;

  $: isEdit = $selectedAgentIndex !== null;
  $: title = isEdit ? 'Edit Agent' : 'Create Agent';
  $: buttonText = isEdit ? 'Update' : 'Create';

  function handleSubmit() {
    if (isEdit) {
      updateAgent($selectedAgentIndex);
    } else {
      createAgent();
    }
  }
</script>

{#if $showModal}
<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
  <div class="bg-white p-4 rounded max-w-md w-full">
    <h2 class="text-xl font-bold mb-4">{title}</h2>
    
    {#if !isEdit}
    <div class="mb-4">
      <label class="block mb-2">Agent Name:</label>
      <input type="text" bind:value={agentName} class="w-full p-2 border rounded" />
    </div>
    {/if}
    
    <div class="mb-4">
      <label class="block mb-2">Agent Instructions:</label>
      <textarea bind:value={agentInstructions} class="w-full p-2 border rounded h-32"></textarea>
    </div>
    
    {#if $errorMessage}
    <div class="text-red-500 mb-4">{$errorMessage}</div>
    {/if}
    
    <div class="flex justify-end space-x-2">
      <button on:click={closeModal} class="bg-gray-300 p-2 rounded">Cancel</button>
      <button on:click={handleSubmit} class="bg-blue-500 text-white p-2 rounded">{buttonText}</button>
    </div>
  </div>
</div>
{/if}
