# Raja Emas Indonesia - Web Platform

Situs web resmi dan platform digital untuk Raja Emas Indonesia, penyedia emas murni bersertifikat terdepan. Dibangun untuk performa, SEO, dan pengalaman pengguna yang premium.

## Teknologi yang Digunakan

- **Framework**: Nuxt 3
- **Styling**: Tailwind CSS
- **Animasi**: GSAP (GreenSock) & ScrollTrigger
- **Smooth Scrolling**: Studio Freight Lenis
- **Ikon**: Nuxt Icon
- **Font**: Google Fonts (El Messiri & Raleway)

## Fitur

- **Sumber Data Dinamis**: Konten sepenuhnya digerakkan oleh `data/siteData.json`.
- **Performa Tinggi**: Animasi yang diakselerasi perangkat keras (`will-change: transform`), pengiriman aset yang dioptimalkan.
- **Animasi Premium**: Interaksi mikro, interpolasi gulir halus (*smooth scroll*), dan urutan *timeline* yang kompleks.
- **Pencarian Real-Time**: Pemfilteran dinamis terintegrasi untuk lokasi cabang (*offline store*).
- **Tata Letak Responsif**: Dioptimalkan untuk perangkat desktop, tablet, dan seluler.
- **Siap SEO**: HTML semantik, penandaan meta yang tepat, dan skor *lighthouse* yang dioptimalkan.

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

- `/pages`: Rute aplikasi (`index.vue`, `offline-store.vue`, `products/[category].vue`).
- `/components`: Komponen antarmuka pengguna (UI) yang dapat digunakan kembali (mis. Global Header, Global Footer).
- `/assets`: Konfigurasi CSS dan gaya global (`main.css`).
- `/data`: Sumber kebenaran tunggal untuk konten dinamis (`siteData.json`).
- `/plugins`: Plugin Nuxt (mis. plugin klien Lenis Smooth Scroll).
- `/public`: Aset statis (gambar, logo).

## Konfigurasi

### Tipografi

- **Judul Utama (h1-h3)**: El Messiri (Semi-Bold)
- **Teks Paragraf (Body)**: Raleway (Regular)

### Palet Warna

- **Dark Amethyst**: `#331432` (R 51, G 20, B 50 | C 79, M 99, Y 41, K 61)
- **White Dust**: `#F8F4ED` (R 248, G 244, B 237 | C 4, M 4, Y 8, K 0)
- **Light Amethyst**: `#FFF3FD` (R 255, G 243, B 253 | C 0, M 7, Y 0, K 0)
- **Golden Sand**: `#D3A85F` (R 211, G 168, B 95 | C 18, M 33, Y 73, K 0)
- **Black Obsidian**: `#111111` (R 17, G 17, B 17 | C 79, M 70, Y 62, K 89)

## Panduan Pengembangan

1. Pastikan semua *styling* menggunakan kelas utilitas melalui Tailwind CSS kecuali integrasi GSAP kompleks memerlukan CSS kustom.
2. Simpan semua modifikasi konten dinamis di dalam `data/siteData.json`.
3. Pertahankan animasi akselerasi perangkat keras yang sudah ada saat memperkenalkan *timeline* GSAP baru.
