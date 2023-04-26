import math

def compare_color(payload_color, target_color):
    if payload_color == target_color:
        return 1
    else:
        from colormath.color_objects import sRGBColor, LabColor
        from colormath.color_conversions import convert_color
        from deltae2000 import delta_e_cie2000
        color1_lab = 0;
        color2_lab = 0;
        if (payload_color == 'RED'):
            payload_color_rgb = sRGBColor(255, 0, 0)
            color1_lab = convert_color(payload_color_rgb, LabColor)
        elif (payload_color == 'ORANGE'):
            payload_color_rgb = sRGBColor(255, 128, 0)
            color1_lab = convert_color(payload_color_rgb, LabColor)
        elif (payload_color == 'YELLOW'):
            payload_color_rgb = sRGBColor(255, 255, 0)
            color1_lab = convert_color(payload_color_rgb, LabColor)
        elif (payload_color == 'GREEN'):
            payload_color_rgb = sRGBColor(0, 255, 0)
            color1_lab = convert_color(payload_color_rgb, LabColor)
        elif (payload_color == 'BLUE'):
            payload_color_rgb = sRGBColor(0, 0, 255)
            color1_lab = convert_color(payload_color_rgb, LabColor)
        elif (payload_color == 'PURPLE'):
            payload_color_rgb = sRGBColor(128, 0, 128)
            color1_lab = convert_color(payload_color_rgb, LabColor)
        elif (payload_color == 'BLACK'):
            payload_color_rgb = sRGBColor(0, 0, 0)
            color1_lab = convert_color(payload_color_rgb, LabColor)
        elif (payload_color == 'WHITE'):
            payload_color_rgb = sRGBColor(255, 255, 255)
            color1_lab = convert_color(payload_color_rgb, LabColor)
        elif (payload_color == 'GRAY'):
            payload_color_rgb = sRGBColor(128, 128, 128)
            color1_lab = convert_color(payload_color_rgb, LabColor)
        else: # Brown
            payload_color_rgb = sRGBColor(150, 75, 0)
            color1_lab = convert_color(payload_color_rgb, LabColor)

        if (target_color == 'RED'):
            target_color_rgb = sRGBColor(255, 0, 0)
            color2_lab = convert_color(target_color_rgb, LabColor)
        elif (target_color == 'ORANGE'):
            target_color_rgb = sRGBColor(255, 128, 0)
            color2_lab = convert_color(target_color_rgb, LabColor)
        elif (target_color == 'YELLOW'):
            target_color_rgb = sRGBColor(255, 255, 0)
            color2_lab = convert_color(target_color_rgb, LabColor)
        elif (target_color == 'GREEN'):
            target_color_rgb = sRGBColor(0, 255, 0)
            color2_lab = convert_color(target_color_rgb, LabColor)
        elif (target_color == 'BLUE'):
            target_color_rgb = sRGBColor(0, 0, 255)
            color2_lab = convert_color(target_color_rgb, LabColor)
        elif (target_color == 'PURPLE'):
            target_color_rgb = sRGBColor(128, 0, 128)
            color2_lab = convert_color(target_color_rgb, LabColor)
        elif (target_color == 'BLACK'):
            target_color_rgb = sRGBColor(0, 0, 0)
            color2_lab = convert_color(target_color_rgb, LabColor)
        elif (target_color == 'WHITE'):
            target_color_rgb = sRGBColor(255, 255, 255)
            color2_lab = convert_color(target_color_rgb, LabColor)
        elif (target_color == 'GRAY'):
            target_color_rgb = sRGBColor(128, 128, 128)
            color2_lab = convert_color(target_color_rgb, LabColor)
        else: # Brown
            target_color_rgb = sRGBColor(150, 75, 0)
            color2_lab = convert_color(target_color_rgb, LabColor)

        # Finding the difference
        diff = abs(0.001*(1000-delta_e_cie2000(color1_lab, color2_lab)))

        return diff

