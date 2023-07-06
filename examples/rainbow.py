from colorboard import Colorboard
import colorsys


def generate_rainbow_colors(num_colors):
    rainbow_colors = []
    hue_step = 1.0 / num_colors
    for i in range(num_colors):
        hue = i * hue_step
        rgb = colorsys.hsv_to_rgb(hue, 0.5, 0.8)
        r, g, b = [int(val * 255) for val in rgb]
        hex_color = '#{:02X}{:02X}{:02X}'.format(r, g, b)
        rainbow_colors.append(hex_color)
    return rainbow_colors


# Create empty swatch
colorboard = Colorboard()
# Add colors
rainbow_colors = generate_rainbow_colors(10 * 12)
for index, color in enumerate(rainbow_colors, 1):
    colorboard.add_color(index, color)
# Check colors
print(colorboard.colors)
# Save file
colorboard.save('rainbow.saiswat')
