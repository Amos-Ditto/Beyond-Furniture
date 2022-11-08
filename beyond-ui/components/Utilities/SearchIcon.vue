<script setup lang="ts">
defineProps<{
	class: string;
}>();
</script>
<template>
	<div class="search-icon">
		<img src="@/assets/components/icons8-search.svg" alt="search" :class="class" />
	</div>
</template>
