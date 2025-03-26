#원의 반지름 입력받아 원의 둘레와 넓이를 구하는 코드

radius = float(input("반지름 입력> "))
circumference = 2 * 3.14 * radius
area = 3.14 * radius**2

print("반지름이", radius, "인 원의 둘레는 약", circumference, "이고, 넓이는 약", area, "입니다.")