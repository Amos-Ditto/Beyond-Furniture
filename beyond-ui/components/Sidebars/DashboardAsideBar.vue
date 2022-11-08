<template>
	<aside class="col-span-2 fixed md:relative top-10 md:top-0 left-0 bottom-0 right-0 flex flex-col gap-y-3 z-20">
		<div class="desktop-side hidden md:flex flex-col gap-y-6 rounded h-auto py-2">
			<div class="categories flex flex-col gap-y-2">
				<h3 class="text-lg tracking-wide font-semibold capitalize px-3.5">categories</h3>
				<label for="living">
					<input type="checkbox" name="living" id="living" />
					<small>Living Room</small>
				</label>
				<label for="bedroom">
					<input type="checkbox" name="bedroom" id="bedroom" />
					<small>Bed Room</small>
				</label>
				<label for="kitchen">
					<input type="checkbox" name="kitchen" id="kitchen" />
					<small>kitchen</small>
				</label>
				<label for="others">
					<input type="checkbox" name="others" id="others" />
					<small>others</small>
				</label>
			</div>
			<div class="filters flex flex-col gap-y-2 w-full">
				<h3 class="text-lg tracking-wide font-semibold capitalize px-2">filters</h3>

				<div class="prices flex flex-col gap-y-2">
					<h3 class="text-sm font-semibold uppercase px-3.5 text-gray-700">price</h3>
					<label for="less">
						<input type="checkbox" name="less" id="less" />
						<small>less than $30</small>
					</label>
					<label for="between">
						<input type="checkbox" name="between" id="between" />
						<small>$30 - $50</small>
					</label>
					<label for="more">
						<input type="checkbox" name="more" id="more" />
						<small>more than $50</small>
					</label>
				</div>
				<div class="colors py-2 flex flex-col gap-y-2">
					<h3 class="text-sm font-semibold uppercase px-3.5 text-gray-700">colors</h3>
					<div class="color-list flex flex-wrap gap-x-3 gap-y-3 px-4 items-center justify-start">
						<label for="white">
							<input type="checkbox" name="white" id="white" class="bg-gray-50 checked:after:text-gray-800" />
						</label>
						<label for="blue">
							<input type="checkbox" name="blue" id="blue" class="bg-sky-600 checked:after:text-gray-50" />
						</label>
						<label for="green">
							<input type="checkbox" name="green" id="green" class="bg-emerald-500 checked:after:text-gray-50" />
						</label>
						<label for="orange">
							<input type="checkbox" name="orange" id="orange" class="bg-orange-400 checked:after:text-gray-50" />
						</label>
						<label for="black">
							<input type="checkbox" name="black" id="black" class="bg-dark checked:after:text-gray-50" />
						</label>
						<label for="brown">
							<input type="checkbox" name="brown" id="brown" class="bg-amber-700 checked:after:text-gray-50" />
						</label>
						<label for="purple">
							<input type="checkbox" name="purple" id="purple" class="bg-purple-800 checked:after:text-gray-50" />
						</label>
					</div>
				</div>
			</div>
			<div class="apply px-3.5 pt-4 pb-2">
				<button
					class="text-sm tracking-wide bg-amber-600 hover:bg-amber-500 focus:bg-amber-500 text-gray-50 capitalize px-5 py-2 w-full rounded transition duration-200"
				>
					apply
				</button>
			</div>
		</div>
		<div class="toggle-side absolute md:hidden top-0 left-0 bottom-0 right-0 bg-gray-100 opacity-10 -z-10"></div>
		<div class="mobile flex flex-col gap-y-6 md:hidden w-1/2 h-full pt-10 pb-3 bg-gray-100 overflow-y-auto">
			<div class="categories flex flex-col gap-y-2">
				<h3 class="text-lg tracking-wide font-semibold capitalize px-4">categories</h3>
				<label for="living">
					<input type="checkbox" name="living" id="living" />
					<small>Living Room</small>
				</label>
				<label for="bedroom">
					<input type="checkbox" name="bedroom" id="bedroom" />
					<small>Bed Room</small>
				</label>
				<label for="kitchen">
					<input type="checkbox" name="kitchen" id="kitchen" />
					<small>kitchen</small>
				</label>
				<label for="others">
					<input type="checkbox" name="others" id="others" />
					<small>others</small>
				</label>
			</div>
			<div class="filters flex flex-col gap-y-2 w-full">
				<h3 class="text-lg tracking-wide font-semibold capitalize px-4">filters</h3>

				<div class="prices flex flex-col gap-y-2">
					<h3 class="text-sm font-semibold uppercase px-5 text-gray-700">price</h3>
					<label for="less">
						<input type="checkbox" name="less" id="less" />
						<small>less than $30</small>
					</label>
					<label for="between">
						<input type="checkbox" name="between" id="between" />
						<small>$30 - $50</small>
					</label>
					<label for="more">
						<input type="checkbox" name="more" id="more" />
						<small>more than $50</small>
					</label>
				</div>
				<div class="colors py-2 flex flex-col gap-y-2">
					<h3 class="text-sm font-semibold uppercase px-5 text-gray-700">colors</h3>
					<div class="color-list flex flex-wrap gap-x-3 gap-y-3 px-6 items-center justify-start">
						<label for="white">
							<input type="checkbox" name="white" id="white" class="bg-gray-50 checked:after:text-gray-800" />
						</label>
						<label for="blue">
							<input type="checkbox" name="blue" id="blue" class="bg-sky-600 checked:after:text-gray-50" />
						</label>
						<label for="green">
							<input type="checkbox" name="green" id="green" class="bg-emerald-500 checked:after:text-gray-50" />
						</label>
						<label for="orange">
							<input type="checkbox" name="orange" id="orange" class="bg-orange-400 checked:after:text-gray-50" />
						</label>
						<label for="black">
							<input type="checkbox" name="black" id="black" class="bg-dark checked:after:text-gray-50" />
						</label>
						<label for="brown">
							<input type="checkbox" name="brown" id="brown" class="bg-amber-700 checked:after:text-gray-50" />
						</label>
						<label for="purple">
							<input type="checkbox" name="purple" id="purple" class="bg-purple-800 checked:after:text-gray-50" />
						</label>
					</div>
				</div>
			</div>
			<div class="apply px-5 pt-4 pb-2">
				<button
					class="text-sm tracking-wide bg-amber-600 hover:bg-amber-500 focus:bg-amber-500 text-gray-50 capitalize px-5 py-2 w-full rounded transition duration-200"
				>
					apply
				</button>
			</div>
		</div>
	</aside>
