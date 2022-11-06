<script setup lang="ts">
import { OverviewItems } from "@/Types/common";

const router = useRouter();

const overviewitems = ref<OverviewItems[]>([
	{ Name: "all", id: 0 },
	{ Name: "Sofas", id: 1 },
	{ Name: "Chairs", id: 2 },
	{ Name: "Beds", id: 3 },
	{ Name: "Light", id: 4 },
]);
const activeitemid = ref<number>(0);

const selectOverviewItem = (item: OverviewItems): void => {
	activeitemid.value = item.id;
};
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
				<div class="sub-links w-full flex gap-x-3 sm:gap-x-12 justify-start sm:justify-center items-center px-3 pt-6 sm:pt-10">
					<button
						class="sub-link"
						:class="activeitemid === item.id ? 'border-orange-400 text-inherit' : 'border-transparent text-gray-600'"
						v-for="item in overviewitems"
						:key="item.id"
						@click="selectOverviewItem(item)"
					>
						{{ item.Name }}
					</button>
				</div>
				<div class="hero-items w-full flex flex-col">
					<HeroesHomeOverviewItems />
				</div>
			</section>
			<section class="w-full flex flex-col pt-8 pb-12">
				<ServicesDescription />
			</section>
		</section>
	</NuxtLayout>
</template>

<style scoped>
.sub-links .sub-link {
	@apply capitalize text-base border-b-2 px-2.5 sm:px-3 py-1 tracking-wide hover:border-orange-400 hover:text-inherit transition-colors duration-200;
}

.categories .link button:hover .i-mdi-arrow-right {
	@apply translate-x-1;
}
</style>
