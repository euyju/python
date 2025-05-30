class Car:
    def __init__(self):
        self.color = ""
        self.speed = 0

    def upSpeed(self, value):
        self.speed += value
        if self.speed > 150:         # 속도 제한 조건
            self.speed = 150         # 최대 속도를 150km로 고정

    def downSpeed(self, value):
        self.speed -= value

# 메인 코드
myCar1 = Car()
myCar1.color = "빨강"
myCar1.upSpeed(30)

myCar2 = Car()
myCar2.color = "파랑"
myCar2.upSpeed(200)  # 150km 초과 입력

myCar3 = Car()
myCar3.color = "노랑"
myCar3.upSpeed(180)  # 150km 초과 입력

# 출력
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar1.color, myCar1.speed))
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar2.color, myCar2.speed))
print("자동차3의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar3.color, myCar3.speed))