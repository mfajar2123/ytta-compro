<template>
  <div class="min-h-screen" id="product-page">
    <!-- Header -->
    <section class="hero-section bg-blackobsidian text-white pt-32 pb-24 md:pt-40 md:pb-32 relative overflow-hidden">
      <div class="hero-bg-icon absolute right-0 top-0 opacity-10 transform translate-x-1/4 -translate-y-1/4">
        <Icon name="mdi:diamond-stone" class="text-[400px] text-goldensand" />
      </div>
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
        <div class="max-w-4xl mx-auto">
          <h1 class="hero-title hero-anim opacity-0 translate-y-12 transition-all duration-1000 ease-out text-5xl md:text-7xl font-semibold mb-6 text-goldensand tracking-tight">{{ categoryTitle }}</h1>
          <p class="hero-subtitle hero-anim opacity-0 translate-y-12 transition-all duration-1000 ease-out delay-100 text-xl md:text-2xl text-gray-400">{{ categorySubtitle }}</p>
        </div>
      </div>
    </section>

    <!-- Products Grid -->
    <section class="py-20 md:py-32 relative z-20 -mt-10 group">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative">
        <!-- Navigation Buttons for Slider -->
        <button 
          aria-label="Previous Products"
          @click="scrollSlider('left')"
          class="absolute left-2 md:-left-6 lg:-left-12 top-1/2 -translate-y-1/2 w-14 h-14 md:w-16 md:h-16 rounded-full bg-white/90 backdrop-blur-md border-2 border-goldensand/30 text-goldensand flex items-center justify-center hover:bg-goldensand hover:border-goldensand hover:text-white hover:scale-110 transition-all duration-300 z-30 opacity-0 group-hover:opacity-100 shadow-xl focus:outline-none hidden md:flex"
        >
          <Icon name="mdi:chevron-left" class="text-4xl md:text-5xl" />
        </button>
        <button 
          aria-label="Next Products"
          @click="scrollSlider('right')"
          class="absolute right-2 md:-right-6 lg:-right-12 top-1/2 -translate-y-1/2 w-14 h-14 md:w-16 md:h-16 rounded-full bg-white/90 backdrop-blur-md border-2 border-goldensand/30 text-goldensand flex items-center justify-center hover:bg-goldensand hover:border-goldensand hover:text-white hover:scale-110 transition-all duration-300 z-30 opacity-0 group-hover:opacity-100 shadow-xl focus:outline-none hidden md:flex"
        >
          <Icon name="mdi:chevron-right" class="text-4xl md:text-5xl" />
        </button>

        <div 
          ref="sliderContainer"
          class="product-slider hide-scrollbar snap-x snap-mandatory"
        >
          <div 
            v-for="product in categoryProducts" 
            :key="product.id"
            class="product-card bg-white rounded-3xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-500 border border-gray-100 flex flex-col h-full transform snap-start"
          >
            <div class="relative h-56 md:h-64 flex-shrink-0 overflow-hidden bg-lightamethyst flex items-center justify-center p-6 group/img">
              <NuxtImg :src="product.image" :alt="product.name" class="product-image h-full w-full object-contain rounded-2xl group-hover/img:scale-110 transition-transform duration-700 ease-out" loading="lazy" format="webp" width="600" height="600" />
              <div class="absolute top-6 right-6 bg-goldensand/90 backdrop-blur-sm text-blackobsidian text-sm font-bold px-4 py-2 rounded-full shadow-lg transform translate-y-2 opacity-0 group-hover/img:translate-y-0 group-hover/img:opacity-100 transition-all duration-300">
                {{ product.weight }}
              </div>
            </div>
            <div class="p-6 flex flex-col flex-grow bg-gradient-to-b from-white to-whitedust/50">
              <h3 class="text-xl font-semibold text-blackobsidian mb-2 line-clamp-2 leading-tight">
                {{ product.name }}
              </h3>
              <p class="text-gray-500 text-sm flex-grow line-clamp-3 leading-relaxed">
                {{ product.description }}
              </p>
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
import { computed, onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { useFadeUp } from '~/composables/useFadeUp'
import siteData from '~/data/siteData.json'

useFadeUp()

const route = useRoute()
const category = route.params.category

const categoryTitle = computed(() => {
  if (category === 'logam-series') return 'Logam Series'
  if (category === 'logam-custom') return 'Logam Custom'
  if (category === 'portofolio') return 'Portfolio'
  return 'Produk'
})

const categorySubtitle = computed(() => {
  if (category === 'logam-series') {
    return 'Hadir dengan kemasan eksklusif yang dapat dikustomisasi sesuai kebutuhan personal, perusahaan, maupun acara spesial Anda.'
  }
  if (category === 'logam-custom') {
    return 'Layanan pembuatan logam mulia dengan desain dan bentuk yang sepenuhnya disesuaikan dengan permintaan client baik untuk corporate gift, penghargaan, souvenir premium, dan kebutuhan branding eksklusif.'
  }
  if (category === 'portofolio') {
    return 'Eksplorasi berbagai karya dan mahakarya desain logam mulia yang telah kami ciptakan untuk klien-klien terbaik Raja Emas Indonesia.'
  }
  return `Temukan koleksi eksklusif ${categoryTitle.value} dari Raja Emas Indonesia.`
})

const categoryProducts = computed(() => {
  return siteData.products[category] || []
})

useSeoMeta({
  title: categoryTitle,
  description: categorySubtitle,
  ogTitle: () => `${categoryTitle.value} - Raja Emas Indonesia`,
  ogDescription: categorySubtitle,
  twitterTitle: categoryTitle,
  twitterDescription: categorySubtitle,
})

useHead({
  script: [
    {
      type: 'application/ld+json',
      children: computed(() => JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'ItemList',
        itemListElement: categoryProducts.value.map((product, index) => ({
          '@type': 'ListItem',
          position: index + 1,
          item: {
            '@type': 'Product',
            name: product.name,
            description: product.description,
            image: `https://rajaemasindonesia.co.id${product.image}`
          }
        }))
      }))
    }
  ]
})


