# 리스트 : 연속적으로 저장되는 형태의 자료형, 크기가 동적으로 변함
# 자바와 다른 점은 여러가지 데이터 타입이 섞여 있을 수 있음, [리스트 내에 리스트]가 존재 할 수 있음
# 리스트는 읽기 쓰기 가능, 튜플은 동일한 구조이지만 읽기만 가능
# number = [1,2,3,4,5,6,7]
# fruits = ['apple', 'banana', 'orange']
# mixed = [1, 'apple', True, 3.14, ['EV6', 'Santafe', 'Sorento']]

# print(number[1])
# print(fruits[0])
# print(mixed[1][2])  # p
# print(mixed[4][2][5])  # t
# print(mixed[3][1])  # error (문자열이 아님)
# print(len(mixed[4]))  # 3
# print(len(mixed[0]))  # error (문자열이 아님)

# list_a = [1,2,3]
# list_b = [4,5,6]
# list_c = list_a + list_b
# print(list_c)
#
# new_list = [1,2,3]
# new_list.append(4)  # 뒤에 값을 추가
# new_list.append(5)
# new_list.insert(1, 1000)  # 1번 인덱스에 1000 값을 추가
# print(new_list)

# 리스트에서 값 제거하기 : pop, remove, clear
# pop : 인덱스가 없으면 마지막 인덱스의 값을 반환하고 삭제
# print(new_list.pop())  # 맨 마지막의 5를 반환하고(print) 제거
# print(new_list.pop(1))  # 인덱스를 주면 해당 값을 반환하고 제거
# new_list.remove(3)  # 해당 값을 제거 (반환 X), 동일한 값이 여러개 존재 하는 경우 낮은 인덱스 값 제거
# print(new_list)
# # new_list.clear()
# del new_list[1]  # 해당 인덱스의 값 제거
# print(new_list)

# 변수와 리스트의 차이 비교
# kor, eng, mat = map(int, input().split())
# total = kor + eng + mat  # 변수
# print(total/3)
# score = list(map(int, input().split()))  # 리스트
# print(sum(score)/len(score))

#  중복 제거
my_list = ["A", "B", "C", "D", "B", "C", "E"]
new_list = []
for e in my_list:
    if e not in new_list:  # 포함 되어 있지 않으면
        new_list.append(e)
print(new_list)

# 리스트 순회하기
x = ["John", "George", "Paul", "Ringo"]
# for e in x:
#     print(e, end=" ")  # 향상된 for 문과 유사
for i in range(len(x)):
    print(x[i], end=" ")  # 자바 기본 for 문과 유사
