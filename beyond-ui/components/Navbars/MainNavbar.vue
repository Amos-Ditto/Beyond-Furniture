<script setup lang="ts"></script>

<template>
	<nav id="nav" class="w-full py-4 px-2 sm:px-[8px] md:[20px] lg:px-[78px] xl:px-[90px] grid grid-cols-8 bg-gray-50 opacity-90">
		<div class="logo col-span-2">
			<img src="@/assets/Img/Logo/BEYOND-removebg-preview-light.png" alt="logo" />
		</div>
		<div class="navbar-dashboard col-span-6 flex items-center justify-end gap-x-16">
			<div class="search-bar relative flex items-center w-[20rem]">
				<div class="i-mdi-magnify text-lg left-1.5 absolute text-slate-500"></div>
				<input type="text" name="find" id="find" placeholder="Search for items" />
				<div class="search-options w-[5rem] bg-gray-50 rounded-md flex flex-row items-center absolute right-1 px-1">
					<button class="relative flex items-center justify-start py-1 px-2 w-full">
						<small class="tracking-wide text-base capitalize font-light text-slate-600">by</small>
						<div class="i-mdi-chevron-down text-base text-slate-600 absolute right-0"></div>
					</button>
				</div>
			</div>
			<div class="right-navbar flex items-center justify-end gap-x-12">
				<div class="notification flex flex-row gap-x-8 items-center">
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
					<div class="icon">
						<img src="@/assets/Img/profile-min.svg" alt="avatar" class="w-9 h-9 bg-orange-300 rounded-full" />
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
	@apply w-[8rem];
}

.search-bar input {
	@apply py-2 pl-7 pr-24 bg-gray-100 rounded-md w-full text-base tracking-wide outline-none border border-gray-200 focus:border-gray-300 transition-colors duration-200;
}
</style>
