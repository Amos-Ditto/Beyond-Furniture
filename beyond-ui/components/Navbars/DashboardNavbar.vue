<template>
	<nav
		class="w-full py-4 px-2 sm:px-4 md:px-12 lg:px-24 xl:px-36 2xl:px-40 grid grid-cols-2 gap-x-4 bg-gray-50 opacity-[0.95] transition-all duration-200 z-40"
	>
		<div class="left-nav flex flex-row items-center justify-between">
			<RouterLink to="/" class="logo">
				<img src="@/assets/Img/Logo/BEYOND-removebg-preview-light.png" alt="logo" />
			</RouterLink>
			<div class="search-bar grid grid-cols-10 border border-gray-200 rounded bg-gray-100 py-1">
				<label for="find" class="icon col-span-1 flex items-center justify-center border-r border-gray-200 bg-gray-100">
					<div class="i-mdi-magnify text-gray-500 text-lg scale-110"></div>
				</label>
				<input type="search" name="find" id="find" placeholder="search for items" />
				<div class="search-options col-span-3 flex flex-row items-center border-l border-gray-200 px-1 bg-inherit">
					<button
						class="relative flex items-center justify-start py-1.5 px-1 w-full rounded border border-transparent hover:border-gray-200"
					>
						<small class="tracking-wide text-xs pr-3.5 truncate capitalize font-light text-slate-600">All categories</small>
						<div class="i-mdi-chevron-down text-base text-slate-600 absolute right-1"></div>
					</button>
				</div>
			</div>
		</div>
		<div class="right-nav"></div>
	</nav>
</template>
<style scoped>
nav {
	box-shadow: 0 1px 8px 0 rgb(0 0 0 / 6%), 0 1px 0 0 rgb(0 0 0 / 4%);
}
.logo img {
	@apply w-[7rem] sm:w-[9rem];
}

.search-bar input {
	@apply outline-none col-span-6 px-2 py-1.5 bg-gray-100 text-gray-700 tracking-wide;
}
</style>
