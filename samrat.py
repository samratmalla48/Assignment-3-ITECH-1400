MAX_WEIGHT_CAP = 10000
MAX_BASKET_WEIGHT = 25000
MIN_EATING_WEIGHT = 501
FISH_TYPES = ['AustralianBass','ShortFinnedEel','EelTailedCatfish','GippslandPerch']

class AustralianBass:
    Max_Weight = 4000
    Max_Eating_Weight = 2500
    NAME = 'Australian Bass'
    LATIN_NAME = 'Macquaria Novemaculeata'
    def __init__(self,weight):
        if weight not in range(self.Max_Weight + 1):
            raise ValueError(f'weight must be between 0 and {self.Max_Weight}')
        self.weight = weight
    #getter
    def get_weight(self):
            return self.weight
    # setter
    def set_weight(self,weight):
            if weight not in range({self.MAX_Weight+1}):
                raise ValueError(f'weight must be between 0 and {self.Max_Eating_Weight}')
            self.weight= weight
    def is_good_eating(self):
        return self.weight in range(MIN_EATING_WEIGHT,self.Max_Eating_Weight)
    def __str__(self):
        return f"{self.NAME}({self.LATIN_NAME}),weights {self.weight/1000} KG."
    # Another Class
class ShortFinnedEel:
    Max_Weight = 3000
    Max_Eating_Weight = 3000
    NAME = 'Short Finned Eel'
    LATIN_NAME = '(Anguilla Australis'
    def __init__(self,weight):
        if weight not in range(self.Max_Weight + 1):
            raise ValueError(f'weight must be between 0 and {self.Max_Weight}')
        self.weight = weight
    #getter
    def get_weight(self):
            return self.weight
    # setter
    def set_weight(self,weight):
            if weight not in range({self.MAX_Weight+1}):
                raise ValueError(f'weight must be between 0 and {self.Max_Eating_Weight}')
            self.weight= weight
    def is_good_eating(self):
        return self.weight in range(MIN_EATING_WEIGHT,self.Max_Eating_Weight)
    def __str__(self):
        return f"{self.NAME}({self.LATIN_NAME}),weights {self.weight/1000} KG."

class EelTailedCatfish:
    Max_Weight = 6800
    Max_Eating_Weight = 4000
    NAME = 'Eel Tailed Catfish '
    LATIN_NAME = 'Tandanus Tandanus'
    def __init__(self,weight):
        if weight not in range(self.Max_Weight + 1):
            raise ValueError(f'weight must be between 0 and {self.Max_Weight}')
        self.weight = weight
    #getter
    def get_weight(self):
            return self.weight
    # setter
    def set_weight(self,weight):
            if weight not in range({self.MAX_Weight+1}):
                raise ValueError(f'weight must be between 0 and {self.Max_Eating_Weight}')
            self.weight= weight
    def is_good_eating(self):
        return self.weight in range(MIN_EATING_WEIGHT,self.Max_Eating_Weight)
    def __str__(self):
        return f"{self.NAME}({self.LATIN_NAME}),weights {self.weight/1000} KG."
class GippslandPerch :
    Max_Weight = 10000
    Max_Eating_Weight = 6000
    NAME = 'Gippsland Perch'
    LATIN_NAME = 'Macquaria Colonorum'
    def __init__(self,weight):
        if weight not in range(self.Max_Weight + 1):
            raise ValueError(f'weight must be between 0 and {self.Max_Weight}')
        self.weight = weight
    #getter
    def get_weight(self):
            return self.weight
    # setter
    def set_weight(self,weight):
            if weight not in range({self.MAX_Weight+1}):
                raise ValueError(f'weight must be between 0 and {self.Max_Eating_Weight}')
            self.weight= weight
    def is_good_eating(self):
        return self.weight in range(MIN_EATING_WEIGHT,self.Max_Eating_Weight)
    def __str__(self):
        return f"{self.NAME}({self.LATIN_NAME}),weights {self.weight/1000} KG."
#  creating rest two classes
class GippslandPerch :
    Max_Weight = 10000
    Max_Eating_Weight = 6000
    NAME = 'Gippsland Perch'
    LATIN_NAME = 'Macquaria Colonorum'
    def __init__(self,weight):
        if weight not in range(self.Max_Weight + 1):
            raise ValueError(f'weight must be between 0 and {self.Max_Weight}')
        self.weight = weight
    #getter
    def get_weight(self):
            return self.weight
    # setter
    def set_weight(self,weight):
            if weight not in range({self.MAX_Weight+1}):
                raise ValueError(f'weight must be between 0 and {self.Max_Eating_Weight}')
            self.weight= weight
    def is_good_eating(self):
        return self.weight in range(MIN_EATING_WEIGHT,self.Max_Eating_Weight)
    def __str__(self):
        return f"{self.NAME}({self.LATIN_NAME}),weights {self.weight/1000} KG."
    class GippslandPerch :
        Max_Weight = 10000
    Max_Eating_Weight = 6000
    NAME = 'Gippsland Perch'
    LATIN_NAME = 'Macquaria Colonorum'
    def __init__(self,weight):
        if weight not in range(self.Max_Weight + 1):
            raise ValueError(f'weight must be between 0 and {self.Max_Weight}')
        self.weight = weight
    #getter
    def get_weight(self):
            return self.weight
    # setter
    def set_weight(self,weight):
            if weight not in range({self.MAX_Weight+1}):
                raise ValueError(f'weight must be between 0 and {self.Max_Eating_Weight}')
            self.weight= weight
    def is_good_eating(self):
        return self.weight in range(MIN_EATING_WEIGHT,self.Max_Eating_Weight)
    def __str__(self):
        return f"{self.NAME}({self.LATIN_NAME}),weights {self.weight/1000} KG."
    #this comment is for experimental purpose only and this will be for few more minutes
