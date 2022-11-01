<script setup lang="ts">
defineProps<{
	bg: string;
}>();
</script>

<template>
	<div class="item flex flex-col rounded-md px-2 py-3 gap-y-3 h-[24rem] sm:h-[22rem] w-[15rem] sm:w-auto" :class="bg">
		<div class="item-image w-full h-[75%] sm:h-[60%] flex items-center justify-center">
			<slot name="img"></slot>
		</div>
		<div class="item-details grid grid-cols-2 gap-x-3 py-3">
			<slot name="name"></slot>
			<slot name="prices"></slot>
		</div>
	</div>
</template>
