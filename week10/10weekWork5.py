inFp, outFP = None,None
inStr = ""
inFname,outFname = "",""

inFname = input("소스 파일명을 입력하세요:")
outFname = input("타깃 파일명을 입력하세요:")

inFp = open(inFname, "r", encoding="utf-8")
outFp = open(outFname, "w", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("----파일이 정상적으로 복사되었음-----")