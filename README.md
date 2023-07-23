# SaiSwatchesBuilder

<p align="center">
    <strong>English</strong> | <a href="./README_zh-CN.md">中文</a>
</p>

---

A tool for generating PaintTool SAI's swatches files (`*.saiswat`) from hex text or image.

## Usage

Download the `colorboard.py`, and create a python file `*.py` in the same directory, and write your code.

Here is a template in `examples/example.py` :

```python
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

```

Then just copy the generated swatch file `*.saiswat` to the swatch folder¹.

¹ : `...\Documents\SYSTEMAX Software Development\SAIv2\settings\swatch\` 

## Examples

### From math function

#### **> Rainbow swatches:**

see `examples/rainbow.py`

![](/assets/rainbow_saiswat.png)

### From PNG file

see `examples/picture.py`

#### **> Bulb swatches:**

**Original file (12 × 12 px) :**

![](/assets/bulb.png)

**Generated swatches:**

![](/assets/bulb_saiswat.png)

#### **> Blue swatches:**

**Original file (500 × 500 px) :**

![](/assets/blue.png)

**Generated swatches:**

![](/assets/blue_saiswat.png)

