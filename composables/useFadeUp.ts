import { onMounted, onUnmounted } from 'vue'

export const useFadeUp = (selector = '.gsap-fade-up, .store-card, .product-card, .feature-card, .testimonial-card') => {
  let observer: IntersectionObserver | null = null

  onMounted(() => {
    // Delay initialization slightly to ensure DOM is ready and not block main thread
    setTimeout(() => {
      const elements = document.querySelectorAll(selector)
      if (elements.length === 0) return

      // Terapkan state awal menggunakan class utilitas Tailwind
      elements.forEach(el => {
        el.classList.add('opacity-0', 'translate-y-12', 'transition-all', 'duration-[800ms]', 'ease-out')
      })

      let delay = 0
      let lastTime = Date.now()

      observer = new IntersectionObserver((entries) => {
        const now = Date.now()
        // Reset stagger delay if this is a new scroll batch
        if (now - lastTime > 200) {
          delay = 0
        }
        lastTime = now

        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const target = entry.target as HTMLElement
            setTimeout(() => {
              target.classList.remove('opacity-0', 'translate-y-12')
              target.classList.add('opacity-100', 'translate-y-0')
            }, delay)
            
            // Stagger next element
            delay += 100 
            
            observer?.unobserve(target)
          }
        })
      }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
      })

      elements.forEach(el => observer?.observe(el))
    }, 100)
  })

  onUnmounted(() => {
    if (observer) observer.disconnect()
  })
}
