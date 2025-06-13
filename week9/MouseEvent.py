from tkinter import *
from tkinter import messagebox

def shiftUp(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키: Shift + 위쪽 화살표")

def shiftDown(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키: Shift + 아래쪽 화살표")

def shiftLeft(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키: Shift + 왼쪽 화살표")

def shiftRight(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키: Shift + 오른쪽 화살표")

window = Tk()

window.bind("<Shift-Up>", shiftUp)
window.bind("<Shift-Down>", shiftDown)
window.bind("<Shift-Left>", shiftLeft)
window.bind("<Shift-Right>", shiftRight)

window.mainloop()