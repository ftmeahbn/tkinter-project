class Person:
    def __init__(self, name, family, ability, code=0):
        self.name = name
        self.family = family
        self.ability = ability
        self.code = code


    def name(self):
        return self.__name

  
    def name(self, name):
        self.__name = name


    def family(self):
        return self.__family


    def family(self, family):
        self.__family = family

    def ability(self):
        return self.__ability


    def ability(self, ability):
        self.__ability = ability



    def __str__(self):
        return f'{self.code} - {self.name} {self.family}{self.ability}'




















    
