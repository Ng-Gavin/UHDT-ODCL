import os, fontforge

# Font Forge must be installed on your computer for this script to work.
# Script can be executed by running "fontforge -script font_export.py fonts" in the command line

character_dict = {
    'A_cap': 65,
    'B_cap': 66,
    'C_cap': 67,
    'D_cap': 68,
    'E_cap': 69,
    'F_cap': 70,
    'G_cap': 71,
    'H_cap': 72,
    'I_cap': 73,
    'J_cap': 74,
    'K_cap': 75,
    'L_cap': 76,
    'M_cap': 77,
    'N_cap': 78,
    'O_cap': 79,
    'P_cap': 80,
    'Q_cap': 81,
    'R_cap': 82,
    'S_cap': 83,
    'T_cap': 84,
    'U_cap': 85,
    'V_cap': 86,
    'W_cap': 87,
    'X_cap': 88,
    'Y_cap': 89,
    'Z_cap': 90,
    'a': 97,
    'b': 98,
    'c': 99,
    'd': 100,
    'e': 101,
    'f': 102,
    'g': 103,
    'h': 104,
    'i': 105,
    'j': 106,
    'k': 107,
    'l': 108,
    'm': 109,
    'n': 110,
    'o': 111,
    'p': 112,
    'q': 113,
    'r': 114,
    's': 115,
    't': 116,
    'u': 117,
    'v': 118,
    'w': 119,
    'x': 120,
    'y': 121,
    'z': 122,
    '0': 48,
    '1': 49,
    '2': 50,
    '3': 51,
    '4': 52,
    '5': 53,
    '6': 54,
    '7': 55,
    '8': 56,
    '9': 57
}


def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f


font_folder = os.sys.argv[1]
for font_file in listdir_nohidden(font_folder):
    font_path = os.path.join(font_folder, font_file)
    if os.path.isfile(font_path):
        export_parent_folder = os.path.join('exported_fonts')
        font_export_folder = os.path.splitext(font_file)[0]
        font_export_folder_path = os.path.join(export_parent_folder, font_export_folder)
        if not os.path.exists(font_export_folder_path):
            os.makedirs(font_export_folder_path)
        font = fontforge.open(font_path)
        char_file_names = list(character_dict.values())
        char_names_keys = list(character_dict.keys())
        for char in font:
            char_unicode_decimal = fontforge.unicodeFromName(char)
            if char_unicode_decimal in char_file_names:
                position = char_file_names.index(char_unicode_decimal)
                char_name = char_names_keys[position]
                font_png = f'{char_name}.png'
                font[char].export(os.path.join(font_export_folder_path, font_png), 5000, 5000)