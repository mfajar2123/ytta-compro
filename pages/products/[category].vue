<template>
  <div class="min-h-screen" id="product-page">
    <!-- Header -->
    <section class="hero-section bg-blackobsidian text-white pt-32 pb-24 md:pt-40 md:pb-32 relative overflow-hidden">
      <div class="hero-bg-icon absolute right-0 top-0 opacity-10 transform translate-x-1/4 -translate-y-1/4">
        <Icon name="mdi:diamond-stone" class="text-[400px] text-goldensand" />
      </div>
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
        <div class="max-w-4xl mx-auto">
          <h1 class="hero-title text-5xl md:text-7xl font-semibold mb-6 text-goldensand tracking-tight">{{ categoryTitle }}</h1>
          <p class="hero-subtitle text-xl md:text-2xl text-gray-400">Temukan koleksi eksklusif {{ categoryTitle }} dari Raja Emas Indonesia.</p>
        </div>
      </div>
    </section>

    <!-- Products Grid -->
    <section class="py-20 md:py-32 relative z-20 -mt-10">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10 lg:gap-12">
          <div 
            v-for="product in categoryProducts" 
            :key="product.id"
            class="product-card bg-white rounded-3xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-500 border border-gray-100 group flex flex-col h-full transform"
          >
            <div class="relative h-80 flex-shrink-0 overflow-hidden bg-lightamethyst flex items-center justify-center p-8">
              <img :src="product.image" :alt="product.name" class="product-image h-full w-full object-cover rounded-2xl group-hover:scale-110 transition-transform duration-700 ease-out" loading="lazy" width="600" height="600" />
              <div class="absolute top-6 right-6 bg-goldensand/90 backdrop-blur-sm text-blackobsidian text-sm font-bold px-4 py-2 rounded-full shadow-lg transform translate-y-2 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                {{ product.weight }}
              </div>
            </div>
            <div class="p-8 flex flex-col flex-grow bg-gradient-to-b from-white to-whitedust/50">
              <h3 class="text-2xl font-semibold text-blackobsidian mb-4 h-16 overflow-hidden leading-tight" style="display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
                {{ product.name }}
              </h3>
              <p class="text-gray-600 text-base mb-8 flex-grow h-12 overflow-hidden leading-relaxed" style="display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
                {{ product.description }}
              </p>
              
              <button class="w-full py-4 mt-auto bg-blackobsidian text-white rounded-2xl font-bold hover:bg-goldensand hover:text-blackobsidian transition-all duration-300 flex items-center justify-center gap-3 group-hover:-translate-y-1 shadow-md hover:shadow-xl">
                <Icon name="mdi:whatsapp" class="text-2xl" />
                Pesan Sekarang
              </button>
            </div>
          </div>
        </div>
        
        <div v-if="!categoryProducts || categoryProducts.length === 0" class="text-center py-32 bg-white rounded-3xl shadow-sm border border-gray-100 mt-10">
          <Icon name="mdi:package-variant" class="text-6xl text-gray-300 mb-4" />
          <p class="text-2xl text-gray-500 font-medium">Produk tidak ditemukan untuk kategori ini.</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import siteData from '~/data/siteData.json'

gsap.registerPlugin(ScrollTrigger)

const route = useRoute()
const category = route.params.category

const categoryTitle = computed(() => {
  if (category === 'logam-series') return 'Logam Series'
  if (category === 'logam-custom') return 'Logam Custom'
  return 'Produk'
})

useSeoMeta({
  title: categoryTitle.value,
  titleTemplate: '%s - Raja Emas Indonesia',
  description: `Temukan koleksi eksklusif ${categoryTitle.value}.`,
})

const categoryProducts = computed(() => {
  return siteData.products[category] || []
})

onMounted(() => {
  // Hero Animation
  const tl = gsap.timeline()
  
  tl.fromTo('.hero-bg-icon',
    { scale: 0.8, opacity: 0, rotation: -15 },
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

  // Complex Scroll Animation for Cards
  gsap.fromTo('.product-card',
    { 
      y: 100, 
      opacity: 0,
      scale: 0.95
    },
    {
      y: 0,
      opacity: 1,
      scale: 1,
      duration: 1,
      stagger: 0.15,
      ease: 'back.out(1.2)',
      scrollTrigger: {
        trigger: '.grid',
        start: 'top 85%',
      }
    }
  )

  // Parallax effect on scroll
  gsap.to('.hero-section', {
    yPercent: 30,
    ease: "none",
    scrollTrigger: {
      trigger: "#product-page",
      start: "top top",
      end: "bottom top",
      scrub: true
    }
  })
})
</script>
