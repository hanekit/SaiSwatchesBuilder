# SaiSwatchesBuilder

A tool for generating PaintTool SAI's swatch files (*.saiswat) from hex text or image.

## Usage

下载 `colorboard.py`，在其同目录下创建 python 文件 `*.py`，编写所需代码即可。

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

将生成的色板文件 `*.saiswat` 复制到色板文件夹¹ 即可。

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

