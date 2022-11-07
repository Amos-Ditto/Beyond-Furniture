<template>
	<NuxtLayout name="dashboard">
		<section class="w-full flex flex-col gap-y-3">
			<header
				class="dashboard-status w-full h-[3rem] sm:h-[3.5rem] py-2 flex flex-row items-center justify-start gap-x-3 bg-gray-200 px-2 sm:px-4 md:px-12 lg:px-24 xl:px-36 2xl:px-40 transition-all duration-200"
			>
				<small>home</small>
				<small>></small>
				<small>categories</small>
			</header>
			<section class="px-2 sm:px-4 md:px-12 lg:px-24 xl:px-36 2xl:px-40 flex flex-col gap-y-6 transition-all duration-200">
				<h3>dashboard</h3>
				Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat eaque pariatur, cumque vero ipsam eveniet beatae doloremque
				natus optio! Voluptatum doloremque totam quibusdam omnis, dolores dolor debitis nemo quasi magnam.
			</section>
		</section>
	</NuxtLayout>
</template>

<style scoped>
.dashboard-status small {
	@apply capitalize tracking-wide text-sm sm:text-base text-gray-600;
}
</style>
