<template>
  <div>
    <!-- Hero Section -->
    <section class="relative min-h-screen pt-24 pb-16 flex items-center justify-center bg-blackobsidian overflow-hidden">
      <!-- Background Elements -->
      <div class="absolute inset-0 z-0 pointer-events-none">
        <div class="absolute top-0 right-0 w-1/2 h-1/2 bg-goldensand/10 rounded-full blur-[150px] translate-x-1/4 -translate-y-1/4"></div>
        <div class="absolute bottom-0 left-0 w-1/2 h-1/2 bg-darkamethyst/10 rounded-full blur-[150px] -translate-x-1/4 translate-y-1/4"></div>
      </div>

      <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-8 items-center">
          <!-- Text Content -->
          <div class="max-w-2xl text-center lg:text-left order-2 lg:order-1 mx-auto lg:mx-0">
            <div class="hero-title">
              <h1 class="block text-4xl sm:text-5xl lg:text-6xl font-semibold text-white mb-4 tracking-tight leading-tight">
                About <br class="hidden lg:block"/>Emas Murni Asli
              </h1>
              <h2 class="block text-xl sm:text-2xl lg:text-3xl text-goldensand font-medium mb-6 lg:mb-8 leading-snug">
                Exclusive Gifts for Meaningful Moments
              </h2>
            </div>
            
            <div class="hero-text space-y-4 text-gray-400 text-base sm:text-lg leading-relaxed mb-8 sm:mb-10">
              <p>
                <strong class="text-white font-medium">PT Emas Murni Asli</strong> adalah penyedia logam mulia 24 Karat (99,99%) yang dapat digunakan untuk hadiah (gift), apresiasi, penghargaan, souvenir, dan investasi. Melalui brand <strong class="text-white font-medium">Raja Emas Indonesia</strong>, kami menghadirkan berbagai pilihan <strong class="text-white font-medium">emas batangan</strong> serta <strong class="text-white font-medium">layanan custom</strong> yang dapat disesuaikan dengan kebutuhan individu, komunitas, perusahaan, maupun instansi.
              </p>
              <p>
                Dengan mengutamakan kualitas, desain eksklusif, dan layanan profesional, kami membantu menciptakan hadiah emas yang tidak hanya berkesan, tetapi juga memiliki nilai yang bertahan dan terus berkembang dari waktu ke waktu.
              </p>
            </div>

            <!-- CTAs -->
            <div class="hero-cta flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4">
              <NuxtLink to="/products/logam-series" class="w-full sm:w-auto px-8 py-4 bg-goldensand text-blackobsidian font-bold rounded-full hover:bg-yellow-500 hover:shadow-[0_0_20px_rgba(211,168,95,0.4)] hover:-translate-y-1 transition-all duration-300 text-center">
                Koleksi Logam Series
              </NuxtLink>
              <NuxtLink to="/offline-store" class="w-full sm:w-auto px-8 py-4 bg-transparent border-2 border-white/20 text-white font-bold rounded-full hover:bg-white/5 hover:border-white/40 hover:-translate-y-1 transition-all duration-300 text-center">
                Hubungi Kami
              </NuxtLink>
            </div>
          </div>

          <!-- Video Container -->
          <div class="hero-video order-1 lg:order-2 w-full max-w-2xl mx-auto lg:max-w-none relative group">
            <!-- Decorative Glow Behind Video -->
            <div class="absolute -inset-4 bg-gradient-to-tr from-goldensand/40 via-transparent to-darkamethyst/40 rounded-[2.5rem] blur-2xl opacity-50 group-hover:opacity-80 transition-opacity duration-700"></div>
            
            <div class="relative rounded-3xl overflow-hidden border border-white/10 bg-blackobsidian shadow-2xl transform transition-transform duration-700 hover:scale-[1.02] flex items-center justify-center">
              <video 
                src="/vid/Vid_Compro.mp4" 
                class="w-full h-auto max-h-[80vh] object-contain"
                autoplay 
                loop 
                muted 
                playsinline
              ></video>
              
              <!-- Subtle inner shadow to blend video edges -->
              <div class="absolute inset-0 shadow-[inset_0_0_30px_rgba(0,0,0,0.6)] pointer-events-none"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- About Slider -->
    <section class="relative w-full overflow-hidden bg-blackobsidian group">
      <div 
        class="flex transition-transform duration-700 ease-in-out h-[60vh] sm:h-[80vh] md:h-screen"
        :style="{ transform: `translateX(-${currentSlide * 100}%)` }"
      >
        <div 
          v-for="(img, idx) in sliderImages" 
          :key="'slide-'+idx"
          class="w-full h-full flex-shrink-0 relative flex items-center justify-center bg-blackobsidian"
        >
          <img :src="`/img/home/slider/${img}`" alt="Slider Image" class="w-full h-full object-cover" loading="lazy" />
        </div>
      </div>
      
      <!-- Navigation Buttons -->
      <button 
        aria-label="Previous Slide"
        @click="prevSlide"
        class="absolute left-4 md:left-8 top-1/2 -translate-y-1/2 w-12 h-12 md:w-14 md:h-14 rounded-full bg-black/40 backdrop-blur-md border-2 border-white/20 text-white flex items-center justify-center hover:bg-goldensand hover:border-goldensand hover:scale-110 transition-all duration-300 z-10 opacity-0 group-hover:opacity-100 shadow-xl focus:outline-none"
      >
        <Icon name="mdi:chevron-left" class="text-3xl md:text-4xl" />
      </button>
      <button 
        aria-label="Next Slide"
        @click="nextSlide"
        class="absolute right-4 md:right-8 top-1/2 -translate-y-1/2 w-12 h-12 md:w-14 md:h-14 rounded-full bg-black/40 backdrop-blur-md border-2 border-white/20 text-white flex items-center justify-center hover:bg-goldensand hover:border-goldensand hover:scale-110 transition-all duration-300 z-10 opacity-0 group-hover:opacity-100 shadow-xl focus:outline-none"
      >
        <Icon name="mdi:chevron-right" class="text-3xl md:text-4xl" />
      </button>

      <!-- Indicators -->
      <div class="absolute bottom-6 md:bottom-10 left-1/2 -translate-x-1/2 flex space-x-3 md:space-x-4 z-10">
        <button 
          v-for="(_, idx) in sliderImages" 
          :key="'dot-'+idx"
          @click="currentSlide = idx"
          aria-label="Go to slide"
          class="h-2 md:h-2.5 rounded-full transition-all duration-300 focus:outline-none shadow-lg"
          :class="currentSlide === idx ? 'bg-goldensand w-8 md:w-12' : 'bg-white/50 hover:bg-white w-2 md:w-2.5'"
        ></button>
      </div>
    </section>

    <!-- Partners Marquee -->
    <section class="py-16 bg-whitedust border-b border-gray-200">
      <div class="w-full overflow-hidden">
        <div class="container mx-auto px-4 mb-8 text-center">
          <h3 class="text-xl font-semibold text-gray-500">Telah Dipercaya Oleh:</h3>
        </div>
        <div class="relative flex w-full overflow-hidden group">
          <!-- First Track -->
          <div class="animate-marquee-infinite flex whitespace-nowrap items-center shrink-0">
            <div v-for="i in 8" :key="`p1-${i}`" class="px-8 md:px-12 lg:px-16 flex items-center justify-center">
              <img :src="`/img/home/partner/${(i - 1) % 4 + 1}.png`" alt="Partner Logo" class="h-16 sm:h-20 md:h-24 lg:h-28 w-auto max-w-[200px] md:max-w-[250px] object-contain hover:scale-110 transition-all duration-500 drop-shadow-sm cursor-pointer" loading="lazy" />
            </div>
          </div>
          <!-- Second Track (Duplicate for infinite loop) -->
          <div class="animate-marquee-infinite flex whitespace-nowrap items-center shrink-0" aria-hidden="true">
            <div v-for="i in 8" :key="`p2-${i}`" class="px-8 md:px-12 lg:px-16 flex items-center justify-center">
              <img :src="`/img/home/partner/${(i - 1) % 4 + 1}.png`" alt="Partner Logo" class="h-16 sm:h-20 md:h-24 lg:h-28 w-auto max-w-[200px] md:max-w-[250px] object-contain hover:scale-110 transition-all duration-500 drop-shadow-sm cursor-pointer" loading="lazy" />
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Services / Features Section -->
    <section class="py-24 bg-whitedust border-t border-gray-200">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="gsap-fade-up text-4xl md:text-5xl font-semibold mb-4 text-blackobsidian">Mengapa <span class="text-goldensand">Raja Emas?</span></h2>
          <p class="gsap-fade-up text-gray-600 max-w-2xl mx-auto text-lg">Bandingkan dengan tempat lain, Anda akan merasakan bedanya. Proses mudah, transparan, dan harga beli tertinggi.</p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Featured large card -->
          <div class="feature-card lg:col-span-2 bg-blackobsidian rounded-[2rem] p-8 md:p-12 shadow-2xl text-white relative overflow-hidden group">
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
          <div v-for="(feature, idx) in siteData.features.slice(1)" :key="'feat-'+idx" class="feature-card bg-white rounded-[2rem] p-8 shadow-xl border border-goldensand/20 hover:border-goldensand transition-colors group">
            <div class="w-14 h-14 bg-whitedust text-goldensand rounded-xl flex items-center justify-center mb-6 group-hover:bg-goldensand group-hover:text-white transition-colors duration-300">
              <Icon :name="feature.icon" class="text-2xl" />
            </div>
            <h3 class="text-xl font-semibold mb-3 text-blackobsidian">{{ feature.title }}</h3>
            <p class="text-gray-600 font-sans leading-relaxed text-sm">{{ feature.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials (Swipeable Carousel) -->
    <section class="py-24 bg-whitedust relative overflow-hidden">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10 mb-12 text-center md:text-left flex flex-col md:flex-row justify-between items-end gap-6">
        <div class="gsap-fade-up">
          <h2 class="text-4xl md:text-5xl font-semibold mb-4 text-blackobsidian">Apa Kata <span class="text-goldensand">Klien Kami</span></h2>
          <p class="text-gray-600 max-w-xl text-lg font-sans">Geser untuk melihat testimoni dari pelanggan yang telah mempercayakan investasi dan kebutuhan emasnya kepada Raja Emas Indonesia.</p>
        </div>
        <div class="gsap-fade-up hidden md:flex gap-4">
          <button aria-label="Previous Review" @click="scrollTesti('left')" class="w-12 h-12 rounded-full border border-goldensand flex items-center justify-center text-goldensand hover:bg-goldensand hover:text-white transition-colors focus:outline-none focus:ring-2 focus:ring-goldensand">
            <Icon name="mdi:chevron-left" class="text-2xl" />
          </button>
          <button aria-label="Next Review" @click="scrollTesti('right')" class="w-12 h-12 rounded-full border border-goldensand flex items-center justify-center text-goldensand hover:bg-goldensand hover:text-white transition-colors focus:outline-none focus:ring-2 focus:ring-goldensand">
            <Icon name="mdi:chevron-right" class="text-2xl" />
          </button>
        </div>
      </div>

      <div class="w-full relative px-4 sm:px-6 lg:px-8 gsap-fade-up">
        <div ref="testiContainer" class="flex overflow-x-auto gap-6 pb-8 snap-x snap-mandatory hide-scrollbar">
          <div v-for="(testi, index) in siteData.testimonials" :key="'testi-'+index" class="min-w-[70vw] sm:min-w-[300px] md:min-w-[350px] snap-center shrink-0 bg-white p-2 rounded-[2rem] border border-gray-100 shadow-xl hover:shadow-2xl transition-all duration-300 relative group h-[350px] sm:h-[400px]">
            <img :src="testi.image" alt="Customer Review" class="w-full h-full rounded-[1.5rem] object-contain" loading="lazy" />
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ Section -->
    <section class="py-24 bg-white relative overflow-hidden border-t border-gray-100">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10 max-w-4xl">
        <div class="text-center mb-16 gsap-fade-up">
          <!-- <span class="inline-block py-1.5 px-4 rounded-full bg-whitedust border border-gray-200 text-goldensand text-xs sm:text-sm font-semibold tracking-widest uppercase mb-4">
            Pertanyaan Umum
          </span> -->
          <h2 class="text-3xl md:text-5xl font-semibold mb-6 text-blackobsidian tracking-tight">
            <span class="text-goldensand">Frequently Ask Question</span> (FAQ)
          </h2>
          <p class="text-gray-500 max-w-2xl mx-auto text-lg font-sans">
            Temukan jawaban atas pertanyaan yang paling sering diajukan seputar layanan pembelian, penjualan, dan pengecekan emas di Raja Emas Indonesia.
          </p>
        </div>

        <!-- FAQ Tabs -->
        <div class="flex flex-wrap justify-center gap-2 md:gap-4 mb-10 gsap-fade-up">
          <button 
            v-for="(_, category) in faqs" 
            :key="category"
            @click="activeCategory = category; activeFaq = null"
            class="px-6 py-2.5 rounded-full font-semibold transition-all duration-300 border-2 text-sm sm:text-base"
            :class="activeCategory === category ? 'bg-goldensand border-goldensand text-white shadow-md' : 'bg-transparent border-gray-200 text-gray-500 hover:border-goldensand hover:text-goldensand'"
          >
            {{ category }}
          </button>
        </div>

        <div class="space-y-4 gsap-fade-up">
          <div 
            v-for="(faq, index) in faqs[activeCategory]" 
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
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import siteData from '~/data/siteData.json'

gsap.registerPlugin(ScrollTrigger)

const testiContainer = ref(null)

const sliderImages = [
  'Page1.png',
  'page2.png',
  'page3.png',
  'page4.png',
  'page5.png'
]
const currentSlide = ref(0)

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % sliderImages.length
}
const prevSlide = () => {
  currentSlide.value = (currentSlide.value - 1 + sliderImages.length) % sliderImages.length
}

const activeCategory = ref('Product')
const activeFaq = ref(null)

const toggleFaq = (index) => {
  activeFaq.value = activeFaq.value === index ? null : index
}

const faqs = {
  "Product": [
    { question: "Apakah produk Logam Mulia Raja Emas Indonesia terbuat dari emas asli?", answer: "Ya. Seluruh produk Logam Mulia Raja Emas Indonesia dibuat menggunakan emas murni 24 Karat (99,9%) dengan kualitas yang terjamin." },
    { question: "Apakah setiap Logam Mulia Raja Emas Indonesia dilengkapi sertifikat atau tanda autentikasi?", answer: "Ya. Setiap produk dilengkapi dengan sertifikat keaslian." },
    { question: "Apakah Logam Mulia Raja Emas Indonesia bisa dicustom?", answer: "Ya. PT Emas Murni Asli melayani pembuatan Logam Mulia Custom untuk kebutuhan perusahaan, instansi, komunitas, maupun personal." },
    { question: "Apakah customer bisa memilih desain dan ukuran Logam Mulia Custom?", answer: "Ya. Customer dapat menentukan desain, bentuk, ukuran, gramasi, serta spesifikasi produk sesuai kebutuhan." },
    { question: "Apakah proses custom dapat mengurangi gramasi emas?", answer: "Tidak. Gramasi emas akan tetap mengikuti spesifikasi yang telah disepakati pada saat pemesanan." },
    { question: "Apakah bisa custom gramasi selain yang tersedia?", answer: "Ya. Untuk kebutuhan tertentu, customer dapat berkonsultasi dengan tim kami terkait gramasi yang diinginkan." },
    { question: "Apakah bisa custom bentuk logam mulia selain yang tersedia?", answer: "Ya. Kami dapat membantu memproduksi berbagai bentuk dan desain custom sesuai kebutuhan dan identitas customer." },
    { question: "Apakah bisa custom produk dengan kadar emas selain 24 Karat (99,9%)?", answer: "Untuk informasi terkait ketersediaan kadar emas selain 24 Karat, silahkan konsultasikan langsung dengan tim kami." },
    { question: "Apakah ada tambahan biaya untuk custom desain?", answer: "Biaya akan disesuaikan dengan tingkat kompleksitas desain, gramasi, jumlah pesanan, dan spesifikasi produk yang diminta." },
    { question: "Apakah customer bisa melihat preview desain sebelum produksi?", answer: "Ya. Tim kami akan memberikan desain atau mockup terlebih dahulu untuk mendapatkan persetujuan sebelum proses produksi dimulai." },
    { question: "Apakah bisa custom warna pada produk?", answer: "Warna produk mengikuti karakteristik logam mulia yang digunakan. Untuk kebutuhan khusus, silahkan konsultasikan dengan tim kami." },
    { question: "Apakah PT Emas Murni Asli menyediakan katalog desain jika customer belum memiliki desain sendiri?", answer: "Ya. Kami memiliki berbagai referensi desain yang dapat dijadikan inspirasi atau disesuaikan dengan kebutuhan customer." },
    { question: "Apakah ada contoh foto produk dan hasil jadi untuk berbagai bentuk dan gramasi?", answer: "Ya. Customer dapat melihat portofolio dan contoh hasil produksi melalui website, media sosial, atau langsung berkonsultasi dengan tim kami." },
    { question: "Berapa ukuran standar setiap bentuk dan gramasi Logam Mulia Raja Emas Indonesia?", answer: "Ukuran produk akan menyesuaikan dengan gramasi dan desain yang dipilih. Informasi detail dapat diperoleh melalui tim customer service kami." },
    { question: "Packaging apa yang akan didapat pada setiap pembelian?", answer: "Setiap pembelian Logam Mulia Raja Emas Indonesia dilengkapi dengan packaging premium berbahan akrilik, invoice pembelian, thank you card." },
    { question: "Apakah tersedia pilihan packaging selain packaging standar?", answer: "Untuk kebutuhan khusus atau pesanan custom, customer dapat berkonsultasi dengan tim kami terkait pilihan packaging yang tersedia." },
    { question: "Apakah produk Logam Mulia Raja Emas Indonesia dapat dijual kembali di masa depan?", answer: "Ya. Sebagai produk logam mulia, emas memiliki nilai yang dapat diperjualbelikan kembali sesuai ketentuan dan harga pasar yang berlaku." },
    { question: "Bagaimana dengan harga buyback?", answer: "Harga buyback mengikuti harga buyback nasional serta menyesuaikan kebijakan perusahaan." },
    { question: "Bagaimana cara melakukan buyback Logam Mulia Raja Emas Indonesia?", answer: "Customer dapat mengunjungi cabang Raja Emas Indonesia terdekat untuk mendapatkan informasi dan prosedur buyback yang berlaku." }
  ],
  "Order": [
    { question: "Bagaimana cara melakukan pemesanan produk Logam Mulia Raja Emas Indonesia?", answer: "Pemesanan dapat dilakukan melalui WhatsApp yang tertera." },
    { question: "Berapa lama waktu pengerjaan produk custom?", answer: "Waktu pengerjaan produk custom 14 hari - 1 bulan tidak termasuk sabtu, minggu, dan hari libur nasional serta disesuaikan juga dengan bentuk dan jumlah pesanan." },
    { question: "Apakah ada jumlah minimum pemesanan untuk produk custom?", answer: "Tidak ada minimal order." }
  ],
  "Price & Payment": [
    { question: "Bagaimana cara pembayaran pemesanan?", answer: "Kami menerima berbagai metode pembayaran, termasuk transfer bank, kartu debit/kredit, dan metode pembayaran lainnya yang tersedia sesuai ketentuan perusahaan." },
    { question: "Apakah bisa pembayaran secara tempo?", answer: "Untuk informasi mengenai pembayaran tempo atau termin pembayaran, silahkan menghubungi tim kami. Ketentuan pembayaran akan disesuaikan dengan jenis pesanan dan kebijakan perusahaan yang berlaku." },
    { question: "Di mana saya bisa melihat harga terbaru yang berlaku hari ini?", answer: "Untuk mendapatkan informasi harga terbaru, bisa kunjungi instagram emasmurniasli.id dan website emasmurniasli.id atau silahkan menghubungi tim kami untuk update seputar harga custom." },
    { question: "Promo apa saja yang sedang berlaku dan bagaimana cara mendapatkannya?", answer: "Informasi seputar promo dapat diperoleh melalui WhatsApp, Marketplace Official, dan social media Emas Murni Asli." },
    { question: "Apakah tersedia pembayaran DP untuk pesanan Logam Mulia?", answer: "Ya. Ketentuan pembayaran DP ada di 70% dan pelunasan pada saat barang diterima." }
  ],
  "Delivery": [
    { question: "Apakah PT Emas Murni Asli bisa mengirim produk ke seluruh Indonesia?", answer: "Ya. PT Emas Murni Asli melayani pengiriman produk ke seluruh wilayah Indonesia melalui jasa pengiriman yang aman dan terpercaya." },
    { question: "Untuk pengiriman, menggunakan jasa pengiriman apa saja?", answer: "Kami bekerja sama dengan beberapa jasa pengiriman terpercaya seperti JNE serta memiliki kurir internal." },
    { question: "Apakah pengiriman produk logam mulia aman?", answer: "Ya. Setiap produk akan dikemas dengan aman menggunakan packaging premium dan melalui proses pengecekan sebelum dikirim. Kami juga bekerja sama dengan jasa pengiriman terpercaya untuk menjaga keamanan produk selama proses pengiriman." },
    { question: "Bagaimana cara melacak pesanan?", answer: "Setelah pesanan dikirim, customer akan mendapatkan nomor resi yang dapat digunakan untuk memantau status pengiriman melalui layanan kurir." },
    { question: "Apakah PT Emas Murni Asli memiliki toko atau offline store?", answer: "Ya. PT Emas Murni Asli memiliki offline store bernama Raja Emas Indonesia dan dapat dikunjungi langsung oleh pelanggan untuk melihat produk, berkonsultasi, maupun melakukan transaksi secara langsung." }
  ]
}

const scrollTesti = (direction) => {
  if (testiContainer.value) {
    const scrollAmount = window.innerWidth > 768 ? 450 + 24 : window.innerWidth * 0.85;
    testiContainer.value.scrollBy({
      left: direction === 'left' ? -scrollAmount : scrollAmount,
      behavior: 'smooth'
    })
  }
}

useSeoMeta({
  title: 'Home',
  titleTemplate: '%s - Raja Emas Indonesia',
  description: siteData.company.about,
  ogTitle: 'Raja Emas Indonesia - Investasi Emas Terpercaya',
  ogDescription: siteData.company.tagline,
})

onMounted(() => {
  // Hero Animations
  const tl = gsap.timeline()
  
  tl.fromTo('.hero-video',
    { x: 50, opacity: 0, scale: 0.95 },
    { x: 0, opacity: 1, scale: 1, duration: 1.2, ease: 'power4.out', delay: 0.2 }
  )
  .fromTo('.hero-title .block', 
    { y: 50, opacity: 0 },
    { y: 0, opacity: 1, duration: 1, stagger: 0.15, ease: 'power4.out' },
    "-=0.8"
  )
  .fromTo('.hero-text p',
    { y: 30, opacity: 0 },
    { y: 0, opacity: 1, duration: 0.8, stagger: 0.2, ease: 'power3.out' },
    "-=0.6"
  )
  .fromTo('.hero-cta a',
    { y: 30, opacity: 0 },
    { y: 0, opacity: 1, duration: 0.8, stagger: 0.15, ease: 'power3.out' },
    "-=0.6"
  )

  // Scroll Animations for generic fade up elements
  gsap.set('.gsap-fade-up', { y: 50, opacity: 0 })
  ScrollTrigger.batch('.gsap-fade-up', {
    onEnter: batch => gsap.to(batch, {
      opacity: 1, 
      y: 0, 
      duration: 0.8,
      stagger: 0.1, 
      ease: 'power2.out',
      overwrite: true
    }),
    start: 'top 90%',
    once: true // Animate only once to save GPU memory on scroll
  })

  // Feature cards optimized batch animation
  gsap.set('.feature-card', { y: 50, opacity: 0 })
  ScrollTrigger.batch('.feature-card', {
    onEnter: batch => gsap.to(batch, {
      opacity: 1, 
      y: 0, 
      duration: 0.8,
      stagger: 0.15, 
      ease: 'power2.out',
      overwrite: true
    }),
    start: 'top 90%',
    once: true
  })
})
</script>

<style scoped>
.animate-marquee-infinite {
  animation: marquee-infinite 35s linear infinite;
}

.group:hover .animate-marquee-infinite {
  animation-play-state: paused;
}

@keyframes marquee-infinite {
  0% { transform: translateX(0%); }
  100% { transform: translateX(-100%); }
}

/* Custom Scrollbar for pricing table */
.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.02);
  border-radius: 10px;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: rgba(211, 168, 95, 0.3); /* goldensand with opacity */
  border-radius: 10px;
}
.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: rgba(211, 168, 95, 0.8);
}

/* Hide scrollbar for carousel but keep functionality */
.hide-scrollbar {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}
.hide-scrollbar::-webkit-scrollbar {
  display: none; /* Chrome, Safari and Opera */
}
</style>
