class Superhero:
    def __init__(self, name,gender,power):
        self._name=name
        self.gender = gender
        self.power = power
        
    def get_name(self):
      return self._name #encapsulated 
  
    def show_power(self):
        return f"{self._name} has the power of {self.power}"    

class Batman(Superhero):
    def __init__(self, gender,power,gadget):
        super().__init__("Batman",gender, power)
        self.gadget = gadget
        
    def show_power(self):
        return f"{self.get_name()} fights crime using {self.gadget} and is {self.power}!"
    
hero= Batman("Male","Rich","High-tech gadgets")
print(hero.show_power()) 


#Polymorphisim
class Duck:
    def speak(self):
        return "Quack"

class Cow:
    def speak(self):
        return "Mooo!"

# Polymorphism in action
for animal in [Duck(), Cow()]:
    print(animal.speak())






