# - 1 ~ 45까지의 로또 번호 6개를 자동 생성 하기
# - 중복 번호는 제거

# import random
# lotto = []
# while True:
#     rand = random.randrange(1, 45)
#     if rand not in lotto:
#         lotto.append(rand)
#     if len(lotto) == 6:
#         break
# print(lotto)

# 임의의 수를 연속(공백) 으로 입력 받아 홀수, 짝수 리스트로 나누어 담기
num = list(map(int, input().split()))
holl = []
zzak = []
for e in num:
    if e % 2 == 0:
        zzak.append(e)
    else:
        holl.append(e)
print(f"홀수 : {holl}")
print(f"홀수 : {zzak}")
