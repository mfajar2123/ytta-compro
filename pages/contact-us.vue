<template>
  <div class="bg-blackobsidian min-h-screen flex flex-col pt-20 relative overflow-hidden">
    <!-- Centered Content Section -->
    <section class="relative flex-grow flex items-center justify-center py-20">
      
      <!-- Subtle Purple Glow Accent -->
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] md:w-[800px] md:h-[800px] bg-darkamethyst rounded-full blur-[100px] md:blur-[150px] opacity-80 pointer-events-none"></div>

      <!-- Subtle Background Icon (Not AI glow) -->
      <div class="hero-bg-icon absolute right-0 top-0 opacity-5 transform translate-x-1/4 -translate-y-1/4 pointer-events-none">
        <Icon name="mdi:headset" class="text-[600px] text-white" />
      </div>

      <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
        <div class="max-w-4xl mx-auto">
          
          
          <h1 class="hero-title hero-anim opacity-0 translate-y-12 transition-all duration-1000 ease-out text-4xl md:text-6xl lg:text-7xl font-semibold mb-8 tracking-tight leading-tight font-heading text-white">
            Celebrate Every <span class="text-goldensand italic">Achievement</span><br/> with Precious Gold
          </h1>
          
          <p class="hero-subtitle hero-anim opacity-0 translate-y-12 transition-all duration-1000 ease-out delay-100 text-lg md:text-xl text-gray-300 mb-10 font-sans leading-relaxed max-w-3xl mx-auto">
            Hubungi kami melalui WhatsApp atau Linktree untuk mendapatkan konsultasi dan layanan terbaik terkait logam mulia, atau kebutuhan custom gold Anda. Tim Emas Murni Asli / Raja Emas Indonesia siap membantu mewujudkan produk emas yang eksklusif, bernilai, dan berkesan untuk setiap momen spesial, apresiasi, maupun kebutuhan branding perusahaan Anda.
          </p>

          <p class="hero-quote hero-anim opacity-0 translate-y-12 transition-all duration-1000 ease-out delay-200 text-xl md:text-2xl font-medium text-goldensand mb-12 italic font-heading">
            "Wujudkan ide, penghargaan, dan kenangan berharga bersama Raja Emas Indonesia!"
          </p>

          <div class="hero-cta hero-anim opacity-0 translate-y-12 transition-all duration-1000 ease-out delay-300 flex flex-col sm:flex-row justify-center items-center gap-6">
            <!-- WhatsApp Button -->
            <a :href="siteData.company.contact.marketing[0].whatsapp" target="_blank" rel="noopener noreferrer" class="w-full sm:w-auto px-10 py-5 bg-goldensand text-blackobsidian font-bold rounded-full hover:bg-yellow-600 transition-colors duration-300 flex items-center justify-center group font-sans">
              <Icon name="mdi:whatsapp" class="text-2xl mr-3 group-hover:scale-110 transition-transform" />
              <span>WhatsApp Kami</span>
            </a>

            <!-- Linktree Button -->
            <a :href="siteData.company.contact.linktree" target="_blank" rel="noopener noreferrer" class="w-full sm:w-auto px-10 py-5 bg-white text-blackobsidian font-bold rounded-full hover:bg-gray-200 transition-colors duration-300 flex items-center justify-center group font-sans">
              <Icon name="simple-icons:linktree" class="text-xl mr-3 text-goldensand group-hover:scale-110 transition-transform" />
              <span>Kunjungi Linktree</span>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Floating WhatsApp Menu -->
    <div class="fixed bottom-4 right-4 md:bottom-8 md:right-8 z-50 flex flex-col items-end">
      <!-- Popup Menu -->
      <transition 
        enter-active-class="transition duration-300 ease-out"
        enter-from-class="transform translate-y-4 opacity-0 scale-95"
        enter-to-class="transform translate-y-0 opacity-100 scale-100"
        leave-active-class="transition duration-200 ease-in"
        leave-from-class="transform translate-y-0 opacity-100 scale-100"
        leave-to-class="transform translate-y-4 opacity-0 scale-95"
      >
        <div v-show="isWaMenuOpen" class="mb-4 bg-white rounded-2xl shadow-2xl border border-gray-100 overflow-hidden w-64 origin-bottom-right">
          <div class="bg-blackobsidian text-white p-4 text-center border-b border-goldensand/30">
            <h4 class="font-semibold font-heading">Hubungi Marketing</h4>
            <p class="text-xs text-gray-400 mt-1">Pilih admin yang tersedia</p>
          </div>
          <div class="p-2 space-y-1">
            <a 
              v-for="(admin, index) in siteData.company.contact.marketing" 
              :key="index"
              :href="admin.whatsapp" 
              target="_blank" 
              rel="noopener noreferrer" 
              class="flex items-center p-3 hover:bg-whitedust rounded-xl transition-colors group"
            >
              <div class="w-10 h-10 bg-[#25D366]/10 text-[#25D366] rounded-full flex items-center justify-center mr-3 group-hover:bg-[#25D366] group-hover:text-white transition-colors">
                <Icon name="mdi:whatsapp" class="text-xl" />
              </div>
              <span class="font-medium text-blackobsidian text-sm">{{ admin.name }}</span>
            </a>
          </div>
        </div>
      </transition>

      <!-- Main Floating Button -->
      <button 
        @click="isWaMenuOpen = !isWaMenuOpen"
        class="w-16 h-16 bg-[#25D366] text-white rounded-full shadow-[0_4px_20px_rgba(37,211,102,0.4)] flex items-center justify-center hover:bg-[#20bd5a] hover:scale-110 transition-all duration-300 focus:outline-none focus:ring-4 focus:ring-[#25D366]/30"
        :class="{'bg-blackobsidian shadow-xl focus:ring-blackobsidian/30': isWaMenuOpen}"
      >
        <Icon :name="isWaMenuOpen ? 'mdi:close' : 'mdi:whatsapp'" class="text-3xl transition-transform duration-300" :class="{'rotate-90': isWaMenuOpen}" />
      </button>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useFadeUp } from '~/composables/useFadeUp'
import siteData from '~/data/siteData.json'

useFadeUp()

const isWaMenuOpen = ref(false)

useSeoMeta({
  title: 'Hubungi Kami - Layanan & Konsultasi',
  description: 'Hubungi tim marketing Raja Emas Indonesia melalui WhatsApp atau Linktree untuk konsultasi logam mulia, custom gold, souvenir perusahaan, dan pembelian emas murni.',
  ogTitle: 'Hubungi Kami - Layanan & Konsultasi Raja Emas Indonesia',
  ogDescription: 'Hubungi tim marketing Raja Emas Indonesia melalui WhatsApp atau Linktree untuk konsultasi logam mulia, custom gold, souvenir perusahaan, dan pembelian emas murni.',
  twitterTitle: 'Hubungi Kami - Layanan & Konsultasi',
  twitterDescription: 'Hubungi tim marketing Raja Emas Indonesia melalui WhatsApp untuk konsultasi logam mulia dan custom gold.',
})

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
