# SF Building & Carpentry — website

The website for SF Building & Carpentry (Stuart Freeth, Truro, Cornwall).
Live at https://freethstuart-jpg.github.io/SF-Building-Photos/

- `index.html` — the whole site (one page: work, services, about, how it works, contact).
- `logo.svg` — the SF roofline mark, used as the browser icon. `apple-touch-icon.png` is the phone home-screen icon and `og-image.jpg` is the preview shown when the link is shared.
- `images/projects/<project>/` — before, during and after photos for each project. A project can be split into rooms (see the flat renovation in `photos.json`).
- `images/gallery/` — single photos of other jobs.
- `images/photos.json` — the list of projects, their descriptions and photos. Add a new photo to a folder and list it here, and it appears on the site.
- `images/thumbs/` — smaller copies used in the photo grids. Rebuild them with `python3 tools/make_thumbs.py` after adding or removing photos.

Photos are cropped, resized to a maximum of 1600px and have location data removed before they're added.
