# 내장 함수란? 별도로 import 하지 않고도 사용 할 수 있도록 내장되어 있는 함수를 의미 합니다.
print(max(32, 45, 48, 57, 23))
print(min(32, 45, 48, 57, 23))

# sum 에는 리스트 또는 튜플 형태로 전달
print(sum((26, 34, 45, 67, 67)))
value = 1,2,3,4,5,6,7,8,9,10
print(sum(value))
print(f"평균 : {sum(value)/len(value)}")
# divmod : 몫과 나머지
print(divmod(sum(value), 4))