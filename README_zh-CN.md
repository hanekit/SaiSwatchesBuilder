# SaiSwatchesBuilder

<p align="center">
    <a href="./README.md">English</a> | <strong>中文</strong>
</p>

---

用于从十六进制文本或图像生成 PaintTool SAI 的色板文件 (`*.saiswat`) 的工具。

## 用法

下载 `colorboard.py`，在其同目录下创建 python 文件 `*.py`，编写所需代码即可。

以下是一个基本示例 `examples/example.py` :

```python
from colorboard import Colorboard

# 创建空白色板对象
colorboard = Colorboard()
# 添加颜色（简易版）
colorboard.add_color(1, '#FF0000')
# 添加颜色（带参数版）
colorboard.add_color(index=2, color='#00FF00')
# 查看色板颜色
print(colorboard.colors)
# 保存文件
colorboard.save('example.saiswat')

```

将生成的色板文件 `*.saiswat` 复制到色板文件夹¹ 即可。

¹ : `...\Documents\SYSTEMAX Software Development\SAIv2\settings\swatch\` 

## 例子

### 通过数学表达式生成

#### **> 彩虹色色板：**

见 `examples/rainbow.py`

![](/assets/rainbow_saiswat.png)

### 通过 PNG 图片生成

见 `examples/picture.py`

#### **> 灯泡色板：**

**原始图片 (12 × 12 px)：**

![](/assets/bulb.png)

**生成色板：**

![](/assets/bulb_saiswat.png)

#### **> 蓝色色板：**

**原始图片 (500 × 500 px)：**

![](/assets/blue.png)

**生成色板：**

![](/assets/blue_saiswat.png)