def compare_shape(payload_shape, target_shape):
    if payload_shape == 'quartercircle':
        if target_shape == 'quartercircle':
            return 1;
        elif target_shape == 'triangle':
            return 0
        elif target_shape == 'cross':
            return 0
        elif target_shape == 'star':
            return 0
        elif target_shape == 'square':
            return 0
        elif target_shape == 'rectangle':
            return 0
        elif target_shape == 'semicircle':
            return 0
        elif target_shape == 'trapezoid':
            return 0
        elif target_shape == 'pentagon':
            return 0
        elif target_shape == 'hexagon':
            return 0
        elif target_shape == 'heptagon':
            return 0
        elif target_shape == 'octagon':
            return 0
        else:
            return 0
    elif payload_shape == 'triangle':
        if target_shape == 'quartercircle':
            return 0;
        elif target_shape == 'triangle':
            return 1
        elif target_shape == 'cross':
            return 0
        elif target_shape == 'star':
            return 0
        elif target_shape == 'square':
            return 0
        elif target_shape == 'rectangle':
            return 0
        elif target_shape == 'semicircle':
            return 0
        elif target_shape == 'trapezoid':
            return 0
        elif target_shape == 'pentagon':
            return 0
        elif target_shape == 'hexagon':
            return 0
        elif target_shape == 'heptagon':
            return 0
        elif target_shape == 'octagon':
            return 0
        else:
            return 0
    elif payload_shape == 'cross':
        if target_shape == 'quartercircle':
            return 0;
        elif target_shape == 'triangle':
            return 0
        elif target_shape == 'cross':
            return 1
        elif target_shape == 'star':
            return 0
        elif target_shape == 'square':
            return 0
        elif target_shape == 'rectangle':
            return 0
        elif target_shape == 'semicircle':
            return 0
        elif target_shape == 'trapezoid':
            return 0
        elif target_shape == 'pentagon':
            return 0
        elif target_shape == 'hexagon':
            return 0
        elif target_shape == 'heptagon':
            return 0
        elif target_shape == 'octagon':
            return 0
        else:
            return 0
    elif payload_shape == 'star':
        if target_shape == 'quartercircle':
            return 0;
        elif target_shape == 'triangle':
            return 0
        elif target_shape == 'cross':
            return 0
        elif target_shape == 'star':
            return 1
        elif target_shape == 'square':
            return 0
        elif target_shape == 'rectangle':
            return 0
        elif target_shape == 'semicircle':
            return 0
        elif target_shape == 'trapezoid':
            return 0
        elif target_shape == 'pentagon':
            return 0
        elif target_shape == 'hexagon':
            return 0
        elif target_shape == 'heptagon':
            return 0
        elif target_shape == 'octagon':
            return 0
        else:
            return 0
    elif payload_shape == 'square':
        if target_shape == 'quartercircle':
            return 0;
        elif target_shape == 'triangle':
            return 0
        elif target_shape == 'cross':
            return 0
        elif target_shape == 'star':
            return 0
        elif target_shape == 'square':
            return 1
        elif target_shape == 'rectangle':
            return 0
        elif target_shape == 'semicircle':
            return 0
        elif target_shape == 'trapezoid':
            return 0
        elif target_shape == 'pentagon':
            return 0
        elif target_shape == 'hexagon':
            return 0
        elif target_shape == 'heptagon':
            return 0
        elif target_shape == 'octagon':
            return 0
        else:
            return 0
    elif payload_shape == 'rectangle':
        if target_shape == 'quartercircle':
            return 0;
        elif target_shape == 'triangle':
            return 0
        elif target_shape == 'cross':
            return 0
        elif target_shape == 'star':
            return 0
        elif target_shape == 'square':
            return 0
        elif target_shape == 'rectangle':
            return 1
        elif target_shape == 'semicircle':
            return 0
        elif target_shape == 'trapezoid':
            return 0
        elif target_shape == 'pentagon':
            return 0
        elif target_shape == 'hexagon':
            return 0
        elif target_shape == 'heptagon':
            return 0
        elif target_shape == 'octagon':
            return 0
        else:
            return 0
    elif payload_shape == 'semicircle':
        if target_shape == 'quartercircle':
            return 0;
        elif target_shape == 'triangle':
            return 0
        elif target_shape == 'cross':
            return 0
        elif target_shape == 'star':
            return 0
        elif target_shape == 'square':
            return 0
        elif target_shape == 'rectangle':
            return 0
        elif target_shape == 'semicircle':
            return 1
        elif target_shape == 'trapezoid':
            return 0
        elif target_shape == 'pentagon':
            return 0
        elif target_shape == 'hexagon':
            return 0
        elif target_shape == 'heptagon':
            return 0
        elif target_shape == 'octagon':
            return 0
        else:
            return 0
    elif payload_shape == 'trapezoid':
        if target_shape == 'quartercircle':
            return 0;
        elif target_shape == 'triangle':
            return 0
        elif target_shape == 'cross':
            return 0
        elif target_shape == 'star':
            return 0
        elif target_shape == 'square':
            return 0
        elif target_shape == 'rectangle':
            return 0
        elif target_shape == 'semicircle':
            return 0
        elif target_shape == 'trapezoid':
            return 1
        elif target_shape == 'pentagon':
            return 0
        elif target_shape == 'hexagon':
            return 0
        elif target_shape == 'heptagon':
            return 0
        elif target_shape == 'octagon':
            return 0
        else:
            return 0
    elif payload_shape == 'pentagon':
        if target_shape == 'quartercircle':
            return 0;
        elif target_shape == 'triangle':
            return 0
        elif target_shape == 'cross':
            return 0
        elif target_shape == 'star':
            return 0
        elif target_shape == 'square':
            return 0
        elif target_shape == 'rectangle':
            return 0
        elif target_shape == 'semicircle':
            return 0
        elif target_shape == 'trapezoid':
            return 0
        elif target_shape == 'pentagon':
            return 1
        elif target_shape == 'hexagon':
            return 0
        elif target_shape == 'heptagon':
            return 0
        elif target_shape == 'octagon':
            return 0
        else:
            return 0
    elif payload_shape == 'hexagon':
        if target_shape == 'quartercircle':
            return 0;
        elif target_shape == 'triangle':
            return 0
        elif target_shape == 'cross':
            return 0
        elif target_shape == 'star':
            return 0
        elif target_shape == 'square':
            return 0
        elif target_shape == 'rectangle':
            return 0
        elif target_shape == 'semicircle':
            return 0
        elif target_shape == 'trapezoid':
            return 0
        elif target_shape == 'pentagon':
            return 0
        elif target_shape == 'hexagon':
            return 1
        elif target_shape == 'heptagon':
            return 0
        elif target_shape == 'octagon':
            return 0
        else:
            return 0
    elif payload_shape == 'heptagon':
        if target_shape == 'quartercircle':
            return 0;
        elif target_shape == 'triangle':
            return 0
        elif target_shape == 'cross':
            return 0
        elif target_shape == 'star':
            return 0
        elif target_shape == 'square':
            return 0
        elif target_shape == 'rectangle':
            return 0
        elif target_shape == 'semicircle':
            return 0
        elif target_shape == 'trapezoid':
            return 0
        elif target_shape == 'pentagon':
            return 0
        elif target_shape == 'hexagon':
            return 0
        elif target_shape == 'heptagon':
            return 1
        elif target_shape == 'octagon':
            return 0
        else:
            return 0
    elif payload_shape == 'octagon':
        if target_shape == 'quartercircle':
            return 0;
        elif target_shape == 'triangle':
            return 0
        elif target_shape == 'cross':
            return 0
        elif target_shape == 'star':
            return 0
        elif target_shape == 'square':
            return 0
        elif target_shape == 'rectangle':
            return 0
        elif target_shape == 'semicircle':
            return 0
        elif target_shape == 'trapezoid':
            return 0
        elif target_shape == 'pentagon':
            return 0
        elif target_shape == 'hexagon':
            return 0
        elif target_shape == 'heptagon':
            return 0
        elif target_shape == 'octagon':
            return 1
        else:
            return 0
    else:
        if target_shape == 'quartercircle':
            return 0;
        elif target_shape == 'triangle':
            return 0
        elif target_shape == 'cross':
            return 0
        elif target_shape == 'star':
            return 0
        elif target_shape == 'square':
            return 0
        elif target_shape == 'rectangle':
            return 0
        elif target_shape == 'semicircle':
            return 0
        elif target_shape == 'trapezoid':
            return 0
        elif target_shape == 'pentagon':
            return 0
        elif target_shape == 'hexagon':
            return 0
        elif target_shape == 'heptagon':
            return 0
        elif target_shape == 'octagon':
            return 0
        else:
            return 1


