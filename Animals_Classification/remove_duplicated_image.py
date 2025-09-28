import os
from PIL import Image
import imagehash

# Folder containing images
folder_path = r"C:\Users\sevug\Desktop\New folder\pantech_solutions\simple_images\Elephant"

# Dictionary to store hashes
hashes = {}

# Loop through all files in folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Skip non-images
    try:
        img = Image.open(file_path)
    except:
        continue

    # Compute hash (phash is robust to minor changes)
    img_hash = imagehash.phash(img)

    # If hash exists, it's a duplicate
    if img_hash in hashes:
        print(f"Duplicate found: {filename} (same as {hashes[img_hash]})")
        os.remove(file_path)  # Remove the duplicate
    else:
        hashes[img_hash] = filename

print("Duplicate removal complete!")
