import numpy as np

# Test background pixel: (242, 245, 242)
r, g, b = 242.0, 245.0, 242.0
exg = 2.0 * g - r - b
print(f"Background (242, 245, 242) ExG = {exg}")
is_light_bg = (r > 200) and (g > 200) and (b > 200) and (abs(r - g) < 15) and (abs(g - b) < 15)
print(f"Is background: {is_light_bg}")

# Test real green leaf pixel: (45, 160, 45)
r_l, g_l, b_l = 45.0, 160.0, 45.0
exg_l = 2.0 * g_l - r_l - b_l
print(f"Leaf (45, 160, 45) ExG = {exg_l}")
