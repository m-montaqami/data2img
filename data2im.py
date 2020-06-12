import numpy as np
import cv2,math
from tkinter import filedialog
from tkinter import *
root = Tk()
path= filedialog.askopenfilename(initialdir = "/",title = "Select file")
file=list(open(path,encoding='ansi'))
file=''.join(i for i in file)
file=[ord(i) for i in file]
file=np.array(file)
file_norm=((file-min(file))/(max(file)-min(file)))*255
file_norm=np.array(file_norm,dtype='int')
shape=int(file_norm.size)
buff=math.ceil(math.sqrt(file_norm.size))
buff2=1 
for i in range(buff,1,-1):
    if shape%i==0:
        buff2=i
        break
img = file_norm.reshape(buff2,shape//buff2)
cv2.imwrite('export.jpg',img)
