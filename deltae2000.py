import math
from colormath.color_objects import LabColor


def delta_e_cie2000(color1: LabColor, color2: LabColor):
    """
    Return the Delta-E CIE2000 distance between the colours.

    This implementation is intended to be used with PyPy. If using CPython
    then the colormath library has a faster numpy implementation.
    """
    l1, a1, b1 = color1.lab_l, color1.lab_a, color1.lab_b
    l2, a2, b2 = color2.lab_l, color2.lab_a, color2.lab_b

    avg_lp = (l1 + l2) / 2

    c1 = hypot([a1, b1])
    c2 = hypot([a2, b2])
    c_delta = (c1 + c2) / 2

    g = 0.5 * (1 - math.sqrt(c_delta ** 7.0 / (c_delta ** 7.0 + 25.0 ** 7.0)))
    a1p = (1.0 + g) * a1
    a2p = (1.0 + g) * a2

    c1p = hypot([a1p, b1])
    c2p = hypot([a2p, b2])

    avg_c1p_c2p = (c1p + c2p) / 2.0

    h1p = math.degrees(math.atan2(b1, a1p))
    if h1p < 0:
        h1p += 360

    h2p = math.degrees(math.atan2(b2, a2p))
    if h2p < 0:
        h2p += 360

    avg_hp = (((abs(h1p - h2p) > 180) * 360) + h1p + h2p) / 2.0

    t = (
        1
        - 0.17 * math.cos(math.radians(avg_hp - 30))
        + 0.24 * math.cos(math.radians(2 * avg_hp))
        + 0.32 * math.cos(math.radians(3 * avg_hp + 6))
        - 0.2 * math.cos(math.radians(4 * avg_hp - 63))
    )

    diff_h2p_h1p = h2p - h1p
    delta_hp = diff_h2p_h1p + (abs(diff_h2p_h1p) > 180) * 360
    delta_hp -= (h2p > h1p) * 720

    delta_lp = l2 - l1
    delta_cp = c2p - c1p
    delta_hp = 2 * math.sqrt(c2p * c1p) * math.sin(math.radians(delta_hp) / 2.0)

    s_l = 1 + ((0.015 * (avg_lp - 50) ** 2) / math.sqrt(20 + (avg_lp - 50) ** 2.0))
    s_c = 1 + 0.045 * avg_c1p_c2p
    s_h = 1 + 0.015 * avg_c1p_c2p * t

    delta_ro = 30 * math.exp(-(((avg_hp - 275) / 25) ** 2.0))
    r_c = math.sqrt((avg_c1p_c2p ** 7.0) / (avg_c1p_c2p ** 7.0 + 25.0 ** 7.0))
    r_t = -2 * r_c * math.sin(2 * math.radians(delta_ro))

    kl = 1
    kc = 1
    kh = 1

    return math.sqrt(
        (delta_lp / (s_l * kl)) ** 2
        + (delta_cp / (s_c * kc)) ** 2
        + (delta_hp / (s_h * kh)) ** 2
        + r_t * (delta_cp / (s_c * kc)) * (delta_hp / (s_h * kh))
    )


def hypot(els):
    return math.sqrt(sum(el ** 2 for el in els))
