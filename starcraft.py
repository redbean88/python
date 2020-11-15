from random import *

class Unit:
    def __init__(self, name , hp , speed): # 생성자 ( self 제외 , 동일한 arg를 받는다)
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self , location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name , location , self.speed))
    
    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name , self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))

class AttackUnit(Unit):
    def __init__(self, name , hp , speed , damage): # 생성자 ( self 제외 , 동일한 arg를 받는다)
        Unit.__init__(self, name , hp, speed)
        self.damage = damage

    def attack(self , location):
        print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력 : {2}]"\
            .format(self.name,location,self.damage))

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self , "마린",40,1,5)

    # 스팀팩 (이동속도증가, 공격속도증가, 체력 10 감소)
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다.".format(self.name))
        else:
            print("{0} : 체력이 부족합니다.".format(self.name))

# 탱크
class Tank(AttackUnit):

    def __init__(self):
        AttackUnit.__init__(self , "탱크",150 ,1 ,35)
        self.seize_mode = False

    seize_developed = False # 개발 여부

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        if self.seize_mode == False:
            print("{0} : 시즈모드 전환".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : 일반모드 전환".format(self.name))
            self.damage /= 2
            self.seize_mode = False
        

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
        self.fly(self.name , location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self , "레이스", 80 , 20 , 5)
        self.clocked = False
    def clocking(self):
        if self.clocked == True:
            print("{0} : 클록킹 해제".format(self.name))
            self.clocked == False
        if self.clocked == False:
            print("{0} : 클록킹 시작".format(self.name))
            self.clocked == True
            
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("gg")

# 게임 진행
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동

for unit in attack_units:
    unit.move("1시")

Tank.seize_developed = True

# 공격 모드 준비
for unit in attack_units:
    if isinstance(unit , Marine):
        unit.stimpack()
    elif isinstance(unit ,Tank):
        unit.set_seize_mode()
    elif isinstance(unit ,Wraith):
        unit.clocking()

# 공격 
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20))

game_over()