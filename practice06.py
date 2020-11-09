# 일반

def open_account():
    print("신규 계좌가 생성")

open_account()

def deposit(balance , money):
    print("입급이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
    return balance + money

balance = 0 
balance = deposit(balance , 1000)

print(balance)


def withdrow(balance , money):
    if balance > money:
        print("출급이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance - money))
        return balance - money
    else:
        print("잔액이 부족합니다. 잔액 : {0}".format(balance))
        return balance

def withdrow_closed(balance , money):
    commission = 100 # 수수료
    return (commission, balance - money -commission)

balance = 0 
balance = deposit(balance , 1000)
balance = withdrow(balance , 200)
commission , balance = withdrow_closed(balance, 500)
print("수수료는 {0} 원이며, 잔액은 {1} 원 입니다. ".format(commission,balance))

# 기본값

def profile(name , age ,main_lang):
    print("이름 :{0} \t 나이 : {1}\t 주사용언어 : {2}"\
        .format(name , age ,main_lang))

profile("재석",20,"파이썬")
profile("테호",23,"자바")

# 같은 학교 같은 학년 같은 반 같은 수업.
def profile(name , age=17 ,main_lang="파이썬"):
    print("이름 :{0} \t 나이 : {1}\t 주사용언어 : {2}"\
        .format(name , age ,main_lang))


profile("재석")
profile("테호",10,"자바")

# 키워드 값

def profile(name , age ,main_lang):
    print("이름 :{0} \t 나이 : {1}\t 주사용언어 : {2}"\
        .format(name , age ,main_lang))

profile(name="재석",age=20,main_lang="파이썬")

# 가변인자
def profile(name , age ,lang1, lang2 , lang3, lang4, lang5):
    print("이름 :{0} \t 나이 : {1}\t".format(name , age ), end=" ")
    print(lang1, lang2 , lang3, lang4, lang5)

def profile(name , age ,*lang):
    print("이름 :{0} \t 나이 : {1}\t".format(name , age ), end=" ")
    for i in lang:
        print(i , end=",")
    print()

profile("재석",20,"Pthon","java","swift","C","C")

profile("태호",20,"Pthon","java","swift")

# global / local

gun = 10

def checkpoint(soldiers):   # 경계근무
    global gun
    gun = gun - soldiers
    print("[함수내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun , soldiers):
    gun = gun - soldiers
    print("[함수내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
checkpoint_ret(gun ,2)
print("전체 총 : {0}".format(gun))