<script setup lang="ts"></script>
<template>
	<main class="fixed top-0 bottom-0 left-0 right-0 bg-gray-50 flex flex-col overflow-x-hidden">
		<NuxtLoadingIndicator
			color="repeating-linear-gradient(to right,rgb(253 186 116 / 1) 0%,rgb(249 115 22 / 1) 50%,rgb(251 146 60 /1) 100%)"
			class="bg-orange-300"
		/>
		<NuxtPage />
	</main>
</template>

<style>
:root {
	--tw-bg-opacity: 1;
}

html {
	font-family: "Roboto", "Arial", Tahoma;
	font-synthesis: none;
	text-rendering: optimizeLegibility;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	-webkit-text-size-adjust: 100%;
	-webkit-touch-callout: none;
	-webkit-tap-highlight-color: transparent;
}

body {
	@apply box-border;
}

/* Page transition */

.page-enter-active,
.page-leave-active {
	transition: all 0.3s;
}
.page-enter-from {
	@apply opacity-0 -translate-y-0.5 overflow-y-hidden;
}
.page-leave-to {
	@apply opacity-0;
}
</style>
