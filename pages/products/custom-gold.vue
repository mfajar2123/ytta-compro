<template>
  <div id="custom-gold-page">
    <!-- Hero Section -->
    <section class="hero-section relative min-h-screen pt-24 pb-16 flex items-center justify-center bg-darkamethyst text-white overflow-hidden">
      <!-- Background elements replaced with solid non-gradient subtle decorations -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <div class="absolute top-10 left-10 w-32 h-32 bg-goldensand/10 rounded-full"></div>
        <div class="absolute bottom-10 right-20 w-48 h-48 bg-white/5 rounded-full"></div>
        <div class="absolute top-1/2 right-1/4 w-24 h-24 bg-goldensand/10 rounded-full"></div>
      </div>

      <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-8 items-center">
          <div class="max-w-2xl text-center lg:text-left order-2 lg:order-1 mx-auto lg:mx-0">
            <div class="hero-title">
              <span class="inline-block py-1.5 px-4 rounded-full bg-goldensand/10 border border-goldensand/30 text-goldensand text-sm font-semibold tracking-widest uppercase mb-4 hero-anim opacity-0 translate-y-12 transition-all duration-1000 ease-out">
                Mengapa Memilih Kami?
              </span>
              <h1 class="block text-4xl sm:text-5xl lg:text-6xl font-semibold text-white mb-6 tracking-tight leading-tight hero-anim opacity-0 translate-y-12 transition-all duration-1000 ease-out delay-100">
                <span class="text-goldensand">Custom Gold</span> Design
              </h1>
            </div>
            
            <div class="hero-subtitle space-y-4 text-gray-300 text-base sm:text-lg leading-relaxed mb-8">
              <p class="hero-anim opacity-0 translate-y-12 transition-all duration-1000 ease-out delay-200">
                Di <strong class="text-white font-semibold">Raja Emas Indonesia</strong>, kami menghadirkan layanan <strong class="text-white font-semibold">Custom Gold Design</strong> yang memungkinkan setiap logo, simbol, karakter, maupun desain khusus diwujudkan pada emas murni 24 Karat (99,9%) dan request karat lainnya. Dengan teknologi produksi presisi dan pengerjaan yang detail, setiap desain tampil lebih eksklusif, berkarakter, dan memiliki nilai yang lebih dari sekadar logam mulia.
              </p>
              <p class="hero-anim opacity-0 translate-y-12 transition-all duration-1000 ease-out delay-300">
                Emas custom bukan hanya sebuah produk hadiah atau souvenir. Ia menjadi representasi identitas, apresiasi, dan citra yang ingin ditampilkan oleh individu, komunitas, perusahaan, maupun instansi.
              </p>
            </div>
          </div>

          <div class="hero-video hero-anim opacity-0 scale-95 translate-x-12 transition-all duration-1000 ease-out delay-500 order-1 lg:order-2 w-full max-w-2xl mx-auto lg:max-w-none relative group">
            <div class="relative rounded-3xl overflow-hidden border border-white/10 bg-blackobsidian shadow-2xl transform transition-transform duration-700 hover:scale-[1.02] flex items-center justify-center">
              <video 
                src="/vid/LM_REI.mp4" 
                class="w-full h-auto max-h-[60vh] object-contain rounded-2xl"
                autoplay 
                loop 
                muted 
                playsinline
              ></video>
              <div class="absolute inset-0 border border-gray-100 rounded-2xl pointer-events-none"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useFadeUp } from '~/composables/useFadeUp'

useFadeUp()

useSeoMeta({
  title: 'Jasa Pembuatan Custom Gold & Logam Mulia',
  description: 'Layanan Custom Gold Design eksklusif untuk corporate gift, penghargaan, dan souvenir. Wujudkan logo atau desain Anda pada emas murni 24 Karat bersama Raja Emas Indonesia.',
  ogTitle: 'Jasa Pembuatan Custom Gold & Logam Mulia - Raja Emas Indonesia',
  ogDescription: 'Layanan Custom Gold Design eksklusif untuk corporate gift, penghargaan, dan souvenir. Wujudkan logo atau desain Anda pada emas murni 24 Karat bersama Raja Emas Indonesia.',
  twitterTitle: 'Jasa Pembuatan Custom Gold & Logam Mulia',
  twitterDescription: 'Layanan Custom Gold Design eksklusif untuk corporate gift, penghargaan, dan souvenir. Wujudkan logo atau desain Anda pada emas murni 24 Karat.',
})

useHead({
  script: [
    {
      type: 'application/ld+json',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'Service',
        name: 'Custom Gold Design',
        provider: {
          '@type': 'Organization',
          name: 'Raja Emas Indonesia'
        },
        description: 'Layanan pembuatan logam mulia dengan desain custom sesuai permintaan untuk corporate gift, penghargaan, souvenir premium, dan kebutuhan branding eksklusif.'
      })
    }
  ]
})

onMounted(() => {
  // Fallback for hero without GSAP
  setTimeout(() => {
    const heroElements = document.querySelectorAll('.hero-anim')
    heroElements.forEach(el => {
      el.classList.remove('opacity-0', 'translate-y-12', 'translate-x-12', 'scale-95')
      el.classList.add('opacity-100', 'translate-y-0', 'translate-x-0', 'scale-100')
    })
  }, 100)
})
</script>
