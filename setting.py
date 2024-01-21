import random
import math

exp_table={0:0,1:15}
for i in range(1,200):
    exp_table[i+1]=int(exp_table[i]+((1.07+0.93*(1/i))*(exp_table[i]-exp_table[i-1])))

class character:
    def __init__(self,name):
        self.name=name
        self.exp=0
        self.str=10
        self.dex=10
        self.int=10
        self.luk=10
        self.level=1
        self.att=self.str*1+self.dex*0.5
        self.mana=self.int*2
        self.acc=self.dex*1+self.str*0.5  #명중요구치와 비교
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
        self.att=self.str*1+self.dex*0.5
        self.mana=self.int*2
        self.acc=self.dex*1+self.str*0.5  #명중요구치와 비교
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
                    print('레벨업')
                    self.ap=5*(i+1)-self.str-self.dex-self.int-self.luk+40
                    self.sp=3*(i+1)        #찍은 스킬레벨 빼줘야 함
                self.level=i+1
                self.hp_now=self.hp
                self.mp_now=self.mp
                break
    
    def leveling(self,gain_exp):
        self.exp+=gain_exp
        self.update_status()

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
        print("╔" + "═" * (len(str(self.exp-exp_table[self.level-1]))+len(str(exp_table[self.level]-exp_table[self.level-1])) + 28) + "╗")
        print(f'  현재 경험치 / 경험치 : {self.exp-exp_table[self.level-1]} / {exp_table[self.level]-exp_table[self.level-1]}')
        print("╚" + "═" * (len(str(self.exp-exp_table[self.level-1]))+len(str(exp_table[self.level]-exp_table[self.level-1])) + 28) + "╝")

    def show_status(self):
        self.update_status()
        print('-'*10)
        print(f'이름 : {self.name}')
        print(f'레벨 : {self.level}')
        print('-'*10)
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
        print(f'명중치 : {round(self.acc,2)}')
        print(f'방어율 : {round(self.defe,2)}%')
        print(f'크리티컬 확률 : {self.crit}%')
        print('-'*10)

    def hit(self,req_acc):
        hit=self.acc >= req_acc
        if hit == False:
            hit= 0.5*(self.acc/req_acc) > random.random()
        return hit

    def damage(self,mon_defe):  #몬스터 방어율 기본적으로 0~0.5가 맞을듯, 보스 부터 1이상도 가능하게 하기
        damage=self.att-random.randint(0,int(self.att/2))
        damage=damage(1-(mon_defe*(1-self.pei)))
        if damage <= 0:
            damage = 1
        return damage

    def avoid(self,mon_acc):
        avoid=1-((1+mon_acc*0.02)/self.avo*0.02) #4950이면 99%의 회피율, 어쨋든 100%의 회피율 가능함
        avo=avoid > random.random()
        return avo

    def injury(self,mon_att,att_type_mana):
        if att_type_mana == True:
            return mon_att
        else:
            mon_att=mon_att*(1-self.defe)

player=character('df')
player.exp+=10000000
player.show_exp()
player.show_status()
player.ap_use()
player.show_status()