from colorboard import Colorboard

# Create empty swatch
colorboard = Colorboard()
# Add color without keywords
colorboard.add_color(1, '#FF0000')
# Add color with keywords
colorboard.add_color(index=2, color='#00FF00')
# Check colors
print(colorboard.colors)
# Save file
colorboard.save('example.saiswat')
