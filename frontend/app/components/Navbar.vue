<template>
  <div
    class="w-full h-24 relative overflow-visible border-b-4 border-black bg-zinc-500"
  >
    <!-- Radial gradient background -->
    <div
      class="absolute inset-0 bg-[radial-gradient(circle_at_11%_36%,theme(colors.stone.400),theme(colors.zinc.400/.7)_62%,theme(colors.gray.600/.05))]"
    ></div>

    <!-- Navbar contents -->
    <div
      class="relative z-10 w-full h-full flex items-center justify-between px-8"
    >
      <!-- Menu -->
      <div class="relative">
        <button
          @click="open = !open"
          class="p-2 rounded-lg hover:bg-white/20 transition"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-8 w-8 text-black"
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
            to="/reviews"
            class="block px-4 py-2 rounded hover:bg-gray-100"
          >
            Browse Reviews
          </NuxtLink>

          <NuxtLink
            to="/books"
            class="block px-4 py-2 rounded hover:bg-gray-100"
          >
            Highest Rated Books
          </NuxtLink>
        </div>
      </div>

      <!-- Title -->
      <h1
        class="absolute left-1/2 -translate-x-1/2 text-black text-5xl md:text-6xl font-bold font-mountains drop-shadow-lg whitespace-nowrap"
      >
        Frazzetto’s Book Review
      </h1>

      <div class="flex items-center gap-3">
        <button class="px-4 py-2 bg-gray-200 rounded-lg font-inter text-black">
          Sign in
        </button>

        <button
          class="px-4 py-2 bg-indigo-600 rounded-lg font-inter text-white"
        >
          Register
        </button>

        <!-- Future Search Button -->
        <button
          class="w-12 h-12 rounded-lg hover:bg-white/20 transition flex items-center justify-center"
          aria-label="Search"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="w-8 h-8 text-black"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            stroke-width="2"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M21 21l-4.35-4.35m1.35-5.65a7 7 0 11-14 0 7 7 0 0114 0z"
            />
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import gsap from "gsap";

const open = ref(false);
console.clear();

gsap.registerPlugin(SplitText);

let split = SplitText.create("#heading", { type: "chars" });

gsap.from(split.chars, {
  x: 20,
  yPercent: -50,
  opacity: 0,
  stagger: 0.05,
});

gsap.set("h1", { opacity: 1 });
</script>
