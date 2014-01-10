#!/usr/bin/env python
import os
import sys
from PIL import Image, ImageDraw, ImageFont
import logging as log
log.basicConfig(level=log.INFO)


def usage():
    print("%s <file.jpg|png|gif> message" % sys.argv[0])
    sys.exit(-1)

def main(text):
    font = ImageFont.truetype("../fonts/DejaVuSans.ttf", 24)
    image = Image.open(sys.argv[1])
    draw = ImageDraw.Draw(image)
    draw.text((0, 50), text, (255, 255, 255), font=font)
    log.info("saving file")
    image.save(sys.argv[1], "JPEG")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()
    main(sys.argv[2])
