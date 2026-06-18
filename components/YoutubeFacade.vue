<template>
  <div 
    class="relative rounded-3xl overflow-hidden border border-white/10 bg-blackobsidian shadow-2xl w-full aspect-video flex items-center justify-center cursor-pointer group"
    @click="loadVideo"
  >
    <template v-if="!isLoaded">
      <!-- Thumbnail -->
      <NuxtImg 
        :src="`https://img.youtube.com/vi/${videoId}/hqdefault.jpg`" 
        :alt="title"
        class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
        loading="lazy"
        format="webp"
        width="480"
        height="360"
      />
      <!-- Play Button Overlay -->
      <div class="absolute inset-0 bg-black/40 group-hover:bg-black/20 transition-colors duration-300 flex items-center justify-center">
        <div class="w-16 h-16 md:w-20 md:h-20 bg-goldensand rounded-full flex items-center justify-center shadow-[0_0_30px_rgba(211,168,95,0.6)] transform group-hover:scale-110 transition-transform duration-300">
          <Icon name="mdi:play" class="text-4xl md:text-5xl text-blackobsidian translate-x-0.5" />
        </div>
      </div>
    </template>
    
    <template v-else>
      <!-- Actual Iframe loaded on click -->
      <iframe
        :src="`https://www.youtube-nocookie.com/embed/${videoId}?autoplay=1&rel=0`"
        class="absolute inset-0 w-full h-full"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
        :title="title"
      ></iframe>
    </template>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  videoId: {
    type: String,
    required: true
  },
  title: {
    type: String,
    default: 'YouTube Video'
  }
})

const isLoaded = ref(false)

const loadVideo = () => {
  isLoaded.value = true
}
</script>
