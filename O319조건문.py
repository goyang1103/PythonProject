# 조건문과 반복문은 제어문이라고 하고, 이는 수차적인 흐름을 제어하는 목적으로 사용
# 파이썬의 조건문은 자바의 if 문과 switch 문을 결합한 형태와 유사하며, 파이썬은 switch 문이 없음
# 조건문의 수행은 들여쓰기 구분하고 각각의 조건은 : (클론) 으로 구분
# num = int(input("정수를 입력 하세요 : "))
# if num > 100:
#     print("입력 값이 100 보다 커요.")
# elif num < 100:
#     print("입력 값이 100 보다 작아요.")
# else:
#     print("입력 값이 100 과 같아요")

# season = input("지금 계절은 ? ")
# if season == "spring":
#     print("따뜻한 봄이 왔어요.")
# elif season == "summer":
#     print("무더운 여름 입니다.")
# elif season == "fall" or season == "automn" :
#     print("쓸쓸한 가을 입니다.")
# elif season == "winter":
#     print("윈터는 에스파 입니다.")
# else:
#     print("잘못된 입력 입니다.")

# 성적에 대한 학점 출력 하기
# 국어, 영어, 수학 성적을 입력 받아 평균을 구해 등급 출력 하기
# 평균이 90 이상 A, 80 이상 B, 70 이상 C, 60 이상 D, 나머지는 F

kor, eng, mat = map(int, input("국어, 영어, 수학 성적 입력 : ").split())
sum = (kor + eng + mat)/3

if sum >= 90:
    print("A 입니다.")
elif sum >= 80:
    print("B 입니다.")
elif sum >= 70:
    print("C 입니다.")
elif sum >= 60:
    print("D 입니다.")
else:
    print("F 입니다.")