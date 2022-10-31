<template>
	<section class="w-full px-2 sm:px-4 md:px-12 lg:px-28 xl:px-52 flex flex-col gap-y-3 transition-all duration-200">
		<header class="flex flex-row justify-between w-full px-4 sm:px-0">
			<h3 class="text-3xl font-bold text-gray-800 uppercase">Products</h3>
			<div class="categories hidden sm:grid grid-cols-3 gap-x-3 w-[70%]">
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
			<div class="sub-links w-full flex gap-x-3 sm:gap-x-12 justify-center items-center px-3 pt-6 sm:pt-10">
				<button class="capitalize text-base border-b-2 border-orange-400 px-3 py-1 tracking-wide">All</button>
				<button class="sub-link">Sofas</button>
				<button class="sub-link">Chairs</button>
				<button class="sub-link">Beds</button>
				<button class="sub-link">Light</button>
			</div>
			<div class="list-items-data grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8 lg:gap-14 py-2 px-4 sm:px-0">
				<CardsHomeItemCard :bg="'bg-amber-100'">
					<template #img>
						<img
							src="@/assets/Furnitures/phillip-goldsberry-fZuleEfeA1Q-unsplash-removebg-preview.png"
							alt="chair"
							class="list-img"
						/>
					</template>
					<template #details class="grid grid-cols-2 py-4">
						<div class="name text-start">
							<small class="text-start font-semibold text-base tracking-wide capitalize text-gray-600">Living couch</small>
						</div>
					</template>
				</CardsHomeItemCard>
				<CardsHomeItemCard :bg="'bg-cyan-100'">
					<template #img>
						<img
							src="@/assets/Furnitures/marlon-corona-1tMc27CFUbA-unsplash-removebg-preview.png"
							alt="chair"
							class="list-img"
						/>
					</template>
				</CardsHomeItemCard>
				<CardsHomeItemCard :bg="'bg-indigo-100'">
					<template #img>
						<img
							src="@/assets/Furnitures/nathan-fertig-FBXuXp57eM0-unsplash-removebg-preview.png"
							alt="chair"
							class="list-img"
						/>
					</template>
				</CardsHomeItemCard>
				<CardsHomeItemCard :bg="'bg-cyan-100'">
					<template #img>
						<img src="@/assets/Furnitures/kari-shea-ItMggD0EguY-unsplash-removebg-preview.png" alt="chair" class="list-img" />
					</template>
				</CardsHomeItemCard>
				<CardsHomeItemCard :bg="'bg-indigo-100'">
					<template #img>
						<img
							src="@/assets/Furnitures/daniil-silantev-1P6AnKDw6S8-unsplash-removebg-preview.png"
							alt="chair"
							class="list-img"
						/>
					</template>
				</CardsHomeItemCard>
				<CardsHomeItemCard :bg="'bg-amber-100'">
					<template #img>
						<img src="@/assets/Furnitures/erik-mclean-Ij9nIghkI6k-unsplash-removebg-preview.png" alt="chair" class="list-img" />
					</template>
				</CardsHomeItemCard>
			</div>
		</section>
		<section class="w-full flex flex-col pt-8 pb-12">
			<ServicesDescription />
		</section>
	</section>
</template>

<style scoped>
.sub-links button.sub-link {
	@apply capitalize text-base border-b-2 border-transparent px-2.5 sm:px-3 py-1 text-gray-600 tracking-wide hover:border-orange-400 hover:text-inherit transition-colors duration-200;
}

.categories .link button:hover .i-mdi-arrow-right {
	@apply translate-x-1;
}

.list-items-data img.list-img {
	@apply object-contain h-full w-full bg-inherit;
}
</style>
