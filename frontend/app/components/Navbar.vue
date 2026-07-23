<template>
  <nav
    class="relative h-24 w-full overflow-visible border-b border-black/20 bg-zinc-500"
  >
    <div
      class="absolute inset-0 bg-[radial-gradient(circle_at_11%_36%,theme(colors.stone.400),theme(colors.zinc.400/.75)_62%,theme(colors.gray.600/.05))]"
    ></div>
    <div
      class="relative z-20 mx-auto flex h-full max-w-[1800px] items-center justify-between px-3 sm:px-5 md:px-8"
    >
      <div class="flex items-center gap-6">
        <button
          ref="menuButton"
          @click="toggleMenu"
          class="menuButton btn btn-ghost btn-square rounded-2xl border-none bg-transparent hover:bg-black/20 active:bg-black/30 transition-all duration-300"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-10 w-10 text-black"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            stroke-width="2.2"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M4 6h16M4 12h16M4 18h8"
            />
          </svg>
        </button>
        <Transition
          enter-active-class="duration-200 ease-out"
          enter-from-class="opacity-0 -translate-y-3 scale-95"
          enter-to-class="opacity-100 translate-y-0 scale-100"
          leave-active-class="duration-150 ease-in"
          leave-from-class="opacity-100"
          leave-to-class="opacity-0 -translate-y-2 scale-95"
        >
          <div
            v-if="open"
            class="absolute left-8 top-20 z-50 w-72 overflow-hidden rounded-3xl border border-white/60 bg-white/95 shadow-2xl backdrop-blur-md"
          >
            <NuxtLink
              to="/"
              class="dropdown-item block px-6 py-4 text-lg font-medium transition-all duration-200 hover:bg-neutral-300"
            >
              Home
            </NuxtLink>
            <NuxtLink
              to="/books"
              class="dropdown-item block px-6 py-4 text-lg font-medium transition-all duration-200 hover:bg-neutral-300"
            >
              Browse Books
            </NuxtLink>
            <NuxtLink
              to="/reviews"
              class="dropdown-item block px-6 py-4 text-lg font-medium transition-all duration-200 hover:bg-neutral-300"
            >
              Browse Reviews
            </NuxtLink>
          </div>
        </Transition>
      </div>

      <h1
        id="heading"
        class="absolute left-20 -translate-x-0 min-[1050px]:left-1/2 min-[1050px]:-translate-x-1/2 whitespace-nowrap font-mountains text-2xl min-[700px]:text-3xl min-[750px]:text-4xl min-[1200px]:text-5xl font-bold text-black opacity-0 transition-all"
      >
        Frazzetto's Book Review
      </h1>

      <div class="flex items-center gap-4">
        <button
          class="signin btn min-h-10 h-10 min-[700px]:min-h-12 min-[700px]:h-12 min-[750px]:min-h-14 min-[750px]:h-14 rounded-[22px] border-none bg-[#ECECEC] px-4 min-[700px]:px-6 min-[750px]:px-8 text-base min-[700px]:text-lg min-[750px]:text-xl font-semibold text-black shadow-md transition-all duration-300 hover:-translate-y-1 hover:bg-[#DDDDDD] hover:shadow-xl active:scale-95"
        >
          Sign In
        </button>
        <button
          class="register btn min-h-10 h-10 min-[700px]:min-h-12 min-[700px]:h-12 min-[750px]:min-h-14 min-[750px]:h-14 rounded-[22px] border-none bg-[#2F2F31] px-4 min-[700px]:px-6 min-[750px]:px-8 text-base min-[700px]:text-lg min-[750px]:text-xl font-semibold text-white shadow-md transition-all duration-300 hover:-translate-y-1 hover:bg-[#242426] hover:shadow-xl active:scale-95"
        >
          Register
        </button>
        <button
          class="searchButton btn btn-circle border-none bg-transparent w-10 h-10 min-[700px]:w-12 min-[700px]:h-12 min-[750px]:w-14 min-[750px]:h-14 transition-all duration-300 hover:bg-black/20 active:bg-black/30"
          aria-label="Search"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6 min-[700px]:h-8 min-[700px]:w-8 min-[750px]:h-10 min-[750px]:w-10 text-black"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            stroke-width="2.2"
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
  </nav>
