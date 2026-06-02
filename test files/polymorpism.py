class Plane:
    def takeoff(self):
        print("Plane is taking off")
    def fly(self):
        print('Plane is flying')
    def land(self):
        print('plane is landing')

class Passenger(Plane):
    def carry(self):
        print('Carrying passender')
class Cargo(Plane):
    def carry(self):
        print('carrying goods')
class Fighter(Plane):
    def carry(self):
        print('Carrying missiles')

# p=Passenger()
# p.takeoff()
# p.fly()
# p.land()
# p.carry()
# print('\n\n\n')
# c=Cargo()
# c.takeoff()
# c.fly()
# c.land()
# c.carry()
# print('\n\n\n')
# f=Fighter()
# f.takeoff()
# f.fly()
# f.land()
# f.carry()

def allowPlane(ref):
    ref.takeoff()
    ref.fly()
    ref.land()
    ref.carry()

allowPlane(Passenger())
allowPlane(Cargo())
allowPlane(Fighter())