<template>
  <div v-if="carousel_condicional">
    <div v-if="carousel_condicional" class="py-[15px] mx-5 text-red-600">
      <v-carousel cycle  interval='10000'>
        <v-carousel-item class="" v-for="(item) in carousel_condicional" :key="carousel_condicional.id" :src="item.get_thumnail" cover > 
          <img  alt="" class="">
        </v-carousel-item>
      </v-carousel>
    </div>
  </div>
</template>

<script setup>
import { useDjangoStore } from '../store/tienda';

const DjangoStore = useDjangoStore()
// const carousel_condicional = ref(null)

const carousel_condicional = computed(() => {
  return DjangoStore.vblog.filter(item => item.carousel);
})
</script>


<style lang="scss" scoped>

</style>