# Random Walk

A personal website and public notebook by Andrea Gao. Built with [Hugo](https://gohugo.io/) and the [PaperModX](https://github.com/reorx/hugo-PaperModX) theme.

## Local Development

1. Clone this repository (with submodules):
   ```bash
   git clone --recurse-submodules <repo-url>
   ```
2. Install [Hugo](https://gohugo.io/installation/) (extended version)
3. Run the development server:
   ```bash
   hugo server -D
   ```
4. Visit http://localhost:1313

## Project Structure

- `content/` — Site content
  - `posts/` — Blog posts (each post is a folder with `index.md` + images)
  - `notes/` — Short-form notes
  - `about/` — About page
- `assets/css/extended/` — Custom CSS overrides
- `layouts/` — Custom template overrides
- `static/` — Static files (favicon, images)
- `config.yml` — Site configuration

## Features

### Comments
[Giscus](https://giscus.app/) for GitHub Discussions-based comments. Lazy-loaded via a "Load comments" button to improve page performance. Configuration in `layouts/partials/giscus.html`.

### Analytics
- **Umami** (self-hosted) — Privacy-friendly analytics at `analytics.andreagao.com`
- **Google Analytics 4** — Configured in `config.yml`

### AI / LLM Support
- I use AI coding tool to develop this website but all posts and notes are written by me with no AI. 
- Generates `llms.txt` at build time for AI crawlers and LLM indexing. See `layouts/_default/home.llms.txt` for the template.

## Deployment

Deployed to GitHub Pages via GitHub Actions. Pushes to `main` trigger automatic builds.

## Credits

- Theme: [PaperModX](https://github.com/reorx/hugo-PaperModX)
- Built with [Hugo](https://gohugo.io/)
