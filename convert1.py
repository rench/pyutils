from os import listdir
from fpdf import FPDF

path = "./" # get the path of images

imagelist = [f for f in listdir(path) if f.endswith(".jpg")] # get list of all images

pdf = FPDF('P','mm','A4') # create an A4-size pdf document 

x,y,w,h = 0,0,904/3.78,1176/3.78

for image in imagelist:

    pdf.add_page()
    pdf.image(path+image,x,y,w,h)

pdf.output("images.pdf","F")