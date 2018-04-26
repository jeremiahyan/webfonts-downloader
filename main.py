import os
import urllib.request

css_file_name = "roboto.css"
css_path = "./output/css/fonts/"
css_dir = os.path.dirname(css_path)
fonts_path = "./output/fonts/"
fonts_dir = os.path.dirname(fonts_path)

if not os.path.exists(fonts_dir):
    os.makedirs(fonts_dir)

if not os.path.exists(css_dir):
    os.makedirs(css_dir)

try:
    css = ""
    with open("input/" + css_file_name) as css_file:
        css = css_file.read()
        css_list = css.split("}")
        num = 0
        for css_item in css_list:
            # print("==== \n" + css_item)
            label_name = css_item.split("/* ")[1].split(" */")[0]
            font_name = css_item.split("local('")[2].split("'),")[0].lower()
            css_name = font_name + "-" + label_name
            css_url = css_item.split("url(")[1].split(".woff2)")[0] + ".woff2"
            print("==== " + str(num) + " \n" + css_name)
            print(css_url)
            urllib.request.urlretrieve(css_url, "./output/fonts/" + css_name + ".woff2")
            css = css.replace(css_url, "../../fonts/" + css_name + ".woff2")

            num += 1
except IOError as err:
    print("File error: " + str(err))

except IndexError as err:
    print("Index error: " + str(err))
    print("css \n" + css)

    try:
        file_path = css_path + css_file_name
        with open(file_path, "w") as css_file_w:
            print(css, file=css_file_w)
            print("output_done")
    except err:
        print("output to file error:", + str(err))

except err:
    print("Other error:", + str(err))

