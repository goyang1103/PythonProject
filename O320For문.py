# for문은 정해진 범위 만큼 반복 할 때 주로 사용
# for 요소 in 시퀀스: (시퀀스는 리스트, 튜플, 문자열 등을 의미), 자바의 향상된 for문과 유사
# fruits = ["사과", "바나나", "딸기", "수박", "참외", "복숭아"]
# for e in fruits:
#     print(e, end=" ")
# print()

# for 변수 in range(시작값, 종료값, 증감값): (자바의 일반적인 for문과 유사)
# n = int(input("정수 입력 : "))
# sum = 0;
# for i in range(1, n+1):  # 1부터 n까지 순회 (종료 값은 미만 개념), 증감값 생략 시 1씩 증가
#     sum += i
# print(sum)

# 이중 for문 사용하기
# n = int(input("정수를 입력 : "))
# for i in range(0, n):
#     for j in range(0, n):
#         print("*", end=" ")
#     print()

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{i} X {j} = {i*j}")
#     print("===========")

# 이중 for문과 조건문 사용
# n = int(input("정수를 입력 하세요 : "))
# for i in range(n):  # 시작값도 생략시 0
#     for j in range(n):
#         if j % 2 == 0:
#             print("#", end=" ")
#         else:
#             print("*", end=" ")
#     print()


# n = int(input())
# for i in range(n):
#     for j in range(0, i+1):
#         print("*", end="")
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(n-i):
#         print("*", end=" ")
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(i):
#         print(" ", end="")
#     for k in range(n-i):
#         print("*", end="")
#     print()

# 정수값을 n을 입력 받아 n * n 크기의 행렬을 출력 하는 프로그램 작성
# 값은 1부터 시작하고 순서대로 채워 넣는다.
# n = int(input("정수 입력 : "))
# for i in range(1, n * n + 1):
#     print(f"{i:3}", end='')    #이쁘게 찍기 위해서 오른쪽 정렬 한다. 왼쪽 정렬은 <
#     if i % n == 0:
#         print()

# n = int(input("정수 입력 : "))
# for i in range(n):
#     if i % 2 == 0 : continue
#     print(i, end=" ")

# for문을 반대로 출력하기
# for i in range(10, 0-1, -1):
#     print(f"index : {i}")

# for문으로 알파벳 출력하기 : chr (유니코드 값을 입력 받아 문자 출력)
# ord (문자의 유니 코드 값을 반환)
# for i in range(ord("A"), ord("Z")+1):
#     print(chr(i), end=" ")

for i in range(65, 91):  # A:65 Z:90
    print(chr(i), end=" ")
