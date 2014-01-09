#!/usr/bin/env python
import os
import sys
from PIL import Image, ImageDraw


def usage():
	print("%s <file.jpg|png|gif" % sys.argv[0])
	sys.exit(-1)

def main(text):
	image = Image.open(sys.argv[1])
	mark = Image.new('RGBA', image.size)
	mark = ImageDraw.ImageDraw(mark, "RGBA")
	mark.text((0, 100), text)
	mark = mark.convert("L").point(lambda x: min(x, 100))
	mark.putalpha(mark)
	image.paste(mark, None, mark)
	image.save(sys.argv[1], "JPEG")

if __name__ == '__main__':
	main("test out")