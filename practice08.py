# 마린 : 공격 유닛 , 군인 , 원거리 공격
name = "마린" # 유닛의 이름
hp = 40
damage = 5 # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}.".format(hp , damage))

# 탱크 : 공격 유닛 ,탱크 , 원격 공격 , 일반 / 시즈모드


tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}.".format(tank_hp , tank_damage))

def attack(name, location , damage):
    print("{0} : {1} 방향으로 적군을 공격합니다.[공격력{2}]".format(name , location , damage))


attack(name , "1시", damage)
attack(tank_name , "1시", tank_damage)

## class

class Unit:
    def __init__(self, name , hp , damage): # 생성자 ( self 제외 , 동일한 arg를 받는다)
        self.name = name
        self.damage = damage
        self.hp = hp
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}.".format(self.hp , self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛 , 비행기 , 클로킬 ( 상대방에게 보이지 않음)

wraith1 = Unit("레이스", 80 , 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

#마인드 컨트롤 : 상대방유닛을 내 것으로 만드는 것 
wraith2 = Unit("레이스", 80 , 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
