<script setup lang="ts">
defineProps<{
	class: string;
}>();
</script>
<template>
	<div class="orders">
		<img src="@/assets/components/orders.png" alt="" :class="class" />
	</div>
</template>
