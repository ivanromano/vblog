<template>
  <main v-for="item in data" :key="item.id" class="mb-4 ">
  <!-- <main grid grid-cols-3> -->
<v-hover v-slot="{ isHovering, props }">
  <v-card class="flex flex-wrap mx-6" max-width="400" v-bind="props">
    <v-img class="align-end text-white" height="200" :src="`${item.imagen}`" cover>
      <v-expand-transition>
          <a :href="`${ item.disponible ? 'https://api.whatsapp.com/send?phone=5492665036048' : '#'}`" v-if="isHovering" class="d-flex transition-fast-in-fast-out bg-orange-darken-2 v-card--reveal text-h2" style="height: 100%;">
            <icon :class="`${item.disponible ? 'text-170px' : 'text-40'}`" v-bind:name="`${item.disponible ? 'logos:whatsapp' : 'fe:disabled'}`" />
            <div v-if="!item.disponible" class="text-20px" > No disponible </div>
        </a>
      </v-expand-transition>
      <v-card-title class="bg-gray-400 bg-opacity-50">{{ item.titulo  }}</v-card-title>
    </v-img>

    <v-card-text>    
      <div> {{ item.subtitulo }}</div>
      <v-btn variant="outlined" class="mt-2">
        <span>
          $
          <span>
            {{ item.precio }}
          </span>
        </span>
    </v-btn>
    </v-card-text>

  </v-card>
</v-hover>

  <!-- </main> -->
</main> </template>

<script setup>
const supabase = useSupabaseClient()

const {data} = await useAsyncData(async () => {
  const {data} = await supabase.from('LoUltimo').select('*')
  return data
  console.log(data);
})
</script>

<style lang="scss" scoped>
  .v-card--reveal {
    align-items: center;
    bottom: 0;
    justify-content: center;
    opacity: .9;
    position: absolute;
    width: 100%;
  }
</style>