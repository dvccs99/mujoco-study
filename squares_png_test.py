from PIL import Image
import numpy as np

# Image size
width, height = 100, 100

# Create 10 descending shades from white to black and then mirror them
half_shades = np.linspace(255, 0, 10, dtype=np.uint8)
gray_levels = np.concatenate([half_shades, half_shades[::-1]])
num_bands = len(gray_levels)  # should be 20

# Center coordinates
cx, cy = width // 2, height // 2

# Create coordinate grids
y, x = np.ogrid[:height, :width]
square_dist = np.maximum(np.abs(x - cx), np.abs(y - cy))

# White center settings: a larger white square (40x40)
center_size = 40
half_center = center_size // 2

# Create a mask for the white center
white_mask = square_dist < half_center

# For pixels outside the white center, we want to map their distance
# (starting from the white center edge) to band indices from 1 to 19.
# Compute the distance offset from the white center boundary:
d = np.maximum(0, square_dist - half_center)
max_d = d.max()  # Maximum distance outside the white center

# Calculate the band index so that:
# - At d = 0 (right at the white boundary), index will be 1 (just a bit darker than white)
# - At d = max_d, index will reach 19.
band_indices = np.clip(
    ((d / max_d) * (num_bands - 1)).astype(int) + 1, 0, num_bands - 1
)

# Map the band indices to gray levels
image_array = gray_levels[band_indices]

# Override the white center with pure white
image_array[white_mask] = 255

# Create and save the image
img = Image.fromarray(image_array, mode="L")
img.save("concentric_squares_wave_fixed.png")
