# 세자리 수 중에서 가장 큰 수

# num = (input("세자리 정수 입력 : "))
#
# if num[0] > num[1]:
#     if num[0] > num[2]: print(num[0])
#     else: print(num[2])
# else:
#     if num[1] > num[2]: print(num[1])
#     else: print(num[2])

n = int(input("정수 입력 : "))
a = n // 100
b = (n % 100) //10
c = n % 10
if a > b:
    if a > c: print(a)
    else: print(c)
else:
    if b > c : print(b)
    else: print(c)


# 주/야간 근무 시간을 입력 받아 아르바이트 급여 계산 하기
juya = int(input("주간근무[1], 야간근무[2]를 입력 하세요 : "))
time = int(input("근무 시간을 입력해 주세요 : "))

if juya == 1:
    money = time * 9620
else:
    money = int(time * 9620 * 1.5)

what = juya == 1 and "주간" or "야간"
print(f"{time}시간 동안 근무한 {what} 급여는 {money}원 입니다.")