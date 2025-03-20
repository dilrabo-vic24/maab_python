class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age  
        self.weight = weight 
        self.energy = 100
        self.hunger = 0
    
    def eat(self, food_amount):
        """Animal eats to reduce hunger and gain weight"""
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - food_amount * 10)
            self.weight += food_amount * 0.1
            return f"{self.name} eats and reduces hunger to {self.hunger}%"
        return f"{self.name} is not hungry"
    
    def sleep(self, hours):
        """Animal sleeps to regain energy"""
        self.energy = min(100, self.energy + hours * 10)
        self.hunger += hours * 5
        return f"{self.name} sleeps for {hours} hours and now has {self.energy}% energy"
    
    def move(self, distance):
        # """Generic movement method that uses energy and increases hunger"""
        if self.energy >= distance:
            self.energy -= distance
            self.hunger += distance * 2
            return f"{self.name} moves {distance} units"
        return f"{self.name} is too tired to move"
    
    def make_sound(self):
        # """Generic animal sound method to be overridden by child classes"""
        return f"{self.name} makes a sound"
    
    def __str__(self):
        return f"{self.__class__.__name__} named {self.name}, age: {self.age}, weight: {self.weight:.1f}kg"


class Chicken(Animal):
    def __init__(self, name, age, weight, egg_production=1):
        super().__init__(name, age, weight)
        self.egg_production = egg_production
        self.eggs_collected = 0
    
    def lay_eggs(self):
        # """Chicken lays eggs based on production rate"""
        if self.energy > 20 and self.hunger < 50:
            laid_eggs = self.egg_production
            self.eggs_collected += laid_eggs
            self.energy -= 20
            self.hunger += 15
            return f"{self.name} laid {laid_eggs} eggs (total: {self.eggs_collected})"
        return f"{self.name} is too tired or hungry to lay eggs"
    
    def move(self, distance):
        """Chickens scratch and peck as they move"""
        result = super().move(distance * 0.5)
        return f"{result} while scratching and pecking"
    
    def make_sound(self):
        return f"{self.name} clucks!"


class Cow(Animal):
    def __init__(self, name, age, weight, milk_production=10):
        super().__init__(name, age, weight)
        self.milk_production = milk_production
        self.milk_available = 0
    
    def produce_milk(self):
        """Cow produces milk based on production rate"""
        if self.energy > 30 and self.hunger < 60:
            milk_produced = self.milk_production
            self.milk_available += milk_produced
            self.energy -= 25
            self.hunger += 20
            return f"{self.name} produced {milk_produced} liters of milk (available: {self.milk_available}L)"
        return f"{self.name} is too tired or hungry to produce milk"
    
    def graze(self, hours):
        """Cows eat grass directly from the field"""
        food_amount = hours * 2
        self.hunger = max(0, self.hunger - food_amount * 8)
        self.energy += hours * 5
        return f"{self.name} grazes for {hours} hours, reducing hunger to {self.hunger}%"
    
    def make_sound(self):
        return f"{self.name} moos loudly!"


class Dog(Animal):
    def __init__(self, name, age, weight, sniffing_skill=5):
        super().__init__(name, age, weight)
        self.sniffing_skill = sniffing_skill
        self.items_found = []
    
    def sniff_out(self, hours):
        # """Dogs can find items while sniffing around"""
        possible_finds = ["bone", "stick", "ball", "shoe", "wallet"]
        import random
        
        finds = min(int(hours * self.sniffing_skill / 3), 5)
        if self.energy > 30:
            new_finds = random.sample(possible_finds, min(finds, len(possible_finds)))
            self.items_found.extend(new_finds)
            self.energy -= hours * 10
            self.hunger += hours * 15
            return f"{self.name} found: {', '.join(new_finds)}"
        return f"{self.name} is too tired to sniff around"
    
    def wag_tail(self):
        """Dogs wag their tail when happy"""
        self.energy -= 5
        return f"{self.name} wags its tail excitedly!"
    
    def make_sound(self):
        return f"{self.name} barks happily!"



molly = Cow("Molly", 4, 600, milk_production=15)
chip_chip = Chicken("Chip_chip", 2, 1.5, egg_production=2)
betxoven = Dog("Betxoven", 3, 250, sniffing_skill=7)
    
print("=== FARM ANIMALS ===")
print(molly)
print(chip_chip)
print(betxoven)
print("\n=== ANIMAL SOUNDS ===")
print(molly.make_sound())
print(chip_chip.make_sound())
print(betxoven.make_sound())
    
print("\n=== COW ACTIVITIES ===")
print(molly.graze(3))
print(molly.produce_milk())
print(molly.sleep(5))
    
print("\n=== CHICKEN ACTIVITIES ===")
print(chip_chip.eat(2))
print(chip_chip.lay_eggs())
print(chip_chip.move(3))
    
print("\n=== Dog ACTIVITIES ===")
print(betxoven.sniff_out(2))
print(betxoven.wag_tail()) 
print(betxoven.eat(4))  
    
print("\n=== UPDATED ANIMAL STATUS ===")
print(f"Molly: Energy {molly.energy}%, Hunger {molly.hunger}%, Milk {molly.milk_available}L")
print(f"Chip_chip: Energy {chip_chip.energy}%, Hunger {chip_chip.hunger}%, Eggs {chip_chip.eggs_collected}")
print(f"Betxoven: Energy {betxoven.energy}%, Hunger {betxoven.hunger}%, Found {betxoven.items_found}")
