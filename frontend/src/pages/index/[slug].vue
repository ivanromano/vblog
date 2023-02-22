<template>
  <template v-if="category_and_blog.length"> 
  <div class="flex items-center justify-center">
    <button  v-for="item in sub_category" :key="item" @click="handleSelector(item.new_id)" :class="`${categ_selector == item.new_id ? 'bg-gradient-to-t from-amber-300 to-amber-200' : 'bg-gradient-to-t from-amber-500 to-amber-300' }  rounded-[15px] mx-2 p-2 <lg:mt-12 lg:mt-16`">
    {{ item.name.charAt(0).toUpperCase() + item.name.slice(1) }}
  </button>
  </div>
<NuxtLink > </NuxtLink>
  <main  class="grid grid-cols-3 <lg:(grid-cols-2)"> 
    <template v-for="subcategory in [category_and_blog[categ_selector] ?? {}]" :key="subcategory.id">
    <template v-for="item in subcategory.post" :key="item.id" >
      <nav class="mx-5 my-5 bg-purple-100 ">
        <div class="bg-white rounded-lg shadow-lg">

          <img :src="`${item.get_thumnail}`" alt="" />
          <div class="p-6">
            <h2 class="font-bold mb-2 text-2xl text-purple-800 ">{{ item.title }}</h2>
            <span class="float-right text-purple-700 mb-2"> {{ item.published.slice(0, 10).replace(/-/g, '/') }} </span>
            <p> {{ item.excerpt }} </p>
            <NuxtLink :to="`/blog/${item.slug}`"  class="text-purple-600 hover:text-purple-500 underline text-sm">Ver Mas 👉</NuxtLink>
          </div>
        </div> 
      </nav>
    </template>
    </template> 
  </main>
  </template>
</template>
<script setup>
import { useDjangoStore } from '~~/src/store/tienda';

const DjangoStore = useDjangoStore()
const route = useRoute()
const loading = ref(false)
let sub_cate_id = ref(null)
const activeButton = ref(null)
let categ_selector = ref(0)

const post =  DjangoStore.vblog
const category =  DjangoStore.principal_categories
let sub_category = ref([]);

//  Tenemos dos objetos, "post" y "categorias". Cada post tiene un "id" y "category", que es el mismo "id" de una categoria. 
// Queremos crear un nuevo objeto llamado "CategoryMap", 
// donde cada categoria es el padre de los posts que tienen su "id". 
const CategoryMap = {};

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

// sub_cate_id.value = DjangoStore.principal_categories[route.params.slug].sub_categories.map((objeto, index) => {
//   return { ...objeto, new_id: index }
//   })
sub_category.value = DjangoStore.principal_categories[route.params.slug]?.sub_categories?.map((objeto, index) => {
  return { ...objeto }
}) ?? navigateTo(`/`);



const categories = Object.values(CategoryMap);
const category_and_blog = [];
for (const cat of categories) {
  if (sub_category.value.some((subCate) => subCate.id === cat.id)) {
    category_and_blog.push(cat);
  }
}

// console.log(category_and_blog);

const handleSelector = (new_id) => {
  activeButton.value = new_id
  categ_selector.value = new_id
}

// useHead({
//     title: DjangoStore.principal_categories[route.params.slug].name
// })

const currentRoute = computed(() => {
  return route.path;
})

// console.log(sub_category);

  
</script>

<style lang="scss" scoped>
.active {
  background-color: blue;
  color: white;
}
</style>
