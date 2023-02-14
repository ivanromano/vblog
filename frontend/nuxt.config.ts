
export default defineNuxtConfig({
  modules: [
    'nuxt-windicss', 'nuxt-icon', '@pinia/nuxt', 
  ],
  srcDir: 'src',
  css: ['vuetify/lib/styles/main.sass', '@mdi/font/css/materialdesignicons.min.css'],
  build: {
    transpile: ['vuetify'],
  },
  // vite: {
  //   define: {
  //     'process.env.DEBUG': false,
  //   },
  // },
  // ssr: {
  //   noExternal: ['moment', 'compute-scroll-into-view', '@nuxtjs/vuetify', 'vue3-carousel', ''],
  //   },
  nitro: {
    plugins: ['~/server/index.js']
  },
  runtimeConfig: {
    MONGODB_URI: process.env.MONGODB_URI
  }
})
