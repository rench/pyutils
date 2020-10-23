from PIL import Image as ImagePIL, ImageFont, ImageDraw
#from StringIO import StringIO

im = ImagePIL.open('./2.jpg')
im.save(r'./2-1.jpg',dpi=(300.0,300.0))