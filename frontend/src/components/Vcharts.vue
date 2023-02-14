<template>
  <!-- {{ props.stats }} -->
  <main v-for="item in props.stats" :key="item.id">
    {{ item.stat.name }}: {{ item.base_stat }}
    <v-progress-linear :model-value="`${item.base_stat}`" bg-color="pink-lighten-3" color="pink-lighten-1"/>
    <br>
  </main>

    
    <!-- <v-progress-linear
      model-value="30"
      bg-color="blue-grey"
      color="lime"
    ></v-progress-linear>
    <br>
    <v-progress-linear
      model-value="45"
      bg-color="success"
      color="error"
    ></v-progress-linear> -->

</template>

<script setup>
const props = defineProps({
  stats: {
        type: Array,
        required: true
  }
})
</script>

<style lang="scss" scoped>

</style>