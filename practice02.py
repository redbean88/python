# 연산자
print(1+1)  # 2
print(3-2)  # 1
print(5*2)  # 10
print(6/3)  # 2

print(2**3) # 2^3 = 8
print(5%3)  # 2(나머지)
print(10%3) # 1
print(5//3) # 1(몫)
print(10//3) # 3(몫)

print(10 > 3) # True
print(3 == 3) # True
print(4 == 2) # False

print(1 != 3 ) # True
print(not 1 != 3 ) # False
print((3 > 0) and (3 < 5 ))  # True
print((3 > 0) & (3 < 5 ))  # True

print((3 > 0) or (3 < 5 ))  # True
print((3 > 0) | (3 < 5 ))  # True

print(5> 4> 3)  # True

print(2 + 3 * 4 ) # 14
print((2 + 3) * 4 ) # 20
number = 2 + 3 * 4
print(number)
number = number + 2 # 16
print(number)
number += 2
print(number) # 18
number *= 2
print(number) # 36
number /= 2   # 나눗셈시 실수로 표시 된다.
print(number) # 18
number -= 2
print(number) # 16
number %= 5
print(number) # 1

print(abs(-5)) # 5  (절대값)
print(pow(3,2)) # 3^2 (제곱)
print(max(5,12)) # 12 
print(min(5,12)) # 5
print(round(5.12)) # 5 (반올림)

# 라이브러리 import
from math import *
print(floor(4.99)) # 4 (내림)
print(ceil(4.99)) # 5 (올림)
print(sqrt(16)) # 4 (제곱근_루트)

from random import * 

print(random()) # 난수 생성 ( 0.0 ~ 1.0 미만의 임의 값 생성)
print(random()*10 ) # 난수 생성 ( 0.0 ~ 10.0 미만의 임의 값 생성) 
print(int(random()*10 )) # 난수 생성 ( 0.0 ~ 10.0 미만의 임의 값 생성) 
print(int(random()*10 )+1) # 난수 생성 ( 0.0 ~ 10.0 이하의 임의 값 생성) 

print(randrange(1,46 )) # 난수 생성 ( 0.0 ~ 46.0 미만의 임의 값 생성) 
print(randint(1,46 )) # 난수 생성 ( 0.0 ~ 46.0 이사의 임의 값 생성) 

