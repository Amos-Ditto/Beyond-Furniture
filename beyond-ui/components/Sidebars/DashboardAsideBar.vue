<script setup lang="ts">
import { Categories, Prices } from "~~/Types/common";

defineProps<{
	togglesidebar: boolean;
}>();

const emits = defineEmits<{
	(e: "applyFilters"): void;
	(e: "toggleSidebar", payload: boolean);
}>();

const categories = ref<Categories[]>([
	{ Name: "Living Room", id: 1 },
	{ Name: "Bed Room", id: 2 },
	{ Name: "kitchen Dining", id: 3 },
	{ Name: "Office Furniture", id: 4 },
	{ Name: "others", id: 5 },
]);
// Handle categories selection
const selectedcategory = ref<Categories[]>([]);

const selectCategory = (payload: Categories): void => {
	for (let i = 0; i < selectedcategory.value.length; i++) {
		if (selectedcategory.value[i].id === payload.id) {
			selectedcategory.value.splice(i, 1);
			return;
		}
	}
	selectedcategory.value.push(payload);
};
const checkSelectedCategory = (payload: Categories): boolean => {
	for (let i = 0; i < selectedcategory.value.length; i++) {
		if (selectedcategory.value[i].id === payload.id) {
			return true;
		}
	}
	return false;
};

// Handle prices selection
const prices = ref<Prices[]>([
	{ Name: "less than $30", id: 1 },
	{ Name: "$30 - $50", id: 3 },
	{ Name: "more than $50", id: 2 },
]);
const selectedprices = ref<Prices[]>([]);

