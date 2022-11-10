<template>
	<NuxtLayout>
		<section class="w-full py-6 px-2 sm:px-4 md:px-12 lg:px-24 xl:px-32 2xl:px-36 flex flex-col gap-y-3 transition-all duration-200">
			<main class="grid grid-cols-1 md:grid-cols-10 gap-x-4 gap-y-6">
				<div class="items-body md:col-span-7 lg:col-span-8 flex flex-col gap-y-0 border border-gray-200 shadow-sm rounded">
					<div class="cart-details w-full border-b border-gray-200 flex flex-row items-center py-3 px-3">
						<h3 class="text-xl tracking-wide">Cart (1)</h3>
					</div>
					<div class="items-list flex flex-col gap-y-1 w-full">
						<div class="item flex-col flex gap-y-2.5">
							<div class="details grid grid-cols-2 py-2 px-2">
								<div class="item-details flex flex-row gap-x-3">
									<div class="img w-20 h-20">
										<img
											src="@/assets/Furnitures/kari-shea-ItMggD0EguY-unsplash-removebg-preview.png"
											alt=""
											class="object-contain w-full h-full"
										/>
									</div>
									<div class="name flex flex-col gap-y-1 py-2">
										<small class="capitalize text-base lg:text-lg text-gray-700 tracking-wide">Living room sofa</small>
									</div>
								</div>
								<div class="prices flex flex-col items-end px-4 justify-end gap-y-2">
									<h3 class="text-xl tracking-wider">$30</h3>
									<h3 class="text-gray-600 line-through text-lg tracking-wider">$40</h3>
								</div>
							</div>
							<div class="item-footer flex flex-row justify-between px-2 py-2">
								<div class="actions flex flex-row gap-x-2">
									<button
										class="flex flex-row px-2 py-1 rounded text-base text-amber-700 hover:bg-amber-100 uppercase items-center gap-x-2"
									>
										<div class="i-mdi-trash-can-outline text-xl"></div>
										<span>remove</span>
									</button>
								</div>
								<div class="quantity w-full flex flex-row gap-x-6 justify-end items-center px-4">
									<button
										class="bg-amber-500 hover:bg-amber-600 focus:bg-amber-600 transition duration-200 rounded-sm p-1.5 shadow-md"
									>
										<div class="i-mdi-minus text-gray-50 scale-125 text-lg"></div>
									</button>
									<span class="text-lg">1</span>
									<button
										class="bg-amber-500 hover:bg-amber-600 focus:bg-amber-600 transition duration-200 rounded-sm p-1.5 shadow-md"
									>
										<div class="i-mdi-plus text-gray-50 scale-125 text-lg"></div>
									</button>
								</div>
							</div>
						</div>
						<div class="item flex-col flex gap-y-2.5">
							<div class="details grid grid-cols-2 py-2 px-2">
								<div class="item-details flex flex-row gap-x-3">
									<div class="img w-20 h-20">
										<img
											src="@/assets/Furnitures/kari-shea-ItMggD0EguY-unsplash-removebg-preview.png"
											alt=""
											class="object-contain w-full h-full"
										/>
									</div>
									<div class="name flex flex-col gap-y-1 py-2">
										<small class="capitalize text-base lg:text-lg text-gray-700 tracking-wide">Living room sofa</small>
									</div>
								</div>
								<div class="prices flex flex-col items-end px-4 justify-end gap-y-2">
									<h3 class="text-xl tracking-wider">$30</h3>
									<h3 class="text-gray-600 line-through text-lg tracking-wider">$40</h3>
								</div>
							</div>
							<div class="item-footer flex flex-row justify-between px-2 py-2">
								<div class="actions flex flex-row gap-x-2">
									<button
										class="flex flex-row px-2 py-1 rounded text-base text-amber-700 hover:bg-amber-100 uppercase items-center gap-x-2"
									>
										<div class="i-mdi-trash-can-outline text-xl"></div>
										<span>remove</span>
									</button>
								</div>
								<div class="quantity w-full flex flex-row gap-x-6 justify-end items-center px-4">
									<button
										class="bg-amber-500 hover:bg-amber-600 focus:bg-amber-600 transition duration-200 rounded-sm p-1.5 shadow-md"
									>
										<div class="i-mdi-minus text-gray-50 scale-125 text-lg"></div>
									</button>
									<span class="text-lg">1</span>
									<button
										class="bg-amber-500 hover:bg-amber-600 focus:bg-amber-600 transition duration-200 rounded-sm p-1.5 shadow-md"
									>
										<div class="i-mdi-plus text-gray-50 scale-125 text-lg"></div>
									</button>
								</div>
							</div>
						</div>
						<div class="item flex-col flex gap-y-2.5">
							<div class="details grid grid-cols-2 py-2 px-2">
								<div class="item-details flex flex-row gap-x-3">
									<div class="img w-20 h-20">
										<img
											src="@/assets/Furnitures/kari-shea-ItMggD0EguY-unsplash-removebg-preview.png"
											alt=""
											class="object-contain w-full h-full"
										/>
									</div>
									<div class="name flex flex-col gap-y-1 py-2">
										<small class="capitalize text-base lg:text-lg text-gray-700 tracking-wide">Living room sofa</small>
									</div>
								</div>
								<div class="prices flex flex-col items-end px-4 justify-end gap-y-2">
									<h3 class="text-xl tracking-wider">$30</h3>
									<h3 class="text-gray-600 line-through text-lg tracking-wider">$40</h3>
								</div>
							</div>
							<div class="item-footer flex flex-row justify-between px-2 py-2">
								<div class="actions flex flex-row gap-x-2">
									<button
										class="flex flex-row px-2 py-1 rounded text-base text-amber-700 hover:bg-amber-100 uppercase items-center gap-x-2"
									>
										<div class="i-mdi-trash-can-outline text-xl"></div>
										<span>remove</span>
									</button>
								</div>
								<div class="quantity w-full flex flex-row gap-x-6 justify-end items-center px-4">
									<button
										class="bg-amber-500 hover:bg-amber-600 focus:bg-amber-600 transition duration-200 rounded-sm p-1.5 shadow-md"
									>
										<div class="i-mdi-minus text-gray-50 scale-125 text-lg"></div>
									</button>
									<span class="text-lg">1</span>
									<button
										class="bg-amber-500 hover:bg-amber-600 focus:bg-amber-600 transition duration-200 rounded-sm p-1.5 shadow-md"
									>
										<div class="i-mdi-plus text-gray-50 scale-125 text-lg"></div>
									</button>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div class="checkout-body flex flex-col gap-y-2 md:col-span-3 lg:col-span-2">
					<div class="cart-summary px-0 border border-gray-200 shadow-sm rounded flex flex-col">
						<div class="sum-title px-2 py-2.5 border-b border-gray-200">
							<h3 class="text-base uppercase tracking-wider">Cart summary</h3>
						</div>
						<div class="total flex flex-row justify-between items-center px-2 py-2.5 border-b border-gray-200">
							<span class="tracking-wide text-base">Total</span>
							<span class="tracking-wider text-xl">$100</span>
						</div>
						<div class="checkout flex flex-row px-2 py-2.5 items-center">
							<button
								class="py-2 w-full bg-amber-500 hover:bg-amber-600 focus:bg-amber-600 text-gray-50 uppercase tracking-wide text-base rounded-sm shadow-md transition duration-200"
							>
								checkout ($100)
							</button>
						</div>
					</div>
				</div>
			</main>
		</section>
	</NuxtLayout>
</template>

<style scoped>
.items-list .item {
	@apply border-b last:border-b-0 border-gray-200;
}
</style>
