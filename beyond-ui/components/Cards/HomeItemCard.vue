<script setup lang="ts">
defineProps<{
	bg: string;
}>();
</script>

<template>
	<div class="item flex flex-col rounded-md px-2 py-3 gap-y-3 min-h-[24rem]" :class="bg">
		<div class="item-image w-full h-[14rem] flex items-center justify-center">
			<slot name="img"></slot>
		</div>
		<div class="item-details">
			<slot name="details"></slot>
		</div>
	</div>
</template>
