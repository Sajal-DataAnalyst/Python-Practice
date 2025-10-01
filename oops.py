# class College:
#     a="Dog"

#     def hello(self):
#         print('Hi now i am learning oops')   
# obj=College()
# print(obj.hello())

# class Factory:
#     def __init__(self,bag,zip,pocket):
#         self.bag=bag
#         self.zip=zip
#         self.pocket=pocket

# reebok = Factory("nike",3,4)
# print(reebok.bag)







# class Animal:
#     species="lion"

#     def __init__(self,age):
#         self.age=age
#     def describe(self):
#         print(f'Your age is {self.age} ')

#     @classmethod
#     def hello(cls):
#         print(f'Hello. species is {cls.species}')



#     @staticmethod
#     def static():
#         print('How are you?')     

# obj=Animal(12)
# obj.static()
# obj.describe()

# class Animal:
#     def __init__(self,name):
#         self.name=name #instance attribute

#     def show(self):


# class Factory:
#     def __init__(self,material,zip):
#         self.material=material
#         self.zip=zip 

# class BhopalFactory(Factory):
#     def __init__(self, material, zip,color):
#         super().__init__(material, zip)  
#         self.color=color

# class PuneFactory(BhopalFactory):
#     def __init__(self, material, zip, color,pocket):
#         super().__init__(material, zip, color)
#         self.pocket=pocket
# obj=PuneFactory()        


# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def __str__(self):
#         return f"hello how are you and your name is {self.name}" 
      
# obj=Animal("LIon")
# print(obj)



# def decorate(func)
# @decorate
# def hello():
#     return "hi i am sajal complted oops learning decorators now"
# print(hello())

# def addition(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     print(sum)

# addition(12,12,13,45) 

# l={i:i**2 for i in range(1,10)}
# print(l)   

# addition=lambda a: "even" if a%2==0 else "odd"
# print(addition(15))  

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self): pass

class Car(Vehicle):
    def start(self): print("Car started")

c = Car()
c.start()


