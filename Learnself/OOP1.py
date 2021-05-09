#继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    pass
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    pass
    def run(self):
        print('Cat is running...')

animal=Animal()

dog = Dog()
dog.run()

cat = Cat()
cat.run()

print(isinstance(dog, Animal)) #判断一个变量是否是某个类型可以用isinstance()判断

#多态
def run_twice(animal):
    animal.run()
    animal.run()
print(run_twice(Animal()))
print(run_twice(Dog()))
print(run_twice(Cat()))

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
print( run_twice(Tortoise()))  #不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。
