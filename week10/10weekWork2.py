inFp = None
#inStr = ""
inList,inStr = [],""
linenum = 1

inFp = open("C:\\Users\\werty\\OneDrive\\바탕 화면\\수업자료\\python 실습\\fileTest\\data1.txt","r",encoding="UTF-8")

inList = inFp.readlines()
#print(inList) 가로로 쭉 나옴
for inStr in inList :
    print("%d:%s"%(linenum,inStr),end="")
    linenum +=1

inFp.close()