# Usage:
# python gen_html.py -i ./day2golden_results

import argparse
import os
import glob


parser = argparse.ArgumentParser()
parser.add_argument("--input_dir", "-i", default="./", help="path to folder containing images")
a = parser.parse_args()

def append_index(filesets):
    index_path = os.path.join(a.input_dir, "index.html")

    index = open(index_path, "w")
    index.write("<html><body>")
    # index.write("<h1></h1>")
    index.write("<table><tr>")
    index.write("<th>Input</th>")
    index.write("<th>Reflectance</th>")
    index.write("<th>Shading</th>")

    # for path in style_paths:
    #     index.write("<td><img src='0/%s'  width='256'></td>" % os.path.basename(path))
    index.write("</tr>")

    for fileset in filesets:   
        if os.path.isdir(fileset):
            file_name = os.path.basename(fileset)
            index.write("<tr>")

            index.write("<td><img src='%s/%s'  width='256'></td>" % (file_name, "input.jpg"))
            index.write("<td><img src='%s/%s'  width='256'></td>" % (file_name, "output_r.jpg"))
            index.write("<td><img src='%s/%s'  width='256'></td>" % (file_name, "output_s.jpg"))

            index.write("</tr>")

    index.write("</body>")
    index.write("</html>")
    return index_path


if __name__ == '__main__':

    input_folders = glob.glob(os.path.join(a.input_dir, "*"))
    print("%d folders to be processed."%(len(input_folders)))

    append_index(input_folders)





