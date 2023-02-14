<template>
  {{ DjangoStore.vblog}}
<div class=" my-[20px] mx-5 h-[200%]">
  <v-carousel cycle height="400" interval='10000'  >
    <v-carousel-item v-for="(item) in DjangoStore.vblog" :key="DjangoStore.vblog.id" :src="item.get_thumnail" cover > 
    </v-carousel-item>
  </v-carousel>
</div>
</template>

<script setup>
import { useDjangoStore } from '../store/tienda';


const DjangoStore = useDjangoStore()
</script>

<style lang="scss" scoped>

</style>