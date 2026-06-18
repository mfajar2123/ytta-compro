<template>
  <section class="py-24 bg-whitedust relative overflow-hidden">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10 mb-12 text-center md:text-left flex flex-col md:flex-row justify-between items-end gap-6">
      <div class="gsap-fade-up">
        <h2 class="text-4xl md:text-5xl font-semibold mb-4 text-blackobsidian">Apa Kata <span class="text-goldensand">Klien Kami</span></h2>
        <p class="text-gray-600 max-w-xl text-lg font-sans">Geser untuk melihat testimoni dari pelanggan yang telah mempercayakan investasi dan kebutuhan emasnya kepada Raja Emas Indonesia.</p>
      </div>
      <div class="gsap-fade-up hidden md:flex gap-4">
        <button aria-label="Previous Review" @click="scrollTesti('left')" class="w-12 h-12 rounded-full border border-goldensand flex items-center justify-center text-goldensand hover:bg-goldensand hover:text-white transition-colors focus:outline-none focus:ring-2 focus:ring-goldensand">
          <Icon name="mdi:chevron-left" class="text-2xl" />
        </button>
        <button aria-label="Next Review" @click="scrollTesti('right')" class="w-12 h-12 rounded-full border border-goldensand flex items-center justify-center text-goldensand hover:bg-goldensand hover:text-white transition-colors focus:outline-none focus:ring-2 focus:ring-goldensand">
          <Icon name="mdi:chevron-right" class="text-2xl" />
        </button>
      </div>
    </div>

    <div class="w-full relative px-4 sm:px-6 lg:px-8 gsap-fade-up">
      <div ref="testiContainer" class="flex overflow-x-auto gap-6 pb-8 snap-x snap-mandatory hide-scrollbar">
        <div v-for="(testi, index) in siteData.testimonials" :key="'testi-'+index" class="min-w-[70vw] sm:min-w-[300px] md:min-w-[350px] snap-center shrink-0 bg-white p-2 rounded-[2rem] border border-gray-100 shadow-xl hover:shadow-2xl transition-all duration-300 relative group h-[350px] sm:h-[400px]">
          <NuxtImg :src="testi.image" :alt="`Testimoni Pelanggan Raja Emas Indonesia di ${testi.platform}`" class="w-full h-full rounded-[1.5rem] object-contain" loading="lazy" format="webp" width="400" height="400" />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import siteData from '~/data/siteData.json'
import { useFadeUp } from '~/composables/useFadeUp'

const testiContainer = ref(null)

const scrollTesti = (direction) => {
  if (testiContainer.value) {
    const scrollAmount = window.innerWidth > 768 ? 450 + 24 : window.innerWidth * 0.85;
    testiContainer.value.scrollBy({
      left: direction === 'left' ? -scrollAmount : scrollAmount,
      behavior: 'smooth'
    })
  }
}

useFadeUp('.gsap-fade-up')
</script>

<style scoped>
.hide-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.hide-scrollbar::-webkit-scrollbar {
  display: none;
}
</style>
