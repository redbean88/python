# 리스트 []

# 지하철 칸별로 10명 , 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호는 몇 번째 칸에 타고 있는가
print(subway.index("조세호"))

# 하하 탑승
subway.append("하하")
print(subway)

# 형돈을 유재성/조세호 사이
subway.insert(1,"형돈")
print(subway)

# 뒤에서 한명씩 하차
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# sorting
num_list = [5,2,6,7,5,1,9]
num_list.sort()
print(num_list)

# reverse
num_list.reverse()
print(num_list)

# clear
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["재석",20,True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)


# dict (key , value) java와 c의 map과 유사

cabinet = {3:"재석",100:"태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
# print(cabinet[5]    # error
print(cabinet.get(5))   # None
print(cabinet.get(5, "사용 가능"))   # 사용가능
print(cabinet.get(5), "사용 가능")   # none 사용가능

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet2 = {"A-3": "재석","A-100": "태호"}
print(cabinet2)

# insert  / update
cabinet2["A-3"] = "김종국"
cabinet2["C-10"] = "조세호"
print(cabinet2)

# remove
del cabinet2["A-3"]
print(cabinet2)

# key 출력
print(cabinet2.keys())

# value 출력
print(cabinet2.values())

# key , value 출력
print(cabinet2.items())

# removeAll
cabinet2.clear()
print(cabinet2)

# tuple 
# 내부 속성 추가 불가 ( 속성값 변경은 가능)

menu = ("돈가스","치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생성")   #error

(name , age , hobby) = ("종국",20,"코딩")
age+=1
print(name , age , hobby)   # 종국 21 코딩


# set (집합)
# 중복 안됨, 순서 없음(index 없음)
my_set = {1,2,3,3,3,3}
print(my_set)

java = {"재석","태호","세형"}
# print(java.get(0)) # error
python = set(["재석","명수"])

# 교집합 (java 와 python 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 와 python 중 하나라도 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (python 을 못하는 개발자)
print(java - python)
print(java.difference(python))

# add
python.add("태호")
print(python)

# delete
java.remove("태호")
print(java)

# 자료구조의 변경
menu = {"커피","우유","주스"}
print(menu , type(menu))
menu = list(menu)
print(menu , type(menu))
menu = tuple(menu)
print(menu , type(menu))
menu = set(menu)
print(menu , type(menu))