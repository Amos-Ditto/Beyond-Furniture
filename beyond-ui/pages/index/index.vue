<template>
	<section class="w-full px-2 sm:px-4 md:px-12 lg:px-28 xl:px-40">
		<header class="flex flex-row justify-between w-full">
			<h3 class="text-3xl font-bold text-gray-800 uppercase">Products</h3>
			<div class="categories grid grid-cols-3 gap-x-3 w-[70%]">
				<div class="link flex items-center justify-start">
					<button class="text-lg tracking-wide text-gray-700">Best selling</button>
				</div>
				<div class="link flex items-center justify-start">
					<button class="text-lg tracking-wide text-gray-700">Most popular</button>
				</div>
				<div class="link flex items-center justify-start">
					<button
						class="bg-orange-400 rounded flex flex-row gap-x-2 text-slate-100 tracking-wide items-center justify-center px-4 py-1.5 hover:bg-orange-500 transition-colors duration-200"
					>
						See all
						<div class="i-mdi-arrow-right text-lg"></div>
					</button>
				</div>
			</div>
		</header>
	</section>
</template>
