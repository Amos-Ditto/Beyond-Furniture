<template>
	<div
		class="list-items-data w-full grid grid-flow-col grid-rows-1 sm:grid-flow-row sm:grid-cols-2 md:grid-cols-3 gap-3 sm:gap-8 lg:gap-14 py-2 px-2 sm:px-0 overflow-x-auto sm:overflow-x-hidden"
	>
		<CardsHomeItemCard :bg="'bg-amber-100'">
			<template #img>
				<img
					loading="lazy"
					src="@/assets/Furnitures/phillip-goldsberry-fZuleEfeA1Q-unsplash-removebg-preview.png"
					alt="chair"
					class="list-img"
				/>
			</template>
			<template #name class="">
				<small class="text-center font-semibold text-xl tracking-wide whitespace-pre-line capitalize text-gray-600"
					>Living couch</small
				>
			</template>
			<template #prices>
				<div class="prices flex flex-row px-4 items-center justify-center gap-x-4 w-full">
					<small class="font-[800] text-lg italic tracking-wide text-gray-800">$30</small>
				</div>
			</template>
		</CardsHomeItemCard>
		<CardsHomeItemCard :bg="'bg-cyan-100'">
			<template #img>
				<img
					loading="lazy"
					src="@/assets/Furnitures/marlon-corona-1tMc27CFUbA-unsplash-removebg-preview.png"
					alt="chair"
					class="list-img"
				/>
			</template>
			<template #name class="">
				<small class="text-center font-semibold text-xl tracking-wide whitespace-pre-line capitalize text-gray-600"
					>Natuzi chair</small
				>
			</template>
			<template #prices>
				<div class="prices flex flex-row px-4 items-center justify-center gap-x-4 w-full">
					<small class="font-[800] text-lg italic tracking-wide text-gray-800">$30</small>
					<small class="font-[800] text-lg italic tracking-wide text-gray-500 line-through decoration-gray-500">$40</small>
				</div>
			</template>
		</CardsHomeItemCard>
		<CardsHomeItemCard :bg="'bg-indigo-100'">
			<template #img>
				<img
					loading="lazy"
					src="@/assets/Furnitures/nathan-fertig-FBXuXp57eM0-unsplash-removebg-preview.png"
					alt="chair"
					class="list-img"
				/>
			</template>
			<template #name class="">
				<small class="text-center font-semibold text-xl tracking-wide whitespace-pre-line capitalize text-gray-600"
					>3 seat sofa</small
				>
			</template>
			<template #prices>
				<div class="prices flex flex-row px-4 items-center justify-center gap-x-4 w-full">
					<small class="font-[800] text-lg italic tracking-wide text-gray-800">$50</small>
					<small class="font-[800] text-lg italic tracking-wide text-gray-500 line-through decoration-gray-500">$60</small>
				</div>
			</template>
		</CardsHomeItemCard>
		<CardsHomeItemCard :bg="'bg-cyan-100'">
			<template #img>
				<img
					src="@/assets/Furnitures/kari-shea-ItMggD0EguY-unsplash-removebg-preview.png"
					alt="chair"
					class="list-img"
					loading="lazy"
				/>
			</template>
			<template #name class="">
				<small class="text-center font-semibold text-xl tracking-wide whitespace-pre-line capitalize text-gray-600"
					>Wing chair</small
				>
			</template>
			<template #prices>
				<div class="prices flex flex-row px-4 items-center justify-center gap-x-4 w-full">
					<small class="font-[800] text-lg italic tracking-wide text-gray-800">$30</small>
					<small class="font-[800] text-lg italic tracking-wide text-gray-500 line-through decoration-gray-500">$40</small>
				</div>
			</template>
		</CardsHomeItemCard>
		<CardsHomeItemCard :bg="'bg-indigo-100'">
			<template #img>
				<img
					loading="lazy"
					src="@/assets/Furnitures/daniil-silantev-1P6AnKDw6S8-unsplash-removebg-preview.png"
					alt="chair"
					class="list-img"
				/>
			</template>
			<template #name class="">
				<small class="text-center font-semibold text-xl tracking-wide whitespace-pre-line capitalize text-gray-600"
					>couch relax</small
				>
			</template>
			<template #prices>
				<div class="prices flex flex-row px-4 items-center justify-center gap-x-4 w-full">
					<small class="font-[800] text-lg italic tracking-wide text-gray-800">$30</small>
					<small class="font-[800] text-lg italic tracking-wide text-gray-500 line-through decoration-gray-500">$40</small>
				</div>
			</template>
		</CardsHomeItemCard>
		<CardsHomeItemCard :bg="'bg-amber-100'">
			<template #img>
				<img
					src="@/assets/Furnitures/erik-mclean-Ij9nIghkI6k-unsplash-removebg-preview.png"
					alt="chair"
					class="list-img"
					loading="lazy"
				/>
			</template>
			<template #name class="">
				<small class="text-center font-semibold text-xl tracking-wide whitespace-pre-line capitalize text-gray-600">xl bed</small>
			</template>
			<template #prices>
				<div class="prices flex flex-row px-4 items-center justify-center gap-x-4 w-full">
					<small class="font-[800] text-lg italic tracking-wide text-gray-800">$70</small>
					<small class="font-[800] text-lg italic tracking-wide text-gray-500 line-through decoration-gray-500">$80</small>
				</div>
			</template>
		</CardsHomeItemCard>
	</div>
</template>

<style scoped>
.list-items-data img.list-img {
	@apply object-contain h-[10rem] bg-inherit scale-110  w-[15rem] sm:w-full;
}

::-webkit-scrollbar {
	width: 9px;
	height: 0px;
}
::-webkit-scrollbar-track {
	background: #f1f1f1;
}
/* Handle */
::-webkit-scrollbar-thumb {
	@apply bg-gray-300;
}
/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
	background: #555;
}
</style>
