<script setup lang="ts">
const loadingitems = ref<boolean>(false);

const onCreatedLoadItems = (): void => {
	loadingitems.value = true;
	setTimeout(() => {
		loadingitems.value = false;
	}, 800);
};
onCreatedLoadItems();

const applyFilters = (): void => {
	onCreatedLoadItems();
};

// Toggle side Bar
const togglesidebar = ref<boolean>(false);
const toggleSidebar = (payload: boolean): void => {
	togglesidebar.value = payload;
};
</script>
<template>
	<NuxtLayout name="dashboard">
		<section class="w-full flex flex-col gap-y-3 pb-8">
			<header
				class="dashboard-status w-full h-[3.5rem] sm:h-[3.5rem] py-2 flex flex-row items-center justify-between bg-gray-200 px-2 sm:px-4 md:px-12 lg:px-24 xl:px-36 2xl:px-40 transition-all duration-200"
			>
				<div class="navigations flex flex-row items-center justify-start gap-x-3">
					<small>home</small>
					<small>></small>
					<small>categories</small>
				</div>
				<div class="menus flex flex-row items-center justify-center px-3 md:hidden">
					<div
						class="toggle-side-bar px-2 flex flex-row items-center justify-center py-0.5 cursor-pointer"
						@click="toggleSidebar(!togglesidebar)"
					>
						<Transition mode="out-in">
							<LazyUtilitiesMenuIcon :class="'w-8 h-8'" v-if="!togglesidebar" />
							<LazyUtilitiesMenuCloseIcon :class="'w-8 h-8'" v-else />
						</Transition>
					</div>
				</div>
			</header>
			<section class="px-2 sm:px-4 md:px-12 lg:px-24 xl:px-36 2xl:px-40 flex flex-col gap-y-6 transition-all duration-200">
				<main class="grid grid-cols-10 gap-x-5 lg:gap-x-10 py-3">
					<SidebarsDashboardAsideBar
						:togglesidebar="togglesidebar"
						@apply-filters="applyFilters"
						@toggle-sidebar="toggleSidebar"
					/>
					<section class="flex flex-col gap-y-2 col-span-10 md:col-span-8">
						<div class="flex flex-col w-full gap-y-10">
							<Transition mode="out-in">
								<div
									v-if="loadingitems"
									class="items-body grid grid-cols-2 sm:grid-cols-3 md:grid-cols-3 gap-x-2 sm:gap-x-4 gap-y-5 sm:gap-y-12 px-0.5 sm:px-0 py-4 sm:py-0"
								>
									<SuspensesDashboardItemSuspense />
									<SuspensesDashboardItemSuspense />
									<SuspensesDashboardItemSuspense />
									<SuspensesDashboardItemSuspense />
									<SuspensesDashboardItemSuspense />
									<SuspensesDashboardItemSuspense />
								</div>
								<div
									v-else
									class="items-body grid grid-cols-2 sm:grid-cols-3 md:grid-cols-3 gap-x-2 sm:gap-x-4 gap-y-5 sm:gap-y-12 px-0.5 sm:px-0 py-4 sm:py-0"
								>
									<CardsDashboardItem :bg="'bg-amber-100'" />
									<CardsDashboardItem :bg="'bg-indigo-100'" />
									<CardsDashboardItem :bg="'bg-cyan-100'" />
									<CardsDashboardItem :bg="'bg-indigo-100'" />
									<CardsDashboardItem :bg="'bg-amber-100'" />
									<CardsDashboardItem :bg="'bg-cyan-100'" />
									<CardsDashboardItem :bg="'bg-indigo-100'" />
								</div>
							</Transition>
						</div>
					</section>
				</main>
			</section>
		</section>
	</NuxtLayout>
</template>

<style scoped>
.dashboard-status small {
	@apply capitalize tracking-wide text-sm sm:text-base text-gray-600;
}
</style>
