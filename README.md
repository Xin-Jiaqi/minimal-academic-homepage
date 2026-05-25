# Minimal Academic Homepage

A minimal, responsive academic homepage template for GitHub Pages.

This template is designed for students, researchers, and early-career academics who want to build a clean personal academic homepage with only one `index.html` file.

## Features

- Single-file HTML/CSS template
- Responsive layout for desktop and mobile
- Clean Apple-style visual design
- Sections for:
  - Personal profile
  - Selected publications
  - Projects
  - Education & experience
  - Selected awards
  - Posts & notes
- Easy deployment with GitHub Pages
- No framework, no build tools, no extra dependencies

## Demo

After enabling GitHub Pages, the homepage will be available at:

    https://your-username.github.io/minimal-academic-homepage/

## File Structure

    minimal-academic-homepage/
    ├── index.html
    └── assets/
        ├── profile.jpg
        ├── pub-1.jpg
        ├── pub-2.jpg
        ├── pub-3.jpg
        ├── pub-4.jpg
        ├── university-logo-1.png
        ├── university-logo-2.png
        └── university-logo-3.png

## How to Use

### 1. Fork or use this template

Click **Use this template** or fork this repository to your own GitHub account.

### 2. Edit `index.html`

Open `index.html` and replace the placeholder content:

- `Your Name`
- `Your Position or Degree Program`
- `Your Department, Your University`
- Email, GitHub, Google Scholar, ORCID, ResearchGate links
- Publication titles, authors, DOI, journal links, and highlights
- Projects
- Education & experience
- Awards
- Posts & notes

### 3. Replace images

Replace the files in the `assets/` folder with your own images.

Recommended image names:

    assets/profile.jpg
    assets/pub-1.jpg
    assets/pub-2.jpg
    assets/pub-3.jpg
    assets/pub-4.jpg
    assets/university-logo-1.png
    assets/university-logo-2.png
    assets/university-logo-3.png

You can keep the same file names to avoid editing image paths in `index.html`.

### 4. Enable GitHub Pages

Go to:

    Settings → Pages → Build and deployment

Choose:

    Source: Deploy from a branch
    Branch: main
    Folder: /root

Save the settings. After a short wait, your homepage will be online.

## Customization

You can customize colors and spacing in the CSS variables near the top of `index.html`.

For example, edit:

    :root {
      --bg: #f5f5f7;
      --card: rgba(255, 255, 255, 0.94);
      --text: #1d1d1f;
      --link: #0066cc;
    }

You can also remove any section you do not need, such as `Selected Awards` or `Posts & Notes`.

## Notes

This template is intentionally simple. It does not use Jekyll, React, Vue, or any build system. Everything is contained in `index.html`, making it easy to understand, edit, and deploy.

## License

You may use, modify, and adapt this template for your personal academic homepage.
