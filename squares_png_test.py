from PIL import Image
import numpy as np

# Image size
width, height = 100, 100

# Number of shades of gray
num_shades = 10
gray_levels = np.linspace(255, 0, num_shades, dtype=np.uint8)

# Center coordinates
cx, cy = width // 2, height // 2

# Create coordinate grids
y, x = np.ogrid[:height, :width]

# Distance from center in square layers
square_dist = np.maximum(np.abs(x - cx), np.abs(y - cy))

# Normalize to map into shade levels
max_square_dist = square_dist.max()
shade_indices = np.clip(
    (square_dist / max_square_dist * num_shades).astype(int), 0, num_shades - 1
)

# Apply gray levels
image_array = gray_levels[shade_indices]

# Optional: force center square to be pure white
center_size = 20
half = center_size // 2
image_array[cy - half : cy + half, cx - half : cx + half] = 255

# Save as image
img = Image.fromarray(image_array, mode="L")
img.save("concentric_squares.png")
