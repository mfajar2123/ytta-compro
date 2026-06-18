// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  compatibilityDate: '2026-06-12',
  app: {
    pageTransition: { name: 'page', mode: 'out-in' },
    layoutTransition: { name: 'layout', mode: 'out-in' },
    head: {
      htmlAttrs: {
        lang: 'id'
      },
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
      meta: [
        { name: 'author', content: 'Raja Emas Indonesia' },
        { name: 'theme-color', content: '#111111' },
      ],
      link: [
        { rel: 'icon', type: 'image/webp', href: '/img/home/logo.webp' },
        { rel: 'apple-touch-icon', href: '/img/home/logo.webp' }
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
  modules: ["nuxt-icon", "@nuxt/image", "@nuxtjs/google-fonts"],
  googleFonts: {
    families: {
      'El Messiri': [400, 500, 600, 700],
      'Raleway': [400, 500, 600, 700],
    },
    display: 'swap',
    download: true,
  },
  routeRules: {
    '/_nuxt/**': { headers: { 'cache-control': 'public, max-age=31536000, immutable' } },
    '/**/*.js': { headers: { 'cache-control': 'public, max-age=31536000, immutable' } },
    '/**/*.css': { headers: { 'cache-control': 'public, max-age=31536000, immutable' } },
    '/**/*.webp': { headers: { 'cache-control': 'public, max-age=31536000, immutable' } },
    '/**/*.png': { headers: { 'cache-control': 'public, max-age=31536000, immutable' } },
    '/**/*.jpg': { headers: { 'cache-control': 'public, max-age=31536000, immutable' } },
    '/**/*.svg': { headers: { 'cache-control': 'public, max-age=31536000, immutable' } }
  },
});
