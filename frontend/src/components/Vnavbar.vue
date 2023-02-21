<template>

<nav v-if="categories_full" class="z-20 flex flex-col md:flex-row w-full bg-blue-600 text-white shadow-md leading-none shadow-blue-200 shadow-md fixed">
  <div class="flex items-center mx-5 py-1 md:py-0">
    <Icon name="logos:vector-timber" class="text-[50px] "/>
    <h1 class="text-2xl ml-2 inline-block">ecgress</h1>
    <button class="lg:hidden <lg:ml-auto  flex-shrink text-[2rem] " @click="show = !show"> <Icon  name="radix-icons:hamburger-menu"/> </button>
  
  </div>
  <div class="lg:flex lg:flex-grow bg-blue-700 lg:bg-blue-600">
    <ul :class="`text-lg lg:flex lg:ml-auto ${show ? '' : `<lg:hidden`  }`">
      <!-- ! home -->
      <li> <NuxtLink exactActiveClass="lg:border-white bg-blue-800" class="navbar_link" to="/" @click="show = !show">home</NuxtLink> </li>
      <!-- ! categories -->
      <li v-for="item in categories_full" :key="item.new_id">
        <NuxtLink exactActiveClass="lg:border-white bg-blue-800" class="navbar_link" @click="show = !show" 
        :to="`${item.new_id}`" >{{ item.name }}
        </NuxtLink>
      </li>
    </ul>
  </div>
</nav>
</template>

<!--
-->


<script setup>
import { useDjangoStore } from '../store/tienda';

const DjangoStore = useDjangoStore()
// let categories_full = ref(null)
const show = ref(false)

// watch(() => DjangoStore.principal_categories, (newVal, oldVal) => {
//   if (DjangoStore.principal_categories.length) {
//   categories_full.value = DjangoStore.principal_categories
// }
// })

const categories_full = computed(() => {
  return DjangoStore.principal_categories
})



// console.log( nuevoID.value);
</script>

<style scoped>
 /* a {
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
} */


</style>