<template>

<nav v-if="nuevoID" class="z-20 flex flex-col md:flex-row bg-blue-600 text-white shadow-md leading-none shadow-blue-200 shadow-md">
  <div class="flex items-center mx-5 py-1 md:py-0">
    <Icon name="logos:vector-timber" class="text-[50px] "/>
    <h1 class="text-2xl ml-2 inline-block">ecgress</h1>
    <Icon class="lg:invisible <lg:ml-[70%] text-[3rem] " name="radix-icons:hamburger-menu"/>
  </div>
  <div class="md:flex md:flex-grow bg-blue-700 md:bg-blue-600">
    <ul class="text-lg md:flex md:ml-auto ">
      <!-- ! home -->
      <li> <NuxtLink exactActiveClass="lg:border-white bg-blue-800" class="navbar_link" to="/">home</NuxtLink> </li>
      <!-- ! categories -->
      <li v-for="item in nuevoID" :key="item.new_id">
        <NuxtLink exactActiveClass="lg:border-white bg-blue-800" class="navbar_link" :to="`${item.new_id}`">{{ item.name }}</NuxtLink>
      </li>
    </ul>
  </div>
</nav>
</template>

<script setup>
import { useDjangoStore } from '../store/tienda';

const DjangoStore = useDjangoStore()
let nuevoID = ref(null)

watch(() => DjangoStore.principal_categories, (newVal, oldVal) => {
  if (DjangoStore.principal_categories.length) {
  nuevoID.value = DjangoStore.principal_categories.map((objeto, index) => {
    return { ...objeto, new_id: index }
  })
}
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




<!-- 
<template>
      <ul class="text-lg md:flex md:ml-auto ">
        <li v-for="item in nuevoID" :key="item.new_id">
          <NuxtLink exactActiveClass="lg:border-white bg-blue-800" class="navbar_link" :to="`${item.new_id}`">{{ item.name }}</NuxtLink>
        </li>
      </ul>
  </template>
  
  <script setup>
  import { useDjangoStore } from '../store/tienda';
  
  const DjangoStore = useDjangoStore()
  const numberRandom = (min, max) => {
    return Math.floor(Math.random() * (max - min + 1) + min)
  }
  
  let nuevoID = DjangoStore.principal_categories.map((objeto, index) => {
    return { ...objeto, new_id: index }
  });
  </script> -->
  