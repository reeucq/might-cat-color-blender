import numpy as np
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb_color):
    return "#{:02x}{:02x}{:02x}".format(
        int(rgb_color[0]), int(rgb_color[1]), int(rgb_color[2])
    )


def blend_colors(colors):
    lab_colors = []
    for color in colors:
        rgb_color = sRGBColor(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0)
        lab_color = convert_color(rgb_color, LabColor)
        lab_colors.append(lab_color)

    l_values = [color.lab_l for color in lab_colors]
    a_values = [color.lab_a for color in lab_colors]
    b_values = [color.lab_b for color in lab_colors]

    average_l = np.mean(l_values)
    average_a = np.mean(a_values)
    average_b = np.mean(b_values)

    blended_lab = LabColor(average_l, average_a, average_b)
    blended_rgb = convert_color(blended_lab, sRGBColor)
    blended_hex = rgb_to_hex(
        (blended_rgb.rgb_r * 255, blended_rgb.rgb_g * 255, blended_rgb.rgb_b * 255)
    )

    return blended_hex

color_list = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00"]
rgb_colors = [hex_to_rgb(color) for color in color_list]
blended_color = blend_colors(rgb_colors)
print("Blended color:", blended_color)
