class Colorboard:
    def __init__(self):
        self.colors = {}

    def hex_to_bytes(self, hex_string: str) -> bytes:
        return bytes.fromhex(hex_string.replace(" ", ""))

    def index_to_hex(self, index: int, max_value=0xffff) -> str:
        """
        将序号转换为特殊顺序的十六进制数。

        参数:
            index (int): 要转换的十进制数。

        返回:
            str: 转换后的特殊顺序十六进制字符串。

        示例:
            >>> index_to_hex(301)
            '2c01'
        """
        if not isinstance(index, int):
            raise TypeError('参数类型必须为整数')
        index = index - 1
        if not 0x0000 <= index <= max_value:
            raise ValueError(f'参数超出范围（1 ~ {max_value}）')
        else:
            hex_str = format(index, "04x")
        reversed_hex = hex_str[2:4]+hex_str[0:2]
        return reversed_hex

    def color_to_hex(self, color: str) -> str:
        """
        将颜色字符串转换为BGR格式的字符串。

        参数:
            color (str): 要转换的颜色字符串，以'#'开头，后跟6位十六进制字符。

        返回:
            str: 转换后的特殊顺序十六进制字符串。

        示例:
            >>> convert_color("#ABCDEF")
            "efefcdcd"
        """
        # 去除 '#' 字符
        color = color.lstrip('#')

        # 重组字符串
        r, g, b = color[0:2], color[2:4], color[4:6]
        r, g, b = int(r, 16), int(g, 16), int(b, 16)
        rrggbb = "{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}".format(b, b, g, g, r, r)

        return rrggbb

    def colors_to_hex(self) -> bytes:
        colors_hex = ""
        for index in sorted(self.colors.keys()):  # 对字典的键进行排序
            color = self.colors[index]  # 获取对应的颜色值
            index_hex = self.index_to_hex(index)
            color_hex = self.color_to_hex(color)
            colors_hex += "0000 0100" + index_hex + color_hex
        print(colors_hex)
        return colors_hex

    def add_color(self, index: int, color: str, override=False) -> None:
        """
        添加颜色对到色板。

        参数:
            index (int): 颜色对的序号。
            color (str): 要添加的颜色。
        """
        if index in self.colors and not override:
            raise ValueError(f"序号 '{index}' 已定义颜色，如果需要覆盖，需开启 `override=True` .")
        if index not in self.colors:
            self.colors[index] = color

    def get_sub_header(self, boardsize="big"):
        # TODO: 这行编码尚未完全解密完成，目前仅支持添加到最多 4095 个颜色
        # sub_header = "???? 0000 0200 {boardsize_hex} ???? {max_index_hex}"
        boardsize_dic = {"big": "0000 0000",
                         "middle": "0000 0100",
                         "small": "0000 0200"}
        boardsize_hex = boardsize_dic[boardsize]

        max_index = max(self.colors.keys())
        max_index_hex = self.index_to_hex(max_index+1, max_value=0xfff)

        sub_header = f"5207 0000 0200 {boardsize_hex} 0000 {max_index_hex}"
        return sub_header

    def read(self, path: str) -> None:
        raise NotImplementedError("读取文件功能尚未实现，请等待更新。")

    def save(self, path: str) -> None:
        """
        将颜色写入到色板文件中。

        参数:
            path (str): 色板文件的路径。
        """
        HEADER = b"SAI-SWATCH-TYPE0"
        sub_header = self.hex_to_bytes(self.get_sub_header())
        colors = self.hex_to_bytes(self.colors_to_hex())
        FOOTER = self.hex_to_bytes("0000 0000 0000")
        with open(path, 'wb') as file:
            file.write(HEADER)
            file.write(sub_header)
            file.write(colors)
            file.write(FOOTER)


# Example
if __name__ == "__main__":
    # Create empty swatch
    colorboard = Colorboard()
    # Add color without keywords
    colorboard.add_color(1, '#FF0000')
    colorboard.add_color(4095, '#333333')
    # Add color with keywords
    colorboard.add_color(index=2, color='#00FF00')
    # Check colors
    print(colorboard.colors)
    # Save file
    colorboard.save('example.saiswat')
