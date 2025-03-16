<script>
  export let agents;
  
  let traceId = '';
  let traceData = null;
  let isLoading = false;
  
  function viewTrace() {
    if (!traceId) return;
    
    isLoading = true;
    
    // Simulate API call
    setTimeout(() => {
      traceData = {
        id: traceId,
        timestamp: new Date().toISOString(),
        agentName: 'Triage Agent',
        input: 'What is 2+2?',
        steps: [
          {
            type: 'thinking',
            content: 'This is a math question, so I should route to the Math Tutor agent.'
          },
          {
            type: 'handoff',
            content: 'Handing off to Math Tutor agent'
          },
          {
            type: 'response',
            content: '2+2 equals 4. This is a simple addition problem where we add two numbers together.'
          }
        ]
      };
      isLoading = false;
    }, 1000);
  }
</script>

<div class="mb-4 p-4 border rounded bg-gray-50">
  <h2 class="text-xl font-bold mb-2">Trace Viewer</h2>
  
  <div class="mb-4">
    <label class="block mb-2">Trace ID:</label>
    <div class="flex space-x-2">
      <input type="text" bind:value={traceId} class="flex-1 p-2 border rounded" placeholder="Enter trace ID..." />
      <button on:click={viewTrace} class="bg-blue-500 text-white p-2 rounded" disabled={isLoading || !traceId}>
        {isLoading ? 'Loading...' : 'View Trace'}
      </button>
    </div>
  </div>
  
  {#if traceData}
  <div class="p-4 border rounded bg-white">
    <h3 class="font-bold mb-2">Trace: {traceData.id}</h3>
    <div class="text-sm text-gray-600 mb-2">Time: {traceData.timestamp}</div>
    <div class="text-sm text-gray-600 mb-2">Agent: {traceData.agentName}</div>
    <div class="mb-4">
      <h4 class="font-bold">Input:</h4>
      <div class="p-2 bg-gray-100 rounded">{traceData.input}</div>
    </div>
    
    <h4 class="font-bold mb-2">Steps:</h4>
    <div class="space-y-2">
      {#each traceData.steps as step, i}
      <div class="p-2 border-l-4 border-blue-500 pl-4">
        <div class="font-bold capitalize">{step.type}</div>
        <div>{step.content}</div>
      </div>
      {/each}
    </div>
  </div>
  {/if}
</div>
