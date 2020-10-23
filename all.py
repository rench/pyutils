import os
import shutil
import img2pdf
import subprocess
import shlex
 
from pdf2docx import parse

shutil.rmtree('./tmp')
os.mkdir('./tmp')

path = './'
os.chdir(path)
imagelist = [i for i in os.listdir(os.getcwd()) if i.endswith(".jpg")]



#sharink jpg
cmd = 'python ./noteshrink.py -w -q -b N ' + ' '.join(imagelist)
try:
    result = subprocess.call(shlex.split(cmd))
except OSError:
    result = -1

if result == 0:
    print('图片处理成功')
else:
    print('图片处理失败')

#compact pdf
path = './tmp'
os.chdir(path)
imagelist = [i for i in os.listdir(os.getcwd()) if i.endswith(".png")]
a4inpt = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
border = (50,30)
layout_fun = img2pdf.get_layout_fun(pagesize=a4inpt,border=border)

with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert(imagelist, layout_fun=layout_fun))
    print('生成pdf成功: output.pdf')

#pdf2word
print('开始转换pdf到docx')
parse("output.pdf","output.docx")
print('docx转换成功: output.docx')
