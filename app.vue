<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup>
import { useRoute } from 'vue-router'
import siteData from '~/data/siteData.json'

const route = useRoute()
const siteUrl = 'https://rajaemasindonesia.co.id'

useSeoMeta({
  titleTemplate: `%s - ${siteData.company.name}`,
  ogSiteName: siteData.company.name,
  ogType: 'website',
  ogUrl: () => `${siteUrl}${route.path}`,
  ogImage: '/img/home/logo.webp',
  twitterCard: 'summary_large_image',
  twitterImage: '/img/home/logo.webp',
})

useHead({
  link: [
    {
      rel: 'canonical',
      href: () => `${siteUrl}${route.path}`
    }
  ]
})
</script>
