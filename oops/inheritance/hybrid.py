# 


class Crop:
    def __init__(self, crop_name):
        self.crop_name = crop_name

class Farmer(Crop):
    def __init__(self,far_name, nofields, crop_name):
        super().__init__(crop_name)
        self.far_name = far_name
        self.nofields = nofields
    
    def farm(self):
        print(f'{self.far_name} is farming {self.crop_name} fields in {self.nofields} fields')

class Researcher(Crop):
    def __init__(self, crop_name, prediction):
        super().__init__(crop_name)
        self.prediction = prediction

class Agriconsultent(Farmer, Researcher):
    def __init__(self, far_name, nofields, crop_name, prediction):
        Farmer.__init__(self, far_name, nofields, crop_name)
        Researcher.__init__(self, crop_name, prediction)
    
    def predict(self):
        print(f'total {self.nofields*self.prediction}ton of {self.crop_name} will be produced in this year')

ans=Agriconsultent("John", 10, "Wheat", 5)
ans.farm()
ans.predict()