<template>
  <div class="shadow-sm bg-white">
    <div class="flex items-center justify-between px-6 py-4">
      <div class="relative">
        <button
          @click="open = !open"
          class="p-2 rounded-lg hover:bg-gray-100 transition"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16M4 18h7"
            />
          </svg>
        </button>
        <div
          v-if="open"
          class="absolute left-0 mt-2 w-60 bg-white rounded-lg shadow-lg border p-2 z-50"
        >
          <NuxtLink to="/" class="block px-4 py-2 rounded hover:bg-gray-100">
            Home
          </NuxtLink>

          <NuxtLink
            to="/books"
            class="block px-4 py-2 rounded hover:bg-gray-100"
          >
            Browse Reviews
          </NuxtLink>

          <NuxtLink
            to="/reviews"
            class="block px-4 py-2 rounded hover:bg-gray-100"
          >
            Highest Rated Books
          </NuxtLink>
        </div>
      </div>
      <NuxtLink
        to="/"
        class="text-xl font-bold text-gray-800 absolute left-1/2 transform -translate-x-1/2"
      >
        Frazzetto Book Reviews
      </NuxtLink>
      <div>
        <button></button>
      </div>
    </div>
  </div>
</template>

<script setup>
const open = ref(false);
</script>
