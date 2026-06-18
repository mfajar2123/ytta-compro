<template>
  <section class="py-24 md:py-32 bg-whitedust border-b border-gray-200">
    <div class="w-full overflow-hidden">
      <div class="container mx-auto px-4 mb-8 text-center">
        <h3 class="text-xl font-semibold text-gray-500">Telah Dipercaya Oleh:</h3>
      </div>
      <div class="relative flex w-full overflow-hidden group">
        <!-- First Track -->
        <div class="animate-marquee-infinite flex whitespace-nowrap items-center shrink-0">
          <div v-for="i in 8" :key="`p1-${i}`" class="px-8 md:px-12 lg:px-16 flex items-center justify-center">
            <NuxtImg :src="siteData.partners[(i - 1) % siteData.partners.length].logo" :alt="siteData.partners[(i - 1) % siteData.partners.length].name" class="w-32 h-16 sm:w-40 sm:h-20 md:w-48 md:h-24 lg:w-64 lg:h-32 object-contain hover:scale-110 transition-all duration-500 drop-shadow-sm cursor-pointer" loading="lazy" format="webp" width="256" height="128" />
          </div>
        </div>
        <!-- Second Track (Duplicate for infinite loop) -->
        <div class="animate-marquee-infinite flex whitespace-nowrap items-center shrink-0" aria-hidden="true">
          <div v-for="i in 8" :key="`p2-${i}`" class="px-8 md:px-12 lg:px-16 flex items-center justify-center">
            <NuxtImg :src="siteData.partners[(i - 1) % siteData.partners.length].logo" :alt="siteData.partners[(i - 1) % siteData.partners.length].name" class="w-32 h-16 sm:w-40 sm:h-20 md:w-48 md:h-24 lg:w-64 lg:h-32 object-contain hover:scale-110 transition-all duration-500 drop-shadow-sm cursor-pointer" loading="lazy" format="webp" width="256" height="128" />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import siteData from '~/data/siteData.json'
</script>

<style scoped>
.animate-marquee-infinite {
  animation: marquee-infinite 35s linear infinite;
  will-change: transform;
}
.group:hover .animate-marquee-infinite {
  animation-play-state: paused;
}
@keyframes marquee-infinite {
  0% { transform: translateX(0%); }
  100% { transform: translateX(-100%); }
}
</style>
