import random
import math
import pandas as pd

exp_table={0:0,1:15}
for i in range(1,200):
    exp_table[i+1]=int(exp_table[i]+((1.05+2*(1/i))*(exp_table[i]-exp_table[i-1]))) #i:n 의 의미 i레벨 에서 다음레벨로 가려면 n만큼의 exp가 필요하다

monster_book={
    '달팽이':(1,30,5,1,5,5,0,5, False),
    '파란달팽이':(3,50,10,1,8,7,0.01,7,False),
    '빨간달팽이':(5,70,30,1.5,10,18,0.02,30,False),
    '테스트':(1,1,1,1,1,0,1,100000000,False),
    '아이즈':(31,750,300,1.2,70,40,0.05,550,False),
    '발록':(110,100000,1000,0.2,100,70,0.1,1000,True)
    }
class character:
    def __init__(self,name):
        self.name=name
        self.exp=0
        self.str=10
        self.dex=10
        self.int=10
        self.luk=10
        self.level=1
        self.att=self.str*1+self.dex*0.2
        self.mana=self.int*1
        self.speed=1.1    #10이 최대, 먼저 10채우면 행동 가능
        self.acc=self.dex*1+self.str*0.2  #명중요구치와 비교
        self.avo=self.luk*1    #회피율함수 필요, 몬스터의 명중치를 구현해야함
        self.defe=1-(100/(self.str)+90)   #퍼센트로 데미지 감소(방어율), 마딜은 고정딜로 할 생각
        self.crit=self.dex*0.5
        self.crid=self.luk*1
        self.pei=0  #관통, 방어력 무시, 0~1의 값
        self.hp=int(math.log(self.level)*(10+self.level*(5+0.5*self.str+0.25*self.dex+0.125*(self.int+self.luk))))+50
        self.hp_now=50
        self.mp=int(math.log(self.level)*(10+self.level*(5+0.5*self.int+0.25*self.luk+0.125*(self.str+self.dex))))+50
        self.mp_now=50
        self.ap=0
        self.sp=0
        self.prof='초보자'

    def update_status(self):
        self.att=self.str*1+self.dex*0.2
        self.mana=self.int*1
        self.acc=self.dex*1+self.str*0.2  #명중요구치와 비교
        self.avo=self.luk*1    #회피율함수 필요, 몬스터의 명중치를 구현해야함
        self.defe=1-(100/(self.str+90))   #퍼센트로 데미지 감소(방어율), 마딜은 고정딜로 할 생각
        self.crit=self.dex*0.5
        self.crid=self.luk*1
        self.hp=int(math.log(self.level)*(30+self.level*(5+0.5*self.str+0.25*self.dex+0.125*(self.int+self.luk))))+50
        self.mp=int(math.log(self.level)*(30+self.level*(5+0.5*self.int+0.25*self.luk+0.125*(self.str+self.dex))))+50
        self.ap=5*self.level-self.str-self.dex-self.int-self.luk+35
        self.sp=3*self.level-3        #찍은 스킬레벨 빼줘야 함

    def judge_level(self):
        for i in range(200):
            if exp_table[i+1] > self.exp and self.exp >= exp_table[i]: #둘다 t일때, i+1이 현재 레벨
                if self.level != i+1:
                    n=i+1-self.level
                    print('레벨업\n'*n)
                    self.level=i+1
                    self.hp_now=int(math.log(self.level)*(30+self.level*(5+0.5*self.str+0.25*self.dex+0.125*(self.int+self.luk))))+50
                    self.mp_now=int(math.log(self.level)*(30+self.level*(5+0.5*self.int+0.25*self.luk+0.125*(self.str+self.dex))))+50
                self.level=i+1
                self.update_status()
                break

    def full(self):
        self.hp_now=self.hp
        self.mp_now=self.mp

    def str_up(self,how):
        self.ap-=how
        self.str+=how
        print(f'힘을 {how}만큼 올려 {self.str}이 되었습니다.\n')

    def dex_up(self,how):
        self.ap-=how
        self.dex+=how
        print(f'민첩을 {how}만큼 올려 {self.dex}이 되었습니다.\n')

    def int_up(self,how):
        self.ap-=how
        self.int+=how
        print(f'지능을 {how}만큼 올려 {self.int}이 되었습니다.\n')

    def luk_up(self,how):
        self.ap-=how
        self.luk+=how
        print(f'행운을 {how}만큼 올려 {self.luk}이 되었습니다.\n')

    def show_exp(self):
        print('='*10)
        print(f'  현재 경험치 / 경험치 : {self.exp-exp_table[self.level-1]} / {exp_table[self.level]-exp_table[self.level-1]}')
        print('='*10)

    def show_status(self):  #이것만 해도되네
        self.update_status()
        print('-'*10)
        print(f'이름 : {self.name}')
        print(f'레벨 : {self.level}')
        self.show_exp()
        print('스탯창')
        print(f'힘 : {self.str}')
        print(f'민첩 : {self.dex}')
        print(f'지력 : {self.int}')
        print(f'행운 : {self.luk}')
        print(f'남은ap포인트 : {self.ap}')
        print('-'*10)
        print('능력치')
        print(f'공격력 : {self.att}')
        print(f'마력 : {self.mana}')
        print(f'hp : {self.hp_now} / {self.hp}')
        print(f'mp : {self.mp_now} / {self.mp}')
        print(f'공격속도 : {self.speed}')
        print(f'명중치 : {round(self.acc,2)}')
        print(f'회피치 : {round(self.avo,2)}')
        print(f'방어율 : {round(self.defe,2)*100}%')
        print(f'크리티컬 확률 : {self.crit}%')
        print(f'크리티컬 데미지 : {self.crid}%')
        print('-'*10)

