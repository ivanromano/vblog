<template>
  <div class="flex items-center justify-center">
    <button v-for="item in sub_cate_id" :key="item.id"  @click="handleSelector(item.new_id)" class="bg-amber-300 rounded-[15px] mx-2 p-2 mt-16">
      {{ item.name.charAt(0).toUpperCase() + item.name.slice(1) }}
    </button>
  </div>

  <main  class="grid grid-cols-3 <lg:(grid-cols-2)"> 
    <template v-for="subcategory in [category_and_blog[categ_selector]]" :key="subcategory.id" >
    <template v-for="item in subcategory.post" :key="item.id" >
      <nav class="mx-5 my-5 bg-purple-100 ">
        <div class="bg-white rounded-lg shadow-lg">
          <img :src="`${item.get_thumnail}`" alt="" >
          <div class="p-6">
            <h2 class="font-bold mb-2 text-2xl text-purple-800 ">{{ item.title }}</h2>
            <span class="float-right text-purple-700 mb-2"> {{ item.published.slice(0, 10).replace(/-/g, '/') }} </span>
            <NuxtLink :to="`/blog/${item.slug}`"  class="text-purple-600 hover:text-purple-500 underline text-sm">Read More 👉</NuxtLink>
          </div>
        </div> 
      </nav>
    </template>
    </template> 
  </main>
</template>
<!-- tengo en una api esto:  "description": "<p><img alt=\"\" src=\"https://images.pexels.com/photos/15011333/pexels-photo-15011333.png?auto=compress&amp;cs=tinysrgb&amp;w=1260&amp;h=750&amp;dpr=1\" style=\"height:71px; width:80px\" /></p>\r\n\r\n<p>no quiere que compres</p>", -->
<!-- intento acceder a description, pero obtengo solamente el objeto, no el html como tal <p class="text-purple-700 mb-2">{{ item.description }}</p> -->
<script setup>
import { useDjangoStore } from '~~/src/store/tienda';

const DjangoStore = useDjangoStore()
const route = useRoute()
const loading = ref(false)
let sub_cate_id = ref(null)
let categ_selector = ref(0)

const post =  DjangoStore.vblog
const category =  DjangoStore.principal_categories

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

sub_cate_id.value = DjangoStore.principal_categories[route.params.slug].sub_categories.map((objeto, index) => {
  return { ...objeto, new_id: index }
  })


  const categories = Object.values(CategoryMap);
  const category_and_blog = [];
for (const cat of categories) {
  if (sub_cate_id.value.some((subCate) => subCate.id === cat.id)) {
    category_and_blog.push(cat);
  }
}

// console.log(category_and_blog);

const handleSelector = (new_id) => {
  categ_selector.value = new_id
}

useHead({
    title: DjangoStore.principal_categories[route.params.slug].name
})


</script>

<style lang="scss" scoped>

</style>

<!--  
  quiero pasar pametros a una ruta <NuxtLink :to="{ name: 'blog-slug', params: { slug: item.published }, query: { post: item } }" class="text-purple-600 hover:text-purple-500 underline text-sm">Read More 👉</NuxtLink>
  // esto por alguna razon no me esta respetando los grid, se posisiona uno encima del otro

Uncaught (in promise) Error: No match for
 {"name":"blog-slug","params":{"slug":"2023-02-17T07:09:16Z"},"query":{"post":{"id":14,"title":"moscas","thumbnail":"/media/uploads/moscas.png","excerpt":"moscas","description":"<p>moscas</p>","slug":"moscas","published":"2023-02-17T07:09:16Z","category":16,"get_thumnail":"http://127.0.0.1:8000/media/uploads/moscas.png"}}}
    at createRouterError (vue-router.mjs:798:23)
    at Object.resolve (vue-router.mjs:1414:23)
    at Object.resolve (vue-router.mjs:3045:38)
    at ReactiveEffect.fn (vue-router.mjs:2157:41)
    at ReactiveEffect.run (reactivity.esm-bundler.js:187:25)
    at get value [as value] (reactivity.esm-bundler.js:1150:39)
    at useLink (vue-router.mjs:2200:30)
    at setup (vue-router.mjs:2246:31)
    at callWithErrorHandling (runtime-core.esm-bundler.js:157:22)
    at setupStatefulComponent (runtime-core.esm-bundler.js:7246:29)

este es mi codigo en index.vue:
    <nav class="mx-5 my-5 bg-purple-100 ">
      <div class="bg-white rounded-lg shadow-lg">
        <img :src="`${item.get_thumnail}`" alt="" >
        <div class="p-6">
          <h2 class="font-bold mb-2 text-2xl text-purple-800 ">{{ item.title }}</h2>
          <span class="float-right text-purple-700 mb-2"> {{ item.published.slice(0, 10).replace(/-/g, '/') }} </span>
          <NuxtLink :to="{ name: 'blog-slug', params: { slug: item.published }, query: { post: item } }" class="text-purple-600 hover:text-purple-500 underline text-sm">Read More 👉</NuxtLink>
        </div>
      </div> 
    </nav>

el archivo al que quiero acceder y esta dentro de pages es: blog/_slug.vue
-->