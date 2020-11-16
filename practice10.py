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