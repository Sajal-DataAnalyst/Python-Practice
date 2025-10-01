# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def show(self):
#         print(f"Animal name : {self.name}, Age: {self.age}")

# lion=Animal("Lion",24)
# lion.show()


# class Animal:
#     def sound(self):
#         print("Some generic sound")

# class Dog(Animal):
#     def sound(self):
#         print("Bark")

# dog=Dog()
# dog.sound()


# class Cat:
#     def sound(self):print("Meow")

# class Dog:
#     def sound(self):print('Bark')

# animals=[Cat(),Dog()]
# for a in animals:
#     a.sound()   


class Account:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        self.__balance+=amount

    def get_balance(self):
        return self.__balance 

acc=Account(1000)
acc.deposit(500)    
print(acc.get_balance()) 