def compare_alphanum(payload_alphanum, target_alphanum):
    target_alphanum = target_alphanum.lower();
    payload_alphanum = payload_alphanum.lower();
    if payload_alphanum == 'a':
        if target_alphanum == 'a':
            return 1
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == 'b':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 1
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0

    elif payload_alphanum == 'c':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 1
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == 'd':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 1
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0

    elif payload_alphanum == 'e':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 1
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0

    elif payload_alphanum == 'f':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 1
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0

        elif payload_alphanum == 'g':
            if target_alphanum == 'a':
                return 0
            elif target_alphanum == 'b':
                return 0
            elif target_alphanum == 'c':
                return 0
            elif target_alphanum == 'd':
                return 0
            elif target_alphanum == 'e':
                return 0
            elif target_alphanum == 'f':
                return 0
            elif target_alphanum == 'g':
                return 1
            elif target_alphanum == 'h':
                return 0
            elif target_alphanum == 'i':
                return 0
            elif target_alphanum == 'j':
                return 0
            elif target_alphanum == 'k':
                return 0
            elif target_alphanum == 'l':
                return 0
            elif target_alphanum == 'm':
                return 0
            elif target_alphanum == 'n':
                return 0
            elif target_alphanum == 'o':
                return 0
            elif target_alphanum == 'p':
                return 0
            elif target_alphanum == 'q':
                return 0
            elif target_alphanum == 'r':
                return 0
            elif target_alphanum == 's':
                return 0
            elif target_alphanum == 't':
                return 0
            elif target_alphanum == 'u':
                return 0
            elif target_alphanum == 'v':
                return 0
            elif target_alphanum == 'w':
                return 0
            elif target_alphanum == 'x':
                return 0
            elif target_alphanum == 'y':
                return 0
            elif target_alphanum == 'z':
                return 0
            elif target_alphanum == '0':
                return 0
            elif target_alphanum == '1':
                return 0
            elif target_alphanum == '2':
                return 0
            elif target_alphanum == '3':
                return 0
            elif target_alphanum == '4':
                return 0
            elif target_alphanum == '5':
                return 0
            elif target_alphanum == '6':
                return 0
            elif target_alphanum == '7':
                return 0
            elif target_alphanum == '8':
                return 0
            elif target_alphanum == '9':
                return 0

    elif payload_alphanum == 'h':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 1
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0

    elif payload_alphanum == 'i':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 1
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0

    elif payload_alphanum == 'j':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 1
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0

    elif payload_alphanum == 'k':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 1
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == 'l':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 1
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == 'm':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 1
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == 'n':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 1
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == 'o':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 1
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == 'p':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 1
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == 'q':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 1
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == 'r':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 1
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == 's':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 1
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == 't':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 1
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == 'u':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 1
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == 'v':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 1
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == 'w':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 1
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == 'x':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 1
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == 'y':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 1
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == 'z':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 1
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == '0':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 1
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == '1':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 1
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == '2':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 1
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == '3':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 1
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0

    elif payload_alphanum == '4':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 1
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0

    elif payload_alphanum == '5':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 1
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == '6':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 1
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == '7':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 1
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == '8':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 1
        elif target_alphanum == '9':
            return 0
    elif payload_alphanum == '9':
        if target_alphanum == 'a':
            return 0
        elif target_alphanum == 'b':
            return 0
        elif target_alphanum == 'c':
            return 0
        elif target_alphanum == 'd':
            return 0
        elif target_alphanum == 'e':
            return 0
        elif target_alphanum == 'f':
            return 0
        elif target_alphanum == 'g':
            return 0
        elif target_alphanum == 'h':
            return 0
        elif target_alphanum == 'i':
            return 0
        elif target_alphanum == 'j':
            return 0
        elif target_alphanum == 'k':
            return 0
        elif target_alphanum == 'l':
            return 0
        elif target_alphanum == 'm':
            return 0
        elif target_alphanum == 'n':
            return 0
        elif target_alphanum == 'o':
            return 0
        elif target_alphanum == 'p':
            return 0
        elif target_alphanum == 'q':
            return 0
        elif target_alphanum == 'r':
            return 0
        elif target_alphanum == 's':
            return 0
        elif target_alphanum == 't':
            return 0
        elif target_alphanum == 'u':
            return 0
        elif target_alphanum == 'v':
            return 0
        elif target_alphanum == 'w':
            return 0
        elif target_alphanum == 'x':
            return 0
        elif target_alphanum == 'y':
            return 0
        elif target_alphanum == 'z':
            return 0
        elif target_alphanum == '0':
            return 0
        elif target_alphanum == '1':
            return 0
        elif target_alphanum == '2':
            return 0
        elif target_alphanum == '3':
            return 0
        elif target_alphanum == '4':
            return 0
        elif target_alphanum == '5':
            return 0
        elif target_alphanum == '6':
            return 0
        elif target_alphanum == '7':
            return 0
        elif target_alphanum == '8':
            return 0
        elif target_alphanum == '9':
            return 1

