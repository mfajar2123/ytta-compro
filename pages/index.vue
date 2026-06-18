<template>
  <div>
    <!-- Hero Section -->
    <section class="relative min-h-screen pt-24 pb-16 flex items-center justify-center bg-blackobsidian overflow-hidden">
      <!-- Background Elements -->
      <div class="absolute inset-0 z-0 pointer-events-none">
        <div class="absolute top-0 right-0 w-1/2 h-1/2 bg-goldensand/10 rounded-full blur-[150px] translate-x-1/4 -translate-y-1/4"></div>
        <div class="absolute bottom-0 left-0 w-1/2 h-1/2 bg-darkamethyst/10 rounded-full blur-[150px] -translate-x-1/4 translate-y-1/4"></div>
      </div>

      <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-8 items-center">
          <!-- Text Content -->
          <div class="max-w-2xl text-center lg:text-left order-2 lg:order-1 mx-auto lg:mx-0">
            <div class="hero-title">
              <h1 class="block hero-anim opacity-0 translate-y-12 transition-all duration-1000 ease-out text-4xl sm:text-5xl lg:text-6xl font-semibold text-white mb-4 tracking-tight leading-tight">
                About <br class="hidden lg:block"/>Emas Murni Asli
              </h1>
              <h2 class="block hero-anim opacity-0 translate-y-12 transition-all duration-1000 ease-out delay-100 text-xl sm:text-2xl lg:text-3xl text-goldensand font-medium mb-6 lg:mb-8 leading-snug">
                Exclusive Gifts for Meaningful Moments
              </h2>
            </div>
            
            <div class="hero-text space-y-4 text-gray-400 text-base sm:text-lg leading-relaxed mb-8 sm:mb-10">
              <p class="hero-anim opacity-0 translate-y-12 transition-all duration-1000 ease-out delay-200">
                <strong class="text-white font-medium">PT Emas Murni Asli</strong> adalah penyedia logam mulia 24 Karat (99,99%) yang dapat digunakan untuk hadiah (gift), apresiasi, penghargaan, souvenir, dan investasi. Melalui brand <strong class="text-white font-medium">Raja Emas Indonesia</strong>, kami menghadirkan berbagai pilihan <strong class="text-white font-medium">emas batangan</strong> serta <strong class="text-white font-medium">layanan custom</strong> yang dapat disesuaikan dengan kebutuhan individu, komunitas, perusahaan, maupun instansi.
              </p>
              <p class="hero-anim opacity-0 translate-y-12 transition-all duration-1000 ease-out delay-300">
                Dengan mengutamakan kualitas, desain eksklusif, dan layanan profesional, kami membantu menciptakan hadiah emas yang tidak hanya berkesan, tetapi juga memiliki nilai yang bertahan dan terus berkembang dari waktu ke waktu.
              </p>
            </div>

            <!-- CTAs -->
            <div class="hero-cta flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4">
              <NuxtLink to="/products/logam-series" class="hero-anim opacity-0 translate-y-12 transition-all duration-1000 ease-out delay-500 w-full sm:w-auto px-8 py-4 bg-goldensand text-blackobsidian font-bold rounded-full hover:bg-yellow-500 hover:shadow-[0_0_20px_rgba(211,168,95,0.4)] hover:-translate-y-1 text-center">
                Koleksi Logam Series
              </NuxtLink>
              <NuxtLink to="/offline-store" class="hero-anim opacity-0 translate-y-12 transition-all duration-1000 ease-out delay-[600ms] w-full sm:w-auto px-8 py-4 bg-transparent border-2 border-white/20 text-white font-bold rounded-full hover:bg-white/5 hover:border-white/40 hover:-translate-y-1 text-center">
                Hubungi Kami
              </NuxtLink>
            </div>
          </div>

          <!-- Video Container -->
          <div class="hero-video hero-anim opacity-0 scale-95 translate-x-12 transition-all duration-1000 ease-out delay-300 order-1 lg:order-2 w-full max-w-2xl mx-auto lg:max-w-none relative group">
            <div class="absolute -inset-4 bg-gradient-to-tr from-goldensand/40 via-transparent to-darkamethyst/40 rounded-[2.5rem] blur-2xl opacity-50 group-hover:opacity-80 transition-opacity duration-700"></div>
            <!-- Use YoutubeFacade instead of raw iframe to save 2MB FCP -->
            <YoutubeFacade videoId="_DMsSlzT9T0" title="Raja Emas Indonesia Corporate Video" />
          </div>
        </div>
      </div>
    </section>

    <!-- About Slider -->
    <section 
      class="relative w-full h-full overflow-hidden bg-blackobsidian group"
      @touchstart="handleTouchStart"
      @touchend="handleTouchEnd"
    >
      <div 
        class="flex transition-transform duration-700 ease-in-out aspect-[16/9] sm:aspect-video md:aspect-auto md:h-screen"
        :style="{ transform: `translateX(-${currentSlide * 100}%)` }"
      >
        <div 
          v-for="(img, idx) in siteData.heroSlider" 
          :key="'slide-'+idx"
          class="w-full h-full flex-shrink-0 relative flex items-center justify-center bg-blackobsidian"
        >
          <NuxtImg :src="`/img/home/slider/${img}`" :alt="`Promo dan Layanan Raja Emas Indonesia ${idx + 1}`" class="w-full h-full object-cover object-top" :loading="idx === 0 ? 'eager' : 'lazy'" :fetchpriority="idx === 0 ? 'high' : 'auto'" :preload="idx === 0" format="webp" width="1920" height="1080" />
        </div>
      </div>
      
      <!-- Navigation Buttons -->
      <button 
        aria-label="Previous Slide"
        @click="prevSlide"
        class="absolute left-4 md:left-8 top-1/2 -translate-y-1/2 w-12 h-12 md:w-14 md:h-14 rounded-full bg-black/40 backdrop-blur-md border-2 border-white/20 text-white flex items-center justify-center hover:bg-goldensand hover:border-goldensand hover:scale-110 transition-all duration-300 z-10 opacity-0 group-hover:opacity-100 shadow-xl focus:outline-none"
      >
        <Icon name="mdi:chevron-left" class="text-3xl md:text-4xl" />
      </button>
      <button 
        aria-label="Next Slide"
        @click="nextSlide"
        class="absolute right-4 md:right-8 top-1/2 -translate-y-1/2 w-12 h-12 md:w-14 md:h-14 rounded-full bg-black/40 backdrop-blur-md border-2 border-white/20 text-white flex items-center justify-center hover:bg-goldensand hover:border-goldensand hover:scale-110 transition-all duration-300 z-10 opacity-0 group-hover:opacity-100 shadow-xl focus:outline-none"
      >
        <Icon name="mdi:chevron-right" class="text-3xl md:text-4xl" />
      </button>

      <!-- Indicators -->
      <div class="absolute bottom-6 md:bottom-10 left-1/2 -translate-x-1/2 flex space-x-3 md:space-x-4 z-10">
        <button 
          v-for="(_, idx) in siteData.heroSlider" 
          :key="'dot-'+idx"
          @click="currentSlide = idx"
          aria-label="Go to slide"
          class="h-2 md:h-2.5 rounded-full transition-all duration-300 focus:outline-none shadow-lg"
          :class="currentSlide === idx ? 'bg-goldensand w-8 md:w-12' : 'bg-white/50 hover:bg-white w-2 md:w-2.5'"
        ></button>
      </div>
    </section>

    <!-- Lazy Loaded Sections below the fold -->
    <LazyHomePartnerSection />
    <LazyHomeFeatureSection />
    <LazyHomeTestimonialSection />
    <LazyHomeFaqSection />

  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import siteData from '~/data/siteData.json'

