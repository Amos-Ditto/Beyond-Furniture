<script setup lang="ts">
const router = useRouter();

console.log(router.currentRoute.value);
</script>
<template>
	<NuxtLayout>
		<section class="w-full px-2 sm:px-4 md:px-12 lg:px-28 xl:px-52 flex flex-col gap-y-3 transition-all duration-200">
			<header class="flex flex-row justify-between w-full px-4 sm:px-0 pt-8">
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
			<section class="w-full flex flex-col py-2 gap-y-10 sm:gap-y-6">
				<div class="sub-links w-full flex gap-x-3 sm:gap-x-12 justify-center items-center px-3 pt-6 sm:pt-10">
					<RouterLink to="/" class="capitalize text-base border-b-2 px-2.5 sm:px-3 py-1 border-orange-400 text-inherit" exact
						>All</RouterLink
					>
					<RouterLink to="/sofas" class="sub-link">Sofas</RouterLink>
					<RouterLink to="/sofas" class="sub-link">Chairs</RouterLink>
					<RouterLink to="/sofas" class="sub-link">Beds</RouterLink>
					<RouterLink to="/sofas" class="sub-link">Light</RouterLink>
				</div>
				<NuxtPage />
			</section>
			<section class="w-full flex flex-col pt-8 pb-12">
				<ServicesDescription />
			</section>
		</section>
	</NuxtLayout>
</template>

<style scoped>
.sub-links .sub-link {
	@apply capitalize text-base border-b-2 border-transparent px-2.5 sm:px-3 py-1 text-gray-600 tracking-wide hover:border-orange-400 hover:text-inherit transition-colors duration-200;
}

.categories .link button:hover .i-mdi-arrow-right {
	@apply translate-x-1;
}

.nuxt-link-exact-active {
	@apply border-orange-400 text-inherit border-t;
}
</style>
