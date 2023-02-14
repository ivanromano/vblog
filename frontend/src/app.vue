<template>
<Vnavbar/>
<NuxtPage  class="pb-10" />
<Vfooter/>
</template>

<script setup>

useHead({
    titleTemplate: '%s - Vecgres',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description' }
    ],
    link: [{ rel: 'icon', type: 'image/jpeg', href: 'https://fiverr-res.cloudinary.com/images/t_medium7,q_auto,f_auto,q_auto,f_auto/gigs/291844489/original/14bbdb38018cf2c3caf10961328829a0837d20e5/convert-figma-to-vue-with-tailwind-and-ant-desing.jpg' }],
    link: [ 
        {
            rel: "stylesheet",
            href: "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css",
        }
    ],
    script: [
        {
            src: "https://js.stripe.com/v3",
            body: true
        }
    ]
})
</script>

<style lang="scss" scoped>

</style>
