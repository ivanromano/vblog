<template>
<nav v-if="sub_cate_id">

  <main class="bg-white mx-4 p-1 ">
    <div class=" flex items-center justify-center ">
      <button v-for="item in sub_cate_id" :key="item.id" @click="handleconsole(item.new_id)" class="bg-amber-300 rounded-[15px] mx-2 p-2 mt-16">
        {{ item.name.charAt(0).toUpperCase() + item.name.slice(1)}}
      </button>
    </div>
  </main>

  <main>
  <div v-for="subCategory in category" :key="subCategory.id">
    <h2>{{ subCategory.name }}</h2>
    <div v-for="post in subCategory.posts" :key="post.id">
      <h3>{{ post.title }}</h3>
      <p>{{ post.content }}</p>
    </div>
  </div>
</main>
<!-- <main  class="grid grid-cols-3 <lg:(grid-cols-2)">
  <main v-for="item in finalCategoryMap[1].sub_categories" :key="item.id" class="mx-5 my-5 bg-purple-100 ">
  <div class="bg-white rounded-lg shadow-lg">
    <img src="https://images.unsplash.com/photo-1600054800747-be294a6a0d26?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1053&q=80" alt="" >
    <div class="p-6">
      <h2 class="font-bold mb-2 text-2xl text-purple-800">{{ item.name }}
      </h2>
      <p class="text-purple-700 mb-2">This is a little bit better of a card!</p>
      <a href="#" class="text-purple-600 hover:text-purple-500 underline text-sm">Read More 👉</a>
    </div>
  </div>
</main>
</main> -->

</nav>
</template>

<script setup>
import { useDjangoStore } from '~~/src/store/tienda';

const DjangoStore = useDjangoStore()
const route = useRoute()
const loading = ref(false)
let sub_cate_id = ref(null)
let selector_categ = ref(1)

const CategoryMap = {};
const post =  DjangoStore.vblog
const category =  DjangoStore.principal_categories

//  Tenemos dos objetos, "post" y "categorias". Cada post tiene un "id" y "category", que es el mismo "id" de una categoria. 
// Queremos crear un nuevo objeto llamado "CategoryMap", 
// donde cada categoria es el padre de los posts que tienen su "id". 
category.map(cat => {
  cat.sub_categories.forEach(subcat => {
    CategoryMap[subcat.id] = { ...subcat, post: [] };
  });
});

post.map(p => {
  if (CategoryMap[p.category]) {
    CategoryMap[p.category].post.push(p);
  }
});

// const finalCategoryMap = Object.entries(CategoryMap)
//   .filter(([name, cat]) => cat.sub_categories && Object.keys(cat.sub_categories).length > 0)
//   .reduce((acc, [name, cat]) => {
//     return { ...acc, [name]: { ...cat, sub_categories: Object.values(cat.sub_categories) } };
//   }, {});

console.log(CategoryMap);

sub_cate_id.value = DjangoStore.principal_categories[route.params.slug].sub_categories.map((objeto, index) => {
  return { ...objeto, new_id: index }
  })

useHead({
    title: DjangoStore.principal_categories[route.params.slug].name
})

</script>

<style lang="scss" scoped>

</style>




