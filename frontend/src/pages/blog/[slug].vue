<template>
  <main class="bg-[#F1F1F1] py-[15px]">
    <main v-if="blog_slug" class="mt-14  mx-[15px]">
      <div class="p-8 bg-white rounded-lg shadow-lg">
        <h1 class="text-2xl font-bold mb-4">{{ blog_slug.title }}</h1>
        <v-parallax :src="blog_slug.get_thumnail" class="object-cover max-h-[370px] w-full mb-4 rounded-lg" alt=""/>
        <p class="text-gray-500 mb-4" v-html="blog_slug.description"></p>
      </div>
      {{ blog_slug }}
    </main>


    <main v-else>
      <p v-for="item in 10" :key="item">
        <p>Loading...</p>
      </p>
    </main>
  </main>
</template>

<script setup>
import { useDjangoStore } from '~~/src/store/tienda';
import { useRoute } from 'vue-router';

const route = useRoute();
const route_params = route.params.slug;

const DjangoStore = useDjangoStore();

const blog_slug = await DjangoStore.get_blog(route_params);
// console.log(blog_slug);

if (!blog_slug) {
  await navigateTo('/')
}
</script>
