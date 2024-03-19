# 연산자란 프로그램에 계산을 위해서 사용 (사칙, 대입, 비교, 관계, 비트 연산 등이 있음)
# 산술 연산 : +, -, *, /(나누기), %(나머지), //(몫), *(제곱)
# ++, -- 증감 연산자는 없음
# i = 10
# j = 3
# print(i+j)
# print(i**j)  # 10 * 10 * 10 제곱 연산
# print(i/j)
# print(f"{i/j:.2f}")  # 나누기
# print(i//j)
# text = "Python"
# print(text * 3)
#
# tax_rate = 0.10
# income = int(input("당신의 수업은 얼마 입니까? "))
# print(f"당신이 내야 할 세금은 {income * tax_rate:.2f} 입니다.")

# 관계 연산자 (논리 연산자)
x = 10
y = 20
z = 30
rst1 = x > 0 and x > y  # &&, 둘 다 참이여야 참 = 거짓
rst2 = x > 0 or x > y  # ||, 둘 중 하나만 참이여도 참 = 참
rst3 = not(x > 0 or x > y)  # !, 참이면 거짓, 거짓이면 참

# 3항 연산자, 자바는 (조건식) ? (참) : (거짓) / 파이썬 (조건식) and (참) or (거짓)
# age = int(input("나이를 입력 : "))
# adult = age > 19 and "성인" or "미성년자"
# print(f"당신은 {adult} 입니다.")
# num = int(input("정수 입력 : "))
# is_even = num % 2 == 0 and "짝수" or "홀수"
# print(f"{num} 은(는) {is_even} 입니다.")

# 진법 초기화
print(42 == 0b101010)  # b = binary (2진수)
print(42 == 0o52)  # o = octa (8진수)
print(42 == 0x2a)  # x = hexa (16진수)
print(bin(42))
print(oct(42))
print(hex(42))

# 비트 연산자
a = 10
b = 12
print(a & b)  # 둘 다 1이여야 1, 8
print(a | b)  # 둘 중 하나만 1이면 1, 14
print(a ^ b)  # 값이 다른 경우 1, 6
print(~a)
print(a << 1)  # 주어진 값만큼 왼쪽으로 bit 이동, 20
print(a >> 1)
