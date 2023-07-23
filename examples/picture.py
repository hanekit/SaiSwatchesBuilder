from colorboard import Colorboard
from PIL import Image

def rgba_to_rgb(r, g, b, a):
    alpha = a / 255.0

    # 使用白色背景的 RGB 颜色计算
    r_out = int((1 - alpha) * 255 + alpha * r)
    g_out = int((1 - alpha) * 255 + alpha * g)
    b_out = int((1 - alpha) * 255 + alpha * b)

    return r_out, g_out, b_out

def resize_image(image_path, new_width):
    # 打开原始图像
    image = Image.open(image_path)
    # 计算调整后的高度
    original_width, original_height = image.size
    new_height = int((new_width / original_width) * original_height)
    # 缩放图像
    resized_image = image.resize((new_width, new_height))

    return resized_image


def get_pixel_colors(image):
    # 获取图像中每个像素的颜色，并将其以#R2G2B2的格式储存在列表中
    pixel_colors = []
    width, height = image.size
    index = 1
    for y in range(height):
        for x in range(width):
            pixel_color = image.getpixel((x, y))
            if len(pixel_color) == 4:
                r, g, b, a = image.getpixel((x, y))
            else:
                r, g, b = image.getpixel((x, y))[:3]
                a = None
            if a == 0:
                # 跳过透明像素
                pass
            elif a is not None:
                r, g, b = rgba_to_rgb(r, g, b, a)
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                pixel_colors.append((index, hex_color))
            else:
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                pixel_colors.append((index, hex_color))
            index += 1
    return pixel_colors


# 主程序
if __name__ == "__main__":
    # 图片路径
    image_path = R"test.png"
    # 调整图像大小
    # 大=12 中=14 小=16
    resized_image = resize_image(image_path, 12)
    # 获取像素颜色列表
    pixel_colors = get_pixel_colors(resized_image)

    # Create empty swatch
    colorboard = Colorboard()
    # Add colors
    for index, color in pixel_colors:
        colorboard.add_color(index, color)
    # Check colors
    print(colorboard.colors)
    # Save file
    colorboard.save(R'test.saiswat')