const selectPrice = (payload: Prices): void => {
	for (let i = 0; i < selectedprices.value.length; i++) {
		if (selectedprices.value[i].id === payload.id) {
			selectedprices.value.splice(i, 1);
			return;
		}
	}
	selectedprices.value.push(payload);
};
const checkSelectedPrice = (payload: Prices): boolean => {
	for (let i = 0; i < selectedprices.value.length; i++) {
		if (selectedprices.value[i].id === payload.id) {
			return true;
		}
	}
	return false;
};
</script>
<template>
	<aside class="col-span-2 relative flex flex-col gap-y-3 z-20">
		<div class="desktop-side hidden md:flex flex-col gap-y-6 rounded h-auto py-2">
			<div class="categories flex flex-col gap-y-2">
				<h3 class="text-lg tracking-wide font-semibold capitalize px-3.5">categories</h3>
				<div
					class="w-full px-5 md:px-3.5 py-2 flex flex-row items-center gap-x-4 hover:bg-gray-200 transition duration-200 cursor-pointer selection:bg-gray-200 text-gray-700"
					v-for="category in categories"
					:key="category.id"
					@click="selectCategory(category)"
				>
					<button
						class="border border-gray-300 rounded w-5 h-5 py-1 bg-gray-50 after:text-gray-800 flex items-center justify-center after:text-xl"
						:class="checkSelectedCategory(category) ? 'category-check' : ''"
					></button>
					<small class="text-sm text-gray-700 capitalize">{{ category.Name }}</small>
				</div>
			</div>
			<div class="filters flex flex-col gap-y-2 w-full">
				<h3 class="text-lg tracking-wide font-semibold capitalize px-2">filters</h3>

				<div class="prices flex flex-col gap-y-2">
					<h3 class="text-sm font-semibold uppercase px-3.5 text-gray-700">price</h3>

					<div
						class="price w-full px-6 md:px-4 py-2 flex flex-row items-center gap-x-4 hover:bg-gray-200 transition duration-200 cursor-pointer selection:bg-gray-200 text-gray-700"
						v-for="price in prices"
						:key="price.id"
						@click="selectPrice(price)"
					>
						<button
							class="border border-gray-300 rounded w-4 h-4 py-1 bg-gray-50 after:text-gray-800 flex items-center justify-center after:text-xl"
							:class="checkSelectedPrice(price) ? 'category-check' : ''"
						></button>
						<small class="text-sm text-gray-700 capitalize">{{ price.Name }}</small>
					</div>
				</div>
				<div class="colors py-2 flex flex-col gap-y-2">
					<h3 class="text-sm font-semibold uppercase px-3.5 text-gray-700">colors</h3>
					<div class="color-list flex flex-wrap gap-x-3 gap-y-3 px-4 items-center justify-start">
						<label for="white">
							<input type="checkbox" name="white" id="white" class="bg-gray-50 checked:after:text-gray-800" />
						</label>
						<label for="blue">
							<input type="checkbox" name="blue" id="blue" class="bg-sky-600 checked:after:text-gray-50" />
						</label>
						<label for="green">
							<input type="checkbox" name="green" id="green" class="bg-emerald-500 checked:after:text-gray-50" />
						</label>
						<label for="orange">
							<input type="checkbox" name="orange" id="orange" class="bg-orange-400 checked:after:text-gray-50" />
						</label>
						<label for="black">
							<input type="checkbox" name="black" id="black" class="bg-dark checked:after:text-gray-50" />
						</label>
						<label for="brown">
							<input type="checkbox" name="brown" id="brown" class="bg-amber-700 checked:after:text-gray-50" />
						</label>
						<label for="purple">
							<input type="checkbox" name="purple" id="purple" class="bg-purple-800 checked:after:text-gray-50" />
						</label>
					</div>
				</div>
			</div>
			<div class="apply px-3.5 pt-4 pb-2">
				<button
					@click="emits('applyFilters')"
					class="text-sm tracking-wide bg-amber-600 hover:bg-amber-500 focus:bg-amber-500 text-gray-50 capitalize px-5 py-2 w-full rounded transition duration-200"
				>
					apply
				</button>
			</div>
		</div>
		<div
			class="toggle-side fixed md:hidden top-0 left-0 bottom-0 right-0 bg-gray-100 opacity-10 -z-10"
			v-if="togglesidebar"
			@click="emits('toggleSidebar', !togglesidebar)"
		></div>
		<Transition name="slide">
			<div
				class="mobile fixed flex top-10 bottom-0 left-0 flex-col gap-y-6 md:hidden w-1/2 h-full pt-10 pb-3 bg-gray-100 overflow-y-auto shadow-xl"
				v-if="togglesidebar"
			>
				<div class="categories flex flex-col gap-y-2">
					<h3 class="text-lg tracking-wide font-semibold capitalize px-4">categories</h3>
					<div
						class="w-full px-5 md:px-3.5 py-2 flex flex-row items-center gap-x-4 hover:bg-gray-200 transition duration-200 cursor-pointer selection:bg-gray-200 text-gray-700"
						v-for="category in categories"
						:key="category.id"
						@click="selectCategory(category)"
					>
						<button
							class="border border-gray-300 rounded w-5 h-5 py-1 bg-gray-50 after:text-gray-800 flex items-center justify-center after:text-xl"
							:class="checkSelectedCategory(category) ? 'category-check' : ''"
						></button>
						<small class="text-sm text-gray-700 capitalize">{{ category.Name }}</small>
					</div>
				</div>
				<div class="filters flex flex-col gap-y-2 w-full">
					<h3 class="text-lg tracking-wide font-semibold capitalize px-4">filters</h3>

					<div class="prices flex flex-col gap-y-2">
						<h3 class="text-sm font-semibold uppercase px-5 text-gray-700">price</h3>
						<div
							class="price w-full px-6 md:px-4 py-2 flex flex-row items-center gap-x-4 hover:bg-gray-200 transition duration-200 cursor-pointer selection:bg-gray-200 text-gray-700"
							v-for="price in prices"
							:key="price.id"
							@click="selectPrice(price)"
						>
							<button
								class="border border-gray-300 rounded w-4 h-4 py-1 bg-gray-50 after:text-gray-800 flex items-center justify-center after:text-xl"
								:class="checkSelectedPrice(price) ? 'category-check' : ''"
							></button>
							<small class="text-sm text-gray-700 capitalize">{{ price.Name }}</small>
						</div>
					</div>
					<div class="colors py-2 flex flex-col gap-y-2">
						<h3 class="text-sm font-semibold uppercase px-5 text-gray-700">colors</h3>
						<div class="color-list flex flex-wrap gap-x-3 gap-y-3 px-6 items-center justify-start">
							<label for="white">
								<input type="checkbox" name="white" id="white" class="bg-gray-50 checked:after:text-gray-800" />
							</label>
							<label for="blue">
								<input type="checkbox" name="blue" id="blue" class="bg-sky-600 checked:after:text-gray-50" />
							</label>
							<label for="green">
								<input type="checkbox" name="green" id="green" class="bg-emerald-500 checked:after:text-gray-50" />
							</label>
							<label for="orange">
								<input type="checkbox" name="orange" id="orange" class="bg-orange-400 checked:after:text-gray-50" />
							</label>
							<label for="black">
								<input type="checkbox" name="black" id="black" class="bg-dark checked:after:text-gray-50" />
							</label>
							<label for="brown">
								<input type="checkbox" name="brown" id="brown" class="bg-amber-700 checked:after:text-gray-50" />
							</label>
							<label for="purple">
								<input type="checkbox" name="purple" id="purple" class="bg-purple-800 checked:after:text-gray-50" />
							</label>
						</div>
					</div>
				</div>
				<div class="apply px-5 pt-4 pb-8">
					<button
						@click="emits('applyFilters')"
						class="text-sm tracking-wide bg-amber-600 hover:bg-amber-500 focus:bg-amber-500 text-gray-50 capitalize px-5 py-2 w-full rounded transition duration-200"
					>
						apply
					</button>
				</div>
			</div>
		</Transition>
	</aside>
</template>

<style scoped>
.desktop-side {
	box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 8px;
}

.color-list label input[type="checkbox"] {
	@apply w-8 md:w-6 h-8 md:h-6 appearance-none first:border rounded border-gray-300;
	@apply flex items-center justify-center checked:after:content-['\2713'] checked:after:text-xl;
}

/* Selection style */
.category-check {
	@apply after:content-['\2713'];
}

.slide-enter-from,
.slide-leave-to {
	@apply -translate-x-full opacity-0;
}
.slide-enter-active,
.slide-leave-active {
	transition: transform 300ms ease, opacity 300ms ease;
}
</style>
