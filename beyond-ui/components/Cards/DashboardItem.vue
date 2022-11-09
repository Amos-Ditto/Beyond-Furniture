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
		class="item flex flex-col rounded-md px-2 py-3 gap-y-3 sm:gap-y-8 h-auto sm:h-[22rem] w-auto transition-all duration-500 relative"
		:class="bg"
		v-bind:class="loaded ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-2'"
	>
		<div class="item-image w-full h-[74%] sm:h-[60%] flex items-center justify-center bg-gray-300 sm:bg-inherit">
			<!-- <slot name="img"></slot> -->
			<img
				src="@/assets/Furnitures/phillip-goldsberry-fZuleEfeA1Q-unsplash-removebg-preview.png"
				alt="furniture"
				class="object-contain h-full bg-inherit w-full sm:hover:scale-105 transition-transform duration-300 cursor-pointer"
			/>
		</div>
		<div class="item-body flex flex-col items-center w-full gap-y-1">
			<div class="item-details grid grid-cols-1 gap-y-1 sm:gap-y-2.5 py-3">
				<small class="text-gray-700 tracking-wide text-base sm:text-xl">Living room sofa</small>
				<div class="prices flex flex-row justify-center items-center gap-x-3">
					<small class="text-sm text-gray-700 tracking-wide">$30</small>
					<small class="text-sm text-gray-500 tracking-wide line-through decoration-gray-500">$40</small>
				</div>
			</div>
			<div class="add-cart w-full flex sm:hidden flex-col items-center">
				<button
					class="text-base tracking-wide w-full text-gray-100 font-light capitalize bg-orange-300 rounded-sm hover:bg-orange-400 transition-colors duration-200 py-1.5 px-4"
				>
					add cart
				</button>
			</div>
		</div>
		<div class="add-cart hidden sm:block absolute bottom-0 translate-y-1/2 -translate-x-1/2 left-1/2">
			<button class="p-2 rounded-full bg-amber-500 shadow-md hover:bg-amber-600 focus:bg-amber-600 duration-200 transition">
				<div class="i-mdi-plus text-gray-50 text-xl scale-125 sm:scale-110"></div>
			</button>
		</div>
	</div>
</template>
