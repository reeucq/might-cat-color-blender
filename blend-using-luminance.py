import math


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb_color):
    return "#{:02x}{:02x}{:02x}".format(*rgb_color)


def calculate_luminance(rgb_color):
    r, g, b = rgb_color
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def blend_colors(colors):
    rgb_colors = [hex_to_rgb(color) for color in colors]

    total_luminance = sum(calculate_luminance(color) for color in rgb_colors)

    red_weighted_sum = sum(
        color[0] * calculate_luminance(color) for color in rgb_colors
    )
    green_weighted_sum = sum(
        color[1] * calculate_luminance(color) for color in rgb_colors
    )
    blue_weighted_sum = sum(
        color[2] * calculate_luminance(color) for color in rgb_colors
    )

    blended_red = math.floor(red_weighted_sum / total_luminance)
    blended_green = math.floor(green_weighted_sum / total_luminance)
    blended_blue = math.floor(blue_weighted_sum / total_luminance)

    blended_rgb = (blended_red, blended_green, blended_blue)
    blended_hex = rgb_to_hex(blended_rgb)

    return blended_hex


color_list = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00"]
blended_color = blend_colors(color_list)
print("Blended color:", blended_color)
