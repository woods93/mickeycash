# Mickey Cash — website

Single-page static site (GitHub Pages). Preview: https://woods93.github.io/mickeycash/

## Edit
- Content and links live in `build.py`. Run `python3 build.py` to regenerate `index.html`, then commit and push.
- Drop files in `assets/images/` and `assets/audio/`:
  - `assets/images/hero.jpg` — portrait; the hero shows it automatically when it exists
  - `assets/images/victory-cover.jpg` — album art, shown in the Music section when it exists
  - audio: add `("Title", "assets/audio/file.mp3")` to the `AUDIO` list in `build.py`
- Contact form: paste the Web3Forms access key into `WEB3FORMS_KEY` in `build.py`.

## To confirm with Mickey
- Exact wording of the Cash family relationship (bio says only "She comes from the Cash family")
- Streaming links beyond Apple Music (Spotify, Bandcamp, etc.), social profiles
- That her booking email can be public, and the final bio text
- Hero photo and album art files
