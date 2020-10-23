import os
import img2pdf
import subprocess
import shlex

import noteshrink

path = './'
os.chdir(path)
imagelist = [i for i in os.listdir(os.getcwd()) if i.endswith(".jpg")]

cmd = 'python ./noteshrink.py -w -q -b NShrink ' + ' '.join(imagelist)
try:
    result = subprocess.call(shlex.split(cmd))
except OSError:
    result = -1

if result == 0:
    print('图片处理成功')

path = './'
os.chdir(path)
imagelist = [i for i in os.listdir(os.getcwd()) if i.endswith(".png")]

with open("output1.pdf", "wb") as f:
    f.write(img2pdf.convert(imagelist))
    print('生成pdf成功')
