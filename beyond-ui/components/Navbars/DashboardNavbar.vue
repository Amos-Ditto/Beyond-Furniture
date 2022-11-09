<script setup lang="ts">
import { useSearchStore } from "@/store/searchStore";
import { Categories } from "~~/Types/common";

const searchstore = useSearchStore();

const categories = ref<Categories[]>([
	{ Name: "all categories", id: 6 },
	{ Name: "Living Room", id: 1 },
	{ Name: "Bed Room", id: 2 },
	{ Name: "kitchen Dining", id: 3 },
	{ Name: "Office Furniture", id: 4 },
	{ Name: "others", id: 5 },
]);

if (searchstore.categories.length === 0) {
	searchstore.updateCategories(categories.value);
}

const selectedcategory = ref<Categories>({ Name: "all categories", id: 6 });
const searchdata = ref<string>("");
// Check if already there is placed search value

if (searchstore.selectedcategory.id !== 0) {
	selectedcategory.value = searchstore.selectedcategory;
	searchdata.value = searchstore.searchdata;
}

const togglecategories = ref<boolean>(false);

const chooseCategory = (payload: Categories): void => {
	selectedcategory.value = payload;
	togglecategories.value = !togglecategories.value;
};

// Handle Account Details
const toggleaccount = ref<boolean>(false);

// Handle Cart
const togglecart = ref<boolean>(false);

const toggleAccount = (): void => {
	togglecart.value = false;
	toggleaccount.value = !toggleaccount.value;
};
const toggleCart = (): void => {
	toggleaccount.value = false;
	togglecart.value = !togglecart.value;
};
</script>
<template>
	<nav
		class="w-full py-4 px-2 sm:px-4 md:px-12 lg:px-24 xl:px-36 2xl:px-40 grid grid-cols-3 xl:grid-cols-2 gap-x-4 bg-gray-50 opacity-[0.95] transition-all duration-200 z-40"
	>
		<div class="left-nav flex flex-row items-center sm:justify-between gap-x-4 col-span-1 sm:col-span-2 xl:col-span-1">
			<!-- <div class="toggle-side-bar px-2 flex flex-row items-center justify-center py-0.5">
				<LazyUtilitiesMenuIcon :class="'w-8 h-8 scale-110'" />
			</div> -->
			<RouterLink to="/" class="logo">
				<img src="@/assets/Img/Logo/BEYOND-removebg-preview-light.png" alt="logo" />
			</RouterLink>
			<div
				class="search-bar relative hidden sm:grid grid-cols-8 lg:grid-cols-10 grid-rows-1 border border-gray-200 rounded bg-gray-100 py-1 hover:border-gray-300 hover:shadow focus-within:shadow focus-within:border-gray-300 transition duration-200"
			>
				<label for="find" class="icon col-span-1 flex items-center justify-center border-r border-gray-200 bg-gray-100">
					<!-- <div class="i-mdi-magnify text-gray-500 text-lg scale-110"></div> -->
					<UtilitiesSearchIcon :class="'w-4 h-4 scale-110'" />
				</label>
				<input type="search" name="find" id="find" placeholder="search for items" v-model="searchdata" />
				<div class="search-options col-span-2 lg:col-span-3 flex flex-row items-center border-l border-gray-200 px-1 bg-inherit">
					<button
						@click="togglecategories = !togglecategories"
						class="relative flex items-center justify-start py-1.5 px-1 w-full rounded border border-transparent hover:border-gray-200"
					>
						<small class="tracking-wide text-xs pr-3.5 truncate capitalize font-light text-slate-600">{{
							selectedcategory.Name
						}}</small>
						<div
							class="i-mdi-chevron-down text-base text-slate-600 absolute right-1 transition duration-200"
							:class="togglecategories ? 'rotate-180' : 'rotate-0'"
						></div>
					</button>
				</div>
				<NavbarsDashboardSearchDropDown
					:categories="categories"
					:togglecategories="togglecategories"
					@choose-category="chooseCategory"
				/>
			</div>
		</div>
		<div class="right-nav flex flex-row items-center justify-end gap-x-6 sm:gap-x-8 col-span-2 sm:col-span-1">
			<div
				class="search-mobile flex sm:hidden items-center justify-center p-2 bg-gray-100 hover:bg-gray-200 transition duration-200 cursor-pointer rounded-full"
			>
				<UtilitiesSearchIcon :class="'w-4 h-4 scale-110'" />
			</div>
			<div class="cart relative items-center flex justify-center">
				<div
					class="cart-icon relative rounded-full items-center flex justify-center hover:bg-gray-100 cursor-pointer p-2"
					@click="toggleCart"
				>
					<div class="i-mdi-cart-outline text-2xl scale-110 text-gray-700"></div>
					<div class="new absolute rounded-full w-2.5 h-2.5 bg-orange-500 right-2 top-2"></div>
				</div>
				<Transition name="drop-down">
					<NavbarsCartDropDown v-if="togglecart" />
				</Transition>
				<div
					v-if="togglecart"
					@click="togglecart = false"
					class="cart-toggling-container fixed top-20 left-0 right-0 bottom-0 bg-transparent"
				></div>
			</div>
			<!-- <div class="push-notification relative items-center flex justify-center hover:bg-gray-100 cursor-pointer p-2 rounded-full">
				<div class="i-mdi-bell-outline text-xl"></div>
				<div class="new absolute rounded-full w-2 h-2 bg-orange-500 right-2 top-2"></div>
			</div> -->
			<div class="user relative">
				<div class="icon cursor-pointer" @click="toggleAccount">
					<img src="@/assets/Img/profile-min.svg" alt="avatar" class="w-9 h-9 bg-orange-200 rounded-full" />
				</div>
				<Transition name="drop-down">
					<NavbarsAccountDropDown :toggleaccount="toggleaccount" />
				</Transition>
				<div
					v-if="toggleaccount"
					@click="toggleaccount = false"
					class="cart-toggling-container fixed top-20 left-0 right-0 bottom-0 bg-transparent"
				></div>
			</div>
		</div>
	</nav>
</template>
<style scoped>
nav {
	box-shadow: 0 1px 8px 0 rgb(0 0 0 / 6%), 0 1px 0 0 rgb(0 0 0 / 4%);
}
.logo img {
	@apply w-[8rem] sm:w-[9rem];
}

.search-bar input {
	@apply outline-none col-span-5 lg:col-span-6 px-2 py-1 md:py-1 bg-gray-100 text-gray-700 tracking-wide;
}
.search-mobile:hover .i-mdi-magnify {
	@apply scale-110;
}

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
