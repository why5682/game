import random

class character:
    def __init__(self,name):
        self.name=name
        self.exp=0
        self.stat_str=10
        self.stat_dex=10
        self.stat_int=10
        self.stat_luk=10
        self.level=1
        self.att=self.stat_str*1+self.stat_dex*0.5
        self.mana=self.stat_int*0.5
        self.acc=self.stat_dex*1+self.stat_luk*0.5
        