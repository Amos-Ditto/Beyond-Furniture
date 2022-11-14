<script setup lang="ts">
defineProps<{
	toggleaccount: boolean;
}>();
</script>
<template>
	<div
		v-if="toggleaccount"
		class="account-drop-down border border-gray-200 absolute bottom-0 right-0 translate-y-[110%] min-w-[12rem] py-2 rounded z-20 shadow-lg bg-gray-50 flex flex-col gap-y-2"
	>
		<div class="account-links flex flex-col gap-y-0.5 w-full">
			<button
				class="w-full py-2 px-3 flex flex-row gap-x-2 justify-start items-center hover:bg-gray-200 focus:bg-gray-200 transition duration-200 tracking-wide text-gray-700 text-sm"
			>
				<UtilitiesOrdersIcon :class="'w-5 h-5 scale-110'" />
				Orders
			</button>
			<button
				class="w-full py-2 px-3 flex flex-row gap-x-2 justify-start items-center hover:bg-gray-200 focus:bg-gray-200 transition duration-200 tracking-wide text-gray-700 text-sm"
			>
				<UtilitiesFavouritesIcon :class="'w-5 h-5 scale-110'" />
				Saved
			</button>
		</div>
		<div class="account-auths flex flex-col gap-y-0.5 border-t border-gray-200 pt-2">
			<div class="new-auth flex flex-col gap-y-0.5">
				<button
					class="py-2 px-3 flex flex-row gap-x-2 items-center justify-start text-sm tracking-wide text-gray-700 hover:bg-gray-200 transition duration-200"
				>
					<div class="i-mdi-account-arrow-right-outline text-xl text-gray-600"></div>
					Sign-Up
				</button>
				<button
					class="py-2 px-3 flex flex-row gap-x-2 items-center justify-start text-sm tracking-wide text-gray-700 hover:bg-gray-200 transition duration-200"
				>
					<div class="i-mdi-login-variant text-xl text-gray-600"></div>
					Login
				</button>
			</div>
			<!-- <div class="logout w-full items-center flex justify-center">
                <button
                    class="px-2 py-1 uppercase text-base text-orange-400 tracking-wide hover:bg-amber-100 rounded transition duration-200"
                >
                    Logout
                </button>
            </div> -->
		</div>
	</div>
</template>
