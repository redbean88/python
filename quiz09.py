""" 문제 ) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출격 예제)
총 3개의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

[코드] """
class House:
    houseList = []
    # 초기화
    def __init__(self , location , house_type , deal_type , price ,completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
        self.houseList.append(self)

    # 메물 정보 표시
    def show_detail(self):
        print("총 {0}개의 매물이 있습니다.".format(len(House.houseList)))
        for house in House.houseList:
            print(house.location , house.house_type , house.deal_type ,\
                 house.price ,house.completion_year)

h = House("강남","아파트","매매","10억","2010년")
h = House("마포","오피스텔","전세","5억","2007년")
h = House("송파","빌라","월세","500/50","2007년")
h.show_detail()