class monster:
    def __init__(self,name):
        self.mon_name=name
        self.mon_level=monster_book[name][0]
        self.mon_hp=monster_book[name][1]
        self.mon_att=monster_book[name][2]
        self.mon_speed=monster_book[name][3]
        self.mon_acc=monster_book[name][4]
        self.mon_avo=monster_book[name][5]
        self.mon_defe=monster_book[name][6]   #0~1값
        self.gain_exp=monster_book[name][7]
        self.mon_skill=monster_book[name][8]  #t or f

def hit(character,monster):
    hit=character.acc >= monster.mon_avo
    if hit == False:
        hit= 0.5*(character.acc/monster.mon_avo) > random.random()
    return hit

def damage(character,monster):  #몬스터 방어율 기본적으로 0~0.5가 맞을듯, 보스 부터 1이상도 가능하게 하기
    damage=character.att-random.randint(0,int(character.att*(0.6+0.2*(1/(character.acc-5)))))
    damage=damage*(1-(monster.mon_defe*(1-character.pei)))
    if damage <= 0:
        damage = 1
    if character.crit/100 > random.random():
        damage*=(1+character.crid/100)
        return round(damage), True
    return round(damage) , False

def avoid(character,monster):
    avoid=1-((1+monster.mon_acc*0.02)/(character.avo*0.02)) #4950이면 99%의 회피율, 어쨋든 100%의 회피율 가능함
    avo=avoid > random.random()
    return avo

def injury(character, monster):
    mond=monster.mon_att-random.randint(0,int(monster.mon_att/3))
    if monster.mon_skill == True:
        return round(mond), True
    else:
        mond=monster.mon_att*(1-character.defe)
        return round(mond), False

def judge_turn(character, monster,a=0, b=0 ):
    while a < 10 and b < 10:
        a+=character.speed
        b+=monster.mon_speed
        if a >= 10 and b >= 10 :
            a-=10
            b-=10
            return 0, a, b
        elif a >= 10:
            a-=10
            return 1, a, b
        elif b >= 10:
            b-=10
            return 2, a, b
    
