<template>
  <div
    class="flex flex-col overflow-hidden rounded-3xl bg-white/40 shadow-xl backdrop-blur-md transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl md:flex-row"
  >
    <div class="flex items-center justify-center p-6 md:w-1/3">
      <img
        :src="imageurl"
        :alt="title"
        class="h-64 w-44 rounded-xl object-cover shadow-lg"
      />
    </div>
    <div class="flex flex-col justify-center p-6 md:w-2/3">
      <h3 class="text-3xl font-bold text-black">
        {{ title }}
      </h3>
      <p class="mt-2 text-xl text-black/60">
        {{ author }}
      </p>
      <p class="mt-5 text-lg leading-relaxed text-black/70">
        {{ summary }}
      </p>
      <div class="mt-6 flex items-center gap-2">
        <span class="text-2xl text-yellow-500"> ★ </span>
        <span class="text-xl font-semibold">
          {{ rating }}
        </span>
      </div>
    </div>
  </div>
</template>
<script setup>
defineProps({
  title: {
    type: String,
    required: true,
  },
  author: {
    type: String,
    required: true,
  },
  imageurl: {
    type: String,
    required: true,
  },
  summary: {
    type: String,
    required: true,
  },
  rating: {
    type: Number,
    required: true,
  },
});
</script>
