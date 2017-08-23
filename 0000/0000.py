# -*- coding: UTF-8 -*-
import Image,ImageDraw,ImageFont

im = Image.open("0.jpg")
draw = ImageDraw.Draw(im)

xsize,ysize = im.size

myFont = ImageFont.truetype("ARIAL.TTF", 40)

draw.text((xsize-42,2),"99",fill = (255,0,0),font = myFont)
del draw

im.save('result.jpg','jpeg')
