<script setup lang="ts">
const descriptions = ref<Element>(null);
const imgdescription = ref<Element>(null);
const loadedservices = ref<boolean>(false);
const loadedimg = ref<boolean>(false);

onMounted(() => {
	const servicesObs = new IntersectionObserver(
		(entry) => {
			if (entry[0].isIntersecting) {
				loadedservices.value = true;
				servicesObs.unobserve(entry[0].target);
			}
		},
		{
			threshold: 0.3,
		}
	);
	const imgObs = new IntersectionObserver(
		(entry) => {
			if (entry[0].isIntersecting) {
				loadedimg.value = true;
				imgObs.unobserve(entry[0].target);
			}
		},
		{
			threshold: 0.3,
		}
	);

	servicesObs.observe(descriptions.value);
	imgObs.observe(imgdescription.value);
});
</script>
<template>
	<div class="services-description w-full grid grid-cols-1 md:grid-cols-2 grid-rows-1 gap-x-4 gap-y-6 py-2 px-2 sm:px-0">
		<div
			ref="descriptions"
			class="descriptions flex flex-col gap-y-6 transition-all duration-500"
			:class="loadedservices ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-7'"
		>
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
		<div
			ref="imgdescription"
			class="img-description w-full relative flex flex-col items-center justify-center transition-all duration-500"
			:class="loadedimg ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-7'"
		>
			<img src="@/assets/Img/Bg/carpenter.webp" alt="image" />
		</div>
	</div>
</template>

<style scoped>
.img-description img {
	@apply rounded max-h-full min-h-full min-w-full max-w-full object-center;
}
</style>
