<template>
	<div class="item flex flex-col rounded-md px-2 py-3 gap-y-4 h-[24rem] sm:h-[22rem] w-[15rem] sm:w-auto bg-gray-100">
		<div class="item-image w-full h-[75%] sm:h-[60%] flex items-center justify-center bg-gray-200 animate-pulse"></div>
		<div class="item-body flex flex-col items-center justify-center w-full gap-y-2">
			<div class="item-details flex flex-col items-center justify-center gap-y-2 py-3 w-full">
				<button class="animate-pulse bg-gray-200 h-3 w-[60%] py-4"></button>
				<button class="animate-pulse bg-gray-200 h-3 py-4 w-[40%]"></button>
			</div>
			<div class="add-cart w-full flex flex-col items-center">
				<button class="h-5 py-4 w-full bg-gray-200 animate-pulse"></button>
			</div>
		</div>
	</div>
</template>
