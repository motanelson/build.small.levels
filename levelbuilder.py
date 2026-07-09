import os 
import copy
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import random
import subprocess

print("\033c\033[47;30m\ngive me x\n")
a="output.txt"
x=int(input().strip())
if x> 10:
     x=10
print("\033[47;30m\ngive me y\n")

y=int(input().strip())
if y> 10:
     y=10
f=""
for yy in range(y):
    for xx in range(x):
        r=int(random.random()*4) & 3
        f=f+str(r)
    f=f+"\n"

f1=open(a,"w")
f1.write(f)
f1.close()
a="map table"