// Slider Logic
const currentSlide = ref(0)
const nextSlide = () => { currentSlide.value = (currentSlide.value + 1) % siteData.heroSlider.length }
const prevSlide = () => { currentSlide.value = currentSlide.value === 0 ? siteData.heroSlider.length - 1 : currentSlide.value - 1 }

const touchStartX = ref(0)
const touchEndX = ref(0)

const handleTouchStart = (e) => { touchStartX.value = e.changedTouches[0].screenX }
const handleTouchEnd = (e) => {
  touchEndX.value = e.changedTouches[0].screenX
  const swipeThreshold = 50
  if (touchEndX.value < touchStartX.value - swipeThreshold) nextSlide()
  if (touchEndX.value > touchStartX.value + swipeThreshold) prevSlide()
}

useSeoMeta({
  title: 'Home',
  titleTemplate: 'Raja Emas Indonesia - Jual Beli Logam Mulia & Custom Gold',
  description: siteData.company.about,
  ogTitle: 'Raja Emas Indonesia - Jual Beli Logam Mulia & Custom Gold',
  ogDescription: siteData.company.about,
  twitterTitle: 'Raja Emas Indonesia - Jual Beli Logam Mulia & Custom Gold',
  twitterDescription: siteData.company.about,
})

useHead({
  script: [
    {
      type: 'application/ld+json',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'Organization',
        name: siteData.company.name,
        url: 'https://rajaemasindonesia.co.id',
        logo: 'https://rajaemasindonesia.co.id/img/home/logo.webp',
        description: siteData.company.about,
        contactPoint: {
          '@type': 'ContactPoint',
          telephone: siteData.company.contact.phone,
          contactType: 'customer service'
        }
      })
    }
  ]
})

onMounted(() => {
  // Simple Hero Animation Trigger without GSAP
  setTimeout(() => {
    const heroElements = document.querySelectorAll('.hero-anim')
    heroElements.forEach(el => {
      el.classList.remove('opacity-0', 'translate-y-12', 'translate-x-12', 'scale-95')
      el.classList.add('opacity-100', 'translate-y-0', 'translate-x-0', 'scale-100')
    })
  }, 100)
})
</script>
