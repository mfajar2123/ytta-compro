import Lenis from 'lenis'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { nextTick } from 'vue'

export default defineNuxtPlugin((nuxtApp) => {
  gsap.registerPlugin(ScrollTrigger)

  const lenis = new Lenis({
    autoRaf: false, // Disable Lenis's internal RAF to use GSAP's ticker instead
    lerp: 0.08,
    orientation: 'vertical',
    gestureOrientation: 'vertical',
    smoothWheel: true,
    wheelMultiplier: 1,
    smoothTouch: false,
    touchMultiplier: 2,
    infinite: false,
  })

  // Synchronize Lenis with GSAP ScrollTrigger
  lenis.on('scroll', ScrollTrigger.update)

  gsap.ticker.add((time) => {
    lenis.raf(time * 1000)
  })

  gsap.ticker.lagSmoothing(0)

  // Clean up ScrollTrigger on page navigation to prevent zombie triggers
  nuxtApp.hook('page:start', () => {
    ScrollTrigger.getAll().forEach(t => t.kill())
  })

  // Integrate with vue-router & refresh ScrollTrigger
  nuxtApp.hook('page:finish', () => {
    lenis.scrollTo(0, { immediate: true })
    nextTick(() => {
      ScrollTrigger.refresh()
    })
  })
})

