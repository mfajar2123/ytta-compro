# Raja Emas Indonesia - Web Platform

Situs web resmi dan platform digital untuk Raja Emas Indonesia, penyedia emas murni bersertifikat terdepan. Dibangun untuk performa maksimal, SEO-friendly, dan pengalaman pengguna (*User Experience*) tingkat premium.

## Teknologi & Fitur Utama

- **Nuxt 3 & SSR**: Dibangun dengan arsitektur modern yang mendukung rendering sisi server dan pemuatan komponen *lazy loading*.
- **Tailwind CSS**: Desain antarmuka cepat, konsisten, dan kustom dengan gaya *glassmorphism*.
- **Nuxt Image**: Pengolahan gambar terpusat untuk *WebP* otomatis dan format responsif cerdas.
- **Native CSS Animations**: Menggunakan animasi bawaan CSS dipadukan dengan *Intersection Observer* tanpa *library* eksternal.
- **Page Transitions**: Perpindahan rute antar halaman yang mulus dengan efek *fade-slide-blur*.
- **YouTube Facade**: Sistem pemuatan modul video secara tertunda (*lazy*) untuk menghemat data halaman.
- **Data-Driven Content**: Keseluruhan teks, produk, dan lokasi toko diatur secara terpusat melalui berkas `data/siteData.json`.

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
