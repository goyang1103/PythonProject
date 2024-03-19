# 문자열이란 문자로 이루어진 데이터의 집합, 파이썬은 문자를 별도로 다루지 않고 전부 문자열로 간주
# "한줄 문자열", '한줄 문자열', """여러줄 문자열""", '''여러줄 문자열'''
# 인덱싱이란 시퀀스 자료형 (리스트, 튜플, 문자열) 에서 특정 위치의 요소를 선택 하는 작업
# 슬라이싱 이란 시퀀스 자료형 에서 일부분을 추출 하는 작업, seq[start:end:step]
my_list = [0,1,2,3,4,5,6,7,8,9]  # 리스트 생성 []

slice_without_step = my_list[2:7]  # 인덱스는 0부터 시작, end 는 미만
slice_with_step = my_list[1:9:2]  #1,3,5,7

# 인덱싱, 슬라이싱, 실습
# 주민등록번호 자르기, 하위 7자리 중 첫번째는 성별, 앞의 6자리는 생년월일
jumin = "991120-1234567"
print("성별 : " + jumin[7])
print("년 : " + jumin[:2])  # 0부터 2 미만
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])  # 7에서 부터 끝까지
print("뒤 7자리 : " + jumin[-7:])

python_str = "life is too short, You need Python"
new_str = python_str[0] + python_str[1] + python_str[2] + python_str[3]
# python_str[0] = "l"  # 리터럴 상수이기 때문에 변경 불가
print(new_str)

# 대소문자 바꾸기 : upper(), lower()
print(python_str.upper())
print(python_str.lower())
# 문자열 변경
a_str = "Hello Python Program"
print(a_str.replace("Python", "JavaScript"))  # 문자열이 바뀐게 아닌 바뀌여서 그냥 출력 됨
print(a_str)
new_str2 = a_str.replace("Python", "JavaScript")  # 바꿀라면 이케 해야 됨
print(new_str2)

# 문자열에 포함 된 문자 개수 세기 (count(), 문자열 길이(len(), __len__())
a_str2 = "Hello Python Program"
print(a_str2.count("l"))  # 해당 문자열에서 count() 함수에 전달 문자가 몇개 존재 하는 지 반환
print(len(a_str2))  # 문자열 길이를 반환하는 함수
print(a_str2.__len__())  # 문자열 길이를 반환하는 내장 함수

# 문자열 찾기 : find() : 찾은 문자열 인덱스 반환, 없으면 -1
# rfind() : 뒤에서 부터 문자열 찾고 찾은 인덱스는 앞에서 부터 계산
# index() : 찾은 문자열의 인덱스 반환, 없으면 valueError
phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장"))
print(phrase.rfind("가장"))
print(phrase.index("포기"))
print(phrase.find("배고파"))
print(phrase.rfind("밥줘"))
# print(phrase.index("흑")) = Error
new_str3 = phrase.replace("가장", "나에게")
print(new_str3)

# 문자열 연산자 : "문자열" + "문자열" + "문자열"*3
print("태양고", "나희도")
print("태양고"*2)
# print("태양고" + 2) = 이놈은 안됨.

# 문자열 양 옆의 공백 제거 : strip()
input_a = """
    안녕하세요.
문자열 함수를 알아 봅니다.

    """
print(input_a.strip())