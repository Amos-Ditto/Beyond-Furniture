<script setup lang="ts">
import { Categories } from "~~/Types/common";

defineProps<{
	togglecategories: boolean;
	categories: Categories[];
}>();

const emits = defineEmits<{
	(e: "chooseCategory", payload: Categories);
}>();
</script>
<template>
	<Transition name="drop-down">
		<div
			v-if="togglecategories"
			class="search-drop-down absolute bottom-0 shadow-xl translate-y-[105%] right-0 min-w-[10rem] bg-gray-50 rounded flex flex-col py-2 gap-y-2"
		>
			<button
				v-for="category in categories"
				:key="category.id"
				@click="emits('chooseCategory', category)"
				class="py-2 px-3 tracking-wide hover:bg-gray-200 focus:bg-gray-200 text-sm capitalize flex justify-start items-center"
			>
				{{ category.Name }}
			</button>
		</div>
	</Transition>
</template>

<style scoped>
.drop-down-enter-from {
	@apply opacity-0 translate-y-[100%] -z-10;
}
.drop-down-leave-to {
	@apply opacity-0;
}
.drop-down-enter-active,
.drop-down-leave-active {
	@apply transition duration-300;
}
</style>