def pro_turn(turn,character,monster):
    if turn == 0:
        if hit(character,monster) == True:
            damag,cri=damage(character,monster)
            monster.mon_hp-=damag
            if cri == True:
                print(f'{monster.mon_name}{damag}!의 피해를 주었습니다.')
            else:
                print(f'{monster.mon_name}에게{damag}의 피해를 주었습니다.')
        else:
            print('Miss')

        if avoid(character,monster) == True:
            print('회피하였습니다.')
        else:
            dama,man=injury(character,monster)
            character.hp_now-=dama
            if man == True:
                print(f'{dama}만큼의 마법피해를 입었습니다.')
            else:
                print(f'{dama}만큼의 물리피해를 입었습니다.')
    elif turn == 1:
        if hit(character,monster) == True:
            damag,cri=damage(character,monster)
            monster.mon_hp-=damag
            if cri == True:
                print(f'{monster.mon_name}에게{damag}!의 피해를 주었습니다.')
            else:
                print(f'{monster.mon_name}에게{damag}의 피해를 주었습니다.')
        else:
            print('Miss')
    elif turn == 2:
        if avoid(character,monster) == True:
            print('회피하였습니다.')
        else:
            dama,man=injury(character,monster)
            character.hp_now-=dama
            if man == True:
                print(f'{dama}만큼의 마법피해를 입었습니다.')
            else:
                print(f'{dama}만큼의 물리피해를 입었습니다.')
    
def end_turn(character,monster):
    if monster.mon_hp <= 0:
        print(f'{monster.mon_name}을 물리쳤다.\n')
        print(f'{monster.gain_exp}의 경험치를 얻었다.\n')
        character.exp+=monster.gain_exp
        character.judge_level()
        return True
    if character.hp_now <= 0:
        print(f'사망했습니다.\n')
        character.hp_now=character.hp
        character.mp_now=character.mp
        return True
    else:
        return False
        
def turn_go(character,monster):
    a,b=0,0
    while end_turn(character,monster) == False: #이게 문제인듯함
        re=judge_turn(character,monster,a,b)
        a,b=re[1],re[2]
        pro_turn(re[0],character,monster)
    character.show_status()
    cho=input('어떤 행동을 하시겠습니까?\n1.마을\n2.포션 사용\n3.ap 사용\n또는 계속하려면 아무 키나 누르세요.\n')
    return cho
    
def stat_up(character):
    character.judge_level()
    print(f'남은 ap포인트 : {character.ap}')
    if character.ap == 0:
        print('남은 ap포인트가 없습니다.\n')
        return
    while True:
        ans = input('무엇을 올립니까?\n1.힘\n2.민첩\n3.지력\n4.행운\n5.취소\n : ')
        try:
            ans = int(ans)
            if ans in [1, 2, 3, 4, 5]:
                if ans == 5:
                    return
                while True:
                    how = input('얼마나 올립니까?\n')
                    try:
                        how = int(how)
                        if how <= character.ap:
                            if ans == 1:
                                character.str_up(how)
                            elif ans == 2:
                                character.dex_up(how)
                            elif ans == 3:
                                character.int_up(how)
                            elif ans == 4:
                                character.luk_up(how)
                            character.update_status()
                            return  # Exit the function after successful stat increase
                        print('잘못된 입력입니다.')
                    except ValueError:
                        print('잘못된 입력입니다.')
            else:
                print('잘못된 입력입니다.')
        except ValueError:
            print('잘못된 입력입니다.')

def battle(character,monste,num):
    for i in range(num):
        encount=monster(monste)
        a=turn_go(character,encount)
        if a == '1':
            print('마을로 돌아갑니다.')
            character.full()
            return False
        elif a == '2':
            print('포션을 사용합니다.')
            character.hp_now+=100
            if character.hp_now > character.hp:
                character.hp_now = character.hp
        elif a == '3':
            print('ap를 사용합니다.')
            stat_up(character)
    print('설정된 전투가 모두 끝났습니다.\n')

def set_battle(character):
    while True:
        ans = input('어떤 몬스터를 사냥하시겠습니까?\n1.취소\n')
        if ans == '1':
            print('사냥을 취소하고 마을로 돌아갑니다.')
            break
        try:
            monster_book[ans]
            while True:
                how = input('몇 번 사냥하시겠습니까?\n')
                try:
                    how = int(how)
                    if how > 0:
                        battle(character, ans, how)
                        a=input('더 할래? 안할거면 1') #임시 조치
                        return a
                    else:
                        print('사냥 횟수는 양수여야 합니다. 다시 입력하세요.')
                except ValueError:
                    print('잘못된 입력입니다.')
                break  # Exit the second while loop once a valid input is received
        except KeyError:
            print('해당 몬스터가 존재하지 않습니다. 다시 입력하세요.')



playe=character('eheh')
a=0
while a != '1':
    a=set_battle(playe)
#class skill:

#class item: