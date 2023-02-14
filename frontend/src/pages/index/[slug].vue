<template>
  {{ sub_cate_id }}
<nav v-if="sub_cate_id">

<!-- <main class="flex items-center justify-center bg-yellow-100 !-z-10" >
<v-btn v-for="item in sub_cate_id" :key="item.id" class="mx-2 !normal-case -translate-y-1 transform" color="vicOrange" variant="elevated" >
  <button @click="handleconsole(item.new_id)">{{ item.name.charAt(0).toUpperCase() + item.name.slice(1)}} </button>
</v-btn>
</main> -->
<!-- {{ sub_cate_id[route.params.slug].sub_categories[0] }} -->
<!-- <h1>{{ DjangoStore.principal_categories[route.params.slug] }}</h1> -->

{{ selector_categ }}
<main  class="grid grid-cols-3 <lg:(grid-cols-2)">
  <div v-for="item in sub_cate_id" :key="item.id" class="mx-5 my-5 bg-purple-100 ">
  <div class="bg-white rounded-lg shadow-lg">
    <img src="https://images.unsplash.com/photo-1600054800747-be294a6a0d26?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1053&q=80" alt="" >
    <div class="p-6">
      <h2 class="font-bold mb-2 text-2xl text-purple-800">Card with an image
      </h2>
      <p class="text-purple-700 mb-2">This is a little bit better of a card!</p>
      <a href="#" class="text-purple-600 hover:text-purple-500 underline text-sm">Read More 👉</a>
    </div>
  </div>
</div>
</main>

</nav>
</template>

<script setup>
import { useDjangoStore } from '~~/src/store/tienda';


const DjangoStore = useDjangoStore()
const route = useRoute()
let sub_cate_id = ref(null)
let selector_categ = ref(1)

const handleconsole = (itemid) => {
  console.log(`${itemid}`);
}
// watch(() => DjangoStore.principal_categories, (newVal, oldVal) => {
  // if (DjangoStore.principal_categories.length) {
    sub_cate_id.value = DjangoStore.principal_categories[route.params.slug].sub_categories.map((objeto, index) => {
      return { ...objeto, new_id: index }
    })
  // }
// })

definePageMeta({
  pageTransition: {
    name: 'bounce'
  }
})

useHead({
    title: DjangoStore.principal_categories[route.params.slug].name
})
</script>

<style lang="scss" scoped>

</style>