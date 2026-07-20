<template>
  <!--chatgpt styling until figma ver-->
  <div>
    <section class="bg-blue-100">
      <div class="max-w-6xl mx-auto py-28 px-6 text-center">
        <h1 class="text-5xl font-bold mb-6">Student Book Reviews</h1>
        <NuxtLink
          to="/books"
          class="bg-blue-700 text-white px-8 py-3 rounded-lg hover:bg-blue-800 transition"
        >
          Browse Books
        </NuxtLink>
      </div>
    </section>
    <div class="max-w-6xl mx-auto py-16 px-6 grid md:grid-cols-2 gap-10">
      <section>
        <h2 class="text-3xl font-bold mb-8">Featured Books</h2>
        <!--book component-->
      </section>

      <section>
        <h2 class="text-3xl font-bold mb-8">Recent Reviews</h2>
        <!--review component-->
      </section>
    </div>
  </div>
</template>
