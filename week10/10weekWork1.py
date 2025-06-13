inFp = None
inStr=""
lineNum = 1

inFp = open("C:\\Users\\werty\\OneDrive\\바탕 화면\\수업자료\\python 실습\\fileTest\\data1.txt","r",encoding="UTF-8")

while True:
    inStr = inFp.readline()
    if inStr == "":
        break;
    print(f"{lineNum}: {inStr}",end="")
    lineNum += 1
inFp.close()