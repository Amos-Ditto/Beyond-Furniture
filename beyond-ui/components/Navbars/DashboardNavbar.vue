<template>
	<nav
		class="w-full py-4 px-2 sm:px-4 md:px-12 lg:px-24 xl:px-36 2xl:px-40 grid grid-cols-3 xl:grid-cols-2 gap-x-4 bg-gray-50 opacity-[0.95] transition-all duration-200 z-40"
	>
		<div class="left-nav flex flex-row items-center sm:justify-between gap-x-4 col-span-1 sm:col-span-2 xl:col-span-1">
			<RouterLink to="/" class="logo">
				<img src="@/assets/Img/Logo/BEYOND-removebg-preview-light.png" alt="logo" />
			</RouterLink>
			<div
				class="search-bar hidden sm:grid grid-cols-8 lg:grid-cols-10 grid-rows-1 border border-gray-200 rounded bg-gray-100 py-1 hover:border-gray-300 hover:shadow focus-within:shadow focus-within:border-gray-300 transition duration-200"
			>
				<label for="find" class="icon col-span-1 flex items-center justify-center border-r border-gray-200 bg-gray-100">
					<!-- <div class="i-mdi-magnify text-gray-500 text-lg scale-110"></div> -->
					<UtilitiesSearchIcon :class="'w-4 h-4 scale-110'" />
				</label>
				<input type="search" name="find" id="find" placeholder="search for items" />
				<div
					class="search-options col-span-2 lg:col-span-3 flex flex-row items-center border-l border-gray-200 px-1 bg-inherit"
				>
					<button
						class="relative flex items-center justify-start py-1.5 px-1 w-full rounded border border-transparent hover:border-gray-200"
					>
						<small class="tracking-wide text-xs pr-3.5 truncate capitalize font-light text-slate-600"
							>All categories</small
						>
						<div class="i-mdi-chevron-down text-base text-slate-600 absolute right-1"></div>
					</button>
				</div>
			</div>
		</div>
		<div class="right-nav flex flex-row items-center justify-end gap-x-4 sm:gap-x-6 col-span-2 sm:col-span-1">
			<div
				class="search-mobile flex sm:hidden items-center justify-center p-2 bg-gray-100 hover:bg-gray-200 transition duration-200 cursor-pointer rounded-full"
			>
				<UtilitiesSearchIcon :class="'w-4 h-4 scale-110'" />
			</div>
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
			<div class="user">
				<div class="icon cursor-pointer">
					<img src="@/assets/Img/profile-min.svg" alt="avatar" class="w-9 h-9 bg-orange-200 rounded-full" />
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
	@apply w-[8rem] sm:w-[9rem];
}

.search-bar input {
	@apply outline-none col-span-5 lg:col-span-6 px-2 py-1 md:py-1 bg-gray-100 text-gray-700 tracking-wide;
}
.search-mobile:hover .i-mdi-magnify {
	@apply scale-110;
}
</style>
