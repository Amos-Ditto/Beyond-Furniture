<script setup lang="ts">
defineProps<{
	bg: string;
}>();
</script>

<template>
	<div class="item flex flex-col rounded-md px-2 py-3 gap-y-3 min-h-[20rem]" :class="bg"></div>
</template>
