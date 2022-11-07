<script setup lang="ts">
defineProps<{
	bg: string;
}>();

const itemref = ref<Element>(null);
const loaded = ref<boolean>(false);

onMounted(() => {
	const itemObs = new IntersectionObserver(
		(entry) => {
			if (entry[0].isIntersecting) {
				loaded.value = true;
				itemObs.unobserve(entry[0].target);
			}
		},
		{
			threshold: 0.25,
		}
	);

	itemObs.observe(itemref.value);
});
</script>

<template>
	<div
		ref="itemref"
		class="item flex flex-col rounded-md px-2 py-3 gap-y-4 h-[24rem] sm:h-[22rem] w-[15rem] sm:w-auto transition-all duration-500"
		:class="bg"
		v-bind:class="loaded ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-5'"
	>
		<div class="item-image w-full h-[75%] sm:h-[60%] flex items-center justify-center">
			<slot name="img"></slot>
		</div>
		<div class="item-body flex flex-col items-center w-full gap-y-2">
			<div class="item-details grid grid-cols-1 gap-y-2 py-3">
				<slot name="name"></slot>
				<slot name="prices"></slot>
			</div>
			<div class="add-cart w-full flex flex-col items-center">
				<button
					class="text-base tracking-wide w-full text-gray-100 font-bold capitalize bg-orange-300 rounded-sm hover:bg-orange-400 transition-colors duration-200 py-2 px-4"
				>
					add cart
				</button>
			</div>
		</div>
	</div>
</template>
