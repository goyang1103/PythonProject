#표준 출력은 print() 함수 사용

print(38)   #정수형
print("문자열")    #문자열
print([1,2,3])  #리스트
print("파"+"이"+"썬")
print("파""이""썬")
print('파''이''썬') #파이썬에서는 '', "" 모두 문자열로 간주
print("파","이","썬") #콤마는 구분자를 의미하고 기본값은 공백 한캍
print("\n\n\n") #\n 은 줄바꿈을 의미
print("""
마음대로
출력되는 구간
asdhfohsdfoasdf
asdofshaoashdofahsiodfsaoi
""")
print("안녕하세요. 라고 \"곰돌이사육사\"가 말했습니다.")   #\" \" 문자열 내에서 ""사용
print('안녕하세요. 라고 "곰돌이사육사"가 말했습니다.') #'' 내에 "" 를 섞어서 사용도 가능

print("서울시\t강남구\t역삼동")  #\t : tap만큼 간격 띄우기
print("사과\r바나나")    #커서를 앞으로 돌림

#end : 출력할 때 가장 마지막에 자동으로 삽입되는 문자 지정 옵션 print 기본은 줄바꿈
#sep : 중간에 삽입되는 문자를 지정하는 옵션 print 기본은 공백 한칸
print("Hello", end="*")
print("World", end="\n")

#콤마를 Seperator(구분자) 라고 함
print(1,2,3,4,5,6,7,8,9,10, sep="^")
print("010","1234","4567", sep="-")
year = 2024
month = 3
day = 19
print(year,month,day, sep="/")