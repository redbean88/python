# 문제 ) 당신은 Cocoa 서비스를 이용하는 택시 기사님 입니다.
# 50명의 승객과 매칭기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1 : 승객별 운행 소요시간은 5 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5 ~ 15분 사이의 승객만 매칭해야 합니다.

# (예제)
# [0] 1번째 손님 ( 소요시간 : 15분)
# [ ] 2번째 손님 ( 소요시간 : 16분)

# 총 탑승 승객 : 2 분

from random import *
customer = 0
for i in range(1,51):
    flag = " "
    time = randint(5,50)
    if(15 >= time >= 5 ):
        flag = "O"
        customer+=1
    print("[{0}] {1}번째 손님 ( 소요시간 : {2}분)".format(flag,i,time))
print("총 탑승 승객 : {0} 분".format(customer))
