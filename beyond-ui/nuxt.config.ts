import presetIcons from "@unocss/preset-icons";

export default defineNuxtConfig({
	css: ["~/assets/css/tailwind.css", "~/assets/css/global.css"],
	buildModules: ["@nuxtjs/tailwindcss", "@unocss/nuxt", "@nuxtjs/color-mode"],
	coloMode: {
		classSuffix: "",
	},
	app: {
		head: {
			charset: "utf-16",
			viewport: "width=500, initial-scale=1",
			title: "Beyond-Products",
			meta: [{ name: "description", content: "Find and get amazing furniture products." }],
		},
		pageTransition: { name: "page", mode: "out-in" },
	},
	unocss: {
		icons: true,
		presets: [presetIcons({})],
	},
	loading: {
		duration: 3000,
		continuous: true,
	},
});
