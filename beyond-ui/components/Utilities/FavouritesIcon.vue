<script setup lang="ts">
defineProps<{
	class: string;
}>();
</script>
<template>
	<div class="favorites">
		<img src="@/assets/components/icons8-favorites.svg" alt="" :class="class" />
	</div>
</template>