</template>

<style scoped>
.desktop-side {
	box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 8px;
}
.categories label {
	@apply w-full px-5 md:px-3.5 py-2 flex flex-row items-center gap-x-4 hover:bg-gray-200 transition duration-200 cursor-pointer selection:bg-gray-200 text-gray-700;
}
.categories label input[type="checkbox"] {
	@apply w-5 h-5 checked:bg-orange-300 indeterminate:bg-gray-300 outline-1 outline-gray-300 appearance-none border rounded border-gray-300;
	@apply flex items-center justify-center checked:after:content-['\2713'] checked:after:text-gray-50 checked:after:text-xl checked:border-transparent;
}
.categories label small {
	@apply text-base tracking-wide capitalize;
}

.prices label {
	@apply w-full px-6 md:px-4 py-2 flex flex-row items-center gap-x-4 hover:bg-gray-200 transition duration-200 cursor-pointer selection:bg-gray-200 text-gray-700;
}
.prices label input[type="checkbox"] {
	@apply w-4 h-4 checked:bg-emerald-500 indeterminate:bg-gray-300 outline-1 outline-gray-300 appearance-none border rounded border-gray-300;
	@apply flex items-center justify-center checked:after:content-['\2713'] checked:after:text-gray-50 checked:after:text-xl checked:border-transparent;
}
.prices label small {
	@apply text-sm tracking-wide capitalize;
}

.color-list label input[type="checkbox"] {
	@apply w-8 md:w-6 h-8 md:h-6 appearance-none first:border rounded border-gray-300;
	@apply flex items-center justify-center checked:after:content-['\2713'] checked:after:text-xl;
}
</style>
