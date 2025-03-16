<script>
  export let errorMessage;
</script>

{#if $errorMessage}
<div class="fixed bottom-4 right-4 bg-red-500 text-white p-4 rounded shadow-lg">
  {$errorMessage}
  <button on:click={() => errorMessage.set('')} class="ml-2 font-bold">×</button>
</div>
{/if}
