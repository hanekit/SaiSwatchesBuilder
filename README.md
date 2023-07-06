# SaiSwatchesBuilder
A tool for generating PaintTool SAI's swatch files (*.saiswat) from hex text or image.



## Usage

下载 `colorboard.py`，在其同目录下创建 python 文件 `*.py`，编写所需代码即可。

Here is a template:

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

### RainbowSwatches

![Fig1](/assets/rainbow_saiswat.png)

