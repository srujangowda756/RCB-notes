class Test:
    def __init__(self,id):
        self.id=id
        print("creted a object with id",self.id)
    def __del__(self):
        print(self.id," is deleted")

a=Test(23)
b=Test(24)
del b 
c=Test(25)