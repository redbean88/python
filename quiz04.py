# 문제 ) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참셕률을 옾이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.

# 조선1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조선2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다 --

# (활용 예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

from random import *
replyList = list(range(1,21)) # 1부터 20까지 숫자 생성
shuffle(replyList)
print("""
 -- 당첨자 발표 --
 치킨 당첨자 : %s
 커피 당첨자 : %s
 -- 축하합니다 --
"""%(replyList[0],replyList[1:4]))
