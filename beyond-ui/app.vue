<script setup lang="ts"></script>
<template>
	<main class="fixed top-0 bottom-0 left-0 right-0 bg-gray-50 flex flex-col">
		<NuxtPage />
	</main>
</template>

<style>
:root {
	--tw-bg-opacity: 1;
}

html {
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
</style>
