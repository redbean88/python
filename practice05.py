# if

weather = input("오늘 날씨는 어떤가요?")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("그냥 가세요")

temp = int(input("기온은 어때요? "))

if 30 <= temp:
    print("너무 더워료. 나가지 마세요")
elif 10 <= temp and temp < 30 :
    print("괜찮은 날씨에요")
elif 0 <= temp < 10 : 
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")

# for

for waiting_no in [0,1,2,3,4]: # 0 ,1 ,2, 3, 4
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5): # 0 ,1 ,2, 3, 4
    print("대기번호 : {0}".format(waiting_no))

startbucks = ["아이언맨","토르","그루트"]
for customer in startbucks:
    print("{0}, 커피가 준비 되었습니다.".format(customer))

# while
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요".format(customer,index))
    index -= 1
    if index == 0:
        print("폐기")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요".format(customer,index))
#     index += 1
#     if index == 10:
#         print("폐기")

costomer = "토르"
person ="Unknown"

while person != customer:
    print("{0}, 커피가 준비 되었습니다. ".format(customer))
    person = input("이름이 어떻게 되세요?")


# continue / break

absent = [2,5]  # 결석
no_book = [7]   # 책을 안가져옴
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("수업 종료 , {0}는 교무실로".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

# oneline for

# 출석 번호가 1,2,3,4, 아에 100을 붙이기로 함

students =[1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor"]
students = [len(x) for x in students]
print(students)

# 대문자로 변환
# 학생 이름을 길이로 변환
students = ["Iron man", "Thor"]
students = [x.upper() for x in students]
print(students)