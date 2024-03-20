# 회원정보를 입력 받아서 출력 하는 예제 진행
# - 이름 입력
# - 나이 입력 : 1 ~ 199까지 입력 받고 잘못된 값이 오면 재 입력 요청을 한다.
# - 성별 입력 : 영문자 (M과 m은 남성) (F와 f는 여성)으로 입력 받고 나머지는 재 입력 요청을 한다.
# - 직업 입력 : 1(학생), 2(회사원), 3(주부), 4(무직)으로 입력 받고 나머지는 재 입력 요청 한다.
# - 결과는 마지막에 한번에 출력 한다.

name = input("이름 입력 : ")
while True:
    age = int(input("나이 입력 : "))
    if 0 < age < 200:
        break
    else:
        print("다시 입력 해주세요. ")
while True:
    gen = input("성별 입력 : ")
    if gen == "M" or gen == "m":

        break
    elif gen == "F" or gen == "f":
        break
    else:
        print("다시 입력 해주세요. ")
while True:
    job = int(input("1(학생) 2(회사원) 3(주부) 4(무직)으로 입력 : "))
    if 0 < job < 5:
        break
    else: print("다시 입력 해주세요. ")

if gen == "M" or gen == "m":
    gen_name = "남성"
else:
    gen_name = "여성"

jobs_name = ("", "학생", "회사원", "주부", "무직") # 튜플 사용

print(f"이름 : {name}, 나이 : {age}, 성별 : {gen_name}, 직업 : {jobs_name[job]}")
