<template>
	<div class="w-full flex flex-col gap-y-1.5">
		<div class="icon flex flex-row justify-start items-center">
			<slot name="icon"></slot>
		</div>
		<h3 class="title text-xl font-semibold tracking-wide text-start text-gray-800 capitalize">
			<slot name="title"></slot>
		</h3>
		<p class="line-clamp-3 leading-7 text-sm text-start text-gray-600">
			<slot name="about"></slot>
		</p>
	</div>
</template>
