<template>
  <footer class="bg-blackobsidian text-white pt-16 pb-8 border-t border-darkamethyst">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12 mb-12">
        
        <!-- Brand -->
        <div class="space-y-4">
          <NuxtLink to="/" class="flex items-center gap-2">
            <img src="/img/home/logo.png" alt="Raja Emas Logo" class="h-10 w-auto" width="40" height="40" loading="lazy" />
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

        <!-- Contact CTA -->
        <div class="flex flex-col justify-center items-start md:items-end md:text-right">
          <h3 class="text-goldensand font-semibold text-xl mb-4">Butuh Bantuan?</h3>
          <p class="text-gray-400 mb-6 max-w-sm">
            Tim layanan pelanggan kami siap membantu Anda untuk informasi lebih lanjut mengenai produk dan layanan Raja Emas Indonesia.
          </p>
          <NuxtLink to="/contact-us" class="inline-flex items-center px-6 py-3 bg-goldensand text-white font-semibold rounded-full hover:bg-white hover:text-blackobsidian transition-colors duration-300 shadow-lg">
            Hubungi Kami
            <Icon name="mdi:arrow-right" class="ml-2 text-xl" />
          </NuxtLink>
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
