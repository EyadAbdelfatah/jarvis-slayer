<template>
  <div
    class="w-full min-h-screen bg-gradient-to-b from-green-200 to-indigo-300 overflow-hidden"
  >
    <section
      class="w-full min-h-[484px] flex flex-col items-center justify-center px-6"
    >
      <h1
        class="text-center text-black text-5xl md:text-6xl font-bold font-inter drop-shadow-lg"
        id="heading"
      >
        Upload your reviews - or browse others.
      </h1>
      <div class="mt-12 flex flex-col md:flex-row gap-12">
        <button
          class="w-60 h-16 bg-indigo-500 rounded-full text-white text-2xl font-bold font-inter hover:bg-indigo-600 transition"
        >
          Browse Books
        </button>

        <button
          class="w-60 h-16 bg-indigo-500 rounded-full text-white text-2xl font-bold font-inter hover:bg-indigo-600 transition"
        >
          View Reviews
        </button>
      </div>
    </section>
    <section class="w-full flex flex-col md:flex-row">
      <!--books-->
      <div class="w-full md:w-1/2 min-h-[700px] flex justify-center pt-10">
        <h2 class="text-black text-5xl md:text-6xl font-bold font-josefin">
          View Books
        </h2>
      </div>
      <!--reviews-->
      <div class="w-full md:w-1/2 min-h-[700px] flex justify-center pt-10">
        <h2 class="text-black text-5xl md:text-6xl font-bold font-josefin">
          View Reviews
        </h2>
      </div>
    </section>
  </div>
</template>
<script setup lang="ts">
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { SplitText } from "gsap/SplitText";
onMounted(() => {
  gsap.registerPlugin(SplitText);
  let split = SplitText.create("#heading", { type: "chars" });
  gsap.from(split.chars, {
    x: 20,
    yPercent: -50,
    opacity: 0,
    stagger: 0.05,
  });
  gsap.set("h1", { opacity: 1 });
});
</script>
