<template>
	<div
		class="item flex flex-col rounded-md px-2 py-3 gap-y-2 sm:gap-y-6 h-[18rem] sm:h-[22rem] w-auto transition-all duration-500 relative bg-gray-100"
	>
		<div class="item-image w-full p-3 h-[75%] sm:h-[60%] flex items-center justify-center">
			<div class="h-full w-full bg-gray-200 animate-pulse"></div>
		</div>
		<div class="item-body flex flex-col items-center w-full gap-y-2">
			<div class="item-details flex flex-col items-center justify-center gap-y-2.5 py-3 px-3 sm:px-0 w-full">
				<button class="animate-pulse bg-gray-200 h-3 w-[60%] py-4"></button>
				<button class="animate-pulse bg-gray-200 h-3 py-4 w-[40%]"></button>
				<button class="animate-pulse bg-gray-200 h-4 py-4 w-full"></button>
			</div>
		</div>
		<div class="add-cart hidden sm:block absolute bottom-0 translate-y-1/2 -translate-x-1/2 left-1/2">
			<button class="p-3 sm:p-2 rounded-full shadow-md bg-gray-200 animate-pulse">
				<div class="i-mdi-plus text-gray-300 text-xl scale-125 sm:scale-110"></div>
			</button>
		</div>
	</div>
</template>
