<template>
  <section class="py-24 bg-white relative overflow-hidden border-t border-gray-100">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10 max-w-4xl">
      <div class="text-center mb-16 gsap-fade-up">
        <h2 class="text-3xl md:text-5xl font-semibold mb-6 text-blackobsidian tracking-tight">
          <span class="text-goldensand">Frequently Ask Question</span> (FAQ)
        </h2>
        <p class="text-gray-500 max-w-2xl mx-auto text-lg font-sans">
          Temukan jawaban atas pertanyaan yang paling sering diajukan seputar layanan pembelian, penjualan, dan pengecekan emas di Raja Emas Indonesia.
        </p>
      </div>

      <!-- FAQ Tabs -->
      <div class="flex overflow-x-auto hide-scrollbar gap-4 pb-4 px-4 -mx-4 justify-start md:justify-center mb-10 gsap-fade-up">
        <button 
          v-for="(_, category) in siteData.faqs" 
          :key="category"
          @click="activeCategory = category; activeFaq = null"
          class="px-6 py-2.5 rounded-full font-semibold transition-all duration-300 border-2 text-sm sm:text-base whitespace-nowrap"
          :class="activeCategory === category ? 'bg-goldensand border-goldensand text-white shadow-md' : 'bg-transparent border-gray-200 text-gray-500 hover:border-goldensand hover:text-goldensand'"
        >
          {{ category }}
        </button>
      </div>

      <div class="space-y-4 max-w-4xl mx-auto gsap-fade-up">
        <div 
          v-for="(faq, index) in siteData.faqs[activeCategory]" 
          :key="index"
          class="border border-gray-200 rounded-2xl overflow-hidden transition-all duration-300 bg-white"
          :class="{'ring-1 ring-goldensand shadow-lg': activeFaq === index}"
        >
          <button 
            @click="toggleFaq(index)"
            class="w-full text-left px-6 py-5 flex justify-between items-center focus:outline-none hover:bg-whitedust/50 transition-colors"
          >
            <h3 class="font-semibold text-lg text-blackobsidian pr-8" :class="{'text-goldensand': activeFaq === index}">
              {{ faq.question }}
            </h3>
            <div class="flex-shrink-0 w-8 h-8 rounded-full border flex items-center justify-center transition-all duration-300" :class="activeFaq === index ? 'rotate-180 border-goldensand bg-goldensand text-white' : 'border-gray-300 text-gray-500 bg-white'">
              <Icon name="mdi:chevron-down" class="text-xl" />
            </div>
          </button>
          <div 
            class="overflow-hidden transition-all duration-300 ease-in-out"
            :style="{ maxHeight: activeFaq === index ? '500px' : '0', opacity: activeFaq === index ? 1 : 0 }"
          >
            <div class="px-6 pb-6 pt-2 border-t border-gray-100">
              <p class="text-gray-600 font-sans leading-relaxed">
                {{ faq.answer }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import siteData from '~/data/siteData.json'
import { useFadeUp } from '~/composables/useFadeUp'

const activeCategory = ref(Object.keys(siteData.faqs)[0])
const activeFaq = ref(null)

const toggleFaq = (index) => {
  activeFaq.value = activeFaq.value === index ? null : index
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
