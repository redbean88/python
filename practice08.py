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
    def __init__(self, name , hp , speed): # 생성자 ( self 제외 , 동일한 arg를 받는다)
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self , location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name , location , self.speed))

marine1 = Unit("메딕", 5,5)

#마인드 컨트롤 : 상대방유닛을 내 것으로 만드는 것 
wraith2 = Unit("레이스", 80,5 )
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

class AttackUnit(Unit):
    def __init__(self, name , hp , speed , damage): # 생성자 ( self 제외 , 동일한 arg를 받는다)
        Unit.__init__(self, name , hp, speed)
        self.damage = damage

    def attack(self , location):
        print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력 : {2}]"\
            .format(self.name,location,self.damage))
    
    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name , self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛 , 범위공격

firebat = AttackUnit("파이어뱃",50,16,0)
firebat.attack("5시")

# 공격을 2번 받는다고 가정
firebat.damaged(25)
firebat.damaged(25)

class Flyable:
    def __init__(self , flying_speed):
        self.flying_speed = flying_speed

    def fly(self , name , location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name , location , self.flying_speed))

# 다중상속

class FlyableAttackUnit(AttackUnit , Flyable):
    def __init__(self , name ,hp , damage , flying_speed):
        AttackUnit.__init__(self, name, hp ,0 , damage) # 지상 speed 0 
        Flyable.__init__(self ,flying_speed)

    def move(self , location):
        print("[공중 유닛 이동]")
        self.fly(self.name , location)

# 발키리 : 공중공격유닛 , 한번에 14발 발사
valkyrie = FlyableAttackUnit("발키리", 200 , 6, 5)
valkyrie.fly(valkyrie.name , "3시")

# 벌쳐 : 지상 유닛 , 기동성이 좋음

vulture = AttackUnit("벌쳐 ", 80 , 10 ,20 )
vulture.move("11시")
# 배틀크루저 : 공중 유닛

battecruiser = FlyableAttackUnit("배틀크루저 " , 500 , 25, 3)
# battecruiser.fly(battecruiser.name , "9시")
battecruiser.move("9시")

# pass
class BuildingUnit(Unit):
    def __init__(self , name , hp , location):
        # pass # 임시로 컴파일 진행
        # Unit.__init__(self, name, hp , 0)
        super().__init__(name,hp,0) # 다중 상속할 경우, 상속받은 첫번째 부모의 메소드를 호출
        self.location = location

supply_depot = BuildingUnit("서플라이 디폿", 500 , "7시")