import sys
arg = sys.argv

import os
import qrcode

file_path = arg[1]

with open(file_path,mode="r",encoding="utf-8") as s:
     for line_number, line in enumerate(s, start=1):
        img = qrcode.make(line)
        path = os.path.join(f"/home/matcha-23training/projects/files/{line_number}.png")
        img.save(path)