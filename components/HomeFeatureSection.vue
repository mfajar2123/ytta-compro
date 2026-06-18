<template>
  <section class="py-24 bg-whitedust border-t border-gray-200">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="gsap-fade-up text-4xl md:text-5xl font-semibold mb-4 text-blackobsidian">Mengapa <span class="text-goldensand">Raja Emas?</span></h2>
        <p class="gsap-fade-up text-gray-600 max-w-2xl mx-auto text-lg">Bandingkan dengan tempat lain, Anda akan merasakan bedanya. Proses mudah, transparan, dan harga beli tertinggi.</p>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Featured large card -->
        <div class="gsap-fade-up lg:col-span-2 bg-blackobsidian rounded-[2rem] p-8 md:p-12 shadow-2xl text-white relative overflow-hidden group">
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
        <div v-for="(feature, idx) in siteData.features.slice(1)" :key="'feat-'+idx" class="gsap-fade-up bg-white rounded-[2rem] p-8 shadow-xl border border-goldensand/20 hover:border-goldensand transition-colors group">
          <div class="w-14 h-14 bg-whitedust text-goldensand rounded-xl flex items-center justify-center mb-6 group-hover:bg-goldensand group-hover:text-white transition-colors duration-300">
            <Icon :name="feature.icon" class="text-2xl" />
          </div>
          <h3 class="text-xl font-semibold mb-3 text-blackobsidian">{{ feature.title }}</h3>
          <p class="text-gray-600 font-sans leading-relaxed text-sm">{{ feature.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import siteData from '~/data/siteData.json'
import { useFadeUp } from '~/composables/useFadeUp'

useFadeUp('.gsap-fade-up')
</script>
