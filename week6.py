import requests
import os
from urllib.parse import urlparse
import hashlib

# Directory for saving images
SAVE_DIR = "Fetched_Images"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB limit

def hash_content(content):
    """Return an MD5 hash of the file content."""
    return hashlib.md5(content).hexdigest()

def fetch_image(url, downloaded_hashes):
    try:
        response = requests.get(url, timeout=30, stream=True)
        response.raise_for_status()

        # Check content type
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipping {url} — not an image (Content-Type: {content_type})")
            return

        # Check content length
        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > MAX_FILE_SIZE:
            print(f"✗ Skipping {url} — file too large ({int(content_length)/1024/1024:.2f} MB)")
            return

        # Read content
        content = response.content

        # Check for duplicates
        content_hash = hash_content(content)
        if content_hash in downloaded_hashes:
            print(f"✗ Skipping {url} — duplicate detected.")
            return
        downloaded_hashes.add(content_hash)

        # Extract filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = f"downloaded_image_{len(downloaded_hashes)}.jpg"

        filepath = os.path.join(SAVE_DIR, filename)

        # Avoid overwriting if same filename exists
        if os.path.exists(filepath):
            base, ext = os.path.splitext(filename)
            filename = f"{base}_{len(downloaded_hashes)}{ext}"
            filepath = os.path.join(SAVE_DIR, filename)

        # Save file
        with open(filepath, "wb") as f:
            f.write(content)

        print(f"✓ Saved {filename} ({len(content)} bytes)")
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ Error processing {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get multiple URLs from user
    urls = input("Enter image URLs (separated by commas): ").split(",")

    os.makedirs(SAVE_DIR, exist_ok=True)

    downloaded_hashes = set()

    for url in [u.strip() for u in urls if u.strip()]:
        fetch_image(url, downloaded_hashes)

    print("\n✅ Finished downloading images. Community enriched.")

if __name__ == "__main__":
    main()
