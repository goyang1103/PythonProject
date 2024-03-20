# 내장 함수란? 별도로 import 하지 않고도 사용 할 수 있도록 내장되어 있는 함수를 의미 합니다.
# print(max(32, 45, 48, 57, 23))
# print(min(32, 45, 48, 57, 23))

# sum 에는 리스트 또는 튜플 형태로 전달
# print(sum((26, 34, 45, 67, 67)))
# value = 1,2,3,4,5,6,7,8,9,10
# print(sum(value))
# print(f"평균 : {sum(value)/len(value)}")
# # divmod : 몫과 나머지
# print(divmod(sum(value), 4))

# 외장함수 : 파이썬의 표준 모듈이지만 import 해야 사용 가능
# import random
# for i in range(10):
#     # rand = random.randint(0, 4)  # 0에서 4 사이의 임의의 정수 반환 (4가 포함)
#     # rand = random.randrange(0, 4)  # 0에서 4 미만
#     rand = random.randrange(4)  # for문처럼 0 생략 가능
#     print(rand)

# 날짜 및 시간 관련 처리 모듈
from datetime import datetime  # datetime 모듈에서 datetime 라는 함수만 import
datetime.today()  # 현재 날짜 가져 오기
print(datetime.today().year)  # 현재 연도 가져 오기
print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)


# 달력 생성
import calendar
print(calendar.calendar(2024, 3))

# math 모듈
import math
print(math.sin(100))
print(math.cos(100))
print(math.tan(100))
print(math.ceil(1.000000001))  # 반올림
print(math.floor(1.000000001))  # 내림
