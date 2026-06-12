# Raja Emas Indonesia - Web Platform

Official website and digital platform for Raja Emas Indonesia, the leading certified pure gold provider. Built for performance, SEO, and premium user experience.

## Technology Stack

- **Framework**: Nuxt 3
- **Styling**: Tailwind CSS
- **Animations**: GSAP (GreenSock) & ScrollTrigger
- **Smooth Scrolling**: Studio Freight Lenis
- **Icons**: Nuxt Icon
- **Fonts**: Google Fonts (El Messiri & Raleway)

## Features

- **Dynamic Data Source**: Content is driven entirely by `data/siteData.json`.
- **High Performance**: Hardware-accelerated animations (`will-change: transform`), optimized asset delivery.
- **Premium Animations**: Micro-interactions, smooth scroll interpolation, and complex timeline sequences.
- **Real-Time Search**: Integrated dynamic filtering for offline store locations.
- **Responsive Layout**: Optimized for desktop, tablet, and mobile devices.
- **SEO Ready**: Semantic HTML, proper meta tagging, and optimized lighthouse scores.

## Installation & Setup

1. **Install Dependencies**
   ```bash
   pnpm install
   ```

2. **Development Server**
   ```bash
   pnpm run dev
   ```
   The application will be available at `http://localhost:3000`.

3. **Production Build**
   ```bash
   pnpm run build
   ```

4. **Preview Production**
   ```bash
   pnpm run preview
   ```

## Project Structure

- `/pages`: Application routes (`index.vue`, `offline-store.vue`, `products/[category].vue`).
- `/components`: Reusable UI components (e.g., Global Header, Global Footer).
- `/assets`: Global CSS and styling configuration (`main.css`).
- `/data`: Single source of truth for dynamic content (`siteData.json`).
- `/plugins`: Nuxt plugins (e.g., Lenis Smooth Scroll client plugin).
- `/public`: Static assets (images, logos).

## Configuration

### Typography

- **Headlines (h1-h3)**: El Messiri (Semi-Bold)
- **Body Copy**: Raleway (Regular)

### Color Palette

- **Golden Sand**: `#D3A85F`
- **Black Obsidian**: `#111111`
- **White Dust**: `#F5F5F5`

## Development Guidelines

1. Ensure all styling uses utility classes via Tailwind CSS unless complex GSAP integration requires custom CSS.
2. Store all dynamic content modifications in `data/siteData.json`.
3. Preserve established hardware-accelerated animations when introducing new GSAP timelines.
