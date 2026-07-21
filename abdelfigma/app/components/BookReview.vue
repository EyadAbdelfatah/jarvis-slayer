<template>
  <div>
    <h1>hi</h1>
  </div>
</template>
<script setup lang="ts">
//reviewid, bookid, studentid (figure out how to pull info from that), text from review, rating, spoiler (y/n), creation date
const vModel = defineModel<string>();
const props = defineProps<{
  reviewid: string;
  bookid: string;
  studentid: string;
  author: string;
  review: string;
  rating: number;
  spoiler: boolean;
  date: Date;
}>();
</script>
