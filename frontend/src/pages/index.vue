<template>
<main v-if="route.params.slug">
  <NuxtPage/>
</main>
<main v-else class="pt-[90px]">
  <h1 class="text-lg text-center bg-light-500 p-3">Bereshipsis</h1>
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



