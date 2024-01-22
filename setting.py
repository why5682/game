import random
import math
import pandas as pd

exp_table={0:0,1:15}
for i in range(1,200):
    exp_table[i+1]=int(exp_table[i]+((1.05+2*(1/i))*(exp_table[i]-exp_table[i-1]))) #i:n 의 의미 i레벨 에서 다음레벨로 가려면 n만큼의 exp가 필요하다
print(exp_table)
class character:
    def __init__(self,name):
        self.name=name
        self.exp=0
        self.str=10
        self.dex=10
        self.int=10
        self.luk=10
        self.level=1
        self.att=self.str*0.5+self.dex*0.1
        self.mana=self.int*1
        self.speed=1    #10이 최대, 먼저 10채우면 행동 가능
        self.acc=self.dex*1+self.str*0.2  #명중요구치와 비교
        self.avo=self.luk*1    #회피율함수 필요, 몬스터의 명중치를 구현해야함
        self.defe=1-(1/(self.str*1))   #퍼센트로 데미지 감소(방어율), 마딜은 고정딜로 할 생각
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
        self.att=self.str*0.5+self.dex*0.1
        self.mana=self.int*1
        self.acc=self.dex*1+self.str*0.2  #명중요구치와 비교
        self.avo=self.luk*1    #회피율함수 필요, 몬스터의 명중치를 구현해야함
        self.defe=1-(1/(self.str*1))   #퍼센트로 데미지 감소(방어율), 마딜은 고정딜로 할 생각
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

    def hit_by_mon(self,damage):
        self.hp_now-=damage

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
        print(f'방어율 : {round(self.defe,2)}%')
        print(f'크리티컬 확률 : {self.crit}%')
        print(f'크리티컬 데미지 : {self.crid}%')
        print('-'*10)

class monster:
    monster_book={
        '달팽이':(1, 120, 45, 1.5, 10, 18,0.02, 30, False)
        }
    def __init__(self):
        self.mon_name='달팽이'
        self.mon_level=1
        self.mon_hp=12
        self.mon_att=45
        self.mon_speed=2
        self.mon_acc=10
        self.mon_avo=1
        self.mon_defe=0.02   #0~1값
        self.gain_exp=30
        self.mon_skill=False  #t or f

def hit(character,monster):
    hit=character.acc >= monster.mon_avo
    if hit == False:
        hit= 0.5*(character.acc/monster.mon_avo) > random.random()
    return hit

def damage(character,monster):  #몬스터 방어율 기본적으로 0~0.5가 맞을듯, 보스 부터 1이상도 가능하게 하기
    damage=character.att-random.randint(0,int(character.att/2))
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
    mond=monster.mon_att-random.randint(0,int(monster.mon_att/4))
    if monster.mon_skill == True:
        return round(mond), True
    else:
        mond=monster.mon_att*(1-character.defe)
        return round(mond), False

def judge_turn(character, monster,a=0, b=0 ):
    while a < 10 and b < 10:
        a+=character.speed
        b+=monster.mon_speed
        print(a, b)

        if a >= 10 and b >= 10 :
            a-=10
            b-=10
            turn=0 #동시
            return turn, a, b
        elif a >= 10:
            a-=10
            turn=1 #player
            return turn, a, b
        elif b > 10:
            b-=10
            turn=2 #mon
            return turn, a, b
    
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
                print(f'{monster.mon_name}{damag}!의 피해를 주었습니다.')
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
        print(f'{monster.mon_name}을 물리쳤다.')
        print(f'{monster.gain_exp}의 경험치를 얻었다.')
        character.exp+=monster.gain_exp
        character.judge_level()
        return True
    if character.hp_now <= 0:
        print(f'사망했습니다.')
        character.hp_now=character.hp
        character.mp_now=character.mp
        return True
    else:
        return False
        
def turn_go(character,monster):
    a,b=0,0
    while end_turn(character,monster) == False:
        re=judge_turn(character,monster,a,b)
        a,b=re[1],re[2]
        pro_turn(re[0],character,monster)
        end_turn(character,monster)
    
def stat_up(character):
    character.judge_level()
    print(f'남은 ap포인트 : {character.ap}')
    while True:
        ans=input('무엇을 올립니까?\n1.힘\n2.민첩\n3.지력\n4.행운')
        try:
            int(ans)

playe=character('eheh')

for i in range(15):
    encount=monster()
    turn_go(playe,encount)
    input()

#class skill:

#class item: