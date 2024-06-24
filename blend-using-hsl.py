import colorsys


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb_color):
    return "#{:02x}{:02x}{:02x}".format(
        int(rgb_color[0] * 255), int(rgb_color[1] * 255), int(rgb_color[2] * 255)
    )


def blend_colors(colors):
    hsl_colors = [
        colorsys.rgb_to_hls(*[c / 255.0 for c in hex_to_rgb(color)]) for color in colors
    ]

    hue_sum = sum(color[0] for color in hsl_colors)
    saturation_sum = sum(color[1] for color in hsl_colors)
    lightness_sum = sum(color[2] for color in hsl_colors)

    num_colors = len(colors)
    average_hue = hue_sum / num_colors
    average_saturation = saturation_sum / num_colors
    average_lightness = lightness_sum / num_colors

    blended_hsl = (average_hue, average_saturation, average_lightness)
    blended_rgb = colorsys.hls_to_rgb(*blended_hsl)
    blended_hex = rgb_to_hex(blended_rgb)

    return blended_hex


color_list = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00"]
blended_color = blend_colors(color_list)
print("Blended color:", blended_color)
