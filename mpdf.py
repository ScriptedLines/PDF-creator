from pypdf import *
from os import *
l=[]

d=listdir()

for i in d:
    if".pdf" in i:
        l.append(i)
        

merger=PdfWriter()


for i in l:
    merger.append(i)

merger.write("meged.pdf")
merger.close()