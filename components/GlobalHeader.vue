<template>
  <header
    ref="headerRef"
    class="fixed top-0 left-0 w-full z-50 transition-colors duration-300"
    :class="[isScrolled || route.path !== '/' ? 'bg-blackobsidian/95 backdrop-blur-md shadow-lg' : 'bg-transparent']"
  >
    <div class="container mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        <!-- Logo -->
        <div class="flex-shrink-0 flex items-center">
          <NuxtLink to="/" class="flex items-center gap-2">
            <Icon name="mdi:gold" class="text-3xl text-goldensand" />
            <span class="font-semibold text-xl tracking-tight text-white font-heading">
              Raja Emas
            </span>
          </NuxtLink>
        </div>

        <!-- Desktop Navigation -->
        <nav class="hidden md:flex space-x-8 items-center">
          <NuxtLink to="/" class="nav-link text-white/90 hover:text-goldensand" :class="[isScrolled || route.path !== '/' ? 'text-white' : 'text-white/90']">
            Home
          </NuxtLink>

          <!-- Dropdown -->
          <div class="relative group">
            <button class="nav-link flex items-center gap-1 text-white/90 hover:text-goldensand" :class="[isScrolled || route.path !== '/' ? 'text-white' : 'text-white/90']">
              Product
              <Icon name="mdi:chevron-down" class="text-lg transition-transform group-hover:rotate-180" />
            </button>
            <div class="absolute left-0 mt-2 w-48 rounded-md shadow-lg bg-blackobsidian ring-1 ring-goldensand/20 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 transform origin-top-left scale-95 group-hover:scale-100 border border-darkamethyst z-50">
              <div class="py-1" role="menu" aria-orientation="vertical" aria-labelledby="options-menu">
                <NuxtLink to="/products/logam-series" class="block px-4 py-3 text-sm text-gray-300 hover:bg-darkamethyst hover:text-goldensand" role="menuitem">
                  Logam Series
                </NuxtLink>
                <NuxtLink to="/products/logam-custom" class="block px-4 py-3 text-sm text-gray-300 hover:bg-darkamethyst hover:text-goldensand" role="menuitem">
                  Logam Custom
                </NuxtLink>
              </div>
            </div>
          </div>

          <NuxtLink to="/offline-store" class="nav-link text-white/90 hover:text-goldensand" :class="[isScrolled || route.path !== '/' ? 'text-white' : 'text-white/90']">
            Offline Store
          </NuxtLink>
          
          <a :href="siteData.company.contact.linktree" target="_blank" rel="noopener noreferrer" class="ml-4 inline-flex items-center justify-center px-6 py-2 border border-transparent rounded-full shadow-sm text-sm font-medium text-blackobsidian bg-goldensand hover:bg-yellow-600 transition-colors duration-300">
            Contact Us
          </a>
        </nav>

        <!-- Mobile menu button -->
        <div class="md:hidden flex items-center">
          <button aria-label="Toggle Mobile Menu" @click="isMobileMenuOpen = !isMobileMenuOpen" class="inline-flex items-center justify-center p-2 rounded-md focus:outline-none text-white">
            <Icon :name="isMobileMenuOpen ? 'mdi:close' : 'mdi:menu'" class="text-3xl" />
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Menu -->
    <div v-show="isMobileMenuOpen" class="md:hidden bg-blackobsidian text-white border-t border-darkamethyst max-h-[calc(100vh-5rem)] overflow-y-auto">
      <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
        <NuxtLink to="/" class="block px-3 py-2 rounded-md text-base font-medium hover:text-goldensand hover:bg-darkamethyst" @click="isMobileMenuOpen = false">Home</NuxtLink>
        
        <div class="px-3 py-2 text-base font-medium text-gray-400">Product</div>
        <NuxtLink to="/products/logam-series" class="block pl-6 pr-3 py-2 rounded-md text-sm font-medium text-gray-300 hover:text-goldensand hover:bg-darkamethyst" @click="isMobileMenuOpen = false">- Logam Series</NuxtLink>
        <NuxtLink to="/products/logam-custom" class="block pl-6 pr-3 py-2 rounded-md text-sm font-medium text-gray-300 hover:text-goldensand hover:bg-darkamethyst" @click="isMobileMenuOpen = false">- Logam Custom</NuxtLink>

        
        <NuxtLink to="/offline-store" class="block px-3 py-2 rounded-md text-base font-medium hover:text-goldensand hover:bg-darkamethyst" @click="isMobileMenuOpen = false">Offline Store</NuxtLink>
        
        <a :href="siteData.company.contact.linktree" target="_blank" rel="noopener noreferrer" class="block px-3 py-2 mt-4 rounded-md text-base font-medium text-center bg-goldensand text-blackobsidian">
          Contact Us
        </a>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'
import siteData from '~/data/siteData.json'

const route = useRoute()
const isScrolled = ref(false)
const isMobileMenuOpen = ref(false)
const headerRef = ref(null)

const handleScroll = () => {
  isScrolled.value = window.scrollY > 20
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.nav-link {
  @apply font-medium text-base transition-colors duration-200;
}
</style>
