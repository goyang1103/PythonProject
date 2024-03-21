# 세준이는 피시방에서 아르바이트를 한다. 세준이의 피시방에는 1번부터 100번까지 컴퓨터가 있다.
# 들어 오는 손님은 모두 자기가 앉고 싶은 자리에만 앉고 싶어 한다. 따라서 들어오면서 번호를 말한다.
# 만약에 그 자리에 사람이 없으면 그 손님은 그 자리에 앉아서 컴퓨터를 할 수 있고, 사람이 있다면 거절 당한다.
# 거절 당하는 사람의 수를 출력하는 프로그램을 작성 하시오. 자리는 맨 처음에 모두 비어 있고, 어떤 사람이 자리에 앉으면 자리를 비우는 일은 없다.
# 입력 : 첫째 줄에 손님의 수 N이 주어진다. N은 100보다 작거나 같다. 둘째 줄에 손님이 들어오는 순서대로 각 손님이 앉고 싶어 하는 자리가 입력으로 주어진다.
# 출력 : 첫째 줄에 거절 당하는 사람의 수를 출력 한다.

# ex = 0
# seat = []
# num = int(input("손님 수 입력 : "))
# if 0 < num < 101:
#     person = list(map(int,input("희망 자리 입력 : ").split()))
#     if len(person) != num:
#         print("잘못된 입력 입니다. 손님 수와 희망 자리 개수가 일치 해야 합니다.")
#     else:
#         for e in person:
#             if e not in seat:
#                 seat.append(e)
#             else:
#                 ex += 1
#         print(f"거절 당한 손님은 {ex} 명 입니다.")
# else:
#     print("잘못 된 입력 입니다. ")

# 풀이
# person = int(input())
# num = list(map(int, input().split()))
# pc = [0]*100  # 0 값으로 초기화 된 100 개의 리스트 생성
# cnt = 0
# for e in num:
#     if pc[e-1] != 0:
#         cnt += 1
# print(cnt)


# 저항 : 3가지 색상의 값을 조합해서 저항값 구하기 (중급)
color = ("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white")
f_name = color.index(input())  # 입력 받은 컬러 값의 인덱스 반환
s_name = color.index(input())
t_name = color.index(input())
print(int(str(f_name) + str(s_name)) * (10 ** t_name))

