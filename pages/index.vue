<template>
  <div>
    <!-- Hero Section -->
    <section class="relative min-h-screen flex items-center justify-center bg-blackobsidian overflow-hidden">
      <!-- Background Image with Overlay -->
      <div class="absolute inset-0 z-0">
        <img src="https://images.unsplash.com/photo-1610375461246-83df859d849d?auto=format&fit=crop&q=80&w=2000" alt="Gold Background" class="w-full h-full object-cover opacity-30" fetchpriority="high" />
        <div class="absolute inset-0 bg-gradient-to-b from-blackobsidian/80 via-blackobsidian/50 to-blackobsidian"></div>
      </div>

      <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
        <h1 class="hero-title text-5xl md:text-7xl font-semibold text-white mb-6 tracking-tight">
          <span class="block">Kemilau Emas,</span>
          <span class="block text-goldensand mt-2">Masa Depan Cerah.</span>
        </h1>
        <p class="hero-text text-xl md:text-2xl text-gray-300 max-w-3xl mx-auto mb-10">
          {{ siteData.company.tagline }}
        </p>
        <div class="hero-cta flex flex-col sm:flex-row justify-center items-center gap-4">
          <NuxtLink to="/products/logam-series" class="px-8 py-4 bg-goldensand text-blackobsidian font-bold rounded-full hover:bg-yellow-600 transition-colors duration-300 w-full sm:w-auto text-lg">
            Koleksi Logam Series
          </NuxtLink>
          <NuxtLink to="/offline-store" class="px-8 py-4 border-2 border-goldensand text-goldensand font-bold rounded-full hover:bg-goldensand hover:text-blackobsidian transition-colors duration-300 w-full sm:w-auto text-lg">
            Kunjungi Toko
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- Company Profile / About -->
    <section class="py-24 bg-whitedust">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8">
        <div class="max-w-4xl mx-auto text-center">
          <h2 class="gsap-fade-up text-sm font-semibold text-goldensand tracking-widest uppercase mb-4">Tentang Kami</h2>
          <p class="gsap-fade-up text-2xl md:text-4xl font-light text-blackobsidian leading-relaxed mb-8">
            "{{ siteData.company.about }}"
          </p>
          <div class="gsap-fade-up w-24 h-1 bg-goldensand mx-auto"></div>
        </div>
      </div>
    </section>

    <!-- Partners Marquee -->
    <section class="py-16 bg-white border-y border-gray-200 overflow-hidden">
      <div class="container mx-auto px-4 mb-8 text-center">
        <h3 class="text-xl font-semibold text-gray-500">Telah Dipercaya Oleh:</h3>
      </div>
      <div class="relative w-full flex overflow-x-hidden">
        <div class="animate-marquee whitespace-nowrap flex items-center gap-16 py-4">
          <img v-for="(partner, index) in siteData.partners" :key="'p1-'+index" :src="partner.logo" :alt="partner.name" class="h-16 object-contain grayscale hover:grayscale-0 transition-all duration-300" loading="lazy" width="150" height="80" />
          <!-- Duplicate for infinite loop effect -->
          <img v-for="(partner, index) in siteData.partners" :key="'p2-'+index" :src="partner.logo" :alt="partner.name" class="h-16 object-contain grayscale hover:grayscale-0 transition-all duration-300" loading="lazy" width="150" height="80" />
        </div>
      </div>
    </section>

    <!-- Services / Features Section -->
    <section class="py-24 bg-whitedust border-t border-gray-200">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="gsap-fade-up text-4xl md:text-5xl font-semibold mb-4 text-blackobsidian">Mengapa <span class="text-goldensand">Raja Emas?</span></h2>
          <p class="gsap-fade-up text-gray-600 max-w-2xl mx-auto text-lg">Bandingkan dengan tempat lain, Anda akan merasakan bedanya. Proses mudah, transparan, dan harga beli tertinggi.</p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Featured large card -->
          <div class="feature-card lg:col-span-2 bg-blackobsidian rounded-[2rem] p-8 md:p-12 shadow-2xl text-white relative overflow-hidden group">
            <div class="absolute top-0 right-0 w-64 h-64 bg-goldensand/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2"></div>
            <div class="relative z-10">
              <div class="w-16 h-16 bg-goldensand text-blackobsidian rounded-2xl flex items-center justify-center mb-6">
                <Icon :name="siteData.features[0].icon" class="text-3xl" />
              </div>
              <h3 class="text-3xl font-semibold mb-4 text-goldensand">{{ siteData.features[0].title }}</h3>
              <p class="text-gray-300 text-lg leading-relaxed font-sans max-w-xl">{{ siteData.features[0].description }}</p>
            </div>
          </div>
          
          <!-- Smaller cards -->
          <div v-for="(feature, idx) in siteData.features.slice(1)" :key="'feat-'+idx" class="feature-card bg-white rounded-[2rem] p-8 shadow-xl border border-goldensand/20 hover:border-goldensand transition-colors group">
            <div class="w-14 h-14 bg-whitedust text-goldensand rounded-xl flex items-center justify-center mb-6 group-hover:bg-goldensand group-hover:text-white transition-colors duration-300">
              <Icon :name="feature.icon" class="text-2xl" />
            </div>
            <h3 class="text-xl font-semibold mb-3 text-blackobsidian">{{ feature.title }}</h3>
            <p class="text-gray-600 font-sans leading-relaxed text-sm">{{ feature.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Pricing Section -->
    <section class="py-24 bg-blackobsidian relative overflow-hidden border-t border-darkamethyst">
      <div class="absolute inset-0 z-0">
        <div class="absolute top-1/4 left-0 w-96 h-96 bg-goldensand/5 rounded-full blur-3xl"></div>
        <div class="absolute bottom-0 right-0 w-[500px] h-[500px] bg-darkamethyst/10 rounded-full blur-3xl"></div>
      </div>
      
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="text-center mb-16">
          <h2 class="gsap-fade-up text-4xl md:text-5xl font-semibold mb-4 text-white">Harga Beli Emas <span class="text-goldensand">Hari Ini</span></h2>
          <p class="gsap-fade-up text-gray-400 font-sans text-lg">Update terakhir: <span class="text-goldensand font-semibold">{{ siteData.pricing.lastUpdate }}</span></p>
        </div>

        <div class="flex flex-col lg:flex-row gap-8 items-start">
          <!-- Karat Table (Scrollable vertically) -->
          <div class="gsap-fade-up w-full lg:w-1/2 bg-white/5 backdrop-blur-md border border-white/10 rounded-3xl overflow-hidden shadow-2xl flex flex-col h-[500px]">
            <div class="bg-gradient-to-r from-goldensand to-yellow-600 p-6 text-center shrink-0">
              <h3 class="text-xl font-bold text-blackobsidian uppercase tracking-wider">Kadar Karat</h3>
            </div>
            <div class="p-6 overflow-y-auto custom-scrollbar flex-grow">
              <table class="w-full text-left font-sans text-white border-collapse">
                <thead>
                  <tr class="text-gray-400 text-sm border-b border-white/10">
                    <th class="pb-3 font-medium">Kadar Karat</th>
                    <th class="pb-3 font-medium text-right">Harga per Gram</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(item, index) in siteData.pricing.karat" :key="'karat-'+index" class="border-b border-white/5 hover:bg-white/5 transition-colors">
                    <td class="py-4 font-semibold text-goldensand">{{ item.karat }}</td>
                    <td class="py-4 text-right font-medium tracking-wide">{{ item.price }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Logam Mulia Table -->
          <div class="gsap-fade-up w-full lg:w-1/2 bg-white/5 backdrop-blur-md border border-white/10 rounded-3xl overflow-hidden shadow-2xl flex flex-col h-[500px]">
            <div class="bg-gradient-to-r from-gray-700 to-blackobsidian p-6 text-center border-b border-goldensand/30 shrink-0">
              <h3 class="text-xl font-bold text-goldensand uppercase tracking-wider">Logam Mulia (S)</h3>
            </div>
            <div class="p-6 overflow-y-auto custom-scrollbar flex-grow">
              <table class="w-full text-left font-sans text-white border-collapse">
                <thead>
                  <tr class="text-gray-400 text-sm border-b border-white/10">
                    <th class="pb-3 font-medium">Jenis</th>
                    <th class="pb-3 font-medium">Kadar</th>
                    <th class="pb-3 font-medium text-right">Harga / Gr</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(item, index) in siteData.pricing.logamMulia" :key="'lm-'+index" class="border-b border-white/5 hover:bg-white/5 transition-colors">
                    <td class="py-4">
                      <span class="block font-semibold text-white">{{ item.name }}</span>
                      <span v-if="item.karat !== '-'" class="text-xs text-goldensand">{{ item.karat }}</span>
                    </td>
                    <td class="py-4 text-gray-400">{{ item.purity }}</td>
                    <td class="py-4 text-right font-medium text-goldensand">{{ item.price }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials (Swipeable Carousel) -->
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
            <img :src="testi.image" alt="Customer Review" class="w-full h-full rounded-[1.5rem] object-cover" loading="lazy" />
          </div>
        </div>
      </div>
    </section>

    <!-- Add Review External Link CTA -->
    <section class="py-24 bg-goldensand relative overflow-hidden">
      <!-- Decorative background element -->
      <div class="absolute inset-0 opacity-10 pointer-events-none" style="background-image: radial-gradient(circle at center, #ffffff 1px, transparent 1px); background-size: 24px 24px;"></div>
      
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="bg-blackobsidian text-white rounded-[2.5rem] p-10 md:p-16 lg:p-20 text-center max-w-5xl mx-auto shadow-2xl border border-white/5 relative overflow-hidden group">
          
          <!-- Inner Glow -->
          <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[200%] md:w-full h-1/2 bg-goldensand/20 blur-[100px] pointer-events-none"></div>

          <div class="relative z-10 max-w-3xl mx-auto">
            <h2 class="gsap-fade-up text-3xl md:text-5xl lg:text-6xl font-semibold mb-6 leading-tight">
              Bagikan <span class="text-goldensand">Pengalaman Berharga</span> Anda
            </h2>
            <p class="gsap-fade-up text-lg md:text-xl text-gray-300 mb-12 font-sans leading-relaxed">
              Testimoni Anda sangat berarti bagi kami. Bantu calon investor lainnya membuat keputusan yang tepat dengan membagikan pengalaman transaksi emas Anda di platform favorit Indonesia.
            </p>
            
            <div class="gsap-fade-up flex flex-col sm:flex-row justify-center gap-6">
              <!-- Google CTA -->
              <a href="#" class="flex items-center justify-center gap-4 bg-white text-blackobsidian px-8 py-4 rounded-2xl font-semibold hover:bg-gray-50 transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_10px_40px_-10px_rgba(255,255,255,0.3)] group/btn">
                <Icon name="logos:google-icon" class="text-2xl group-hover/btn:scale-110 transition-transform" />
                <div class="text-left">
                  <span class="block text-xs text-gray-500 font-sans uppercase tracking-wider mb-0.5">Ulas Kami Di</span>
                  <span class="block text-lg font-heading">Google Maps</span>
                </div>
              </a>

              <!-- Shopee CTA -->
              <a href="#" class="flex items-center justify-center gap-4 bg-[#EE4D2D] text-white px-8 py-4 rounded-2xl font-semibold hover:bg-[#d74226] transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_10px_40px_-10px_rgba(238,77,45,0.4)] group/btn">
                <Icon name="simple-icons:shopee" class="text-3xl group-hover/btn:scale-110 transition-transform" />
                <div class="text-left">
                  <span class="block text-xs text-white/80 font-sans uppercase tracking-wider mb-0.5">Ulas Kami Di</span>
                  <span class="block text-lg font-heading">Shopee ID</span>
                </div>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import siteData from '~/data/siteData.json'

gsap.registerPlugin(ScrollTrigger)

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

useSeoMeta({
  title: 'Home',
  titleTemplate: '%s - Raja Emas Indonesia',
  description: siteData.company.about,
  ogTitle: 'Raja Emas Indonesia - Investasi Emas Terpercaya',
  ogDescription: siteData.company.tagline,
})

onMounted(() => {
  // Hero Animations
  const tl = gsap.timeline()
  
  tl.fromTo('.hero-title .block', 
    { y: 100, opacity: 0 },
    { y: 0, opacity: 1, duration: 1, stagger: 0.2, ease: 'power4.out', delay: 0.2 }
  )
  .fromTo('.hero-text',
    { y: 30, opacity: 0 },
    { y: 0, opacity: 1, duration: 0.8, ease: 'power3.out' },
    "-=0.5"
  )
  .fromTo('.hero-cta',
    { y: 30, opacity: 0 },
    { y: 0, opacity: 1, duration: 0.8, ease: 'power3.out' },
    "-=0.6"
  )

  // Scroll Animations for generic fade up elements
  gsap.set('.gsap-fade-up', { y: 50, opacity: 0 })
  ScrollTrigger.batch('.gsap-fade-up', {
    onEnter: batch => gsap.to(batch, {
      opacity: 1, 
      y: 0, 
      duration: 0.8,
      stagger: 0.1, 
      ease: 'power2.out',
      overwrite: true
    }),
    start: 'top 90%',
    once: true // Animate only once to save GPU memory on scroll
  })

  // Feature cards optimized batch animation
  gsap.set('.feature-card', { y: 50, opacity: 0 })
  ScrollTrigger.batch('.feature-card', {
    onEnter: batch => gsap.to(batch, {
      opacity: 1, 
      y: 0, 
      duration: 0.8,
      stagger: 0.15, 
      ease: 'power2.out',
      overwrite: true
    }),
    start: 'top 90%',
    once: true
  })
})
</script>

<style scoped>
.animate-marquee {
  animation: marquee 25s linear infinite;
}

@keyframes marquee {
  0% { transform: translateX(0%); }
  100% { transform: translateX(-50%); }
}

/* Custom Scrollbar for pricing table */
.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.02);
  border-radius: 10px;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: rgba(211, 168, 95, 0.3); /* goldensand with opacity */
  border-radius: 10px;
}
.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: rgba(211, 168, 95, 0.8);
}

/* Hide scrollbar for carousel but keep functionality */
.hide-scrollbar {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}
.hide-scrollbar::-webkit-scrollbar {
  display: none; /* Chrome, Safari and Opera */
}
</style>
