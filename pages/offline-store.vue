<template>
  <div class="bg-whitedust min-h-screen" id="store-page">
    <!-- Header -->
    <section class="hero-section bg-blackobsidian text-white pt-32 pb-24 md:pt-40 md:pb-32 relative overflow-hidden">
      <div class="hero-bg-icon absolute right-0 top-0 opacity-10 transform translate-x-1/4 -translate-y-1/4">
        <Icon name="mdi:map-marker-radius" class="text-[400px] text-goldensand" />
      </div>
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="max-w-4xl">
          <h1 class="hero-title text-5xl md:text-7xl font-semibold mb-6 text-white tracking-tight">Our <span class="text-goldensand">Offline Store</span></h1>
          <p class="hero-subtitle text-xl md:text-2xl text-gray-400">Store Raja Emas Indonesia telah tersebar di 70 lokasi di seluruh Indonesia. Kunjungi store terdekat di kotamu untuk cek langsung keaslian logam mulia atau emas custom menggunakan mesin XRF dengan hasil akurat 100%.</p>
        </div>
      </div>
    </section>

    <!-- Search Bar -->
    <section class="relative z-30 -mt-10 mb-10">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8">
        <div class="max-w-4xl mx-auto bg-white rounded-full p-2 shadow-2xl border border-goldensand/20 flex items-center transform transition-transform hover:scale-[1.02] duration-300">
          <div class="pl-4 pr-2 sm:pl-6 sm:pr-4">
            <Icon name="mdi:magnify" class="text-3xl text-goldensand" />
          </div>
          <input 
            v-model="searchQuery"
            type="text" 
            placeholder="Cari lokasi cabang berdasarkan kota atau area (misal: Jakarta, Bandung, Serang)..."
            class="w-full py-4 bg-transparent text-lg focus:outline-none font-sans text-blackobsidian placeholder-gray-400"
          >
          <button v-if="searchQuery" @click="searchQuery = ''" class="pr-4 pl-2 sm:pr-6 sm:pl-4 text-gray-400 hover:text-goldensand transition-colors">
            <Icon name="mdi:close-circle" class="text-2xl" />
          </button>
        </div>
      </div>
    </section>

    <!-- Main Content -->
    <section class="pb-20 md:pb-32 relative z-20">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8">
        
        <TransitionGroup name="list" tag="div" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 lg:gap-10 relative">
          <div 
            v-for="(store, index) in filteredStores" 
            :key="store.id"
            class="store-card bg-white rounded-3xl shadow-lg hover:shadow-2xl transition-all duration-500 border border-gray-100 overflow-hidden flex flex-col h-full"
          >
            <!-- Decorative Header -->
            <div class="h-4 bg-gradient-to-r from-goldensand to-yellow-600"></div>
            
            <div class="p-8 lg:p-10 flex-grow flex flex-col relative">
              <div class="absolute top-8 right-8 text-whitedust opacity-50">
                <span class="text-5xl md:text-6xl font-bold italic font-sans">{{ String(index + 1).padStart(2, '0') }}</span>
              </div>
              
              <h3 class="text-2xl font-semibold text-blackobsidian mb-8 pr-12 relative z-10">{{ store.name }}</h3>
              
              <div class="space-y-6 mb-10 flex-grow relative z-10">
                <div class="flex items-start group">
                  <div class="bg-lightamethyst p-2 rounded-xl mr-4 text-darkamethyst group-hover:bg-goldensand group-hover:text-white transition-colors duration-300">
                    <Icon name="mdi:map-marker" class="text-xl" />
                  </div>
                  <p class="text-gray-600 text-sm leading-relaxed mt-1 font-sans">{{ store.address }}</p>
                </div>
                
                <div class="flex items-start group">
                  <div class="bg-lightamethyst p-2 rounded-xl mr-4 text-darkamethyst group-hover:bg-goldensand group-hover:text-white transition-colors duration-300">
                    <Icon name="mdi:phone" class="text-xl" />
                  </div>
                  <p class="text-gray-600 text-sm font-medium mt-1 font-sans">{{ store.phone }}</p>
                </div>
                
                <div class="flex items-start group">
                  <div class="bg-lightamethyst p-2 rounded-xl mr-4 text-darkamethyst group-hover:bg-goldensand group-hover:text-white transition-colors duration-300">
                    <Icon name="mdi:clock-outline" class="text-xl" />
                  </div>
                  <div class="mt-1 font-sans">
                    <p class="text-gray-600 text-sm font-medium">{{ store.hours }}</p>
                    <div class="inline-block mt-2 px-3 py-1 bg-green-100 text-green-700 text-xs font-bold rounded-full">
                      {{ store.note }}
                    </div>
                  </div>
                </div>
              </div>

              <div class="mt-auto relative z-10">
                <a :href="store.mapCoordinates" target="_blank" rel="noopener noreferrer" class="w-full py-4 bg-whitedust text-blackobsidian rounded-2xl font-bold hover:bg-goldensand hover:text-white transition-all duration-300 flex items-center justify-center gap-2 group font-sans">
                  <Icon name="mdi:map" class="text-xl group-hover:scale-110 transition-transform" />
                  Lihat Peta Arah
                </a>
              </div>
            </div>
          </div>
        </TransitionGroup>

        <!-- No Results -->
        <div v-if="filteredStores.length === 0" class="text-center py-24 bg-white rounded-3xl border border-gray-100 shadow-sm mt-8 mx-auto max-w-2xl transform transition-all">
          <div class="w-24 h-24 bg-whitedust rounded-full flex items-center justify-center mx-auto mb-6">
            <Icon name="mdi:map-search-outline" class="text-5xl text-goldensand" />
          </div>
          <h3 class="text-3xl font-semibold text-blackobsidian mb-4">Lokasi Tidak Ditemukan</h3>
          <p class="text-gray-500 font-sans text-lg">Kami belum memiliki cabang di area <strong>"{{ searchQuery }}"</strong>. <br/>Silakan coba kota atau kata kunci lain.</p>
        </div>

      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import siteData from '~/data/siteData.json'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

