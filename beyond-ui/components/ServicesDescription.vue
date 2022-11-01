<script setup lang="ts"></script>
<template>
	<div class="services-description w-full grid grid-cols-1 md:grid-cols-2 gap-x-4 gap-y-6 py-2 px-2 sm:px-0">
		<div class="descriptions flex flex-col gap-y-6">
			<div class="title">
				<h3 class="text-2xl tracking-wide font-semibold">Our Services</h3>
			</div>
			<div class="details-list grid grid-cols-2 gap-6">
				<CardsAboutDetail>
					<template #icon>
						<img src="@/assets/Img/Bg/free-delivery.svg" alt="" class="w-[3rem] text-gray-600" />
					</template>
					<template #title>Fast & Free Shipping </template>
					<template #about>
						Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit fugiat assumenda, itaque quaerat aspernatur eum.
					</template>
				</CardsAboutDetail>
				<CardsAboutDetail>
					<template #icon>
						<img src="@/assets/Img/Bg/best-price.svg" alt="" class="w-[3rem] text-gray-600" />
					</template>
					<template #title>Your Best price matching</template>
					<template #about>
						Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit fugiat assumenda, itaque quaerat aspernatur eum.
					</template>
				</CardsAboutDetail>
				<CardsAboutDetail>
					<template #icon>
						<img src="@/assets/Img/Bg/24-7.svg" alt="" class="w-[3rem] text-gray-600" />
					</template>
					<template #title>24/7 Supports</template>
					<template #about>
						Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit fugiat assumenda, itaque quaerat aspernatur eum.
					</template>
				</CardsAboutDetail>
				<CardsAboutDetail>
					<template #icon>
						<img src="@/assets/Img/Bg/exchange.svg" alt="" class="w-[3rem] text-gray-600" />
					</template>
					<template #title>Hassle Free returns</template>
					<template #about>
						Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit fugiat assumenda, itaque quaerat aspernatur eum.
					</template>
				</CardsAboutDetail>
			</div>
		</div>
		<div class="img-description">
			<img src="@/assets/Img/Bg/dwi-agus-prasetiyo-04jcazTIYCQ-unsplash_Compressmyimage.com.jpg" alt="image" loading="lazy" />
		</div>
	</div>
</template>

<style scoped>
.img-description img {
	@apply object-cover rounded h-[16rem] md:h-[24rem] w-full;
}
</style>