def compare(payload, target):
    score = 0;
    #shape
    score += compare_shape(payload.shape == target.shape)
    #shape_color
    score += compare_color(payload.shapeColor, target.shapeColor)
    #alphanum color
    score += compare_color(payload.alphanumColor, target.alphanumColor)
    #alphanum
    score += compare_alphanum(payload.alphanum, target.alphanum)
    return score



def calculate_dist(drone_lat, drone_lon, target_lat, target_lon):
    dLat = (target_lat-drone_lat) * math.pi / 180
    dLon = (target_lon-drone_lon)*math.pi/180
    lat1 = drone_lat * math.pi / 180
    lat2 = target_lat * math.pi / 180
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.sin(dLon / 2) * math.sin(dLon / 2) * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return c

def sort_targets(targets, drone_lat, drone_lon):
    sorted_targets = []
    target_order = [];
    for i in range(len(targets)):
        target_lat = targets[i]['latitude']
        target_lon = targets[i]['longitude']
        target_distance = calculate_dist(drone_lat, drone_lon, target_lat, target_lon);
        target_order.append([target_distance, i])
    target_order.sort()
    for order in target_order:
        index = order[1]
        sorted_targets.append(targets[index])

    return sorted_targets

def order_payloads(payloads, targets):
    payload_order = []
    target_scores = []
    hasConflicts = False
    unassigned_targets = []
    unassigned_payloads = [0, 1, 2, 3, 4]
    ordered_payloads = []

    for target in targets:
        payload_scores = []
        for payload in payloads:
            payload_score = compare(payload, target)
            payload_scores.append(payload_score)
        target_scores.append(payload_scores)

    for payload_scores in target_scores:
        payload_order.append(payload_scores.index(max(payload_scores)))

    for index in payload_order:
        if payload_order.count(index) > 1: hasConflicts = True
        else: hasConflicts = False

    if hasConflicts:
        for i in range(len(payload_order)):
            if payload_order.count(payload_order[i]) != 1:
                unassigned_targets.append(i)
            if payload_order.count(payload_order[i]) == 1:
                unassigned_payloads.remove(payload_order[i])
            for j in range(len(unassigned_targets)):
                payload_order[unassigned_targets[j]] = unassigned_payloads[j]
        for payload_index in payload_order:
            ordered_payloads.append(payloads[payload_index])
    else:
        for payload_index in payload_order:
            ordered_payloads.append(payloads[payload_index])
    return ordered_payloads

def close_enough_test_cases(drone_lat, drone_lon, payloads, targets):
    sorted_targets = sort_targets(targets, drone_lat, drone_lon)
    return order_payloads(payloads, sorted_targets)









