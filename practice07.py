# 표준입출력

print("Python","Java",sep=" ,",end="?")
print("무엇이 더 재밌을까요?")

import sys
print("Python","Java", file=sys.stdout)
print("Python","Java", file=sys.stderr)

scores = {"수학":0 ,"영어": 50}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 001, 002, 003, ...

for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이다 입력하세요 :") # 항상 String타입으로 저장
print("입력하신 값은 " + answer + "입니다")

# 다양한 출력포맷

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >10}".format(-500))
# 왼쪽 정렬하고, 빈칸을 _로 채음
print("{0:_<+10}".format(500))
# 3자리 마다 콤마 찍어주기
print("{0:,}".format(100000000000000000000000000))
# 3자리 마다 콤마 찍어주기, +-부호도 붙이기
print("{0:+,}".format(100000000000000000000000000))
print("{0:+,}".format(100000000000000000000000000))
# 3자리 마다 콤마 찍어주기, +-부호도 붙이고, 자릿수 확보하기
print("{0:^<+30,}".format(1000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자릿수 까지만 표시 (3째 자리에서 반올림)
print("{0:.2f}".format(5/3))

# 파일입출력
score_file = open("score.txt","w",encoding="utf8") # overwrite
print("수학 : 0",file=score_file)
print("영어 : 30",file=score_file)
score_file.close()

score_file = open("score.txt","a",encoding="utf8") # add
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt","r",encoding="utf8") # read all
print(score_file.read())
score_file.close()

score_file = open("score.txt","r",encoding="utf8") # read line
print(score_file.readline(),end="") # 한줄읽고 라인피드
print(score_file.readline(),end="") # 한줄읽고 라인피드
print(score_file.readline(),end="") # 한줄읽고 라인피드
print(score_file.readline(),end="") # 한줄읽고 라인피드
score_file.close()

score_file = open("score.txt","r",encoding="utf8") # read all
while True:
    line = score_file.readline()
    if not line: # if == null
        break
    print(line,end="")
score_file.close()

# pickle

score_file = open("score.txt","r",encoding="utf8") # read 2 list
lines = score_file.readlines() # tolist
for line in lines:
    print(line,end="")
score_file.close()

import pickle
profile_file = open("profile.pickle","wb")
profile = {"이름":"박명수","나이":30,"취미":["축구","골프"]}
print(profile)
pickle.dump(profile , profile_file) # profile 에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

# with (close 필요 없음)

import pickle

with open("profile.pickle","rb") as profile_file:           # rb (read binary)
    print(pickle.load(profile_file))

with open("study.txt","w",encoding="utf8") as study_file:   
    study_file.write("파이썬 공부중")

with open("study.txt","r",encoding="utf8") as study_file:   # r == rt(read text)
    print(study_file.read())