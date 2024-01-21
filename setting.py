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
        self.judge_level()
        self.att=self.str*0.5+self.dex*0.1
        self.mana=self.int*1
        self.acc=self.dex*1+self.str*0.2  #명중요구치와 비교
        self.avo=self.luk*1    #회피율함수 필요, 몬스터의 명중치를 구현해야함
        self.defe=1-(1/(self.str*1))   #퍼센트로 데미지 감소(방어율), 마딜은 고정딜로 할 생각
        self.crit=self.dex*0.5
        self.crid=self.luk*1
        self.hp=int(math.log(self.level)*(30+self.level*(5+0.5*self.str+0.25*self.dex+0.125*(self.int+self.luk))))+50
        self.mp=int(math.log(self.level)*(30+self.level*(5+0.5*self.int+0.25*self.luk+0.125*(self.str+self.dex))))+50

    def judge_level(self):
        for i in range(1,200):
            if exp_table[i+1] > self.exp and self.exp >= exp_table[i]: #둘다 t일때, i+1이 현재 레벨
                if self.level != i+1:
                    n=i+1-self.level
                    print('레벨업'*n)
                    self.ap=5*(i)-self.str-self.dex-self.int-self.luk+40
                    self.sp=3*(i)        #찍은 스킬레벨 빼줘야 함
                    self.hp_now=self.hp
                    self.mp_now=self.mp
                self.level=i+1
                break

    def ap_use_1(self):
        while True:
            print('ap를 사용합니다.')
            print(f'남은ap : {self.ap}')
            cho=input('----------\n선택지의 번호를 입력하시오\n1.힘\n2.민첩\n3.지력\n4.행운\n5.나가기\n----------\n : ')
            try:
                cho = int(cho)
                if cho in [1,2,3,4,5]:
                    return cho
                print('잘못입력하셨습니다.')
            except ValueError:
                print('잘못입력하셨습니다.')
        
    def ap_use_2(self,cho):
        while True:
            if cho == 5:
                return cho, 0
            how=input('얼마나 올리시겠습니까? : ')
            try:
                how=int(how)
                if how <= self.ap:
                    return cho, how
                print('잘못입력하셨습니다.')
            except ValueError:
                    print('잘못입력하셨습니다.')

    def ap_use_3(self,cho,how):
        self.ap-=how 
        if cho == 1:
            self.str+=how
            print(f'힘을 {how}만큼 올립니다.')
        elif cho == 2:
            self.str += how
            print(f'민첩을 {how}만큼 올립니다.')
        elif cho == 3:
            self.int+=how
            print(f'지력을 {how}만큼 올립니다.')
        elif cho == 4:
            self.luk+=how
            print(f'행운을 {how}만큼 올립니다.')
        elif cho == 5:
            print('처음으로 돌아갑니다.')

    def ap_use(self):
        if self.ap == 0:
            print('남은 ap가 없습니다.')
            return
        cho=self.ap_use_1()
        cho, how=self.ap_use_2(cho)
        self.ap_use_3(cho,how)
        self.update_status()

    def show_exp(self):
        print('='*10)
        print(f'  현재 경험치 / 경험치 : {self.exp-exp_table[self.level-1]} / {exp_table[self.level]-exp_table[self.level-1]}')
        print('='*10)

    def show_status(self):
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
        self.mon_speed=1
        self.mon_acc=10
        self.mon_avo=1
        self.mon_defe=0.02   #0~1값
        self.gain_exp=30
        self.mon_skill=False  #t or f

