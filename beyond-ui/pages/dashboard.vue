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
				<main class="grid grid-cols-8 gap-x-4 py-2">
					<aside class="col-span-2 flex flex-col gap-y-6 py-2 rounded">
						<div class="categories flex flex-col gap-y-2">
							<h3 class="text-lg tracking-wide font-semibold capitalize px-2">categories</h3>
							<label for="living">
								<input type="checkbox" name="living" id="living" />
								<small>Living Room</small>
							</label>
							<label for="kitchen">
								<input type="checkbox" name="kitchen" id="kitchen" />
								<small>Bed Room</small>
							</label>
							<label for="bedroom">
								<input type="checkbox" name="bedroom" id="bedroom" />
								<small>kitchen</small>
							</label>
						</div>
						<div class="filters flex flex-col gap-y-2 w-full">
							<h3 class="text-lg tracking-wide font-semibold capitalize px-2">filters</h3>
							<div class="colors py-2">
								<h3 class="text-sm font-semibold uppercase px-2">colors</h3>
							</div>
						</div>
					</aside>
					<section class="flex flex-col gap-y-2 col-span-6"></section>
				</main>
			</section>
		</section>
	</NuxtLayout>
</template>

<style scoped>
.dashboard-status small {
	@apply capitalize tracking-wide text-sm sm:text-base text-gray-600;
}

aside {
	box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 8px;
}
.categories label {
	@apply w-full px-2 py-2 flex flex-row items-center gap-x-4 hover:bg-gray-200 transition duration-200 cursor-pointer selection:bg-gray-200 text-gray-700;
}
.categories label input[type="checkbox"] {
	@apply w-5 h-5 checked:bg-orange-300 indeterminate:bg-gray-300 outline-1 outline-gray-300 appearance-none border rounded border-gray-300;
	@apply flex items-center justify-center checked:after:content-['\2713'] checked:after:text-gray-50 checked:after:text-xl checked:border-transparent;
}
.categories label small {
	@apply text-base tracking-wide capitalize;
}
</style>
