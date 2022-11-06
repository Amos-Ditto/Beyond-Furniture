<script setup lang="ts"></script>

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
				class="search-bar relative hidden sm:grid grid-cols-10 items-center w-[20rem] md:w-[25rem] bg-gray-100 rounded border border-gray-200 hover:border-gray-300 focus-within:border-gray-300 transition duration-200"
			>
				<label for="find" class="icon flex items-center justify-center col-span-1 border-r border-gray-200">
					<div class="i-mdi-magnify text-lg text-slate-500"></div>
				</label>
				<input type="search" name="find" id="find" placeholder="Search for items" />
				<div class="search-options col-span-3 flex flex-row items-center border-l border-gray-200 px-1">
					<button
						class="relative flex items-center justify-start py-1.5 px-1 w-full rounded border border-transparent hover:border-gray-200"
					>
						<small class="tracking-wide text-xs pr-3.5 truncate capitalize font-light text-slate-600">All categories</small>
						<div class="i-mdi-chevron-down text-base text-slate-600 absolute right-1"></div>
					</button>
				</div>
			</div>
			<div class="right-navbar flex items-center justify-end gap-x-4 sm:gap-x-3 md:gap-x-8 lg:gap-x-12">
				<div class="notification flex flex-row gap-x-4 md:gap-x-6 items-center">
					<div class="cart relative rounded-full items-center flex justify-center hover:bg-gray-100 cursor-pointer p-2">
						<div class="i-mdi-cart-outline text-xl"></div>
						<div class="new absolute rounded-full w-2 h-2 bg-orange-500 right-2 top-2"></div>
					</div>
					<div
						class="push-notification relative items-center flex justify-center hover:bg-gray-100 cursor-pointer p-2 rounded-full"
					>
						<div class="i-mdi-bell-outline text-xl"></div>
						<div class="new absolute rounded-full w-2 h-2 bg-orange-500 right-2 top-2"></div>
					</div>
				</div>
				<div class="user">
					<div class="icon cursor-pointer">
						<img src="@/assets/Img/profile-min.svg" alt="avatar" class="w-9 h-9 bg-orange-200 rounded-full" />
					</div>
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
</style>
