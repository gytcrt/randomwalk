# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Personal website / public notebook for Andrea Gao (andreagao.com). Hugo static site using the PaperModX theme as a git submodule. Deployed to GitHub Pages via [.github/workflows/hugo.yml](.github/workflows/hugo.yml) on push to `main`.

When cloning fresh: `git clone --recurse-submodules` — the theme is in [themes/PaperModX/](themes/PaperModX/) as a submodule and the site won't build without it.

## Common commands

```bash
hugo server -D            # local dev server on :1313 (includes drafts)
hugo --minify             # production build into ./public
python3 scripts/add-note-dates.py   # auto-append dates to undated notes
```

CI uses Hugo extended **0.146.5**. If `hugo server` fails with SCSS / asset errors, you likely have the non-extended build.

## Architecture

This is a fairly stock Hugo setup — most behavior is driven by [config.yml](config.yml) and the PaperModX theme. Things worth knowing before editing:

**Content layout has two distinct shapes.**
- [content/posts/](content/posts/) — long-form. Each post is a folder with `index.md` + co-located images (e.g. [content/posts/blog-set-up/](content/posts/blog-set-up/)). Front matter uses TOML or YAML; see existing posts for the expected fields (`title`, `date`, `description`, `tags`, `category`, `cover.image`, `ShowToc`).
- [content/notes/index.md](content/notes/index.md) — short-form. A *single* file containing a stream of markdown blockquotes (`> …`), newest first. Each blockquote ends with `  - YYYY.MM.DD`. The note layout is overridden in [layouts/notes/single.html](layouts/notes/single.html).

**Notes auto-dating.** [scripts/add-note-dates.py](scripts/add-note-dates.py) scans [content/notes/index.md](content/notes/index.md), finds blockquotes missing the trailing `  - YYYY.MM.DD`, and appends today's date. It stops at the first already-dated note (notes are prepended, so older notes are guaranteed dated). Designed to run as a pre-commit hook — when adding a new note, just write the blockquote without a date and let the script stamp it.

**Theme overrides live in [layouts/](layouts/).** Hugo resolves these before falling back to [themes/PaperModX/layouts/](themes/PaperModX/layouts/). Notable overrides: [layouts/partials/post_nav_links.html](layouts/partials/post_nav_links.html) (renders prev / Reply-by-email / next as a 3-column grid in place of an inline comment system), [layouts/_default/home.llms.txt](layouts/_default/home.llms.txt). Don't edit theme files in [themes/PaperModX/](themes/PaperModX/) — copy into [layouts/](layouts/) and edit there.

**Custom CSS** goes in [assets/css/extended/](assets/css/extended/) — PaperModX auto-includes anything in that directory after its own styles.

**`llms.txt` is a real Hugo output format,** declared in [config.yml](config.yml) under `outputFormats.llms` and `outputs.home`. The template at [layouts/_default/home.llms.txt](layouts/_default/home.llms.txt) renders a markdown index of all posts for AI crawlers; it's served at `/llms.txt`.

**`.cursor/` is gitignored** ([.gitignore:5](.gitignore)), so anything there stays local. Treat it as scratch, not source of truth.

## Editorial positioning (from .cursor/rules/context.md)

This is a **public notebook**, not a résumé site or growth-hacked brand page. When editing content or content-adjacent UI, optimize for: content-first, calm, restrained, first-person, reflective. Avoid: influencer tone, forced authority signals, marketing language. Useful gut-check questions: "Does this feel more like writing or marketing?" "Would this age well in 5 years?"

All posts and notes are written by Andrea — do not generate or rewrite prose unless explicitly asked. AI assistance is for the site infrastructure (layouts, config, scripts, styling), not the writing.