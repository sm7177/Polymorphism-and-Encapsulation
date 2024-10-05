# class Cat():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def intro(self):
#         print(f"My name is {self.name} and age is {self.age}")
    
#     def sound(self):
#         print("The sound it makes is Meow")
        

# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def intro(self):
#         print(f"My name is {self.name} and age is {self.age}")
    
#     def sound(self):
#         print("Dog barks")
        
# Cat1=Cat("Wiskers",7)
# # Cat1.intro()
# # Cat1.sound("Meow")
# Dog1=Dog("Rudolf",10)
# # Dog1.intro()
# # Dog1.sound("Woof")

# for animal in (Cat1,Dog1):
#     animal.intro()
#     animal.sound()



class Computer:
    def __init__(self):
        self.__maxprice=900
    
    def sell(self):
        print("Selling price:",self.__maxprice)
    
    def setMAxPrice(self,price):
        self.__maxprice=price
    
c=Computer()
c.sell()

c.__maxprice=1000
c.sell()

c.setMAxPrice(1000)
c.sell()

