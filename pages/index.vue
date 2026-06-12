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

    <!-- Testimonials -->
    <section class="py-24 bg-blackobsidian text-white relative">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl font-semibold mb-4 text-white">Apa Kata Klien Kami</h2>
          <p class="text-gray-400 max-w-2xl mx-auto text-lg">Testimoni dari pelanggan yang telah mempercayakan investasi dan kebutuhan emasnya kepada Raja Emas Indonesia.</p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 lg:gap-8">
          <div v-for="(testi, index) in siteData.testimonials" :key="'testi-'+index" class="testimonial-card bg-white/5 p-2 rounded-3xl border border-white/10 hover:border-goldensand/50 transition-colors transform hover:-translate-y-2 duration-500 shadow-2xl relative group overflow-hidden h-[450px]">
            <div class="absolute inset-0 bg-gradient-to-t from-blackobsidian/90 via-blackobsidian/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 z-10 rounded-3xl pointer-events-none"></div>
            <img :src="testi.image" alt="Customer Review" class="w-full h-full rounded-2xl object-cover relative z-0" loading="lazy" />
            
            <!-- Hover Overlay Content -->
            <div class="absolute bottom-6 left-6 right-6 z-20 translate-y-4 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-500 pointer-events-none flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-lg">
                  <Icon name="simple-icons:shopee" class="text-[#EE4D2D] text-xl" />
                </div>
                <span class="text-white font-semibold font-sans text-sm tracking-wide">Review dari {{ testi.platform }}</span>
              </div>
              <div class="flex text-goldensand drop-shadow-md">
                <Icon v-for="i in 5" :key="'star-'+i" name="mdi:star" class="text-lg" />
              </div>
            </div>
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
import { onMounted } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import siteData from '~/data/siteData.json'

gsap.registerPlugin(ScrollTrigger)

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

  // Scroll Animations
  gsap.utils.toArray('.gsap-fade-up').forEach(element => {
    gsap.fromTo(element, 
      { y: 50, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 1,
        scrollTrigger: {
          trigger: element,
          start: 'top 80%',
          toggleActions: 'play none none reverse'
        }
      }
    )
  })

  gsap.fromTo('.testimonial-card',
    { y: 50, opacity: 0 },
    {
      y: 0,
      opacity: 1,
      duration: 0.8,
      stagger: 0.2,
      scrollTrigger: {
        trigger: '.testimonial-card',
        start: 'top 85%',
      }
    }
  )
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
</style>
