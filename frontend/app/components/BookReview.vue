<template>
  <div
    class="flex flex-col overflow-hidden rounded-3xl bg-white/40 shadow-xl backdrop-blur-md transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl"
  >
    <div class="flex justify-center p-6">
      <img
        :src="imageurl"
        :alt="title"
        class="h-56 w-40 rounded-xl object-cover shadow-lg"
      />
    </div>
    <div class="px-6 pb-6 text-center">
      <h3 class="text-3xl font-bold text-black">
        {{ title }}
      </h3>
      <p class="mt-2 text-xl text-black/60">Reviewed by {{ author }}</p>
      <div class="mt-4 flex justify-center gap-1">
        <span
          v-for="star in 5"
          :key="star"
          class="text-2xl"
          :class="star <= rating ? 'text-yellow-500' : 'text-black/20'"
        >
          ★
        </span>
      </div>
      <p class="mt-5 text-lg leading-relaxed text-black/70">"{{ review }}"</p>
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
  rating: {
    type: Number,
    required: true,
  },
  review: {
    type: String,
    required: true,
  },
});
</script>
