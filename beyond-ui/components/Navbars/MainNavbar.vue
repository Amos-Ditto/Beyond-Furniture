<script setup lang="ts">
import { Categories } from "~~/Types/common";

const categories = ref<Categories[]>([
	{ Name: "all categories", id: 6 },
	{ Name: "Living Room", id: 1 },
	{ Name: "Bed Room", id: 2 },
	{ Name: "kitchen Dining", id: 3 },
	{ Name: "Office Furniture", id: 4 },
	{ Name: "others", id: 5 },
]);
const selectedcategory = ref<Categories>({ Name: "all categories", id: 6 });
const togglecategories = ref<boolean>(false);

const chooseCategory = (payload: Categories): void => {
	selectedcategory.value = payload;
	togglecategories.value = !togglecategories.value;
};

// Handle Account Details
const toggleaccount = ref<boolean>(false);

// Handle Cart
const togglecart = ref<boolean>(false);
</script>

<template>
	<nav
		id="nav"
		class="w-full py-4 px-4 sm:px-[8px] md:[18px] lg:px-[78px] xl:px-[90px] grid grid-cols-8 bg-gray-50 opacity-[0.95] transition-all duration-200 z-40"
	>
		<RouterLink to="/" class="logo col-span-2">
			<img src="@/assets/Img/Logo/BEYOND-removebg-preview-light.png" alt="logo" />
		</RouterLink>
		<div class="navbar-dashboard col-span-6 flex items-center justify-end gap-x-4 md:gap-x-12 lg:gap-x-16 transition duration-200">
			<div
				class="search-bar relative hidden sm:grid grid-cols-10 items-center w-[20rem] md:w-[25rem] bg-gray-100 rounded border border-gray-200 hover:border-gray-300 focus-within:border-gray-300 hover:shadow focus-within:shadow transition duration-200"
			>
				<label for="find" class="icon flex items-center justify-center col-span-1 border-r border-gray-200">
					<!-- <div class="i-mdi-magnify text-lg text-slate-500"></div> -->
					<UtilitiesSearchIcon :class="'w-4 h-4 scale-110'" />
				</label>
				<input type="search" name="find" id="find" placeholder="Search for items" />
				<div class="search-options col-span-3 flex flex-row items-center border-l border-gray-200 px-1">
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
				<Transition name="drop-down">
					<div
						v-if="togglecategories"
						class="search-drop-down absolute bottom-0 shadow-xl translate-y-[105%] right-0 min-w-[10rem] bg-gray-50 rounded flex flex-col py-2 gap-y-2"
					>
						<button
							v-for="category in categories"
							:key="category.id"
							@click="chooseCategory(category)"
							class="py-2 px-3 tracking-wide hover:bg-gray-200 focus:bg-gray-200 text-sm capitalize flex justify-start items-center"
						>
							{{ category.Name }}
						</button>
					</div>
				</Transition>
			</div>
			<div class="right-navbar flex items-center justify-end gap-x-8 sm:gap-x-3 md:gap-x-8 lg:gap-x-12">
				<div class="notification relative sm:px-3 flex flex-row gap-x-4 md:gap-x-6 items-center">
					<div class="cart md:relative items-center flex justify-center">
						<div
							class="cart-icon relative rounded-full items-center flex justify-center hover:bg-gray-100 cursor-pointer p-2"
							@click="togglecart = !togglecart"
						>
							<div class="i-mdi-cart-outline text-2xl scale-110 text-gray-700"></div>
							<div class="new absolute rounded-full w-2.5 h-2.5 bg-orange-500 right-2 top-2"></div>
						</div>
						<Transition name="drop-down">
							<NavbarsCartDropDown v-if="togglecart" />
						</Transition>
					</div>
				</div>
				<div class="user relative">
					<div class="icon cursor-pointer" @click="toggleaccount = !toggleaccount">
						<img src="@/assets/Img/profile-min.svg" alt="avatar" class="w-9 h-9 bg-orange-200 rounded-full" />
					</div>
					<Transition name="drop-down">
						<NavbarsAccountDropDown :toggleaccount="toggleaccount" />
					</Transition>
				</div>
			</div>
		</div>
	</nav>
</template>

<style scoped>
nav {
	box-shadow: 0 1px 8px 0 rgb(0 0 0 / 6%), 0 1px 0 0 rgb(0 0 0 / 4%);
}

.logo img {
	@apply w-[7rem] sm:w-[8rem];
}

.search-bar input {
	@apply py-2 px-2 bg-gray-100 rounded-md col-span-6 text-base text-gray-600 tracking-wide outline-none;
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
