from tkinter import *
import random

btnList = [None]*9
fnameList = ["a1.gif","a2.gif","a3.gif","a4.gif","a5.gif","a6.gif","a7.gif","a8.gif","a9.gif"]
random.shuffle(fnameList)
photoList = [None]*9
i,k = 0,0
xPos,yPos = 0,0
num = 0

window = Tk()
window.geometry("210x210")

for i in range(0,9) :
    photoList[i] = PhotoImage(file = "C:/Users/werty/OneDrive/바탕 화면/수업자료/python 실습/windowProgramming/gif/" + fnameList[i])
    btnList[i] = Button(window, image = photoList[i])

for i in range(0,3):
    for k in range(0,3):
        btnList[num].place(x=xPos,y=yPos)
        num+=1
        xPos+=70
    xPos = 0
    yPos += 70

window.mainloop()