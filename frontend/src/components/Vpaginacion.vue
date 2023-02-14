<template>
  <div>
    <div class="flex justify-center py-3">
      <v-btn @click="tiendaStore.currentPage--" :disabled="tiendaStore.currentPage <= 1" color="success">
        <Icon class="text-[25px] text-white" name="mdi:arrow-left-drop-circle-outline" />
          <!-- <v-icon>mdi-thumb-up</v-icon> -->
      </v-btn>

      <div class="mx-2 my-auto">
        <span  class="mx-1" :class="{ 'font-bold': page === tiendaStore.currentPage }">
          {{ tiendaStore.currentPage }}
        </span>
      </div>

      <v-btn @click="tiendaStore.currentPage++" :disabled="tiendaStore.currentPage >= 10" color="success">
        <Icon class="text-[25px] text-white" name="mdi:arrow-right-drop-circle-outline" />
          <!-- <v-icon>mdi-thumb-up</v-icon> -->
      </v-btn>
    </div>


  </div>
</template>


<script setup>
import { useTiendaStore } from '../store/tienda';

const tiendaStore = useTiendaStore()
// const itemsPerPage = 2;
// const items = [
//   { id: 1, name: 'item 1' },
//   { id: 2, name: 'item 2' },
//   { id: 3, name: 'item 3' },
//   { id: 4, name: 'item 4' },
//   { id: 5, name: 'item 5' },
//   { id: 6, name: 'item 6' },
//   // ...
// ];


</script>