const sliderContainer = ref(null)

const scrollSlider = (direction) => {
  if (sliderContainer.value) {
    const scrollAmount = window.innerWidth > 1024 ? sliderContainer.value.clientWidth / 3 : 
                         window.innerWidth > 640 ? sliderContainer.value.clientWidth / 2 : 
                         sliderContainer.value.clientWidth * 0.85;
    sliderContainer.value.scrollBy({
      left: direction === 'left' ? -scrollAmount : scrollAmount,
      behavior: 'smooth'
    })
  }
}

onMounted(() => {
  // Fallback for hero without GSAP
  setTimeout(() => {
    const heroElements = document.querySelectorAll('.hero-anim')
    heroElements.forEach(el => {
      el.classList.remove('opacity-0', 'translate-y-12', 'scale-95')
      el.classList.add('opacity-100', 'translate-y-0', 'scale-100')
    })
  }, 100)
})
</script>

<style scoped>
.product-slider {
  display: grid;
  grid-template-rows: repeat(2, 1fr);
  grid-auto-flow: column;
  overflow-x: auto;
  gap: 1.5rem;
  padding-bottom: 2rem;
}
.product-slider > * {
  width: 100%;
}

@media (max-width: 639px) {
  .product-slider {
    grid-auto-columns: 85%;
  }
}

@media (min-width: 640px) and (max-width: 1023px) {
  .product-slider {
    grid-auto-columns: calc(50% - 0.75rem);
  }
}

@media (min-width: 1024px) {
  .product-slider {
    grid-auto-columns: calc(33.333333% - 1rem);
  }
}

.hide-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.hide-scrollbar::-webkit-scrollbar {
  display: none;
}
</style>
