# 모듈
# 같은 경로 , 파이썬 라이브러리 위치

# import theater_module
# import theater_module as mv
# from theater_module import price, price_mornig
# from theater_module import price_soldier as price
from theater_module import *
price(3) # 3명이서 영화 보러 갔을 때 가격
price_mornig(4)
price_soldier(5)

# 패키지
import travel.thailand # 모튤이나 패키지 명만 사용 가능
# from travel.thailand import *
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to2 = vietnam.VietnamPackage()
trip_to2.detail()

from travel import *
trip_to2 = vietnam.VietnamPackage()
trip_to2.detail()

from travel import *
trip_to2 = thailand.ThailandPackage()
trip_to2.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))

# pip install

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# 내장 함수
# input : 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요?")
print("{0}은/는 좋은 언어 입니다.")

# dir : 객체 상태 표시
print(dir())
import random # 외장 함수
print(dir())

print(dir(random))
lst = [1,2,3]
print(dir(lst))

name = "Jim"
print(dir(name))

# 외장함수

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재 합니다.")
    os.rmdir(folder)
    print(folder , "삭제")
else:
    os.makedirs(folder) # 폴더 생성
    print(folder , "폴더를 생성합니다.")

print(os.listdir())

# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y=%m-%d %H:%M:%S"))


import datetime
# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100) # 100일 저장
print("만난지 100일 째 날 : {0}".format(today+td))


