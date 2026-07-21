<template>
  <div>
    <h1>hi</h1>
  </div>
</template>
<script setup lang="ts">
const vModel = defineModel<string>();
const props = defineProps<{
  bookid: string;
  author: string;
  image: string;
  summary: string;
  rating: number;
}>();
</script>
