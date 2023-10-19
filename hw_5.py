class Animal: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
         
    def get_info(self): 
        return f"{self.name} {self.age}" 

class Dog(Animal): 
    def __init__(self, name, age, breed): 
        super().__init__(name, age) 
        self.breed = breed 
             
    def get_breed(self): 
        return self.breed 
         
dog = Dog("Бакс", 2, "Австралийская овчарка") 
print("Имя : ", dog.get_info()) 
print("Возраст: ", dog.age) 
print("Порода: ", dog.get_breed()) 

class Cat(Animal): 
    def __init__(self, name, age, color): 
        super().__init__(name, age) 
        self.color = color 
             
    def get_color(self): 
        return self.color 
         
cat = Cat("Мурка", 3, "коричневый") 
print("Имя: ", cat.get_info()) 
print("Возраст: ", cat.age) 
print("Окрас кота:", cat.get_color())