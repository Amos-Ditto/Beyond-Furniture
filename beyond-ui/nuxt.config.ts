import presetIcons from "@unocss/preset-icons";

export default defineNuxtConfig({
	css: ["~/assets/css/tailwind.css"],
	buildModules: ["@nuxtjs/tailwindcss", "@unocss/nuxt"],
	app: {
		head: {
			charset: "utf-16",
			viewport: "width=500, initial-scale=1",
			title: "Beyond-Products",
			meta: [{ name: "description", content: "Find and get amazing furniture products." }],
		},
	},
	unocss: {
		icons: true,
		presets: [presetIcons({})],
	},
});
