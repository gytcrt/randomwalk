# Random Walk

My personal website built with [Hugo](https://gohugo.io/) and the [PaperModX](https://github.com/reorx/hugo-PaperModX) theme. The site features a clean, minimalist design for sharing thoughts and ideas.

## Features

- Responsive design optimized for all device sizes
- Dark/light mode toggle
- Profile mode with animated GIF support
- Blog posts with reading time, tags, and sharing options
- Search functionality
- Clean, accessible navigation

## Local Development

1. Clone this repository
2. Install Hugo (extended version)
3. Run the development server:
   ```bash
   hugo server -D
   ```
4. Visit http://localhost:1313

## Project Structure

- `/archetypes/`: Default content templates
- `/assets/`: CSS, JavaScript, and other assets
- `/content/`: Contains all the content
  - `/posts/`: Blog posts
  - `/about/`: About page
  - `/home/`: Home page content
- `/data/`: Configuration data files
- `/layouts/`: Custom layout templates
- `/static/`: Static files like images and favicon
- `/themes/`: Contains the PaperModX theme
- `config.yml`: Main configuration file

## Configuration

The site is configured through `config.yml`, which includes:

- Site metadata (title, description, author)
- Theme configuration
- Navigation menu setup
- Social icons and links
- Analytics settings
- Content display preferences

## Deployment

The site is deployed to GitHub Pages using GitHub Actions. Any push to the main branch triggers an automatic build and deployment process.

## Credits

- Theme: [PaperModX](https://github.com/reorx/hugo-PaperModX)
- Built with [Hugo](https://gohugo.io/) 