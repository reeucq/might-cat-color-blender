import math


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return f"#{int(rgb[0]):02x}{int(rgb[1]):02x}{int(rgb[2]):02x}"


def blend_colors(hex_colors):
    num_colors = len(hex_colors)
    product_r = product_g = product_b = 1
    for hex_color in hex_colors:
        r, g, b = hex_to_rgb(hex_color)
        product_r *= r if r > 0 else 1
        product_g *= g if g > 0 else 1
        product_b *= b if b > 0 else 1

    geo_mean_r = round(product_r ** (1 / num_colors))
    geo_mean_g = round(product_g ** (1 / num_colors))
    geo_mean_b = round(product_b ** (1 / num_colors))

    return rgb_to_hex((geo_mean_r, geo_mean_g, geo_mean_b))


colors = ["#FF5733", "#4DE345", "#CDDC39"]
blended_color = blend_colors(colors)
print("Blended color:", blended_color)
