// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  compatibilityDate: '2026-06-12',
  app: {
    head: {
      htmlAttrs: {
        lang: 'id'
      },
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
      meta: [
        { name: 'author', content: 'Raja Emas Indonesia' },
        { name: 'theme-color', content: '#111111' },
      ]
    }
  },
  css: ["~/assets/css/main.css"],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  modules: ["nuxt-icon"],
});
