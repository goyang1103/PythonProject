# 파이썬은 변수 선언 시 데이터 타입을 지정하지 않으며, 변수에 값이 대입될 때 형이 결정 됨
# number = 200
# number2 = 3.14
# str1 = ""
# bool = True
# print(type(number)) # type() : 변수의 데이터 형을 확인
# print(type(str1))
# print(type(tool))
# print(type(number2))

# 형변환 : 선언된 변수에 값이 할당 되는 순간 형이 결정, 이후 다른 데이터 형으로 변경할 때 사용
print(10 + int("10"))
print("나이 : " + str(30))
print(0.1 + float(512.34))

var = ""    # 공백은 거짓
number = None  # 0은 거짓 , None 도 거짓
print(bool(var))
print(bool(number))   # boolean 값의 거짓 : 공백, 0, None, False
