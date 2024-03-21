# - 1 ~ 45까지의 로또 번호 6개를 자동 생성 하기
# - 중복 번호는 제거

# import random
# lotto = []
# while True:  # 반복 횟수를 알 수 없기 때문에 True, 반드시 탈출 조건 필요
#     rand = random.randrange(1, 46)
#     if rand not in lotto:
#         lotto.append(rand)
#     if len(lotto) == 6:
#         break
# print(lotto)

# 임의의 수를 연속(공백) 으로 입력 받아 홀수, 짝수 리스트로 나누어 담기
# num = list(map(int, input().split()))
# holl = []
# zzak = []
# for e in num:  # 리스트의 요소를 한개씩 끄집어 내면서 순회 (시작 부터 끝까지 자동 순회)
#     if e % 2 == 0:
#         zzak.append(e)
#     else:
#         holl.append(e)
# print(f"홀수 : {holl}")
# print(f"짝수 : {zzak}")


# 다른 방법
num = list(map(int, input().split()))
even = list(filter(lambda x:x % 2 == 0, num))
odd = list(filter(lambda x:x % 2 == 1, num))
print(f"홀수 : {odd}")
print(f"짝수 : {even}")