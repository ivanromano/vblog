<template>
<main v-if="route.params.slug">
  <NuxtPage/>
</main>
<main v-else>
  <!-- {{DjangoStore.lista_blog()}} -->
  <Vcarousel/>
</main>
</template>

<script setup>
import { useDjangoStore } from "../store/tienda";

const route = useRoute()

const DjangoStore = useDjangoStore()
useHead({
    title: 'home',
})

</script>

<style lang="scss" scoped>

</style>



