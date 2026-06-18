# Raja Emas Indonesia - Web Platform

Situs web resmi dan platform digital untuk Raja Emas Indonesia, penyedia emas murni bersertifikat terdepan. Dibangun untuk performa maksimal, SEO-friendly, dan pengalaman pengguna (*User Experience*) tingkat premium.

## Teknologi & Fitur Utama

- **Framework Core**: Dibangun menggunakan **Nuxt 3** dengan arsitektur SSR (*Server-Side Rendering*) dan optimasi *Code Splitting* yang agresif menggunakan `<Lazy...>` komponen.
- **Styling & UI**: **Tailwind CSS** dipadukan dengan palet warna khusus dan desain antar muka bergaya *glassmorphism* modern.
- **Performa Ekstrem (Lighthouse 90+)**: 
  - Tidak menggunakan *library* Javascript pihak ketiga yang berat (seperti GSAP atau Lenis). Seluruh animasi dibangun 100% menggunakan **Native CSS Transitions** & **Intersection Observer API** (`useFadeUp`).
  - Terintegrasi dengan modul **Nuxt Image** (`@nuxt/image`) untuk optimasi pengiriman gambar (*WebP* otomatis, atribut `sizes` cerdas, resolusi responsif).
  - Implementasi **YouTube Facade Pattern** untuk memangkas *blocking time* saat memuat video *embed*, menghemat *payload* ukuran halaman hingga 2MB.
  - Optimasi **Google Fonts** (`@nuxtjs/google-fonts`) yang dirampingkan hanya memanggil bobot tulisan (*font-weight*) yang dibutuhkan saja demi memangkas *Critical Path Latency*.
- **Cinematic Ambient Background**: Penggunaan filter CSS tingkat lanjut (`blur`, `saturate`) pada *slider desktop* untuk memunculkan pendaran efek ambient mewah tanpa memakan *bandwith* ekstra.
- **Animasi Transisi Halaman (*Page Transitions*)**: Navigasi perpindahan rute dibekali efek transisi *fade-slide-blur* standar industri yang *smooth* dan sangat responsif.
- **Sumber Data Dinamis**: Keseluruhan konten (produk, kontak pemasaran, cabang, dan slider) dapat dengan mudah dikendalikan melalui berkas terpusat di `data/siteData.json`.

## Prasyarat

Sebelum memulai, pastikan sistem Anda memiliki:
- **Node.js**: (disarankan versi 18.x atau yang lebih baru).
- **pnpm**: Proyek ini diwajibkan menggunakan `pnpm` sebagai *package manager* utama.

Jika Anda belum menginstal `pnpm`, Anda dapat menginstalnya menggunakan npm:
```bash
npm install -g pnpm
```

## Instalasi & Pengaturan

1. **Instal Dependensi**
   Karena proyek ini menggunakan `pnpm`, jalankan perintah berikut untuk menginstal semua dependensi proyek secara efisien:
   ```bash
   pnpm install
   ```

2. **Server Pengembangan (Development)**
   Jalankan server pengembangan:
   ```bash
   pnpm run dev
   ```
   Aplikasi akan tersedia di `http://localhost:3000`.

3. **Build Produksi (Production)**
   Membangun aplikasi untuk lingkungan produksi:
   ```bash
   pnpm run build
   ```

4. **Pratinjau Produksi (Preview)**
   Melihat pratinjau hasil build produksi secara lokal:
   ```bash
   pnpm run preview
   ```

## Struktur Proyek

- `/pages`: Rute utama aplikasi (`index.vue`, `offline-store.vue`, `products/[category].vue`, `contact-us.vue`).
- `/components`: Komponen antarmuka yang modular dan *lazy-loaded* (mis. `HomePartnerSection`, `YoutubeFacade`).
- `/assets`: Repositori gaya global Tailwind dan definisi transisi CSS (`main.css`).
- `/data`: Sumber kebenaran tunggal untuk data konten (*single source of truth*) melalui `siteData.json`.
- `/composables`: Lokasi logika modular yang dapat digunakan ulang (mis. `useFadeUp.ts`).
- `/public`: Tempat meletakkan aset statis murni (logo, *favicon*, video MP4).

## Konfigurasi

### Tipografi

- **Judul Utama (h1-h3)**: El Messiri (Weight: 600, 700)
- **Teks Paragraf (Body)**: Raleway (Weight: 400, 500, 700)

### Palet Warna

- **Dark Amethyst**: `#331432` 
- **White Dust**: `#F8F4ED` 
- **Light Amethyst**: `#FFF3FD` 
- **Golden Sand**: `#D3A85F` 
- **Black Obsidian**: `#111111` 
