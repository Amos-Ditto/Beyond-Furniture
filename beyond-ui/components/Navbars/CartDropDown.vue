<script setup lang="ts">
const emits = defineEmits<{
	(e: "toggleCart");
}>();
</script>
<template>
	<div
		class="cart-drop-down absolute min-w-[18rem] sm:min-w-[20rem] right-0 lg:right-auto translate-x-[20%] lg:translate-x-0 bottom-0 translate-y-[110%] bg-gray-50 z-20 rounded border border-gray-300 shadow-lg flex flex-col gap-y-1 py-2"
	>
		<h3 class="text-lg tracking-wide px-2 text-gray-800">The Latest Addition</h3>
		<div class="items flex flex-col gap-y-0.5">
			<div class="empty-list px-4">
				<small class="text-sm text-gray-600 tracking-wide">No Item In Your Cart</small>
			</div>
		</div>
		<div class="open-cart pt-2 w-full px-2 flex flex-col">
			<RouterLink
				@click="emits('toggleCart')"
				to="/cart"
				class="py-2 flex flex-row items-center justify-center capitalize text-base text-gray-50 bg-amber-500 hover:bg-amber-600 focus:bg-amber-600 transition duration-200 rounded-sm"
			>
				view my cart
			</RouterLink>
		</div>
	</div>
</template>
