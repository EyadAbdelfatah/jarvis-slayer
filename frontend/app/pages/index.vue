<template>
  <main
    class="w-full min-h-screen overflow-hidden bg-gradient-to-b from-green-200 via-cyan-100 to-indigo-300"
  >
    <section
      class="heroSection relative flex min-h-screen flex-col items-center justify-center px-6"
    >
      <div class="max-w-6xl">
        <h1
          id="heroHeading"
          class="heroHeading text-center text-5xl font-bold font-inter text-black opacity-0 md:text-7xl"
        >
          Upload your reviews - or browse others.
        </h1>
        <p
          class="heroSubtitle italic mx-auto mt-10 max-w-3xl text-center text-2xl text-black/70"
        >
          Write reviews, read your classmates reviews, and discover your new
          favorite book.
        </p>
        <div
          class="mt-14 flex flex-col items-center justify-center gap-8 md:flex-row"
        >
          <button
            class="browseBtn py-4 shadow-lg btn rounded-full border-none bg-indigo-500 px-12 text-2xl text-white transition-all duration-300 hover:-translate-y-1 hover:bg-indigo-600 hover:shadow-xl"
          >
            Browse Books
          </button>
          <button
            class="reviewBtn py-4 shadow-lg btn rounded-full border-none bg-zinc-800 px-12 text-2xl text-white transition-all duration-300 hover:-translate-y-1 hover:bg-black hover:shadow-xl"
          >
            View Reviews
          </button>
        </div>
      </div>

      <div
        class="scrollIndicator absolute bottom-10 flex flex-col items-center"
      >
        <span class="text-inter text-xl text-black/40"> Scroll </span>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="mt-2 h-8 w-8 text-black/50"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          stroke-width="2"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M12 5v14m0 0l-5-5m5 5l5-5"
          />
        </svg>
      </div>
    </section>

    <section
      class="relative flex min-h-screen flex-col justify-center px-8 py-20"
    >
      <div class="mx-auto grid w-full max-w-7xl gap-16 lg:grid-cols-2">
        <div class="booksSection">
          <h2
            class="mb-8 text-center font-josefin text-5xl font-bold text-black md:text-7xl"
          >
            View Books
          </h2>
          <div class="flex flex-wrap justify-center gap-8">
            <!--
            <BookDisplay
              v-for="i in book.length"
              :key="i"
              title="book[i].title"
              author="book[i].author"
              image="book[i].image"
              summary="book[i].summary"
              rating="book[i].rating"
            />
            !-->
          </div>
          <div class="mt-10 flex justify-center">
            <button
              class="btn rounded-full text-bold border-none py-1.5 bg-indigo-500 px-10 text-xl text-white transition-all duration-300 hover:-translate-y-1 hover:bg-indigo-600 hover:shadow-xl"
            >
              Browse Books
            </button>
          </div>
        </div>

        <div class="reviewsSection">
          <h2
            class="mb-8 text-center font-josefin text-5xl font-bold text-black md:text-7xl"
          >
            View Reviews
          </h2>
          <div class="flex flex-wrap justify-center gap-8">
            <!--
            <BookReview
              v-for="i in book.length"
              :key="i"
              title="book[i].title"
              author="book[i].author"
              image="book[i].image"
              rating="book[i].rating"
              review="book[i].review"
            />
            !-->
          </div>
          <div class="mt-10 flex justify-center">
            <button
              class="btn rounded-full text-bold border-none bg-zinc-800 py-1.5 px-8 text-xl text-white transition-all duration-300 hover:-translate-y-1 hover:bg-black hover:shadow-xl"
            >
              Read More Reviews
            </button>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>
<script setup>
import { onMounted } from "vue";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

const books = [];
const reviews = [];
// will import reviews and books from backend

gsap.registerPlugin(ScrollTrigger);
onMounted(() => {
  const heroTimeline = gsap.timeline();
  heroTimeline
    .fromTo(
      "#heroHeading",
      {
        opacity: 0,
        y: 100,
        rotateX: 25,
        transformOrigin: "center bottom",
      },
      {
        opacity: 1,
        y: 0,
        rotateX: 0,
        duration: 1.4,
        ease: "expo.out",
      }
    )
    .from(
      ".heroSubtitle",
      {
        opacity: 0,
        y: 30,
        duration: 0.8,
        ease: "power3.out",
      },
      "-=0.5"
    )
    .fromTo(
      ".browseBtn, .reviewBtn",
      {
        opacity: 0,
        y: 30,
      },
      {
        opacity: 1,
        y: 0,
        stagger: 0.15,
        duration: 0.7,
        ease: "back.out(1.7)",
      }
    )
    .from(
      ".scrollIndicator",
      {
        opacity: 0,
        y: -20,
        duration: 0.8,
      },
      "-=0.3"
    );

  gsap.from(".booksSection", {
    scrollTrigger: {
      trigger: ".booksSection",
      start: "top 75%",
    },
    opacity: 0,
    x: -100,
    duration: 1,
    ease: "power3.out",
  });

  gsap.from(".reviewsSection", {
    scrollTrigger: {
      trigger: ".reviewsSection",
      start: "top 75%",
    },
    opacity: 0,
    x: 100,
    duration: 1,
    ease: "power3.out",
  });

  gsap.to(".scrollIndicator svg", {
    y: 10,
    repeat: -1,
    yoyo: true,
    duration: 0.8,
    ease: "power1.inOut",
  });
  ScrollTrigger.refresh();
});
</script>
