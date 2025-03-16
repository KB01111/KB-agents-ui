<script>
  export let apiKey;
</script>

<div class="mb-4 p-4 border rounded bg-gray-50">
  <h2 class="text-xl font-bold mb-2">API Key Configuration</h2>
  <div>
    <label class="block mb-2">OpenAI API Key:</label>
    <input type="password" bind:value={apiKey} class="w-full p-2 border rounded" placeholder="sk-..."/>
    <p class="text-sm text-gray-600 mt-1">Your API key is never stored on our servers</p>
  </div>
</div>
