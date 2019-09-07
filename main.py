import json
import pathlib
import urllib.request


def main():
    # https://gist.github.com/kawanet/a880c83f06d6baf742e45ac9ac52af96
    url = 'https://gist.githubusercontent.com/kawanet/a880c83f06d6baf742e45ac9ac52af96/raw' \
          '/b4fbc9a730394eb977277e73cc37b60955463f21/material-colors.json'
    json_file_name = 'material-colors.json'
    urllib.request.urlretrieve(url, json_file_name)
    with open(json_file_name, 'r') as json_file:
        colors = json.load(json_file)

    out_dir_name = 'material_ui_colors'
    pathlib.Path(out_dir_name).mkdir(exist_ok=True)

    for color in colors:
        with open(out_dir_name + '/_' + color + '.scss', 'w') as out_file:
            shades = colors[color]
            out = ['$material_ui_' + color + '_' + shade + ': ' + value + ';\n' for shade, value in shades.items()]
            out.append('$material_ui_' + color + ': $material_ui_' + color + '_500;')
            out_file.writelines(out)

    with open(out_dir_name + '/_main.scss', 'w') as out_main_file:
        out = ['@import "' + color + '";\n' for color in colors]
        out_main_file.writelines(out)


if __name__ == '__main__':
    main()
