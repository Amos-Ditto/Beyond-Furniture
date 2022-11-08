<template>
	<NuxtLayout name="dashboard">
		<section class="w-full flex flex-col gap-y-3 pb-8">
			<header
				class="dashboard-status w-full h-[3.5rem] sm:h-[3.5rem] py-2 flex flex-row items-center justify-start gap-x-3 bg-gray-200 px-2 sm:px-4 md:px-12 lg:px-24 xl:px-36 2xl:px-40 transition-all duration-200"
			>
				<small>home</small>
				<small>></small>
				<small>categories</small>
			</header>
			<section class="px-2 sm:px-4 md:px-12 lg:px-24 xl:px-36 2xl:px-40 flex flex-col gap-y-6 transition-all duration-200">
				<main class="grid grid-cols-10 gap-x-5 lg:gap-x-10 py-3">
					<SidebarsDashboardAsideBar />
					<section class="flex flex-col gap-y-2 col-span-10 md:col-span-8">
						<div
							class="items-body grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-x-4 gap-y-12 px-4 sm:px-0 py-4 sm:py-0"
						>
							<CardsDashboardItem :bg="'bg-amber-100'" />
							<CardsDashboardItem :bg="'bg-indigo-100'" />
							<CardsDashboardItem :bg="'bg-cyan-100'" />
							<CardsDashboardItem :bg="'bg-indigo-100'" />
							<CardsDashboardItem :bg="'bg-amber-100'" />
							<CardsDashboardItem :bg="'bg-cyan-100'" />
							<CardsDashboardItem :bg="'bg-indigo-100'" />
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
