from tkinter import *
window = Tk()

window.title("이미지들**")
photo1 = PhotoImage(file="C:\\Users\\werty\\OneDrive\\바탕 화면\\수업자료\\python 실습\\windowProgramming\\a1.gif")
photo2 = PhotoImage(file="C:\\Users\\werty\\OneDrive\\바탕 화면\\수업자료\\python 실습\\windowProgramming\\a2.gif")
label1 = Label(window, image = photo1,width=400,height=400)
labe12 = Label(window, image = photo2,width=400,height=400)

label1.pack(side=LEFT)
labe12.pack(side=LEFT)

window.mainloop()