# 계좌 개설
ls = []


def open_account(name):  # 매개 변수와 반환값이 있는 함수 선언
    print(f"{name}님의 개좌가 개설 되었습니다.")
    return name


def deposit(input):  # 잔액과 입금액을 매개 변수로 전달 받음 (입금)
    global balance
    balance += input
    ls.append(balance)
    print(f"{input}이 입금 되었습니다. 잔액은 {balance} 입니다.")


def withdraw(input):
    global balance
    if balance >= input:
        balance -= input
        print(f"{input}이 출금 되었습니다. 잔액은 {balance} 입니다.")
    else:
        print("출금에 실패 하였습니다.")


balance = 0  # 현재 잔액을 외부에서 선언 함
name = open_account("곰돌이사육사")
deposit(1000)
withdraw(500)
print(f"{name}의 잔액은 {balance} 입니다.")

