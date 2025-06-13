from tkinter import *
from time import *

fnameList = ["a1.gif","a2.gif","a3.gif","a4.gif","a5.gif","a6.gif","a7.gif","a8.gif","a9.gif"]
phtoList = [None]*9
num = 0

def clickNext() :
    global num
    num += 1
    if num > 8 :
        num = 0
    photo = PhotoImage(file = "C:/Users/werty/OneDrive/바탕 화면/수업자료/python 실습/windowProgramming/gif/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

def clickPrev() :
    global num
    num -= 1
    if num < 0 :
        num = 8
        photo = PhotoImage(file = "C:/Users/werty/OneDrive/바탕 화면/수업자료/python 실습/windowProgramming/gif/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<<이전", command = clickPrev)
btnFname = Button(window, text = fnameList[num] )
btnNext = Button(window, text = "다음>>", command = clickNext)

photo = PhotoImage(file = "C:/Users/werty/OneDrive/바탕 화면/수업자료/python 실습/windowProgramming/gif/" + fnameList[0])
pLabel = Label(window, image = photo)

btnPrev.place(x=250, y=10)
btnFname.place(x=325, y=10)
btnNext.place(x=400, y=10)
pLabel.place(x=15, y=50)

window.mainloop()