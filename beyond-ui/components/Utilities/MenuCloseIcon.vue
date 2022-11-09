<script setup lang="ts">
defineProps<{
	class: string;
}>();
</script>
<template>
	<div class="orders">
		<img src="@/assets/components/icons8-close-window-50.png" alt="" :class="class" />
	</div>
</template>
