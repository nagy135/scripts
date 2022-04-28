from PIL import Image
import numpy as np

im = Image.open('/home/infiniter/Pictures/nix_gray.png')
im = im.convert('RGBA')

data = np.array(im)

red, green, blue, alpha = data.T # Temporarily unpack the bands for readability
# Replace white with red... (leaves alpha values alone...)
white_areas = (red == 40) & (green == 42) & (blue == 54)
data[..., :-1][white_areas.T] = (11, 11, 11) # Transpose back needed

im2 = Image.fromarray(data)
im2.save("/home/infiniter/Pictures/current_wallpaper.png")