class battle(character,monster):    #누구와 전투를 할지 이미 정한 상태
    def __init__(self,player_dic,encount):
        super().__init__(player)
        self.character= character(**player_dic)
        super().__init__(encount)
        self.monster = monster()
        self.player_turn=0
        self.mon_turn=0
        self.battle_end=False

   # def load(self,dic):
        

    def hit(self):
        hit=self.character.acc >= self.monster.mon_avo
        if hit == False:
            hit= 0.5*(self.character.acc/self.monster.mon_avo) > random.random()
        return hit

    def damage(self):  #몬스터 방어율 기본적으로 0~0.5가 맞을듯, 보스 부터 1이상도 가능하게 하기
        damage=self.character.att-random.randint(0,int(self.character.att/2))
        damage=damage*(1-(self.monster.mon_defe*(1-self.character.pei)))
        if damage <= 0:
            damage = 1
        if self.character.crit/100 > random.random():
            damage*=(1+self.character.crid/100)
            return round(damage), True
        return round(damage) , False

    def avoid(self):
        avoid=1-((1+self.monster.mon_acc*0.02)/(self.character.avo*0.02)) #4950이면 99%의 회피율, 어쨋든 100%의 회피율 가능함
        avo=avoid > random.random()
        return avo

    def injury(self):
        mond=self.monster.mon_att-random.randint(0,int(self.monster.mon_att/4))
        if self.monster.mon_skill == True:
            return round(mond), True
        else:
            mond=self.monster.mon_att*(1-self.character.defe)
            return round(mond), False

    def judge_turn(self, a, b):
        for i in range(10):
            self.player_turn+=a+self.character.speed
            self.mon_turn+=b+self.monster.mon_speed
            print(self.player_turn, self.mon_turn)
            if self.player_turn >= 10 or self.mon_turn >= 10:
                break
        if self.player_turn >= 10 and self.mon_turn >= 10 :
            self.player_turn-=10
            self.mon_turn-=10
            self.turn=0 #동시
            return self.turn, self.player_turn, self.mon_turn
        elif self.player_turn >= 10:
            self.player_turn-=10
            self.turn=1 #player
            return self.turn, self.player_turn, self.mon_turn
        elif self.mon_turn >= 10:
            self.mon_turn-=10
            self.turn=2 #mon
            return self.turn, self.player_turn, self.mon_turn
    
    def pro_turn(self):
        if self.turn == 0:
            if self.hit() == True:
                damag,cri=self.damage()
                self.monster.mon_hp-=damag
                if cri == True:
                    print(f'{self.monster.mon_name}{damag}!의 피해를 주었습니다.')
                else:
                    print(f'{self.monster.mon_name}에게{damag}의 피해를 주었습니다.')
            else:
                print('Miss')
            if self.avoid() == True:
                print('회피하였습니다.')
            else:
                dama,man=self.injury()
                self.character.hp_now-=dama
                if man == True:
                    print(f'{dama}만큼의 마법피해를 입었습니다.')
                else:
                    print(f'{dama}만큼의 물리피해를 입었습니다.')
        elif self.turn == 1:
            if self.hit() == True:
                damag,cri=self.damage()
                self.monster.mon_hp-=damag
                if cri == True:
                    print(f'{self.monster.mon_name}{damag}!의 피해를 주었습니다.')
                else:
                    print(f'{self.monster.mon_name}에게{damag}의 피해를 주었습니다.')
        elif self.turn == 2:
            if self.avoid() == True:
                print('회피하였습니다.')
            else:
                dama,man=self.injury()
                self.character.hp_now-=dama
                if man == True:
                    print(f'{dama}만큼의 마법피해를 입었습니다.')
                else:
                    print(f'{dama}만큼의 물리피해를 입었습니다.')
    
    def end_turn(self):
        if self.monster.mon_hp <= 0:
            print(f'{self.monster.mon_name}을 물리쳤다.')
            print(f'{self.monster.gain_exp}의 경험치를 얻었다.')
            self.leveling(self.monster.gain_exp)
            print(self.character.exp)
            self.battle_end=True
            return self.battle_end
        if self.character.hp_now <= 0:
            print(f'사망했습니다.')
            self.battle_end=True
            return self.battle_end
        else:
            self.battle_end=False
            return self.battle_end
        
    def turn_go(self):
        while self.battle_end == False:
            self.judge_turn(self.player_turn,self.mon_turn)
            print(self.turn)
            self.pro_turn()
            self.end_turn()
            input()
        return self.character.exp, self.character.hp_now

    def leveling(self,gain_exp):
        self.character.exp+=gain_exp

player=character('eheh')
player.exp=550
player.dex=30
player.show_status()
player.update_status()
encount=monster()
scene=battle(player.__dict__,encount)
player.exp,player.hp_now=scene.turn_go()
player.show_status()

print(scene.__dict__)

#class skill:

#class item: