import math


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb_color):
    return "#{:02x}{:02x}{:02x}".format(*rgb_color)


def blend_colors(colors):
    rgb_colors = [hex_to_rgb(color) for color in colors]

    red_sum = sum(color[0] for color in rgb_colors)
    green_sum = sum(color[1] for color in rgb_colors)
    blue_sum = sum(color[2] for color in rgb_colors)

    num_colors = len(colors)
    average_red = math.floor(red_sum / num_colors)
    average_green = math.floor(green_sum / num_colors)
    average_blue = math.floor(blue_sum / num_colors)

    blended_rgb = (average_red, average_green, average_blue)
    blended_hex = rgb_to_hex(blended_rgb)

    return blended_hex


color_list = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00"]
blended_color = blend_colors(color_list)
print("Blended color:", blended_color)
