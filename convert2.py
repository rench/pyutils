import os
import img2pdf

path = './'
os.chdir(path)
images = [i for i in os.listdir(os.getcwd()) if i.endswith(".png")]

with open("output1.pdf", "wb") as f:
    f.write(img2pdf.convert(images))