export default defineNuxtConfig({
    css: ["~/assets/css/tailwind.css", "~/assets/css/global.css"],
    buildModules: ["@nuxtjs/tailwindcss"],
    app: {
        head: {
            charset: "utf-16",
            viewport: "width=500, initial-scale=1",
            title: "Beyond-Products",
            meta: [
                { name: "description", content: "Find and get amazing furniture products." },
            ],
        },
    },
});
