#진수 변환

sel = int(input("입력할 숫자의 진수를 결정하세요 (2, 8, 10, 16): "))
if sel not in [2, 8, 10, 16]:
    print("2, 8, 10, 16 중 하나만 입력하세요. 프로그램을 종료합니다.")
    exit() 
else:
     num = input("값 입력")
if sel == 16 :
    num10 = int(num,16)
elif sel == 8 :
    num10 = int(num,8)
elif sel == 10 :
    num10 = int(num)
elif sel == 2 :
    num10 = int(num,2)
else : 
    print("2, 8, 10, 16 중 하나만 입력하세요. 프로그램을 종료합니다.")
    exit() 


print("16진수==>",hex(num10))
print("10진수==>",num10)
print("8진수==>",oct(num10))
print("2진수==>",bin(num10))
