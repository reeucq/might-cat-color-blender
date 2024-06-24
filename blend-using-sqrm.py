import math


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return f"#{int(rgb[0]):02x}{int(rgb[1]):02x}{int(rgb[2]):02x}"


def blend_hex_colors_root_mean_square(hex_colors):
    num_colors = len(hex_colors)
    sum_r = sum_g = sum_b = 0
    for hex_color in hex_colors:
        r, g, b = hex_to_rgb(hex_color)
        sum_r += r**2
        sum_g += g**2
        sum_b += b**2

    rms_r = round(math.sqrt(sum_r / num_colors))
    rms_g = round(math.sqrt(sum_g / num_colors))
    rms_b = round(math.sqrt(sum_b / num_colors))

    return rgb_to_hex((rms_r, rms_g, rms_b))


colors = ["#FF5733", "#4DE345", "#CDDC39"]
blended_color = blend_hex_colors_root_mean_square(colors)
print("Blended Color", blended_color)
