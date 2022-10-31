<template>
	<section class="w-full px-2 sm:px-4 md:px-12 lg:px-28 xl:px-52 flex flex-col gap-y-3">
		<header class="flex flex-row justify-between w-full">
			<h3 class="text-3xl font-bold text-gray-800 uppercase">Products</h3>
			<div class="categories grid grid-cols-3 gap-x-3 w-[70%]">
				<div class="link flex items-center justify-center">
					<button class="text-lg tracking-wide text-gray-700">Best selling</button>
				</div>
				<div class="link flex items-center justify-center">
					<button class="text-lg tracking-wide text-gray-700">Most popular</button>
				</div>
				<div class="link flex items-center justify-end">
					<button
						class="bg-orange-400 rounded flex flex-row gap-x-2 text-slate-100 tracking-wide items-center justify-center px-4 py-1.5 hover:bg-orange-500 transition-colors duration-200"
					>
						See all
						<div class="i-mdi-arrow-right text-lg transition-transform duration-200"></div>
					</button>
				</div>
			</div>
		</header>
		<section class="w-full flex flex-col py-2 gap-y-6">
			<div class="sub-links w-full flex gap-x-8 sm:gap-x-12 justify-center items-center pt-10">
				<button class="capitalize text-base border-b-2 border-orange-400 px-3 py-1 tracking-wide">All</button>
				<button class="sub-link">Sofa</button>
				<button class="sub-link">Chair</button>
				<button class="sub-link">Bed</button>
				<button class="sub-link">Light</button>
			</div>
			<div class="list-items-data grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8 lg:gap-12 py-2">
				<CardsHomeItemCard :bg="'bg-cyan-100'" />
				<CardsHomeItemCard :bg="'bg-amber-100'" />
				<CardsHomeItemCard :bg="'bg-indigo-100'" />
				<CardsHomeItemCard :bg="'bg-amber-100'" />
				<CardsHomeItemCard :bg="'bg-indigo-100'" />
				<CardsHomeItemCard :bg="'bg-cyan-100'" />
			</div>
		</section>
		<section class="w-full flex flex-col pt-8">
			<ServicesDescription />
		</section>
	</section>
</template>

<style scoped>
.sub-links button.sub-link {
	@apply capitalize text-base border-b-2 border-transparent px-3 py-1 text-gray-600 tracking-wide hover:border-orange-400 hover:text-inherit transition-colors duration-200;
}

.categories .link button:hover .i-mdi-arrow-right {
	@apply translate-x-1;
}
</style>
