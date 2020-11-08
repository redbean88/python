print(5)        # 자연수
print(-10)      # 음수
print(3.14)     # 실수
print(5+4)      # 덧셈
print(6*6)      # 곱

print('풍선')   # 풍선
print("풍선")   # 풍선
print("풍선"*9) # 풍선풍선풍선풍선풍선풍선풍선풍선풍선

print(5>10)     # false
print(5<10)     # true
print(True)     # true
#print(true)     # Exception has occurred: NameError
print(False)     # False
#print(false)     # Exception has occurred: NameError
print(not True)     # false
print(not False)     # true

# 애완동물을 소개해 주세요~
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 "+ animal+"의 이름은 "+ name)
#print(name+"이는 "+str(age)+"살, "+hobby+"을 좋아해요")
print(name,"이는 ",age,"살, ",hobby,"을 좋아해요") # [,]표시는 파싱하지 않아도, 출력 가능
print(name+"이는 어른일까요?"+ str(is_adult))
