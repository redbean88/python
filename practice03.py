sentence = "나는 소년입니다"
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년입니다
파이썬은 쉬워요
"""
print(sentence3)

## 슬라이싱

jumin = '990120-1234567'
print("성별 : " + jumin[7])     # 1
print("연 : " + jumin[0:2])     # 99
print("월 : " + jumin[2:4])     # 01
print("일 : " + jumin[4:6])     # 20
print("생년월일: " + jumin[:6]) # 990120
print("뒤 7자리: " + jumin[7:]) # 1234567
print("뒤 7자리 (뒤에서 부터): " + jumin[-7:]) # 1234567

## 문자열처리함수

python = "Python is Amazing"
print(python.lower())   
print(python.upper())
print(python[0].isupper())  # 대소문자 확인
print(len(python))
print(python.replace("Python","Java"))

index =python.index("n")
print(index)    # 5
index = python.index("n", index+1)
print(index)

# print(python.index("Java")) # valueError
print(python.find("Java"))      # -1

print(python.count("n"))    # 2  나온횟수

# 문자열 포맷

# print("a"+ "b")

# 방법 1
print("나는 %d살입니다." %20)               ## 정수
print("나는 %s를 좋아합니다." %"파이썬")    ## String
print("Apple 은 %c로 시작해요." %"A" )      ## char

print("나는 %s색과 %s색을 좋아해요"%("파란","빨강"))

# 방법2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란","빨강"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨강"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨강"))

# 방법3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20 , color = "빨간"))

# 방법4 ( 3.6 이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")

## 이스케이프 문자
print("백문이 불여일견 \n백견이 불여일타")

print('너는 \"나도코딩\"입니다') # 너는 "나도코딩"입니다
print("너는 \"나도코딩\"입니다") # 너는 "나도코딩"입니다
print("C:\\Users\\")
# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")
# \b : 백스페이스 (한 글자 삭제)
print("RedB\bApple")
# \t : 탭
print("Red\tApple")