const searchQuery = ref('')

const filteredStores = computed(() => {
  const query = searchQuery.value.toLowerCase().trim()
  if (!query) return siteData.stores
  
  return siteData.stores.filter(store => {
    return store.name.toLowerCase().includes(query) || store.address.toLowerCase().includes(query)
  })
})

useSeoMeta({
  title: 'Offline Store',
  titleTemplate: '%s - Raja Emas Indonesia',
  description: 'Kunjungi cabang Raja Emas Indonesia terdekat untuk layanan langsung.',
})

onMounted(() => {
  const tl = gsap.timeline()
  
  tl.fromTo('.hero-bg-icon',
    { scale: 0.8, opacity: 0, rotation: 15 },
    { scale: 1, opacity: 0.1, rotation: 0, duration: 1.5, ease: 'power3.out' }
  )
  .fromTo('.hero-title',
    { y: 50, opacity: 0 },
    { y: 0, opacity: 1, duration: 1, ease: 'power3.out' },
    "-=1"
  )
  .fromTo('.hero-subtitle',
    { y: 30, opacity: 0 },
    { y: 0, opacity: 1, duration: 0.8, ease: 'power3.out' },
    "-=0.6"
  )

  // OPTIMIZATION: Use ScrollTrigger.batch for large lists (68 items)
  // This animates cards in chunks as they enter the viewport, rather than all at once
  gsap.set('.store-card', { y: 50, opacity: 0 })
  
  ScrollTrigger.batch('.store-card', {
    interval: 0.1,
    batchMax: 6,
    onEnter: batch => gsap.to(batch, {
      opacity: 1, 
      y: 0, 
      duration: 0.6,
      stagger: 0.1, 
      ease: 'power2.out',
      overwrite: true
    }),
    start: 'top 95%',
  })

  // Parallax effect on scroll
  gsap.to('.hero-section', {
    yPercent: 30,
    ease: "none",
    scrollTrigger: {
      trigger: "#store-page",
      start: "top top",
      end: "bottom top",
      scrub: true
    }
  })
})
</script>

<style scoped>
/* List transitions */
.list-move,
.list-enter-active,
.list-leave-active {
  transition: all 0.5s cubic-bezier(0.55, 0, 0.1, 1);
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(30px) scale(0.95);
}

.list-leave-active {
  position: absolute;
  visibility: hidden;
}
</style>
