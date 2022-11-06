<template>
	<nav
		class="w-full py-4 px-4 sm:px-[8px] md:[18px] lg:px-[78px] xl:px-[90px] grid grid-cols-2 gap-x-4 bg-gray-50 opacity-[0.95] transition-all duration-200 z-40"
	>
		<div class="left-nav">
			<div class="logo">
				<img src="@/assets/Img/Logo/BEYOND-removebg-preview-light.png" alt="logo" />
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
	@apply w-[7rem] sm:w-[8rem];
}
</style>
