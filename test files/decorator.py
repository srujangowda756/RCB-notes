
#decorator
def execute1(func):
    func()
    
@execute1
def greet():
    print("nice to meet you")

#closure
def outer():
    print('outer')
    def inner():
        print('inner')
    return inner
x=outer()
x()
x()
x()     