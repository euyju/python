# 과제

cal = int(input("1.입력한 수식 계산 2. 두수 사이의 합계 :"))
def sum_between(a, b):
    return sum(range(min(a, b), max(a, b) + 1))

if cal == 1 :
    math = input("수식을 입력하세요:")
    result = eval(math)
    print(math,"결과는 ",result," 입니다.")
if cal == 2 :
    x = int(input("첫 번째 숫자를 입력하세요 :"))
    y = int(input("두 번째 숫자를 입력하세요"))

    z= sum_between(x,y)

    print(x,"+...+",y,"는",z,"입니다.")

else :
    print("1 또는 2만 입력해야 합니다.") 