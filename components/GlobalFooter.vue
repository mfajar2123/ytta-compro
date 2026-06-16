<template>
  <footer class="bg-blackobsidian text-white pt-16 pb-8 border-t border-darkamethyst">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-12 mb-12">
        
        <!-- Brand -->
        <div class="space-y-4">
          <NuxtLink to="/" class="flex items-center gap-2">
            <img src="/img/home/logo.png" alt="Raja Emas Logo" class="h-10 w-auto" />
            <span class="font-semibold text-2xl tracking-tight text-white font-heading">Raja Emas Indonesia</span>
          </NuxtLink>
          <p class="text-gray-400 max-w-sm">
            {{ siteData.company.tagline }}
          </p>
          <div class="flex space-x-4 pt-4">
            <a href="https://instagram.com/emasmurniasli.id/" target="_blank" rel="noopener noreferrer" class="text-gray-400 hover:text-goldensand transition-colors">
              <span class="sr-only">Instagram</span>
              <Icon name="mdi:instagram" class="text-2xl" />
            </a>
            <a href="https://www.tiktok.com/@emasmurniasli_" target="_blank" rel="noopener noreferrer" class="text-gray-400 hover:text-goldensand transition-colors">
              <span class="sr-only">TikTok</span>
              <Icon name="simple-icons:tiktok" class="text-2xl" />
            </a>
            <a href="https://shopee.co.id/emaindonesia" target="_blank" rel="noopener noreferrer" class="text-gray-400 hover:text-goldensand transition-colors">
              <span class="sr-only">Shopee</span>
              <Icon name="simple-icons:shopee" class="text-2xl" />
            </a>
          </div>
        </div>

        <!-- Quick Links -->
        <div>
          <h3 class="text-goldensand font-semibold text-lg mb-4">Navigasi</h3>
          <ul class="space-y-2">
            <li><NuxtLink to="/" class="text-gray-400 hover:text-white transition-colors">Home</NuxtLink></li>
            <li><NuxtLink to="/products/logam-series" class="text-gray-400 hover:text-white transition-colors">Logam Series</NuxtLink></li>
            <li><NuxtLink to="/products/logam-custom" class="text-gray-400 hover:text-white transition-colors">Logam Custom</NuxtLink></li>
            <li><NuxtLink to="/offline-store" class="text-gray-400 hover:text-white transition-colors">Offline Store</NuxtLink></li>
          </ul>
        </div>

        <!-- Contact Info -->
        <div>
          <h3 class="text-goldensand font-semibold text-lg mb-4">Hubungi Kami</h3>
          <ul class="space-y-4">
            <li class="flex items-start">
              <Icon name="mdi:map-marker" class="text-xl text-goldensand mr-2 mt-1 flex-shrink-0" />
              <span class="text-gray-400">{{ siteData.company.contact.address }}</span>
            </li>
            <li class="flex items-center">
              <Icon name="mdi:phone" class="text-xl text-goldensand mr-2 flex-shrink-0" />
              <span class="text-gray-400">{{ siteData.company.contact.phone }}</span>
            </li>
            <li>
              <a :href="siteData.company.contact.linktree" target="_blank" rel="noopener noreferrer" class="inline-flex items-center text-goldensand hover:text-white transition-colors mt-2">
                Hubungi via Linktree
                <Icon name="mdi:arrow-right" class="ml-1" />
              </a>
            </li>
          </ul>
        </div>
      </div>
      
      <div class="border-t border-gray-800 pt-8 flex flex-col md:flex-row justify-between items-center text-sm text-gray-500">
        <p>&copy; {{ new Date().getFullYear() }} {{ siteData.company.name }}. All rights reserved.</p>
        <div class="mt-4 md:mt-0 space-x-4">
          <NuxtLink to="/privacy-policy" class="hover:text-white transition-colors">Privacy Policy</NuxtLink>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import siteData from '~/data/siteData.json'
</script>
