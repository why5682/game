class event:
    def __init__(self,name):
        self.name=name
        
class cha:
    def __init__(self,name):
        self.name=name
    
class card:
    def __init__(self,name,type,value):
        self.name=name
        self.type=type
        self.value=value

class weapon:
    def __init__(self,name,type,value,upgrade):
        self.name=name
        self.type=type
        self.value=value
        self.upgrade=upgrade

good_pencil=weapon()