</template>
<script setup lang="ts">
import { ref, onMounted, onUnmounted, nextTick } from "vue";
import { gsap } from "gsap";
import { SplitText } from "gsap/SplitText";

gsap.registerPlugin(SplitText);

const open = ref(false);
const menuButton = ref<HTMLElement | null>(null);

function toggleMenu() {
  open.value = !open.value;
  gsap.to(menuButton.value, {
    rotation: open.value ? 90 : 0,
    duration: 0.3,
    ease: "power2.out",
  });
  nextTick(() => {
    if (open.value) {
      gsap.from(".dropdown-item", {
        opacity: 0,
        x: -18,
        stagger: 0.06,
        duration: 0.3,
        ease: "power2.out",
      });
    }
  });
}
onMounted(() => {
  const ctx = gsap.context(() => {
    const split = SplitText.create("#heading", {
      type: "chars",
    });
    gsap.set("#heading", {
      opacity: 1,
    });
    const tl = gsap.timeline({
      defaults: {
        ease: "power3.out",
      },
    });

    tl.from(
      split.chars,
      {
        opacity: 0,
        scale: 0,
        rotation: gsap.utils.random(-180, 180),
        y: () => gsap.utils.random(-25, 25),
        x: () => gsap.utils.random(-15, 15),
        stagger: {
          each: 0.035,
          from: "random",
        },
        ease: "back.out(2)",
        duration: 0.7,
      },
      "<0.05"
    );
    tl.to(
      split.chars,
      {
        rotation: 0,
        x: 0,
        y: 0,
        duration: 0.35,
        stagger: 0.03,
        ease: "power2.out",
      },
      "<0.3"
    );

    tl.from(".menuButton", {
      opacity: 0,
      y: -20,
      stagger: 0.3,
      duration: 0.6,
      clearProps: "opacity,transform",
    });

    tl.from(
      ".signin, .register",
      {
        opacity: 0,
        y: -20,
        stagger: 0.3,
        duration: 0.6,
        clearProps: "opacity,transform",
      },
      "<0.1"
    );

    tl.from(".searchButton", {
      opacity: 0,
      y: -20,
      stagger: 0.3,
      duration: 0.6,
      clearProps: "opacity,transform",
    });

    gsap.utils.toArray<HTMLElement>(".signin, .register").forEach((button) => {
      button.addEventListener("mouseenter", () => {
        gsap.to(button, {
          y: -3,
          scale: 1.04,
          duration: 0.18,
          overwrite: "auto",
        });
      });
      button.addEventListener("mouseleave", () => {
        gsap.to(button, {
          y: 0,
          scale: 1,
          duration: 0.18,
          overwrite: "auto",
        });
      });
    });
    gsap.utils.toArray<HTMLElement>(".searchButton").forEach((button) => {
      button.addEventListener("mouseenter", () => {
        gsap.to(button, {
          scale: 1.12,
          duration: 0.2,
          overwrite: "auto",
        });
      });
      button.addEventListener("mouseleave", () => {
        gsap.to(button, {
          scale: 1,
          duration: 0.2,
          overwrite: "auto",
        });
      });
    });
    gsap.utils.toArray<HTMLElement>(".menuButton").forEach((button) => {
      button.addEventListener("mouseenter", () => {
        gsap.to(button, {
          scale: 1.08,
          duration: 0.2,
          overwrite: "auto",
        });
      });
      button.addEventListener("mouseleave", () => {
        gsap.to(button, {
          scale: 1,
          duration: 0.2,
          overwrite: "auto",
        });
      });
    });
  });

  onUnmounted(() => {
    ctx.revert();
  });
});
</script>
