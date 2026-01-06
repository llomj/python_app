"""
Problem: 501
Create a base class Bird with a method fly(). Create a derived class Penguin that overrides the fly() method to print “Cannot fly”.
"""

class Bird:
    def fly(self):
        return "I can fly!"

class Penguin(Bird):

    def fly(self):
        return "Cannot fly"

generic_bird = Bird()
print(generic_bird.fly())

penguin = Penguin()
print(penguin.fly())

"""
Problem: 502
Create a base class Book with attributes title and author. Create a derived class EBook that adds an attribute file_size.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        
        super().__init__(title, author)
    
        self.file_size = file_size

ebook = EBook("Python Programming", "John Doe", 2.5)
print(f"Title: {ebook.title}, Author: {ebook.author}, File Size: {ebook.file_size}MB")

"""
Problem: 503
Create a base class Instrument with a method play(). Create a derived class Guitar that overrides the play() method to print “Strum”.
"""

class Instrument:
    def play(self):
        return "Playing an instrument."

class Guitar(Instrument):
    def play(self):
        return "Strum"

generic_instrument = Instrument()
print(generic_instrument.play())

guitar = Guitar()
print(guitar.play()) 

"""
Problem: 504
Create a base class Game with a method start(). Create a derived class Chess that overrides the start() method to print “Start Chess”.
"""

class Game:
    def start(self):
        return "Starting the game."

class Chess(Game):

    def start(self):
        return "Start Chess"

generic_game = Game()
print(generic_game.start())

chess_game = Chess()
print(chess_game.start())

"""
Problem: 505
Create a base class Vehicle with a method drive(). Create a derived class Bicycle that overrides the drive() method to print “Pedal”.
"""

class Vehicle:
    def drive(self):
        return "Are you ready to drive?"

class Bicycle(Vehicle):

    def drive(self):
        return "Pedal"

bicycle = Bicycle()
print(bicycle.drive()) 

"""
Problem: 506
Create a base class Computer with attributes brand and processor. Create a derived class Laptop that adds an attribute weight.
"""

class Computer:
    def __init__(self, brand, processor):
        self.brand = brand
        self.processor = processor

class Laptop(Computer):
    def __init__(self, brand, processor, weight):
    
        super().__init__(brand, processor)
        
        self.weight = weight

laptop = Laptop("Dell", "Intel i7", 2.3)
print(f"Brand: {laptop.brand}, Processor: {laptop.processor}, Weight: {laptop.weight}kg")

"""
Problem: 507
Create a base class Device with a method turn_on(). Create a derived class Smartphone that adds an attribute apps.
"""

class Device:
    def turn_on(self):
        return "Device is now on."

class Smartphone(Device):
    def __init__(self, apps):
        self.apps = apps


phone = Smartphone(["WhatsApp", "Instagram", "Spotify"])
print(phone.turn_on()) 
print(f"Installed apps: {', '.join(phone.apps)}")

"""
Problem: 508
Create a base class Parent with a method display(). Create a derived class Child that overrides the display() method to print “This is a child”.
"""

class Parent:
    def display(self):
        return "This is the parent."

class Child(Parent):
    def display(self):
        return "This is a child"
        
parent = Parent()
print(parent.display()) 

child = Child()
print(child.display())  

"""
Problem: 509
Create a base class Building with attributes floors and address. Create a derived class Skyscraper that adds an attribute height.
"""

class Building:
    def __init__(self, floors, address):
        self.floors = floors
        self.address = address

class Skyscraper(Building):
    def __init__(self, floors, address, height):
        # Call the base class (Building) constructor to initialize floors and address
        super().__init__(floors, address)
        # Initialize the height attribute specific to Skyscraper
        self.height = height

skyscraper = Skyscraper(50, "123 High Street", 200)
print(f"Floors: {skyscraper.floors}, Address: {skyscraper.address}, Height: {skyscraper.height} meters")

"""
Problem: 510
Create a base class Plant with a method grow(). Create a derived class Flower that overrides the grow() method to print “Bloom”.
"""

class Plant:
    def grow(self):
        return "The plant is growing."

class Flower(Plant):
    
    def grow(self):
        return "Bloom"

plant = Plant()
print(plant.grow())  # Output: The plant is growing.

flower = Flower()
print(flower.grow())  # Output: Bloom

"""
Problem: 511
Create a base class Teacher with attributes name and subject. Create a derived class MathTeacher that adds a method teach_math().
"""

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def __str__(self):
        return f"Name: {self.name}, Subject: {self.subject}"


class MathTeacher(Teacher):
    def __init__(self, name):
    
        super().__init__(name, "Math")

    def teach_math(self):
        return "Teaching math concepts."

# Example usage
teacher = Teacher("John Doe", "Science")
print(teacher)  # Output: Name: John Doe, Subject: Science

math_teacher = MathTeacher("Alice Smith")
print(math_teacher)         # Output: Name: Alice Smith, Subject: Math
print(math_teacher.teach_math())  # Output: Teaching math concepts.

"""
Problem: 512
Create a base class Writer with attributes name and genre. Create a derived class Poet that overrides the genre attribute to “Poetry”.
"""

class Writer:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def __str__(self):
        return f"Name: {self.name}, Genre: {self.genre}"

class Poet(Writer):
    def __init__(self, name):
        
        super().__init__(name, "Poetry")

# Example usage
writer = Writer("Jane Austen", "Fiction")
print(writer)  # Output: Name: Jane Austen, Genre: Fiction

poet = Poet("William Wordsworth")
print(poet)  # Output: Name: William Wordsworth, Genre: Poetry

"""
Problem: 513
Create a base class Appliance with a method use(). Create a derived class Oven that overrides the use() method to print “Bake”
"""

class Appliance:
    def use(self):
        return "Using the appliance."

# Derived class Oven that inherits from Appliance
class Oven(Appliance):
    def use(self):
        return "Bake"

appliance = Appliance()
print(appliance.use())

oven = Oven()
print(oven.use()) 

"""
Problem: 514
Create a base class Artist with attributes name and medium. Create a derived class Painter that adds a method paint().
"""

# Base class Artist
class Artist:
    def __init__(self, name, medium):
        self.name = name
        self.medium = medium

    def __str__(self):
        return f"Name: {self.name}, Medium: {self.medium}"

# Derived class Painter that inherits from Artist
class Painter(Artist):
    def paint(self):
        return "Painting with " + self.medium

# Example usage
artist = Artist("Claude Monet", "Watercolor")
print(artist)  # Output: Name: Claude Monet, Medium: Watercolor

painter = Painter("Vincent van Gogh", "Oil Paint")
print(painter)         # Output: Name: Vincent van Gogh, Medium: Oil Paint
print(painter.paint()) # Output: Painting with Oil Paint

"""
Problem: 515
Create a base class Worker with a method work(). Create a derived class Electrician that overrides the work() method to print “Fix wires”.
"""

# Base class Worker
class Worker:
    def work(self):
        return "Working on general tasks."

# Derived class Electrician that inherits from Worker
class Electrician(Worker):
    def work(self):
        return "Fix wires"

# Example usage
worker = Worker()
print(worker.work())  # Output: Working on general tasks.

electrician = Electrician()
print(electrician.work())  # Output: Fix wires

"""
Problem: 516
Create a base class Animal with a method eat(). Create a derived class Lion that overrides the eat() method to print “Eat meat”.
"""

# Base class Animal
class Animal:
    def eat(self):
        return "Eating food."

# Derived class Lion that inherits from Animal
class Lion(Animal):
    def eat(self):
        return "Eat meat"

# Example usage
animal = Animal()
print(animal.eat())  # Output: Eating food.

lion = Lion()
print(lion.eat())  # Output: Eat meat

"""
Problem: 517
Create a base class Appliance with a method run(). Create a derived class Fan that overrides the run() method to print “Spin blades”
"""

# Base class Appliance
class Appliance:
    def run(self):
        return "Running appliance."

# Derived class Fan that inherits from Appliance
class Fan(Appliance):
    def run(self):
        return "Spin blades"

# Example usage
appliance = Appliance()
print(appliance.run())  # Output: Running appliance.

fan = Fan()
print(fan.run())  # Output: Spin blades

"""
Problem: 518
Create a base class Employee with a method get_salary(). Create a derived class Intern that overrides the get_salary() method to return a lower salary.
"""

# Base class Employee
class Employee:
    def get_salary(self):
        return 5000  # Example salary for a general employee

# Derived class Intern that inherits from Employee
class Intern(Employee):
    def get_salary(self):
        return 2000  # Example lower salary for an intern

# Example usage
employee = Employee()
print(f"Employee Salary: ${employee.get_salary()}")  # Output: Employee Salary: $5000

intern = Intern()
print(f"Intern Salary: ${intern.get_salary()}")  # Output: Intern Salary: $2000

"""
Problem: 519
Create a base class Vehicle with an attribute wheels. Create a derived class Motorcycle that overrides wheels to 2.
"""

# Base class Vehicle
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

    def __str__(self):
        return f"Wheels: {self.wheels}"

# Derived class Motorcycle that inherits from Vehicle
class Motorcycle(Vehicle):
    def __init__(self):
        # Initialize the base class (Vehicle) with wheels set to 2
        super().__init__(2)

# Example usage
vehicle = Vehicle(4)  # Example with a generic vehicle
print(vehicle)  # Output: Wheels: 4

motorcycle = Motorcycle()
print(motorcycle)  # Output: Wheels: 2

"""
Problem: 520
Create a base class Tool with a method use(). Create a derived class Hammer that overrides the use() method to print “Hammer nails”.
"""

# Base class Tool
class Tool:
    def use(self):
        return "Using the tool."

# Derived class Hammer that inherits from Tool
class Hammer(Tool):
    def use(self):
        return "Hammer nails"

# Example usage
tool = Tool()
print(tool.use())  # Output: Using the tool.

hammer = Hammer()
print(hammer.use())  # Output: Hammer nails

"""
Problem: 521
Create a base class BankAccount with attributes balance and owner. Create a derived class SavingsAccount that adds an attribute interest_rate.
"""

# Base class BankAccount
class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def __str__(self):
        return f"Owner: {self.owner}, Balance: ${self.balance}"

# Derived class SavingsAccount that inherits from BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, balance, owner, interest_rate):
        # Initialize base class (BankAccount) with balance and owner
        super().__init__(balance, owner)
        self.interest_rate = interest_rate

    def __str__(self):
        return f"Owner: {self.owner}, Balance: ${self.balance}, Interest Rate: {self.interest_rate}%"

# Example usage
account = BankAccount(1000, "Alice")
print(account)  # Output: Owner: Alice, Balance: $1000

savings = SavingsAccount(1500, "Bob", 2.5)
print(savings)  # Output: Owner: Bob, Balance: $1500, Interest Rate: 2.5%

"""
Problem: 522
Create a base class Weapon with a method attack(). Create a derived class Sword that overrides the attack() method to print “Slash”.
"""

# Base class Weapon
class Weapon:
    def attack(self):
        return "Weapon attack"

# Derived class Sword that inherits from Weapon
class Sword(Weapon):
    def attack(self):
        return "Slash"

# Example usage
weapon = Weapon()
print(weapon.attack())  # Output: Weapon attack

sword = Sword()
print(sword.attack())  # Output: Slash

"""
Problem: 523
Create a base class Appliance with an attribute power. Create a derived class Microwave that adds a method heat_food().
"""

# Base class Appliance
class Appliance:
    def __init__(self, power):
        self.power = power

    def __str__(self):
        return f"Power: {self.power} watts"

# Derived class Microwave that inherits from Appliance
class Microwave(Appliance):
    def __init__(self, power):
        # Initialize the base class (Appliance) with power
        super().__init__(power)

    def heat_food(self):
        return "Heating food"

# Example usage
appliance = Appliance(1500)  # Example with an appliance
print(appliance)  # Output: Power: 1500 watts

microwave = Microwave(1200)
print(microwave)  # Output: Power: 1200 watts
print(microwave.heat_food())  # Output: Heating food

"""
Problem: 524
Create a base class Vehicle with a method start(). Create a derived class ElectricCar that overrides the start() method to print “Silent start”.
"""

# Base class Vehicle
class Vehicle:
    def start(self):
        return "Starting vehicle"

# Derived class ElectricCar that inherits from Vehicle
class ElectricCar(Vehicle):
    def start(self):
        return "Silent start"

# Example usage
vehicle = Vehicle()
print(vehicle.start())  # Output: Starting vehicle

electric_car = ElectricCar()
print(electric_car.start())  # Output: Silent start

"""
Problem: 525
Create a base class Pet with a method make_sound(). Create a derived class Cat that overrides the make_sound() method to print “Meow”.
"""

# Base class Pet
class Pet:
    def make_sound(self):
        return "Some generic pet sound"

# Derived class Cat that inherits from Pet
class Cat(Pet):
    def make_sound(self):
        return "Meow"

# Example usage
pet = Pet()
print(pet.make_sound())  # Output: Some generic pet sound

cat = Cat()
print(cat.make_sound())  # Output: Meow

"""
Problem: 526
Create a base class Chef with a method cook(). Create a derived class PastryChef that overrides the cook() method to print “Bake cake”.
"""

# Base class Chef
class Chef:
    def cook(self):
        return "Cook food"

# Derived class PastryChef that inherits from Chef
class PastryChef(Chef):
    def cook(self):
        return "Bake cake"

# Example usage
chef = Chef()
print(chef.cook())  # Output: Cook food

pastry_chef = PastryChef()
print(pastry_chef.cook())  # Output: Bake cake

"""
Problem: 527
Create a base class Furniture with attributes material and color. Create a derived class Chair that adds an attribute legs.
"""

def create_chair(material, color, legs):
    class Furniture:
        def __init__(self, material, color):
            self.material = material
            self.color = color

    class Chair(Furniture):
        def __init__(self, material, color, legs):
            super().__init__(material, color)
            self.legs = legs

    return Chair(material, color, legs)

my_chair = create_chair("wood", "brown", 4)

"""
Problem: 528
Create a base class Game with an attribute players. Create a derived class Soccer that overrides the players attribute to 22.
"""

# Base class Game
class Game:
    def __init__(self, players):
        self.players = players

    def __str__(self):
        return f"Players: {self.players}"

# Derived class Soccer that inherits from Game
class Soccer(Game):
    def __init__(self):
        # Initialize the base class with the specific number of players for Soccer
        super().__init__(players=22)

# Example usage
game = Game(10)
print(game)  # Output: Players: 10

soccer = Soccer()
print(soccer)  # Output: Players: 22

"""
Problem: 529
Create a base class Musician with a method play_instrument(). Create a derived class Pianist that overrides the play_instrument() method to print “Play piano”.
"""

# Base class Musician
class Musician:
    def play_instrument(self):
        return "Play instrument"

# Derived class Pianist that inherits from Musician
class Pianist(Musician):
    def play_instrument(self):
        return "Play piano"

# Example usage
musician = Musician()
print(musician.play_instrument())  # Output: Play instrument

pianist = Pianist()
print(pianist.play_instrument())  # Output: Play piano

"""
Problem: 530
Create a base class Company with attributes name and location. Create a derived class TechCompany that adds an attribute products.
"""

# Base class Company
class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"Name: {self.name}, Location: {self.location}"

# Derived class TechCompany that inherits from Company
class TechCompany(Company):
    def __init__(self, name, location, products):
        # Initialize the base class (Company) with name and location
        super().__init__(name, location)
        self.products = products

    def __str__(self):
        # Extend the base class string representation to include products
        return f"Name: {self.name}, Location: {self.location}, Products: {', '.join(self.products)}"

# Example usage
company = Company("Global Corp", "New York")
print(company)  # Output: Name: Global Corp, Location: New York

tech_company = TechCompany("Tech Innovators", "San Francisco", ["Smartphone", "Laptop", "Tablet"])
print(tech_company)  # Output: Name: Tech Innovators, Location: San Francisco, Products: Smartphone, Laptop, Tablet

"""
Problem: 531
Create a base class Gadget with a method operate(). Create a derived class Smartwatch that adds an attribute heart_rate_monitor.
"""
# Base class Gadget
class Gadget:
    def operate(self):
        return "Operate gadget"

# Derived class Smartwatch that inherits from Gadget
class Smartwatch(Gadget):
    def __init__(self, heart_rate_monitor):
        # Initialize the base class (Gadget)
        super().__init__()
        self.heart_rate_monitor = heart_rate_monitor

    def __str__(self):
        # Provide a string representation of the Smartwatch
        return f"Heart Rate Monitor: {'Enabled' if self.heart_rate_monitor else 'Disabled'}"

# Example usage
gadget = Gadget()
print(gadget.operate())  # Output: Operate gadget

smartwatch = Smartwatch(heart_rate_monitor=True)
print(smartwatch.operate())  # Output: Operate gadget
print(smartwatch)           # Output: Heart Rate Monitor: Enabled

"""
Problem: 532
Create a base class Trainer with a method train(). Create a derived class FitnessTrainer that overrides the train() method to print “Train body”.
"""

# Base class Trainer
class Trainer:
    def train(self):
        return "Training session"

# Derived class FitnessTrainer that inherits from Trainer
class FitnessTrainer(Trainer):
    def train(self):
        print("Train body")

# Example usage
trainer = Trainer()
print(trainer.train())  # Output: Training session

fitness_trainer = FitnessTrainer()
fitness_trainer.train()  # Output: Train body

"""
Problem: 533
Create a base class Book with a method read(). Create a derived class ComicBook that overrides the read() method to print “Read with pictures”.
"""

# Base class Book
class Book:
    def read(self):
        return "Read the book"

# Derived class ComicBook that inherits from Book
class ComicBook(Book):
    def read(self):
        print("Read with pictures")

# Example usage
book = Book()
print(book.read())  # Output: Read the book

comic_book = ComicBook()
comic_book.read()  # Output: Read with pictures

"""
Problem: 534
Create a base class Software with attributes name and version. Create a derived class GameSoftware that adds an attribute genre.
"""

# Base class Software
class Software:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __str__(self):
        return f"Name: {self.name}, Version: {self.version}"

# Derived class GameSoftware that inherits from Software
class GameSoftware(Software):
    def __init__(self, name, version, genre):
        # Initialize the base class (Software) with name and version
        super().__init__(name, version)
        self.genre = genre

    def __str__(self):
        # Extend the base class string representation to include genre
        return f"Name: {self.name}, Version: {self.version}, Genre: {self.genre}"

# Example usage
software = Software("BasicApp", "1.0")
print(software)  # Output: Name: BasicApp, Version: 1.0

game_software = GameSoftware("EpicQuest", "2.5", "RPG")
print(game_software)  # Output: Name: EpicQuest, Version: 2.5, Genre: RPG

"""
Problem: 535
Write a Python program to count the number of times the letter ‘a’ appears in a string. Use count().
"""

def count_letter(s):
    return s.count("a")
    
string = "what going on today"
print(count_letter(string))

"""
Problem: 536
Write a Python function to count the occurrences of the number 5 in a list of integers. Use count().
"""

def count_number(num):
    return num.count(5)

number = [3, 5, 5, 35, 78]
print(count_number(number))

"""
Problem: 537
Write a Python program to count how many times the word “hello” appears in a sentence. Use count().
"""

def count_hello(string):
    return string.count("hello")
    
string = "hello, you cunt"
print(count_hello(string))

"""
Problem: 538
Write a function that counts how many times the character # appears in a string.  Use count().
"""

def count(string):
    return string.count("#")
    
string = "hello, you cunt ###"
print(count(string))

"""
Problem: 539
Write a Python program to count the occurrences of the substring “cat” in a given string. Use count().
"""

def count_substring(s, substring="cat"):
    return s.count(substring)

input_string = "The cat sat on the mat with another cat."
count = count_substring(input_string)
print(f"The substring 'cat' occurs {count} times.")

"""
Problem: 540
Write a Python function to count how many times the digit 0 appears in a list of numbers. Use count().
"""

def count_number(num):
    return num.count(0)
    
num = [3, 5, 0, 0, 6, 0]
print(count_number(num))

def main(lst):
    total = 0
    for num in lst:
        total += str(num).count('0')
    print(total)

lst = [56700, 40, 0, 0, 570]
main(lst)

"""
Problem: 541
Write a program to count the number of spaces in a given string. Use count().
"""

def count_spaces(string):
    return string.count(" ")
    
num = "i'm going for a walk today"
print(count_spaces(num))

"""
Problem: 542
Write a Python function to count the occurrences of a specific character in a string provided by the user. Use count().
"""

def count_occurrences():
    user_input = input("Type a sentence: ")
    
    char_to_count = input("Enter the character to count: ")
    
    if len(char_to_count) != 1:
        print("Please enter exactly one character.")
        return
    
    count = user_input.count(char_to_count)
    
    print(f"The character '{char_to_count}' occurs {count} times.")

count_occurrences()

"""
Problem: 543
Write a Python program to count how many times a specific word appears in a text file. Use count().
"""

def count_word_in_file(filename, word):
    try:
        # Open the file and read its content
        with open(filename, 'r') as file:
            content = file.read()
        
        # Count the occurrences of the specified word
        word_count = content.count(word)
        
        return word_count
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
        return 0

# Example usage
filename = 'example.txt'  # Replace with your actual file name
word_to_count = 'the'     # Replace with the word you want to count
count = count_word_in_file(filename, word_to_count)
print(f"The word '{word_to_count}' appears {count} times in the file.")

"""
Problem: 544
Write a function to count how many times the letter ‘e’ appears in a list of strings. Use count().
"""

def count_letters(lst):
    total_count = 0
    
    for word in lst:
        total_count += word.count("e")
    return total_count

lst = ["Jonathen", "Nathan", "Netesha"]
print(count_letters(lst))

"""
Problem: 545
Write a Python program to count the number of times a certain element appears in a list of mixed types. Use count().
"""

def count_elements_in_lst(lst, element):
    return lst.count(element)

# Example usage
lst = ["tree", "sea", 42, "world", "sea", 42, 42]
element = 42  # Element to count
print(count_elements_in_lst(lst, element))

"""
Problem: 546
Write a function to count the occurrences of the string “test” in a string where multiple “test” substrings might exist. Use count().
"""

def count_test_occurrences(s):
    return s.count("test")

s = "This is a test. Test the function with another test. Final test."
print(count_test_occurrences(s))

"""
Problem: 547
Write a Python program to count how many times a specific number occurs in a list of floating-point numbers. Use count().
"""

def count_floating_numbers(lst):
    return float(lst.count())
    
lst = [2.3, 5, 6.3, 78, 0.6]
print(count_floating_numbers(lst))

def main(lst):
    result = []
    for num in lst:
        if isinstance(num, float):
            lst.count(num)
            result.append(num)
    return result
    
lst = [2.66, 67, 45556.67, 7888, 1]

main(lst)

"""
Problem: 548
Write a function to count the number of vowels (a, e, i, o, u) in a given string. Use count().
"""

def count_floating_numbers(lst, number):
    return lst.count(number)

lst = [2.3, 5.0, 6.3, 78.0, 0.6, 5.0]
number = 5.0
print(count_floating_numbers(lst, number))

"""
Problem: 549
Write a Python program to count the number of uppercase letters in a string. Use count().
"""

def count_uppercase(string):
    total_uppercase = 0
    
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        total_uppercase += string.count(char)
    return total_uppercase

string = "AFHHJJ ghgghh"
print(count_uppercase(string))

"""
Problem: 550
Write a function that counts the occurrences of a specified digit in a number. Use count().
"""

def count_digit(num):
    num = str(num)
    return num.count("2")

num = 1223452
print(count_digit(num))

"""
Problem: 551
Write a Python program to count how many times each letter appears in a given string. Use count().
"""

def count_letters(string):
    letter_count = {}
    for letter in string.lower():
        letter_count[letter] = string.lower().count(letter)
    return letter_count

string = input("Enter a string: ")
print(count_letters(string))

"""
Problem: 552
Write a function to count the number of times the word “Python” appears in a paragraph of text. Use count().
"""

def count_text(string):
    string = string.lower()
    
    return string.count("python")

string = "python is python in disguise"
print(count_text(string))

"""
Problem: 553
Write a Python program to count the occurrences of a specific item in a list of dictionaries. Use count().
"""

def count_item_in_dict_list(dict_list, item):
    values = []
    
    for d in dict_list:
    
        for val in d.values():
            values.append(val)

    return values.count(item)

dict_list = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Charlie", "age": 35}
]

item = "Alice" 
print(count_item_in_dict_list(dict_list, item))

"""
Problem: 554
Write a function to count how many times the letter ‘z’ appears in a list of strings. Use count().
"""

def count_letters(lst):
    total_count = 0
    for string in lst:
        total_count += string.count("z")
    return total_count

lst = ["z", "h", "z", "gloat"]
print(count_letters(lst))

"""
Problem: 555
Write a Python program to count the occurrences of the character ‘*’ in a given string. Use count().
"""

def count_asterisks(s):
    return s.count('*')

s = "Hello *world* and *everyone*"
print(count_asterisks(s))

"""
Problem: 556
Write a function to count how many times the substring “123” appears in a string. Use count().
"""

def count_substring(s, substring):
    return s.count(substring)

s = "123abc123def123"
substring = "123"
print(count_substring(s, substring))

"""
Problem: 557
Write a Python program to count the number of lines in a text file that contain the word “error”. Use count().
"""

def count_lines_with_word(filename, word):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if line.lower().count(word.lower()) > 0:
                count += 1
    return count

filename = 'example.txt'  # Replace with your actual file path
word = 'error'
print(count_lines_with_word(filename, word))

"""
Problem: 558
Write a function to count the number of times a particular email domain appears in a list of email addresses. Use count().
"""

def count_email_domain(email_list, domain):
    
    count = 0
    for email in email_list:
    
        email_domain = email.split('@')[-1]
        
        if email_domain == domain:
            count += 1
            
    return count

email_list = [
    "user1@example.com",
    "user2@example.com",
    "user3@sample.com",
    "user4@example.com"
]
domain = "example.com"
print(count_email_domain(email_list, domain))

"""
Problem: 559
Write a Python program to count the occurrences of the word “happy” in a given list of sentences. Use count().
"""

def count_word(sentences):
    count = 0
    for sentence in sentences:
        count += sentence.count("happy")
    return count

sentences = ["I am happy today", "She looks very happy", "Happy times are here", "joy joy happy happy"]
print(count_word(sentences))

"""
Problem: 560
Write a function to count the number of times the character ‘!’ appears in a list of strings. Use count().
"""

def count_exclamations(lst):
    count = 0
    for string in lst:
        count += string.count('!')
    return count

lst = ["Hello!", "Wow! Amazing!", "No exclamation here", "Yes!"]
print(count_exclamations(lst))

"""
Problem: 561
Write a Python program to count the number of occurrences of a specific phrase in a block of text. Use count().
"""

def count_phrase_occurrences(text, phrase):
    return text.count(phrase)

text = """The quick brown fox jumps over the lazy dog. The fox is quick and clever.
Quick thinking by the fox saved the day. Foxes are known to be quick and agile."""
phrase = "quick"
print(count_phrase_occurrences(text, phrase))


"""
Problem: 562
Write a function to count the number of occurrences of a word in a list of words. Use count().
"""

def count_word_occurrences(lst, word):
    return lst.count(word)

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_to_count = "apple"
print(count_word_occurrences(words, word_to_count))

"""
Problem: 563
Write a Python program to count how many times the letter ‘x’ appears in a list of mixed data types. Use count().
"""

def count_x_in_mixed_list(lst):
    count = 0
    for item in lst:

        if isinstance(item, str):
            count += item.count('x')
    return count

mixed_list = [1, "xylophone", 3.5, "example", "box", 7, "text", ["x", "x"], "extra"]
print(count_x_in_mixed_list(mixed_list))

"""
Problem: 564
Write a function to count the occurrences of a specific letter in a string and return a formatted message with the result. Use count().
"""

def count_letter_occurrences(string, letter):
    count = string.count(letter)
    
    return f"The letter '{letter}' appears {count} times in the given string."

text = "This is an example sentence with several letters."
letter_to_count = "e"
print(count_letter_occurrences(text, letter_to_count))

"""
Problem: 565
Square List Elements: Write a function that takes a list of numbers and returns a list of their squares using map().
"""

def square_lst(lst):
    return list(map(square, lst))

def square(num):
    return num ** 2

lst = [2, 4, 6, 8]
print(square_lst(lst))

"""
Problem: 566
Filter Odd Numbers: Write a function that takes a list of numbers and returns only the odd numbers using filter().
"""

def filter_odd_numbers(lst):
    return list(filter(is_odd, lst))

def is_odd(x):
    return x % 2 != 0

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(filter_odd_numbers(lst))

"""
Problem: 567
Filter Even Numbers: Write a function that filters all even numbers from a list using filter().
"""

def filters_even_numbers(lst):
    return list(filter(even_num, lst))

def even_num(num):
    if num % 2 != 0:
        return num

lst = [4, 67, 2, 78, 3, 1, 466, 7]
print(filters_even_numbers(lst))

"""
Problem: 568
Convert to Uppercase: Write a function that takes a list of strings and returns the same list with each string converted to uppercase using map().
"""

def convert_to_uppercase(lst):
    return list(map(str.upper, lst))

lst = ["sleep", "walk", "eat"]    
print(convert_to_uppercase(lst))

"""
Problem: 569
Remove Empty Strings: Write a function that filters out empty strings from a list using filter().
"""

def empty_strings(lst):
    return list(filter(call_filter, lst))
    
def call_filter(string):
    return string.strip() != ""
    
lst = ["dog", "  ", "cat"]    
print(empty_strings(lst))

"""
Problem: 570
Multiply List Elements: Write a function that takes a list of numbers and returns a list where each number is multiplied by 5 using map().
"""

def multiply_lst(lst):
    
    def multiply_by_five(x):
        return x * 5
    
    return list(map(multiply_by_five, lst))

lst = [2, 5, 20]
print(multiply_lst(lst))

"""
Problem: 571
String Lengths: Write a function that takes a list of strings and returns their lengths using map().
"""

def lst_of_string(lst):
    
    def len_string(word):
        return len(word)
    return list(map(len_string, lst))
        
lst = ["hot", "cold", "giraffe"]
print(lst_of_string(lst))

"""
Problem: 572
Filter Palindromes: Write a function that filters out palindromes (words that read the same backward) from a list using filter().
"""

def palindromes(lst):
    
    def filter_palindrome(word):
        if word != word[::-1]:
            return word
            
    return list(filter(filter_palindrome, lst))
               
lst = ["radar", "red", "blue", "level", "noon"]
print(palindromes(lst))

"""
Problem: 573
Sum of List: Write a function that calculates the sum of a list of numbers using reduce().
"""

from functools import reduce

def sum_of_lst(lst):
    
    def add(x, y):
        return x + y
        
    return reduce(add, lst)

lst = [1, 2, 3, 4, 5]
print(sum_of_list(lst))

def add(x, y):
    return x + y

def sum_of_list(lst):
    return reduce(add, lst)

lst = [1, 2, 3, 4, 5]
print(sum_of_list(lst))

"""
Problem: 574
Product of List: Write a function that computes the product of a list of numbers using reduce().
"""

from functools import reduce

def sum_of_lst(lst):
    
    def add(x, y):
        return x * y
        
    return reduce(add, lst)

lst = [1, 2, 3, 4, 5]
print(sum_of_list(lst))

def multiply(x, y):
    return x * y

def product_of_list(lst):
    return reduce(multiply, lst)

lst = [1, 2, 3, 4, 5]
print(product_of_list(lst))

"""
Problem: 575
Capitalize Strings: Write a function that takes a list of strings and returns the list with each string capitalized using map().
"""

def capitalize_string(lst):
    return list(map(str.capitalize, lst))
    
lst = ["sam","ion", "kon"]
capitalize_string(lst)

def lst_strings(lst):
    
    def capitalize_lst(word):
        word = word.capitalize()
        return word
        
    return list(map(capitalize_lst, lst))
    
    
lst = ["today", "hello", "sunshine"]
print(lst_strings(lst))  

"""
Problem: 576
Find Minimum: Write a function that finds the minimum number in a list using reduce().
"""

from functools import reduce

def min_number(x, y):
    return x if x < y else y

def number_lst(lst):
    return reduce(min_number, lst)

lst = [34, 67, 1, 778]    
print(number_lst(lst))

"""
Problem: 577
Find Maximum: Write a function that finds the maximum number in a list using reduce(). (hint helper function)
"""

from functools import reduce

def find_max(lst):
    def inner(x, y):
        if x > y:
            return x
        else:
            return y
    
    return reduce(inner, lst)

# Test the function
lst = [567, 4, 1, 57]
print(find_max(lst))  # Output: 567

def main(lst):
    return reduce(max_num, lst)

def max_num(x, y):
    if x > y:
        return x
    return y
    
lst = [567, 4, 100000, 57]
main(lst)

from functools import reduce

def min_number(x, y):
    return x if x > y else y

def number_lst(lst):
    return reduce(min_number, lst)

lst = [34, 67, 1, 778]    
print(number_lst(lst))

"""
Problem: 578
Filter Short Words: Write a function that filters out words shorter than 4 characters from a list using filter().
"""

def list_words(lst):
    
    def filter_word(word):
        if len(word) > 3:
            return word
            
    return list(filter(filter_word, lst))
    
    
lst = ["bot", "not", "boat", "chop"]    
print(list_words(lst))

"""
Problem: 579
Concatenate Strings: Write a function that concatenates all strings in a list using reduce().
"""

from functools import reduce

def lst_strings(lst):
    
    def concatenate_lst(x, y):
        return x + y
        
    return reduce(concatenate_lst, lst)
    

lst = ["to", "day", "is", "great"]    
print(lst_strings(lst)) 

"""
Problem: 580
Filter Positive Numbers: Write a function that filters only positive numbers from a list using filter().
"""

def num_lst(lst):
    
    def filter_num(num):
        if num > 1:
            return num
    return list(filter(filter_num, lst))
    
lst = [-45, 4, 5, -56, 6]    
print(num_lst(lst))

"""
Problem: 581
Cube List Elements: Write a function that returns a list where each element of the input list is cubed using map().
"""

def num_lst(lst):
    
    def cubed_num(num):
        return num ** 3
            
    return list(map(cubed_num, lst))

lst = [-45, 4, 5, -56, 6]    
print(num_lst(lst))

"""
Problem: 582
Sum of Squares: Write a function that returns the sum of squares of a list of numbers using map() and reduce().
"""

from functools import reduce

def lst_numbers(lst):
    
    def square_number(num):
        return num ** 2

    def add(x, y):
        return x + y
    
    squared_lst = map(square_number, lst)
    return reduce(add, squared_lst)

lst = [2, 4, 6, 8]    
print(lst_numbers(lst))

"""
Problem: 583
Combine Names: Write a function that takes two lists (first names, last names) and returns a list of full names using map().
"""

def lst_2(lst1, lst2):
    
    def combine_names(first_last):
        return f"{first_last[0]} {first_last[1]}"
        
    return list(map(combine_names, zip(lst1, lst2)))
    
lst1 = ["Tom", "Bob"]
lst2 = ["Dupond", "lesnake"]    
print(lst_2(lst1, lst2))

"""
Problem: 584
Filter Non-Alphabetic Strings: Write a function that filters out strings that contain non-alphabetic characters using filter().
"""

def non_alphabetical_string(string):
    
    def non_alph(char):
        return char.isalpha()
            
    return ''.join(filter(non_alph, string))
           
string = "whats up dog !?!@$"
print(non_alphabetical_string(string))

"""
Problem: 585
Count Words: Write a function that counts how many times each word appears in a list using reduce(). (hint, result dictionary)
"""

from functools import reduce

def lst_words(lst):
    
    def count_word(counts, word):
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
        return counts
        
    return reduce(count_word, lst, {})

lst = ["Jon", "Chris", "Mike", "Chris", "Chris"]    
print(lst_words(lst))

"""
Problem: 586
Unique Words: Write a function that filters out only unique words from a list using filter() and a helper function.
"""

def unique_words(lst):
    
    def is_unique(word):
        return lst.count(word) == 1
        
    return list(filter(is_unique, lst))

words = ["apple", "banana", "apple", "orange", "kiwi", "banana"]
print(unique_words(words))

"""
Problem: 587
Word Lengths Greater Than N: Write a function that filters words with a length greater than n using filter().
"""

def word_lst(lst):
    
    def filter_word(word):
        if len(word) > n:
            return word
            
    return list(filter(filter_word, lst))
    
lst = ["not", "four", "September", "October"]
n = 4
print(word_lst(lst))

"""
Problem: 588
Apply Multiple Functions: Write a function that applies two different functions to a list, one after another (e.g., first squares the numbers, then filters out even ones).
"""

def apply_lsts(lst):
    
    def square_num(num):
        return num * num
        
    def filter_num(num):
        return num % 2 != 0 
    
    squared_lst = list(map(square_num, lst))
    
    filtered_lst = list(filter(filter_num, squared_lst))
    
    
    return filtered_lst

lst = [2, 4, 2, 3, 5, 22, 3, 8]    
print(apply_lsts(lst))

"""
Problem: 589
Sum of Nested Lists: Write a function that flattens and sums all elements of a nested list using map() and reduce().
"""

from functools import reduce

def sum_nested_list(nested_list):
    """
    This function takes a nested list as input, flattens it, and returns the sum of all elements.
    
    Args:
        nested_list (list): A list that may contain nested lists.
    
    Returns:
        int: The sum of all elements in the nested list.
    """
    # Initialize the sum to 0
    total_sum = 0
    
    # Define a recursive function to flatten the list
    def flatten(lst):
        nonlocal total_sum  # Access the total_sum variable from the outer scope
        for element in lst:
            if isinstance(element, list):
                # If the element is a list, recursively call flatten on it
                flatten(element)
            else:
                # If the element is not a list, add it to the total sum
                total_sum += element
    
    # Call the flatten function on the input list
    flatten(nested_list)
    
    # Return the total sum
    return total_sum

# Example usage:
nested_list = [1, 2, [3, 4, [5, 6]], 7, [8, 9]]
result = sum_nested_list(nested_list)
print(result)  # Output: 45

from functools import reduce

def sum_of_nested(lst):
    
    def flatten(nested_list):
        flat_list = []
        for item in nested_list:
            if isinstance(item, list):
                flat_list.extend(flatten(item))
            else:
                flat_list.append(item)
        return flat_list

    flattened_list = flatten(lst)
    
    return reduce(lambda x, y: x + y, flattened_list)

nested_list = [[1, 2], [3, [4, 5]], [6, [7, [8, 9]]]]
print(sum_of_nested(nested_list))

"""
Problem: 590
First N Fibonacci Numbers: Write a function that generates the first N Fibonacci numbers using reduce().
"""

from functools import reduce

def fibonacci_n_numbers(n):
    
    def fib(acc, _):
        return acc + [acc[-1] + acc[-2]]
        
    return reduce(fib, range(n - 2), [0, 1])[:n]

print(fibonacci_n_numbers(10))

"""
Problem: 591
Count Vowels in Strings: Write a function that counts how many vowels are present in each string of a list using map() and a helper function.
"""

def lst_string(lst):
    
    def count_vowels(word):
        vowels = "aeiou"
        count = 0
        for char in word:
            if char in vowels:
                count += 1
        return count
        
    return list(map(count_vowels, lst))
    
    
lst = ["Jonathan", "mountain", "lion"]    
print(lst_string(lst))

"""
Problem: 592
Sum of Even Numbers: Write a function that computes the sum of all even numbers in a list using filter() and reduce().
"""

from functools import reduce

def sum_even_numbers(lst):
    def is_even(num):
        return num % 2 == 0

    def sum_numbers(x, y):
        return x + y

    even_numbers = filter(is_even, lst)
    return reduce(sum_numbers, even_numbers)

lst = [1, 2, 3, 4, 5, 6]
print(sum_even_numbers(lst))

"""
Problem: 593
Find Longest String: Write a function that finds the longest string in a list using reduce().
"""

from functools import reduce

def lst_string(lst):
    
    def longest_string(x, y):
        if len(x) > len(y):
            return x
        else:
            return y
        
    return reduce(longest_string, lst)
        
lst = ["shop", "mountain", "not"]
print(lst_string(lst))

"""
Problem: 594
Cumulative Sum: Write a function that returns a list of cumulative sums of a given list using reduce().
"""

from functools import reduce

def lst_num(lst):
    
    def cumulative(x, y):
       return x + y
        
    return reduce(cumulative, lst)
        
lst = [2, 2, 2, 2, 2]
print(lst_num(lst))

"""
Problem: 595
Flatten Nested Lists: Write a function that flattens a list of lists into a single list using reduce().
"""

from functools import reduce

def flatten(lst):
    
    def concatenate(x, y):
        return x + y
    return reduce(concatenate, lst)

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened_list = flatten(nested_list)
print(flattened_list)

"""
Problem: 596
Word Frequency Count: Write a function that counts the frequency of each word in a list using reduce().
"""

from functools import reduce

def lst_words(lst):
    
    def count_frequency(result, word):
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
        return result
    
    return reduce(count_frequency, lst, {})

lst = ["word", "sentence", "paragraph", "word", "word"]    
print(lst_words(lst))

"""
Problem: 597
Anagram Filter: Write a function that filters out words that are anagrams of a given word using filter().
"""

def lst_words(lst, target_word):
    
    def anagram_filter(word):
        return sorted(word) != sorted(target_word)

    return list(filter(anagram_filter, lst))

lst = ["listen", "sentence", "stop", "word", "rat", "trail"]
target_word = "listen"
filtered_words = lst_words(lst, target_word)
print(filtered_words)

"""
Problem: 598
Compose Functions: Write a function that takes two functions and composes them (i.e., applies one after another).
"""

def compose(func1, func2):
    
    def composed_function(x):
        return func2(func1(x))
    return composed_function

def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

composed_function = compose(add_one, multiply_by_two)

result = composed_function(5)  # (5 + 1) * 2
print(result)  # Output: 12

"""
Problem: 599
Group By Length: Write a function that groups words by their lengths using reduce().
"""

from functools import reduce

def word_string(string):
    words = string.split()
    
    def sort_len_words(x, y):
        if len(x) == 0:
            return [y]
        if len(y) >= len(x[-1]):
            x.append(y)
            return x
        else:
            x.insert(0, y)
            return x

    return reduce(sort_len_words, words, [])

string = "let's group words by the length"
print(word_string(string))

"""
Problem: 600
Filter Prime Numbers: Write a function that filters prime numbers from a list using filter() and a helper function to check for primality.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(lst):
    return list(filter(is_prime, lst))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
prime_numbers = filter_primes(numbers)
print(prime_numbers)

"""
Problem: 601
Map with Index: Write a function that uses map() but passes the index of each element to the mapping function as well.
"""

def map_with_index(lst, func):
    
    def indexed_func(indexed_item):
        index, item = indexed_item
        return func(index, item)

    return list(map(indexed_func, enumerate(lst)))


def example_func(index, value):
    return index * value

numbers = [10, 20, 30, 40]
result = map_with_index(numbers, example_func)
print(result)

"""
Problem: 602
Intersection of Two Lists: Write a function that finds the intersection of two lists using filter().
"""

def is_in_list(x, list2):
    return x in list2

def intersection(list1, list2):
    
    def check_in_list(x):
        return is_in_list(x, list2)
    
    return list(filter(check_in_list, list1))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = intersection(list1, list2)
print(result)

"""
Problem: 603
Average of List: Write a function that calculates the average of a list of numbers using reduce().
"""

from functools import reduce

def add(x, y):
    return x + y

def average(lst):
    if not lst:
        return 0
    total = reduce(add, lst)
    return total / len(lst)

numbers = [10, 20, 30, 40, 50]
result = average(numbers)
print(result)

"""
Problem: 604
Compose Multiple Functions: Write a function that takes a list of functions and an initial value, and applies the functions sequentially to the value using reduce().
"""

from functools import reduce

def compose_functions(functions, initial_value):
    def apply_functions(x, func):
        return func(x)
    
    return reduce(apply_functions, functions, initial_value)

# Example usage
def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

functions = [add_one, multiply_by_two, add_one]
initial_value = 5
result = compose_functions(functions, initial_value)
print(result)

"""
Problem: 605
Write a program to create a dictionary and retrieve a list of its keys. Use key().
"""

def get_keys(dic):
    return list(dic.keys())

dic = {"Sam": 56, "Chris": 34, "Simon": 12}
print(get_keys(dic)) 

def get_dict_keys():
    my_dict = {
        'apple': 3,
        'banana': 5,
        'cherry': 2,
        'date': 7
    }

    return list(my_dict.keys())

keys_list = get_dict_keys()
print(keys_list)

"""
Problem: 606
Write a function that sorts a list of strings by their length using the key parameter. Use key().
"""

def sort_string_len(lst):
    
    return sorted(lst, key=len)


lst = ["length", "lenny", "len"]    
print(sort_string_len(lst))

"""
Problem: 607
Write a Python program to sort a list of tuples based on the second element of each tuple using key().
"""

def lst_tuples_second(lst):
    
    def sort_tuples(x):
        return x[1]
        
    return sorted(lst, key=sort_tuples)

lst = [("ton", 54), ("tron", 4), ("zicn", 1)]    
print(lst_tuples_second(lst))

"""
Problem: 608
Write a function to sort a list of dictionaries by a specific key in each dictionary using key().
"""

def sort_dicts_by_key(lst, target_key):
    
    def get_key_value(d):
        return d[target_key]
    
    return sorted(lst, key=get_key_value)

dicts = [
    {"id": 5, "name": "zinc"},
    {"id": 3, "name": "metal"},
    {"id": 8, "name": "gold"},
    {"id": 6, "name": "copper"},
    {"id": 3, "name": "ruby"}
]

target_key = "id"
sorted_dicts = sort_dicts_by_key(dicts, target_key)
print(sorted_dicts)

"""
Problem: 609
Write a Python program to sort a list of names by their last name using the key().
""" 

def sort_last_names(names):
    
    def get_last_name(name):
        return name.split()[-1]
    
    return sorted(names, key=get_last_name)

names = ["Tom Simons", "Lisa Johnson", "Mark Twain", "Sarah Connor", "Peter Parker"]
print(sort_last_names(names))

"""
Problem: 610
Write a function that sorts a list of mixed case strings, ignoring case. use key parameter.
"""

def sort_ignore_case(strings):
    
    def case_insensitive_key(s):
        return s.lower()
    
    return sorted(strings, key=case_insensitive_key)

mixed_case_strings = ["banana", "Apple", "orange", "mango", "grape"]
sorted_strings = sort_ignore_case(mixed_case_strings)
print(sorted_strings)

"""
Problem: 611
Write a Python program to sort a list of floats in descending order. Use key().
"""

def list_floats(lst):
    
    def sort(x):
        return x
        
    return sorted(lst, key=sort, reverse=True)


lst = [3.6, 56.5, 78.3, 1.5, 0.006]
print(list_floats(lst))

"""
Problem: 612
Write a function that sorts a list of words by the number of vowels they contain using the key parameter.
"""

def lst_words(lst):
    
    def sort(x):
        vowels = "aeiou"
        
        count = 0
        for char in x.lower():
            if char in vowels:
                count += 1
        return count
        
    return sorted(lst, key=sort)
    
lst = ["jobaeiou", "Jo", "aei"]    
print(lst_words(lst))

"""
Problem: 613
Write a Python program to sort a list of people by their age from a list of dictionaries.
"""

def sort_people_by_age(people):
    
    def get_age(person):
        return person['age']
    
    return sorted(people, key=get_age)

people = [
    {"name": "Jon", "age": 34},
    {"name": "Sam", "age": 23},
    {"name": "Bob", "age": 45}
]
sorted_people = sort_people_by_age(people)
print(sorted_people)

"""
Problem: 614
Write a function that sorts a list of integers based on the sum of their digits using the key parameter.
"""

def lst_integers(lst):
    
    def sort_sum(x):
        total = 0
        for digit in str(x):
            total += int(digit) 
        return total
    
    return sorted(lst, key=sort_sum)

lst = [5666, 566, 56, 6]
sorted_list = lst_integers(lst)
print(sorted_list)

"""
Problem: 615
Write a Python program to sort a list of products by price using the key parameter.
"""

def lst_products(lst):
    
    def sort(product):
        return product['price']

    return sorted(lst, key=sort)

products = [
    {"name": "chocolate", "price": 2.50},
    {"name": "bread", "price": 1.20},
    {"name": "milk", "price": 1.50},
    {"name": "cheese", "price": 3.00}
]
sorted_products = lst_products(products)
print(sorted_products)

"""
Problem: 616
Write a function that sorts a list of dates in string format (e.g., “YYYY-MM-DD”) using the key parameter.
"""

def sort_dates(dates):
    
    def date_key(date_str):
        year, month, day = map(int, date_str.split('-'))
        return (year, month, day) 

    return sorted(dates, key=date_key)

date_list = [
    "2022-01-15",
    "2021-12-25",
    "2023-05-05",
    "2020-11-30"
]

sorted_dates = sort_dates(date_list)
print(sorted_dates)

"""
Problem: 617
Write a Python program to sort a list of tuples by the first element, then by the second if the first elements are equal using key.
"""

def lst_tuples(lst):
    def sort(tup):
        return (tup[0], tup[1]) 
    
    return sorted(lst, key=sort)

lst = [("nice", "good"), ("evil", "bad"), ("nice", "better"), ("evil", "worse")]
sorted_tuples = lst_tuples(lst)
print(sorted_tuples)

"""
Problem: 618
Write a function that sorts a list of names based on the number of characters in each name using the key parameter.
"""

def lst_names(lst):
    
    def sort_len_of_name(name):
        return len(name)
        
    return sorted(lst, key=sort_len_of_name)
        

lst = ["Jonathan", "Christopher", "Chantelle", "Bob", "Mimi"]
print(lst_names(lst))

def lst_names(lst):
    
    def sort_len_of_name(name):
        count = 0
        for char in name:
            count += 1
        return count
        
    return sorted(lst, key=sort_len_of_name)
        
lst = ["Jonathan", "Christopher", "Chantelle", "Bob", "Mimi"]
print(lst_names(lst))


"""
Problem: 619
Write a Python program to sort a list of employees by their hire date using the key parameter.
"""

def sort_by_hire_date(employees):
    
    def get_hire_date(employee):
        return employee[1]  

    return sorted(employees, key=get_hire_date)

employees = [
    ("Alice", "2020-05-15"),
    ("Bob", "2019-03-22"),
    ("Charlie", "2021-07-30"),
    ("David", "2018-12-01")
]

sorted_employees = sort_by_hire_date(employees)
print(sorted_employees)

"""
Problem: 620
Write a function that sorts a list of sentences based on their length using the key parameter.
"""

def lst_of_sentences(sentences):
    
    def sort(sentence):
        return len(sentence) 

    return sorted(sentences, key=sort)


sentences = ["hey what's happening today?", "what is", "what about me"]
print(lst_of_sentences(sentences))

"""
Problem: 621
Write a Python program to sort a list of words based on the frequency of their first letter using the key parameter.
"""

def frequency_first_letter(words):
    letter_count = {}
    for word in words:
        first_letter = word[0]
        if first_letter in letter_count:
            letter_count[first_letter] += 1
        else:
            letter_count[first_letter] = 1
    
    def sort(word):
        return letter_count[word[0]] 
        
    return sorted(words, key=sort)

words = ["apple", "apricot", "banana", "berry", "blueberry", "cherry", "carrot"]
print(frequency_first_letter(words))


from collections import Counter

def frequency_first_letter(words):
    
    letter_count = Counter()
    
    for word in words:
        first_letter = word[0] 
        letter_count[first_letter] += 1

    def sort(word):
        return letter_count[word[0]]
        
    return sorted(words, key=sort)

words = ["apple", "apricot", "banana", "berry", "blueberry", "cherry", "carrot"]
print(frequency_first_letter(words))

"""
Problem: 622
Write a function that sorts a list of tuples by the absolute value of the first element using the key parameter.
"""

def lst_of_tuples(lst):
    
    def sort(x):
        return abs((x)[0])
        
    return sorted(lst, key=sort)


lst = [(2.3, 4.2), (5.3, 7.3), (3.1, 2.4), (5.2, 6.2)]
print(lst_of_tuples(lst))

"""
Problem: 623
Write a Python program to sort a list of strings by their reverse order using the key parameter.
"""

def reverse_order(lst):
    
    def sort(word):
        return word
        
    return sorted(lst, key=sort, reverse= True)
        
lst = ["butt", "shoulders", "legs"]    
print(reverse_order(lst))


def reverse_order(lst):
    
    def sort(word):
        return word[::-1]
        
    return sorted(lst, key=sort)
        
lst = ["butt", "shoulders", "legs"]    
print(reverse_order(lst))

"""
Problem: 624
Write a function that sorts a list of temperatures in Celsius, converting them to Fahrenheit for sorting using the key parameter.
"""

def temperture(lst):
    
    def sort(celsius):
        
        fahrenheit = (9/5) * celsius + 32
        return fahrenheit
        
    return sorted(lst, key=sort)
            
lst = [23, 33, 12, 45]    
print(temperture(lst))

"""
Problem: 625
Write a Python program to sort a list of scores from a game, taking into account that some scores may be negative using the key parameter.
"""

def sort_scores(scores):
    
    def key_function(x):
        return x  
    
    return sorted(scores, key=key_function)

scores = [10, -5, 20, 0, -15, 5]
sorted_scores = sort_scores(scores)
print(sorted_scores)

"""
Problem: 626
Write a function that sorts a list of email addresses by the domain part using the key parameter.
"""

def sort_emails(emails):
    
    def get_domain(email):
        return email.split('@')[1] 
    
    return sorted(emails, key=get_domain)

emails = ["alice@example.com", "bob@test.com", "charlie@example.com", "dave@sample.com"]
sorted_emails = sort_emails(emails)
print(sorted_emails)

"""
Problem: 627
Write a Python program to sort a list of cities by their population using the key parameter.
"""

def sort_cities_by_population(cities):
    
    def get_population(city):
        return city[1] 
    
    return sorted(cities, key=get_population)

# List of cities with their population
cities = [("New York", 8419600), ("Los Angeles", 3980400), ("Chicago", 2716000), ("Houston", 2328000), ("Phoenix", 1690000)]

sorted_cities = sort_cities_by_population(cities)
print(sorted_cities)

"""
Problem: 628
Write a function that sorts a list of words by the last letter of each word using the key parameter.
"""

def last_letter(lst):
    
    def sort(word):
        return word[-1]
        
    return sorted(lst, key=sort)
    
lst = ["house", "garden", "boat", "building"]
print(last_letter(lst))

"""
Problem: 629
Write a Python program to sort a list of numbers by the number of times they appear in another list using the key parameter.
"""

def lst_of_numbers(lst):
    frequency = {}
    for number in lst:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    
    def sort(number):
        return frequency[number]
    
    return sorted(lst, key=sort)

lst = [3, 677, 4, 3, 67, 4]
print(lst_of_numbers(lst))

"""
Problem: 630
Write a function that sorts a list of students by their grades using the key parameter.
"""

def sort_students_by_grades(students):
    
    def get_grade(student):
        return student[1] 
        
    return sorted(students, key=get_grade)

students = [("Alice", 85), ("Bob", 70), ("Charlie", 95), ("David", 65)]
print(sort_students_by_grades(students))

"""
Problem: 631
Write a Python program to sort a list of book titles by the year they were published using the key parameter.
"""

def sort_books_by_year(books):
    
    def get_year(book):
        return book[1]
        
    return sorted(books, key=get_year)

books = [("Book A", 2005), ("Book B", 1999), ("Book C", 2010), ("Book D", 1985)]
print(sort_books_by_year(books)) 
 
"""
Problem: 632
Write a function that sorts a list of files based on their file extension using the key parameter.
"""

def sort_files_by_extension(files):

    def get_extension(file):
        return file.split('.')[-1]
        
    return sorted(files, key=get_extension)

files = ["document.pdf", "image.png", "archive.zip", "presentation.pptx", "notes.txt"]
print(sort_files_by_extension(files))

""" 
Problem: 633
Write a Python program to sort a list of movies by their release date using the key parameter.
"""

def sort_movies_by_release_date(movies):
    
    def get_release_date(movie):
        return movie['release_date'] 
        
    return sorted(movies, key=get_release_date)

movies = [
    {"title": "Inception", "release_date": "2010-07-16"},
    {"title": "The Matrix", "release_date": "1999-03-31"},
    {"title": "Interstellar", "release_date": "2014-11-07"},
    {"title": "The Godfather", "release_date": "1972-03-24"}
]
sorted_movies = sort_movies_by_release_date(movies)
for movie in sorted_movies:
    print(f"{movie['title']} - {movie['release_date']}")

"""
Problem: 634
Write a function that sorts a list of sentences based on the number of unique words in each sentence using the key parameter.
"""

def sort_sentences_by_unique_words(sentences):

    def count_unique_words(sentence):
        words = sentence.split() 
        unique_words = set(words)
        
        return len(unique_words)
        
    return sorted(sentences, key=count_unique_words)

sentences = [
    "This is a test sentence",
    "Hello world",
    "This is a simple sentence",
    "Hello hello world",
    "Unique words are counted here"
]

sorted_sentences = sort_sentences_by_unique_words(sentences)
for sentence in sorted_sentences:
    print(sentence)

"""
Problem: 635
Write a program to create a dictionary and retrieve a list of its keys.
"""

def get_keys_from_dictionary(dic):

    return list(dic.keys())

example_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

keys = get_keys_from_dictionary(example_dict)
print(keys)

"""
Problem: 636
Write a function that takes a dictionary and returns a list of keys that have values greater than 10.
"""

def dic_keys(dic):
    result = []
    for key, value in dic.items():
        if value > 10:
            result.append(key)
    return result

dic = {"a": 5, "b": 34, "c": 67, "d": 9}
print(dic_keys(dic))

"""
Problem: 637
Create a dictionary of fruits with their prices, and print all the keys.
"""

def print_fruit_keys(fruit_prices):
    return list(fruit_prices.keys())
    
fruit_prices = {
    "apple": 1.2,
    "banana": 0.5,
    "orange": 0.75,
    "grape": 2.0
}
print(print_fruit_keys(fruit_prices))

"""
Problem: 638
Write a program to find the maximum key in a dictionary.
"""

def max_key(dic):
    return max(dic.keys())

example_dict = {
    1: "apple",
    3: "banana",
    5: "cherry",
    2: "date"
}
print(max_key(example_dict))

"""
Problem: 639
Create a dictionary of names and ages, and return the keys sorted by age.
"""

def name_age(dic):
    
    def sort_key(name):
        return dic[name]
    
    sorted_keys = sorted(dic.keys(), key=sort_key)
    
    return sorted_keys

dic = {"Natty": 78, "Bob": 45}
print(name_age(dic))


"""
Problem: 640
Write a function that accepts a dictionary and returns the keys as a single concatenated string.
"""

def concatenate_keys(dic):
    result = ""
    for key in dic.keys():
        result += str(key)
    return result
    
dic = {1: 456, 2: 5566, 3: 566}    
print(concatenate_keys(dic))

"""
Problem: 641
Create a dictionary of countries and their capitals, and print each key with its corresponding value.
"""

def print_countries_and_capitals(dic):
    for country, capital in dic.items():
        print(f"{country}: {capital}")

countries_capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Japan": "Tokyo",
    "Germany": "Berlin",
    "India": "New Delhi"
}
print_countries_and_capitals(countries_capitals)

"""
Problem: 642
Write a program to create a dictionary and count how many keys it has.
"""

def count_key(dic):
    count = 0
    for key in dic.keys():
        count += 1
    return count

dic = {"a":1, "b": 2, "c": 3}
print(count_key(dic))

"""
Problem: 643
Write a function that takes a dictionary and returns only the keys that start with a specific letter.
"""

def count_key(dic, letter):
    result = []
    for key in dic.keys():
        if key.startswith(letter):
            result.append(key)
    return result

dic = {"apple": 1, "banana": 2, "apricot": 3, "berry": 4}
print(count_key(dic, 'a'))

"""
Problem: 644
Create a dictionary of students and their grades, and print the keys sorted alphabetically.
"""

def sorted_students_grades(dic):
    return sorted(dic.keys())

students_grades = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 95,
    "David": 88
}
print(sorted_students_grades(students_grades))

"""
Problem: 645
Write a program to create a dictionary from two lists: one for keys and one for values.
"""

def list_dictionary(lst1, lst2):
    dic = {}
    
    for key, value in zip(lst1, lst2):
        dic[key] = value 
    
    return dic

lst1 = [1, 2, 3]    
lst2 = ["goat", "boat", "soap"]    
print(list_dictionary(lst1, lst2))

"""
Problem: 646
Create a dictionary of colors and their hexadecimal values, and print the keys in reverse order.
"""

def reverse_keys(dic):
    return list(dic.keys())[::-1] 

colors = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF",
    "yellow": "#FFFF00"
}
print(reverse_keys(colors))

"""
Problem: 647
Write a function that returns the first key in a dictionary.
"""

def first_key(dic):
    return next(iter(dic))  

example_dict = {"Nat": 90, "Xav": 70, "Zac": 60}
print(first_key(example_dict))

def first_key(dic):
    for key in dic:
        return key
dic = {"apple": 1, "orange": 33, "mango": 5}
first_key(dic)

"""
Problem: 648
Create a dictionary representing a shopping cart, and print the keys of the items in the cart.
"""

def shopping_cart_items(cart):
    for item in cart.keys():
        
        print(item)

cart = {
    "apple": 3,
    "banana": 6,
    "orange": 4,
    "milk": 1
}
shopping_cart_items(cart)

"""
Problem: 649
Write a program that checks if a specific key exists in a dictionary.
"""

def check_key_exists(dic, key):
    if key in dic:
        return True
    else:
        return False

example_dict = {"apple": 3, "banana": 6, "orange": 4, "milk": 1}

key_to_check = "banana"
print(check_key_exists(example_dict, key_to_check))  # Output: True

key_to_check = "bread"
print(check_key_exists(example_dict, key_to_check))  # Output: False

"""
Problem: 650
Create a dictionary of items and their quantities, and print keys with quantities greater than 5.
"""

def print_keys_greater_than_five(dic):
    for item, quantity in dic.items():
        if quantity > 5:
            print(item)
            
items_dict = {
    "apple": 3,
    "banana": 6,
    "orange": 4,
    "milk": 8,
    "bread": 2,
    "eggs": 12
}
print_keys_greater_than_five(items_dict)

"""
Problem: 651
Write a function that accepts a dictionary and returns a list of keys that are strings.
"""

def returns_strings(dic):
    result = []
    for key in dic.keys():
        if isinstance(key, str):
            result.append(key)
    return result

example_dict = {"Nat": 90, 56: 70, "Zac": 60, 56: 56}
print(returns_strings(example_dict))

"""
Problem: 652
Create a dictionary of sports and their popularity rankings, and return the keys sorted by ranking.
"""

def sports_by_popularity(sports_dict):

    def get_ranking(sport):
        return sports_dict[sport]

    return sorted(sports_dict, key=get_ranking)

sports_dict = {
    "Soccer": 1,
    "Basketball": 3,
    "Cricket": 2,
    "Tennis": 4
}
print(sports_by_popularity(sports_dict)) 

"""
Problem: 653
Write a program that retrieves keys from a dictionary that are of type integer.
"""

def main(dic):
    result = {}
    for key, value in dic.items():
        if isinstance(value, int):
            result[key] = value
    return result

dic = {2: 1, "orange": 33, "mango": 5}
main(dic)

# Define a dictionary with integer keys
data = {1: 'one', 2: 'two', 3: 'three', 'a': 4, 'b': 5}

# Retrieve keys that are of type integer
integer_keys = [key for key in data if isinstance(key, int)]

# Print the retrieved keys
print(integer_keys)
"""
Problem: 654
Create a dictionary of books and their authors, and print the keys formatted as a numbered list.
"""

def books_authors(dic):
    for index, book in enumerate(dic.keys(), start=1):
        print(f"{index}. {book}")

dic = {
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell",
    "The Great Gatsby": "F. Scott Fitzgerald",
    "Pride and Prejudice": "Jane Austen",
    "Moby-Dick": "Herman Melville"
}
books_authors(dic)

"""
Problem: 655
Write a function that takes a dictionary and returns a list of keys that are palindromes.
"""

def palindromic_keys(dic):
    result = []
    for key in dic.keys():
        if key == key[::-1]: 
            result.append(key)
    return result

example_dict = {
    "madam": 1,
    "racecar": 2,
    "hello": 3,
    "world": 4,
    "level": 5
}
print(palindromic_keys(example_dict))

"""
Problem: 656
Create a dictionary of pets and their owners, and print all the keys that contain the letter “o”.
"""

def pet_owners(dic):
    result = []
    for key in dic.keys():
        if "o" in key: 
            result.append(key)
    return result

dic = {
    "Boudy": "Alice",
    "Mittens": "Bob",
    "Charlie": "Catherine",
    "Monty": "David",
    "Bella": "Eva"
}
print(pet_owners(dic))

def pet_owners(dic):
    result = []
    for key in dic.keys():
        for char in key:
            if char == "o":
                result.append(key)
    return result
    
dic = {
    "Boudy": "Alice",
    "Mittens": "Bob",
    "Charlie": "Catherine",
    "Monty": "David",
    "Bella": "Eva"
}
print(pet_owners(dic))

"""
Problem: 657
Write a program that counts how many keys in a dictionary are of type tuples.
"""

def count_tuple_keys(dic):
    count = 0
    for key in dic.keys():
        if isinstance(key, tuple):
            count += 1
    return count

dic = {
    (1, 2): "tuple_key_1",
    "string_key": "value1",
    (3, 4): "tuple_key_2",
    3: "integer_key"
}
print(count_tuple_keys(dic)) 

"""
Problem: 658
Create a dictionary of movies and their release years, and return the keys as a sorted list.
"""

def movies(dic):
    return sorted(dic.keys())

dic = {
    "The Shawshank Redemption": 1994,
    "The Godfather": 1972,
    "The Dark Knight": 2008,
    "Pulp Fiction": 1994,
    "Forrest Gump": 1994,
    "Inception": 2010,
    "Fight Club": 1999,
    "The Matrix": 1999,
    "Gladiator": 2000,
    "The Lord of the Rings: The Return of the King": 2003
}
print(movies(dic))

"""
Problem: 659
Write a function that returns the keys of a dictionary whose values are lists.
"""

def main(dic):
    for key, value in dic.items():
        if isinstance(value, list):
            return key

dic = {"apple": 1, "orange": [45, 74], "mango": 5}
main(dic)

def keys_with_list_values(dic):
    result = []
    for key, value in dic.items():
        if isinstance(value, list):
            result.append(key)
    return result

dic = {
    "fruits": ["apple", "banana", "cherry"],
    "vegetable": "carrot",
    "numbers": [1, 2, 3],
    "color": "blue"
}
print(keys_with_list_values(dic))

"""
Problem: 660
Create a dictionary of car brands and their models, and print the keys in a formatted manner.
"""

def print_car_brands(dic):
    print("Car Brands:")
    for index, brand in enumerate(dic.keys(), start=1):
        print(f"{index}. {brand}")

car_brands = {
    "Toyota": ["Camry", "Corolla", "Prius"],
    "Ford": ["Mustang", "F-150", "Explorer"],
    "Honda": ["Civic", "Accord", "CR-V"],
    "Chevrolet": ["Malibu", "Impala", "Silverado"],
}
print_car_brands(car_brands)

"""
Problem: 661
Write a program that retrieves the second key from a dictionary.
"""

def second_key(dic):
    keys_list = list(dic.keys())
    return keys_list[1] if len(keys_list) > 1 else None

dic = {"hope": 12, "dispel": 23, "faith": 34}
print(second_key(dic))

def second_key(dic):
    return list(dic.keys())[1]
  

dic = {"hope": 12, "dispel": 23, "faith": 34}
print(second_key(dic))

"""
Problem: 662
Create a dictionary of temperatures and their units, and return the keys as uppercase strings.
"""

def temperature(dic):
    upper_keys = []
    for key in dic.keys():
        upper_keys.append(key.upper())
    return upper_keys

dic = {
    "Celsius": [0, 20, 37, 100],
    "Fahrenheit": [32, 68, 98.6, 212],
    "Kelvin": [273.15, 293.15, 310.15, 373.15]
}
print(temperature(dic))

"""
Problem: 663
Write a function that takes a dictionary and returns keys that are found in a given list.
"""

def keys_in_list(dic, given_list):
    result = []
    for key in dic.keys():
        if key in given_list:
            result.append(key)
    return result

dic = {
    "apple": 1,
    "banana": 2,
    "cherry": 3,
    "date": 4
}

given_list = ["banana", "date", "grape"]
print(keys_in_list(dic, given_list))

"""
Problem: 664
Create a dictionary of electronic devices and their prices, and print all keys with a price less than $100.
"""

devices = {
    "Phone": 999,
    "Headphones": 50,
    "Keyboard": 80,
    "Mouse": 25,
    "Charger": 15
}

for device, price in devices.items():
    if price < 100:
        print(device)

"""
Problem: 665
Write a function that takes a dictionary and returns a list of keys that have values greater than 10.
"""

def keys_with_values_greater_than_10(dic):
    result = []
    for key in dic.keys(): 
        if dic[key] > 10: 
            result.append(key)
    return result

dic = {"Sam": 5, "Chris": 34, "Simon": 12, "Anna": 9}
print(keys_with_values_greater_than_10(dic)) 

def get_dict_keys(dic):
    result = []
    for key, value in dic.items():
        if value > 10:
            result.append(key)
    return result

my_dict = {'apple': 30, 'banana': 50, 'cherry': 2, 'date': 7}
print(get_dict_keys(my_dict))

"""
Problem: 666
Create a dictionary of fruits with their prices, and print all the keys. Use key().
"""

def print_fruit_keys(fruits):
    
    for key in fruits.keys():
        print(key)

fruits = {
    "Apple": 3,
    "Banana": 1,
    "Mango": 2,
    "Orange": 4
}
print_fruit_keys(fruits)

"""
Problem: 667
Create a dictionary of names and ages, and return the keys sorted by age.
"""

def name_age(dic):
    
    def sort_age(x):
        for keys, values in x:
            return values
    return sorted(dic, key=sort_age)
    

dic = {"Tom": 15, "Lucka": 66, "Bob": 8}    
print(name_age(dic))

"""
Problem: 668
Write a function that accepts a dictionary and returns the keys as a single concatenated string.
"""

def concatenate(dic):
    result = ""
    for key in dic.keys():
        result += str(key)
    return result
        
dic = {1: "one", 2: "two", 3: "three", 4: "four"}    
print(concatenate(dic))

"""
Problem: 669
Create a dictionary of countries and their capitals, and print each key with its corresponding value.
"""

def countries_capitals(dic):
    result = ""
    for key, value in dic.items():
        result += f"{key}: {value}\n" 
    return result
    
dic = {
    "United States": "Washington, D.C.",
    "Canada": "Ottawa",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "Australia": "Canberra",
    "India": "New Delhi",
    "Brazil": "Brasilia",
    "South Africa": "Pretoria"
}
print(countries_capitals(dic))

"""
Problem: 670
Write a program to create a dictionary and count how many keys it has.
dic = {
    "United States": "Washington, D.C.",
    "Canada": "Ottawa",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin"
}
"""

def count_keys(dic):
    return len(dic)

dic = {
    "United States": "Washington, D.C.",
    "Canada": "Ottawa",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin"
}
print(count_keys(dic))

"""
Problem: 671
Write a function that takes a dictionary and returns only the keys that start with a specific letter.
"""

def keys_starting_with(dic, letter):
    result = []
    for key in dic.keys():
        if key.startswith(letter):
            result.append(key)
    return result

dic = {
    "apple": 1,
    "banana": 2,
    "apricot": 3,
    "berry": 4,
    "carrot": 5
}
print(keys_starting_with(dic, "a"))

"""
Problem: 672
Create a dictionary of students and their grades, and print the keys sorted alphabetically.
"""

def students_grades(dic):
    sorted_keys = sorted(dic.keys())

    for key in sorted_keys:
        print(key)

dic = {
    "John": 85,
    "Alice": 92,
    "Bob": 78,
    "Diana": 88,
    "Charlie": 90
}
students_grades(dic)

"""
Problem: 673
Write a program to create a dictionary from two lists: one for keys and one for values.
"""

def two_lst(lst1, lst2):
    result = {}
    for key, value in zip(lst1, lst2):
        result[key] = value
        
    return result
    
lst1 = [1, 2, 3, 4]
lst2 = ["sand", "rock", "wood", "stone"]
print(two_lst(lst1, lst2))

"""
Problem: 674
Create a dictionary of colors and their hexadecimal values, and print the keys in reverse order.
"""

def colors_hex(dic):
    keys_in_reverse = list(dic.keys())[::-1]
    
    for key in keys_in_reverse:
        print(key)

colors_dict = {
    "Red": "#FF0000",
    "Green": "#00FF00",
    "Blue": "#0000FF",
    "Yellow": "#FFFF00",
    "Black": "#000000",
    "White": "#FFFFFF"
}
colors_hex(colors_dict)

def colors_hex(dic):
    return list(dic.keys())[::-1]
colors_dict = {
    "Red": "#FF0000",
    "Green": "#00FF00",
    "Blue": "#0000FF",
    "Yellow": "#FFFF00",
    "Black": "#000000",
    "White": "#FFFFFF"
}
colors_hex(colors_dict)

"""
Problem: 675
Write a function that returns the first key in a dictionary.
"""

def first_key(dic):
    return next(iter(dic))
    
example_dict = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
}
print(first_key(example_dict))

"""
Problem: 676
Create a dictionary representing a shopping cart, and print the keys of the items in the cart.
"""

def print_cart_items(cart):
    for item in cart.keys():
        print(item)

shopping_cart = {
    "apple": 3,
    "banana": 2,
    "bread": 1,
    "milk": 2
}
print_cart_items(shopping_cart)

"""
Problem: 677
Write a program that checks if a specific key exists in a dictionary.
"""

def check_key_exists(dic, key):
    if key in dic:
        return True
    else:
        return False

example_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
key_to_check = "age"

if check_key_exists(example_dict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")

"""
Problem: 678
Create a dictionary of items and their quantities, and print keys with quantities greater than 5.
"""

def items_with_high_quantity(dic):
    result = []
    for item, quantity in dic.items():
        if quantity > 5:
            result.append(item)
    return result

inventory = {
    "apples": 10,
    "bananas": 3,
    "oranges": 7,
    "pears": 5,
    "grapes": 12
}
high_quantity_items = items_with_high_quantity(inventory)
print("Items with quantities greater than 5:")
for item in high_quantity_items:
    print(item)

"""
Problem: 679
Write a function that accepts a dictionary and returns a list of keys that are strings.
"""

def string_keys(dic):
    result = []
    for key in dic.keys():
        if isinstance(key, str): 
            result.append(key)
    return result

example_dict = {
    "name": "Alice",
    42: "answer",
    "city": "Wonderland",
    (1, 2): "tuple_key",
    "age": 30
}
string_keys_list = string_keys(example_dict)
print("Keys that are strings:", string_keys_list)

"""
Problem: 680
Create a dictionary of sports and their popularity rankings, and return the keys sorted by ranking.
"""

def sports_by_popularity(sports_dict):
    def get_ranking(sport):
        return sports_dict[sport]

    return sorted(sports_dict.keys(), key=get_ranking)

sports_dict = {
    "Soccer": 1,
    "Basketball": 3,
    "Cricket": 2,
    "Tennis": 4
}
print(sports_by_popularity(sports_dict))

"""
Problem: 681
Write a program that retrieves keys from a dictionary that are of type integer.
"""

def retrieve_integer_keys(dic):
    result = []
    for key in dic.keys():
        if isinstance(key, int):
            result.append(key)
    return result

example_dict = {
    1: "one",
    "two": 2,
    3: "three",
    "four": 4
}
print(retrieve_integer_keys(example_dict))

"""
Problem: 682
Create a dictionary of books and their authors, and print the keys formatted as a numbered list.
"""

def print_numbered_books(dic):
    for index, items in enumerate(dic.keys(), start=1):
        print(f"{index}. {items}")

books = {
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell",
    "The Great Gatsby": "F. Scott Fitzgerald",
    "Pride and Prejudice": "Jane Austen",
    "Moby-Dick": "Herman Melville"
}
print_numbered_books(books)

"""
Problem: 683
Write a function that takes a dictionary and returns a list of keys that are palindromes.
"""

def palindrome_keys(dic):
    result = []
    for key in dic.keys():
        if str(key) == str(key)[::-1]:
            result.append(key)
    return result

example_dict = {
    "racecar": 1,
    "level": 2,
    "hello": 3,
    "madam": 4,
    "world": 5
}
print(palindrome_keys(example_dict))

"""
Problem: 684
Create a dictionary of pets and their owners, and print all the keys that contain the letter “o”.
"""

def pets_with_o(dic):
    result = []
    for key in dic.keys():
        if 'o' in key:
            result.append(key)
    return result

pets_dict = {
    "Boudy": "Alice",
    "Mittens": "Bob",
    "Charlie": "Catherine",
    "Monty": "David",
    "Bella": "Eva"
}
print(pets_with_o(pets_dict))

"""
Problem: 685
Write a program that counts how many keys in a dictionary are of type list.
"""

def count_list_keys(dic):
    count = 0
    for key in dic.keys():
        if isinstance(key, list):
            count += 1
    return count

example_dict = {
    (1, 2): "tuple_key",
    "string_key": "value1",
    3: "integer_key",
}
print(count_list_keys(example_dict))

"""
Problem: 686
Create a dictionary of movies and their release years, and return the keys as a sorted list.
"""

def sorted_movie_titles(movies):
    return sorted(movies.keys())

movies_dict = {
    "The Shawshank Redemption": 1994,
    "The Godfather": 1972,
    "The Dark Knight": 2008,
    "Pulp Fiction": 1994,
    "Forrest Gump": 1994,
}
print(sorted_movie_titles(movies_dict))

"""
Problem: 687
Write a function that returns the keys of a dictionary whose values are lists.
"""

def keys_with_list_values(dic):
    result = []
    for key, value in dic.items():
        if isinstance(value, list):
            result.append(key)
    return result

example_dict = {
    "fruits": ["apple", "banana"],
    "vegetable": "carrot",
    "grains": ["rice", "wheat"]
}
print(keys_with_list_values(example_dict))

"""
Problem: 688
Create a dictionary of car brands and their models, and print the keys in a formatted manner.
"""

def print_car_brands(dic):
    for brand in dic.keys():
        print(f"Brand: {brand}")

car_brands = {
    "Toyota": ["Camry", "Corolla", "RAV4"],
    "Honda": ["Civic", "Accord", "CR-V"],
    "Ford": ["F-150", "Mustang", "Explorer"]
}
print_car_brands(car_brands)

"""
Problem: 689
Write a program that retrieves the second key from a dictionary.
"""

def second_key(dic):
    return list(dic.keys())[1]

example_dict = {"apple": 1, "banana": 2, "cherry": 3}
print(second_key(example_dict))

"""
Problem: 690
Create a dictionary of temperatures and their units, and return the keys as uppercase strings. keys only ("Celsius": [0, 20, 37, 100]).
"""

def uppercase_keys(dic):
    result = []
    for key in dic.keys():
        result.append(key.upper())
    return result

dic = {
    "Celsius": [0, 20, 37, 100],
    "Fahrenheit": [32, 68, 98.6, 212],
    "Kelvin": [273.15, 293.15, 310.15, 373.15]
}
print(uppercase_keys(dic))

"""
Problem: 691
Write a program to find the maximum key in a dictionary.
"""

def key_max(dic):
    
    return max(dic)
    
dic = {"banana": 1.50, "Apple": 2, "apricot": 3.5}    
print(key_max(dic))

def key_max(dic):
    max_key = None
    max_key_lower = None
    
    for key in dic:

        key_lower = key.lower()
        
        if max_key_lower is None or key_lower > max_key_lower:
            max_key = key
            max_key_lower = key_lower
    
    return max_key

dic = {"banana": 1.50, "Apple": 2, "apricot": 3.5}

print(key_max(dic))

"""
Problem: 692
Write a program that takes a list of numbers and returns a new list with each number squared using map().
"""

def square_numbers(lst):
    
    def square(num):
        return num ** 2
    
    return list(map(square, lst))

numbers = [1, 2, 3, 4, 5]
print(square_numbers(numbers))

"""
Problem: 693
Create a program that takes a list of strings and returns a list of their lengths using map().
"""

def string_lengths(lst):
    
    def length(string):
        return len(string)
    
    return list(map(length, lst))

strings = ["hello", "world", "python", "programming"]
print(string_lengths(strings))

"""
Problem: 694
Write a function that takes a list of strings and converts all of them to uppercase using `map()`.
"""

def lst_words(lst):
    
    def word_len(word):
        return word.upper()
        
    return list(map(word_len, lst))

lst = ["monkey", "lizard", "hippopotamus"]
print(lst_words(lst))

"""
Problem: 695
Given a list of floats, use `map()` to round all the numbers to two decimal places.
"""

def lst_numbers(lst):
    
    def round_two_decimals(x):
        return round(x, 2)
        
    return list(map(round_two_decimals, lst))

lst = [2.6666, 4.77, 7.566, 9.55]
print(lst_numbers(lst))
 
"""
Problem: 696
Write a program that converts a list of temperatures in Celsius to Fahrenheit using `map()`.
"""

def celsius_to_fahrenheit(lst):
    
    def convert(celsius):
        return (celsius * 9/5) + 32
        
    return list(map(convert, lst))

celsius_temps = [0, 20, 37, 100]
fahrenheit_temps = celsius_to_fahrenheit(celsius_temps)
print(fahrenheit_temps)

"""
Problem: 697
Use `map()` to convert a list of numbers into their corresponding ASCII characters.
"""

def numbers_to_ascii(lst):
    
    def to_ascii(number):
        return chr(number)
        
    return list(map(to_ascii, lst))

numbers = [0, 65, 66, 67, 68, 69, 91, 120]
ascii_characters = numbers_to_ascii(numbers)
print(ascii_characters)

"""
Problem: 698
Write a function that takes a list of words and returns the reversed version of each word using `map()`.
"""

def lst_words(lst):
    
    def reverse_word(word):
        return word[::-1]
        
    return list(map(reverse_word, lst))

lst = ["monkey", "lizard", "hippopotamus"]
print(lst_words(lst))

"""
Problem: 700
Create a program that takes a list of integers and returns a list where each number is doubled using `map()`.
"""

def lst_integers(lst):
    
    def double_num(number):
        return number * 2 
        
    return list(map(double_num, lst))

lst = [0, 65, 66, 67, 68, 69, 91, 120]
print(lst_integers(lst))

"""
Problem: 701
Write a program to take a list of strings and return a list of their first characters using `map()`.
"""

def lst_words(lst):
    
    def first_char(word):
        return word[0]
        
    return list(map(first_char, lst))

lst = ["monkey", "lizard", "hippopotamus"]
print(lst_words(lst))

"""
Problem: 702
Use `map()` to convert a list of binary strings to their decimal equivalents.
"""

def lst_words(lst):
    
    def binary(word):
        return int(word, 2)
        
    return list(map(binary, lst))

lst = ["101", "110", "1001"]
print(lst_words(lst))

"""
Problem: 703
Write a program that takes a list of mixed-case strings and returns all strings in lowercase using `map()`.
"""

def lst_mixed_case(lst):
    
    def lowercase(string):
        return string.lower()
        
    return list(map(lowercase, lst))

lst = ["LIZARD", "hiPpopotamus", "FroG"]
print(lst_mixed_case(lst))

"""
Problem: 704
Given two lists of numbers, use `map()` to multiply each pair of numbers from the two lists together.
"""

def lst_integers(lst1, lst2):
    
    def multiply(num1, num2):
        return num1 * num2 
        
    return list(map(multiply, lst1, lst2))

lst1 = [6, 12, 23, 68]
lst2 = [1, 2, 3, 4]
print(lst_integers(lst1, lst2))

"""
Problem: 705
Use `map()` to convert a list of tuples (representing x, y points) into a list of their Euclidean distances from the origin.
"""

import math

def euclidean_distances(points):
    
    def distance(point):
        return math.sqrt(point[0]**2 + point[1]**2)
        
    return list(map(distance, points))

points = [(3, 4), (1, 1), (0, 0), (6, 8)]
print(euclidean_distances(points))

"""
Problem: 706
Write a function that takes a list of email addresses and extracts the domain names using `map()`.
"""

def lst_emails(lst):
    
    def domain(string):
        return string.split('@')[1]
        
    return list(map(domain, lst))

lst = ["user@example.com", "admin@domain.org", "info@website.net"]
print(lst_emails(lst))

"""
Problem: 707
Use `map()` to take a list of numbers and return a list indicating whether each number is even or odd.
"""

def lst_integers(lst):
    
    def even_odd(number):
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"
        
    return list(map(even_odd, lst))

lst = [65, 66, 67, 68, 69, 91, 120]
print(lst_integers(lst))

"""
Problem: 708
Write a program that uses `map()` to convert a list of string representations of numbers to a list of integers.
"""

def negate_bool(value):
    return not value

bool_list = [True, False, True, False]
negated_list = list(map(negate_bool, bool_list))
print(negated_list)  # Output: [False, True, False, True]

"""
Problem: 709
Create a program that takes a list of Boolean values and negates each value using `map()`.
"""

def negate_bool(bool_list):
    def inner(value):
        return not value
    return list(map(inner, bool_list))

bool_list = [True, False, True, False]
negate_bool(bool_list)

def negate_bool(value):
    return not value

bool_list = [True, False, True, False]
negated_list = list(map(negate_bool, bool_list))
print(negated_list)  # Output: [False, True, False, True]

"""
Problem: 710
Write a function that takes a list of strings and returns a list of booleans indicating whether each string is a palindrome using `map()`.
"""

def negate_booleans(lst):
    
    def negate(value):
        return not value
        
    return list(map(negate, lst))

lst = [True, False, True, False]
print(negate_booleans(lst))

"""
Problem: 711
Given a list of sentences, use `map()` to return a list of the number of words in each sentence.
"""

def lst_sentence(lst):
    
    def num_of_words(string):
        words = string.split()
        return len(words)
        
    return list(map(num_of_words, lst))
    
lst = ["how hot is it", "what's up dog", "today is the best day of my life"]    
print(lst_sentence(lst))

"""
Problem: 712
Use `map()` to take a list of strings and return a list of strings where each word has its first letter capitalized.
"""

def lst_sentence(lst):
    
    def cap(word):
        word = word.capitalize()
        return word
           
    return list(map(cap, lst))
    
lst = ["mop", "sop", "dop"]    
print(lst_sentence(lst))

"""
Problem: 713
Write a program that takes a list of strings and removes all spaces from each string using `map()`.
"""

def lst_sentence(lst):
    
    def remove_spaces(word):
        return word.replace(" ", "")
           
    return list(map(remove_spaces, lst))
    
lst = ["mop in tate", "sop in tate", "dop in tate"]    
print(lst_sentence(lst))

"""
Problem: 714
Create a program that takes a list of tuples representing (width, height) and returns a list of their areas using `map()`.
"""

def lst_of_tuples(lst):
    
    def area_lst(dimensions):
        width, height = dimensions
        area = width * height
        return area
        
    return list(map(area_lst, lst))
            
lst = [(3, 5), (4, 9), (3, 9)]    
print(lst_of_tuples(lst))

"""
Problem: 715
Use `map()` to take a list of URLs and extract the domain name from each one.
"""

def extract_domain(lst):
    
    def domain(url):
        return url.split("//")[-1].split("/")[0]
        
    return list(map(domain, lst))

urls = [
    "https://www.example.com/page",
    "http://another-domain.org",
    "https://sub.domain.com/path/to/resource"
]

print(extract_domain(urls))

"""
Problem: 716
Write a function that takes two lists: one of numbers and one of strings, and returns a list of tuples pairing the elements using `map()`.
"""

def pair_elements(numbers, strings):
    
    def pair(num, string):
        return (num, string)
    
    return list(map(pair, numbers, strings))

numbers = [1, 2, 3]
strings = ["apple", "banana", "cherry"]
print(pair_elements(numbers, strings))

"""
Problem: 717
Create a program that converts a list of lowercase letters to uppercase using `map()`.
"""

def lowercase_to_uppercase(lst):
    
    def to_uppercase(letter):
        return letter.upper()
    
    return list(map(to_uppercase, lst))

lst = ['a', 'b', 'c', 'd']
print(lowercase_to_uppercase(lst))

"""
Problem: 718
Use `map()` to calculate the factorial of each number in a list.
"""

def factorial_lst(lst):
    
    def factorial(num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result
    
    return list(map(factorial, lst))

lst = [3, 4, 5, 6]
print(factorial_lst(lst))

import math

def factorial_lst(lst):
    
    def factorial(num):
        return math.factorial(num)
    
    return list(map(factorial, lst))

lst = [3, 4, 5, 6]
print(factorial_lst(lst))

"""
Problem: 719
Write a program that takes a list of sentences and returns a list of sentences in which each word is reversed using `map()`.
"""

def reverse_words_in_sentences(lst):
    
    def reverse_sentence(sentence):
        words = sentence.split()
        reversed_words = []
        for word in words:
            reversed_words.append(word[::-1])
        return ' '.join(reversed_words)
        
    return list(map(reverse_sentence, lst))

lst = ["The cat is fast", "Hello world", "Python is fun"]
print(reverse_words_in_sentences(lst))

"""
Problem: 720
Use `map()` to check whether the elements of a list of strings contain only alphabetic characters.
"""

def lst_strings(lst):
    
    def alpha_only(word):
        if word.isalpha():
            return True
        else:
            return False
            
    return list(map(alpha_only, lst))
                

lst = ["monkey", "tomy&", "magic"]
print(lst_strings(lst))

"""
Problem: 721
Write a function that takes a list of floats and returns a list where each float is squared using `map()`.
"""

def square_floats(lst):
    
    def square(num):
        return num * num
        
    return list(map(square, lst))

lst = [2.5, 3.1, 4.8, 6.7]
print(square_floats(lst))

"""
Problem: 722
Given a list of phone numbers, use `map()` to format them as international phone numbers.
"""

def format_phone_numbers(lst):
    
    def format_number(number):
        return f"+1-{number}"
        
    return list(map(format_number, lst))

lst = ["5551234567", "5559876543", "5556789123"]
print(format_phone_numbers(lst))

"""
Problem: 723
Use `map()` to find the absolute value of each number in a list.
"""

def absolute_values(lst):
    
    def absolute(num):
        return abs(num)
        
    return list(map(absolute, lst))

lst = [-10, 5, -3.2, 8]
print(absolute_values(lst))

"""
Problem: 724
Write a program that takes two lists of integers and returns a list of tuples pairing corresponding numbers from each list using `map()`.
"""

def pair_lists(lst1, lst2):
    
    def pair_numbers(num1, num2):
        return (num1, num2)

    return list(map(pair_numbers, lst1, lst2))

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
print(pair_lists(lst1, lst2))

"""
Problem: 725
Use `map()` to convert a list of tuples representing (x, y) coordinates into polar coordinates.
"""

import math

def cartesian_to_polar(lst):
    
    def to_polar(coords):
        x, y = coords
        r = math.sqrt(x**2 + y**2)
        theta = math.atan2(y, x)
        return (r, theta)

    return list(map(to_polar, lst))

coordinates = [(1, 1), (0, 0), (3, 4)]
print(cartesian_to_polar(coordinates))

"""
Problem: 726
Write a program that uses `map()` to find the cube of each number in a list.
"""

def lst_cubes(lst):
    
    def cube(num):
        return num ** 3
        
    return list(map(cube, lst))

numbers = [1, 2, 3, 4, 5]
print(lst_cubes(numbers))

"""
Problem: 727
Use `map()` to create a program that takes a list of integers and returns a list of their squares and cubes as tuples.
"""

def lst_squares_and_cubes(lst):
    
    def square_and_cube(num):
        return (num ** 2, num ** 3)
        
    return list(map(square_and_cube, lst))

lst = [1, 2, 3, 4, 5]
print(lst_squares_and_cubes(lst))

"""
Problem: 728
Write a program that uses `map()` to convert a list of RGB tuples into hexadecimal color codes.
"""

def rgb_to_hex(lst):
    
    def to_hex(rgb):
        return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
        
    return list(map(to_hex, lst))

lst = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
print(rgb_to_hex(lst))

"""
Problem: 729
Given a list of mixed-case strings, use `map()` to return a list of strings where every second string is converted to uppercase.
"""

def mixed_case_string(lst):
    
    def second_uppercase(word):
        return word[0] + word[1].upper() + word[2:]

    return list(map(second_uppercase, lst))

lst = ["first", "second", "third", "fourth"]
print(mixed_case_string(lst))

"""
Problem: 730
Write a function that uses `map()` to convert a list of dates (in string format) into Python `datetime` objects.
"""

from datetime import datetime

def convert_dates(date_list):
    
    def parse_date(date_string):
        return datetime.strptime(date_string, "%Y-%m-%d")
    
    return list(map(parse_date, date_list))

date_list = ["2024-01-01", "2023-12-25", "2022-07-04"]
print(convert_dates(date_list))

"""
Problem: 731
Use `map()` to calculate the square roots of each number in a list.
"""

import math

def calculate_square_roots(numbers):
    def square_root(x):
        return math.sqrt(x)
    
    return list(map(square_root, numbers))

numbers = [1, 4, 9, 16, 25]
print(calculate_square_roots(numbers))

"""
Problem: 732
Create a program that uses `map()` to calculate the percentage of each score in a list of scores based on the maximum score.
"""

def calculate_percentage(scores, max_score):
    def percentage(score):
        return (score / max_score) * 100
    
    return list(map(percentage, scores))

scores = [50, 75, 100, 80]
max_score = 100
print(calculate_percentage(scores, max_score))

"""
Problem: 733
Write a Python program that defines a helper function `add(a, b)` to return the sum of two numbers, and uses it to sum a list of numbers.
"""

def add(a, b):
    return a + b

def sum_list(numbers):
    total = 0
    for number in numbers:
        total = add(total, number)
    return total

numbers = [1, 2, 3, 4, 5]
result = sum_list(numbers)
print(result)

"""
Problem: 734
Create a program with a helper function `is_even(n)` that returns `True` if a number is even and `False` otherwise, and use it to filter a list of numbers.
"""

def is_even(n):
    return n % 2 == 0

def filter_even_numbers(numbers):
    return list(filter(is_even, numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(numbers)
print(even_numbers)

"""
Problem: 735
Write a program that uses a helper function `capitalize_first_letter(word)` to capitalize the first letter of each word in a list of strings.
"""

def capitalize_first_letter(word):
    return word.capitalize()

def word_list(lst):
    return list(map(capitalize_first_letter, lst))

lst = ["first", "letter", "word"]
print(word_list(lst))


def word_list(lst):
    return list(map(capitalize_first_letter, lst))

def capitalize_first_letter(word):
    return word.capitalize()

lst = ["first", "letter", "word"]
print(word_list(lst))

"""
Problem: 736
Define a helper function `find_max(numbers)` that returns the maximum number from a list, and use it in a program to find the largest number.
"""

def lst_numbers(lst):
    return find_max(lst)
    
def find_max(numbers):
    return max(numbers)
    
lst = [2, 4, 6]
print(lst_numbers(lst))

"""
Problem: 737
Create a helper function `convert_to_celsius(fahrenheit)` that converts a temperature from Fahrenheit to Celsius, and use it to convert a list of temperatures.
"""

def lst_tempertures(lst):
    return list(map(convert_to_celsius, lst))
    
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8
       
lst = [1, 16, 20, 27]    
print(lst_tempertures(lst))

"""
Problem: 738
Write a program that defines a helper function `reverse_string(s)` that returns the reversed version of a string, and uses it to reverse all strings in a list.
"""

def string_lst(lst):
    return list(map(reverse_string, lst))

def reverse_string(word):
    return word[::-1]

lst = ["hello", "twice"]    
print(string_lst(lst))

"""
Problem: 739
Define a helper function `count_vowels(word)` that counts the number of vowels in a word, and use it to find the word with the most vowels in a list.
"""

def lst_words(lst):
    return max(lst, key=count_vowels)

def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for char in word:
        if char.lower() in vowels:
            count += 1
    return count

lst = ["word", "eerie"]    
print(lst_words(lst))

"""
Problem: 740
Create a program with a helper function `is_palindrome(word)` that checks if a word is a palindrome and uses it to filter a list of words.
"""

def lst_of_word(lst):
    return list(filter(is_palindrome, lst)) 
    
def is_palindrome(word):
    return word == word[::-1]

lst = ["radar", "words", "level", "deed"]
print(lst_of_word(lst))

"""
Problem: 741
Write a program that defines a helper function `calculate_area(radius)` to calculate the area of a circle given its radius, and uses it for a list of radii.
"""

def lst_of_radii(lst):
    return list(map(calculate_area, lst))

def calculate_area(radius):
    return 3.14159 * radius ** 2

lst = [1, 2, 3, 4, 5]
print(lst_of_radii(lst))

"""
Problem: 742
Define a helper function `square(n)` that returns the square of a number, and use it to square each element in a list.
"""

def lst_numbers(lst):
    return list(map(sqaure_number, lst))

def sqaure_number(num):
    return num * num
    
lst = [2, 5, 7]
print(lst_numbers(lst))

"""
Problem: 743
Create a program with a helper function `get_first_n_elements(lst, n)` that returns the first `n` elements of a list, and use it on a sample list.
"""

def get_first_n_elements(lst, num):
    return lst[:num] 

def main():
    lst = [1, 2, 3, 4, 5, 6]
    num = 3
    return get_first_n_elements(lst, num)

print(main()) 

"""
Problem: 744
Write a program that defines a helper function `merge_dicts(dict1, dict2)` that merges two dictionaries, and uses it to combine multiple dictionaries.
"""

def merge_dicts(dict1, dict2):
    return {**dict1, **dict2} 

def combine_dicts(dicts):
    result = {}
    for d in dicts:
        result = merge_dicts(result, d) 
    return result
    
dicts = [
    {'a': 1, 'b': 2},
    {'b': 3, 'c': 4},
    {'d': 5}
]

print(combine_dicts(dicts)) 

"""
Problem: 745
Define a helper function `format_name(first_name, last_name)` that returns a formatted full name, and use it to format a list of names.
"""

def format_name(first_name, last_name):
    return f"{first_name} {last_name}"

def format_names(lst):
    
    def format_pair(name_pair):
        return format_name(name_pair[0], name_pair[1])
    
    return list(map(format_pair, lst))

names = [("John", "Doe"), ("Jane", "Smith"), ("Alice", "Johnson")]
formatted_names = format_names(names)
print(formatted_names)

"""
Problem: 746
Create a program with a helper function `find_gcd(a, b)` that finds the greatest common divisor of two numbers, and use it to find the GCD of a list of pairs.
"""

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_of_pairs(lst):
    def gcd_pair(pair):
        return find_gcd(pair[0], pair[1])
    
    return list(map(gcd_pair, lst))

pairs = [(48, 18), (56, 98), (100, 10)]
gcd_results = gcd_of_pairs(pairs)
print(gcd_results)

"""
Problem: 747
Write a program that defines a helper function `count_occurrences(lst, element)` that counts occurrences of an element in a list, and uses it for a given list.
"""

def lst_elements(lst):
    element = "tree" 
    return count_occurrences(lst, element)
    
def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count
    
lst = ["tree", "tree", "tree", "sand"]
print(lst_elements(lst))

"""
Problem: 748
Define a helper function `sort_list(lst)` that sorts a list and returns the sorted list, and use it to sort several lists.
"""

def lst_words(lst1, lst2):
    return sort_lst(lst1), sort_lst(lst2)


def sort_lst(lst):
    return sorted(lst)


lst1 = ["zebra", "frog", "toad", "anaconda", "baboon"]
lst2 = ["ktm", "Honda", "Suzuki"]
sorted_lists = lst_words(lst1, lst2)
print(sorted_lists)

"""
Problem: 749
Create a program with a helper function `extract_domain(url)` that extracts the domain from a URL, and use it on a list of URLs.
"""

def domain_names(lst):
    return list(map(extract_URL, lst))
        
def extract_URL(url):
    site_name = url.split("//")[1]
    return site_name

lst = [
    "http://google.com",
    "http://facebook.com",
    "http://twitter.com",
    "http://linkedin.com",
    "http://github.com",
    "http://stackoverflow.com",
    "http://youtube.com",
    "http://amazon.com",
    "http://microsoft.com",
    "http://apple.com"
]

print(domain_names(lst))
 
"""
Problem: 750
Write a program that defines a helper function `remove_duplicates(lst)` that removes duplicate elements from a list, and uses it on a sample list.
"""

def lst_sites(lst):
    return remove_duplicates(lst)

    
def remove_duplicates(lst):
    return list(set(lst))
    

lst = [
    "google",
    "facebook",
    "twitter",
    "linkedin",
    "github",
    "stackoverflow",
    "youtube",
    "amazon",
    "microsoft",
    "apple",
    "twitter",
    "google"
]
print(lst_sites(lst))

"""
Problem: 751
Define a helper function `flatten_list(nested_list)` that flattens a nested list, and use it to flatten a list of lists.
"""

def main(lst):
    result = []
    for i in lst:
        for j in i:
            result.append(j)       
    return result

lst  = [["list1", "list2"], ["list3", "list4"]]
print(main(lst))

def lst_of_lists(nested_list):
    return flatten_list(nested_list)

def flatten_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

nested_list = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9],
    [10]
]

print(lst_of_lists(nested_list))

"""
Problem: 752
Create a program with a helper function `is_prime(n)` that checks if a number is prime, and uses it to filter a list of numbers.
"""

def filter_primes(lst):
    return list(filter(is_prime, lst))
    
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(filter_primes(numbers))

"""
Problem: 753
Write a program that defines a helper function `calculate_factorial(n)` that calculates the factorial of a number, and uses it for a range of numbers.
"""

def main(lst):
    def inner(n):
        factorial = 1
        for num in range(1, n + 1):
            factorial *= num
        return factorial
    return list(map(inner, lst))
            
lst = [4,5,6,7]
main(lst)

def lst_of_numbers(lst):
    return list(map(calculate_factorial, lst))

def calculate_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

lst = [2, 4, 7, 8]
print(lst_of_numbers(lst))

"""
Problem: 754
Define a helper function `sort_dict_by_value(d)` that sorts a dictionary by its values, and use it to sort a given dictionary.
"""

def main(dic):
    return sort_dict_by_value(dic)

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=get_value))

def get_value(item):
    return item[1]

dic = {
    "name": 2,
    "age": 5,
    "city": 1,
    "job": 3
}    
print(main(dic))

def main(dic):
    return sort_dict_by_value(dic)

def sort_dict_by_value(d):
    sorted_items = sorted(d.items(), key=get_value)

    result = {}
    for key, value in sorted_items:
        result[key] = value
    return result

dic = {
    "name": 2,
    "age": 5,
    "city": 1,
    "job": 3
}    
print(main(dic))

"""
Problem: 755
Create a program with a helper function `get_unique_elements(lst)` that returns the unique elements of a list, and uses it on a sample list.
"""

def main(lst):
    return get_unique_elements(lst)
    
def get_unique_elements(word):
    return list(set(word))


lst = [
    "apple",
    "banana",
    "orange",
    "apple",
    "grape",
    "banana",
    "kiwi",
    "mango",
    "peach",
    "kiwi",
    "pear"
]
print(main(lst))

"""
Problem: 756
Write a program that defines a helper function `check_anagram(str1, str2)` that checks if two strings are anagrams, and uses it on a list of string pairs.
"""

def main(str1, str2):
    return check_anagram(str1, str2)

def check_anagram(x, y):
    return sorted(x) == sorted(y)

str1 = "evil"
str2 = "vile"
print(main(str1, str2))

"""
Problem: 757
Define a helper function `find_index(lst, element)` that returns the index of an element in a list, and uses it for a given list.
"""
def main(lst1, target1):
    return find_index(lst, target1)
    
    
def find_index(lst, target):
    for index, word in enumerate(lst):
        if word == target:
            return index        
lst = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew"
]
target1 = "date"
print(main(lst1, target1))

"""
Problem: 758
Create a program with a helper function `generate_fibonacci(n)` that generates the first `n` Fibonacci numbers, and uses it to print Fibonacci sequences.
"""

def main(n):
    return generate_fibonacci(n)


def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

n = 10 
print(main(n))

"""
Problem: 759
Write a program that defines a helper function `calculate_average(lst)` that calculates the average of a list, and uses it on multiple lists.
"""

def main(lst1, lst2):
    avg1 = calculate_average(lst1)
    avg2 = calculate_average(lst2)
    return avg1, avg2

def calculate_average(lst):
    length_lst = len(lst)
    total = sum(lst)
    average = total / length_lst
    return average

list1 = [3, 7, 2, 9, 12, 5]
list2 = [14, 6, 8, 11, 3, 10]
print(main(list1, list2))

"""
Problem: 760
Define a helper function `convert_to_kilometers(miles)` that converts miles to kilometers, and uses it to convert a list of distances.
"""

def main(lst):
    return list(map(convert_to_kilometers, lst))

def convert_to_kilometers(miles):
    miles_to_km = 1.60934 
    kilometers = miles * miles_to_km
    return kilometers

lst = [34, 67, 157]
print(main(lst))

"""
Problem: 761
Create a program with a helper function `get_last_n_elements(lst, n)` that returns the last `n` elements of a list, and uses it on a sample list. For example 
lst = [1, 2, 3, 4, 5, 6]
n = 3
result = [1, 2, 3]
"""

def main(lst, n):
    return get_last_n_elements(lst, n)
    
def get_last_n_elements(lst, n):
    return lst[:n] 
       
lst = [1, 2, 3, 4, 5, 6]
n = 3    
print(main(lst, n))

"""
Problem: 762
Write a program that defines a helper function `remove_whitespace(s)` that removes whitespace from a string, and uses it on a list of strings.
"""

def main(string):
    return remove_whitespace(string)

def remove_whitespace(s):
    return s.replace(" ", "")

string = "today I'm going to the shopping centre"
print(main(string))

"""
Problem: 763
Define a helper function `get_positive_numbers(lst)` that returns only the positive numbers from a list, and uses it on a sample list.
"""

def main(lst):
    return list(filter(get_positive_numbers, lst))

def get_positive_numbers(number):
    return number > 0

lst = [1, -2, 2, -3, 3, 4, -4]    
print(main(lst))

"""
Problem: 764
Create a program with a helper function `get_common_elements(lst1, lst2)` that returns common elements between two lists, and uses it on two sample lists.
"""

def get_common_elements(lst1, lst2):
    common_word = []
    for word in lst1:
        if word in lst2:
            common_word.append(word)
    return common_word
  
lst1 = ["tree", "boat", "sea", "dog"]
lst2 = ["boat", "cat", "sea"]
print(get_common_elements(lst1, lst2))

def main(lst1, lst2):
    return get_common_elements(lst1, lst2)

def get_common_elements(x, y):
    duplicates = []
    for item in x:
        if item in y and item not in duplicates:
            duplicates.append(item)
    return duplicates

lst1 = ["tree", "boat", "sea", "dog"]
lst2 = ["boat", "cat", "sea"]
print(main(lst1, lst2))

"""
Problem: 765
Write a program that defines a helper function `check_even_odd(n)` that returns "Even" or "Odd" for a number, and uses it for a list of numbers.
"""

def main(lst):
    return list(map(check_even_odd, lst))

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

lst = [45, 7, 2, 3, 68, 36]
print(main(lst))

def main(lst):
    results = []
    for number in lst:
        results.append(check_even_odd(number))
    return results

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

lst = [45, 7, 2, 3, 68, 36]
print(main(lst))

"""
Problem: 766
Define a helper function `convert_to_uppercase(word)` that converts a word to uppercase, and uses it on a list of words.
"""

def main(lst):
    return list(map(convert_to_uppercase, lst))  

def convert_to_uppercase(word):
    return word.upper()

lst = ["eorl", "sitting", "kong"]
print(main(lst))

"""
Problem: 767
Create a program with a helper function `count_characters(s)` that counts the characters in a string, and uses it on a list of strings.
"""

def main(lst_str):
    return list(map(count_characters, lst_str))  

def count_characters(s):
    return len(s)

lst_str = ["eorl", "sitting", "mountain"]
print(count_characters(lst_str))


def main(lst_str):
    return list(map(count_characters, lst_str))  # Apply count_characters to each string in the list

def count_characters(s):
    return len(s)

lst_str = ["eorl", "sitting", "mountain"]
print(main(lst_str))

"""
Problem: 768
Write a program that defines a helper function `remove_special_characters(s)` that removes special characters from a string, and uses it on a sample list of strings.
"""
def main(lst):
    return list(map(remove_special_characters, lst))  

def remove_special_characters(s):
    s = s.replace('@', '').replace('?', '')
    return s

lst = ["eor?@l", "s@itting?", "@mountain?"] 
print(main(lst))

"""
Problem: 769
Define a helper function `is_substring(s1, s2)` that checks if `s1` is a substring of `s2`, and uses it on a list of string pairs.
"""
def main(lst):
    results = []
    for pair in lst:
        results.append(is_substring(pair[0], pair[1]))
    return results

def is_substring(s1, s2):
    return s1 in s2

lst = [("apple", "pineapple"), ("dog", "doghouse"), ("cat", "concatenate")]
print(main(lst))

"""
Problem: 770
Create a program with a helper function `sum_of_list(lst)` that returns the sum of all numbers in a list, and uses it on a sample list.
"""

def main(lst):
    return sum_of_list(lst)
    
def sum_of_list(n):
    count = 0
    for n in lst:
        count += n
    return count

lst = [2, 2, 2, 2, 2]
print(main(lst))

"""
Problem: 771
Write a program that defines a helper function `get_even_numbers(lst)` that filters and returns even numbers from a list, and uses it on a sample list.
"""

def main(lst):
    return list(filter(get_even_numbers, lst))

def get_even_numbers(n):
    return n % 2 == 0  #

lst = [46, 22, 7, 4, 8, 13]
print(main(lst))

"""
Problem: 772
Define a helper function `merge_sorted_lists(lst1, lst2)` that merges and sorts two lists, and uses it to combine multiple sorted lists.
"""

def main(lst1, lst2):
    return merge_sorted_lists(lst1, lst2)

def merge_sorted_lists(x, y):
    return sorted(x + y)

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]   
print(main(lst1, lst2))

def main(lst1, lst2):
    sort1 = sorted(lst1)
    sort2 = sorted(lst2)
    merge_lst = {*sort1, *sort2}
    return merge_lst
    
lst1 = [1, 33, 8]
lst2 = [9, 2, 7]
main(lst1, lst2)

"""
Problem: 773
Write a Python program to create a dictionary from two lists, one containing keys and the other containing values.
"""

def lst_to_dic(lst1, lst2):
    result = {}
    
    for x, y in zip(lst1, lst2):
        result[x] = y
    return result

lst1 = [1, 2, 3]
lst2 = ["start", "middle", "end"]
print(lst_to_dic(lst1, lst2))

def lst_to_dic(lst1, lst2):
    result = {}
    
    for i in range(len(lst1)):
        result[lst1[i]] = lst2[i]
    return result

lst1 = [1, 2, 3]
lst2 = ["start", "middle", "end"]
print(lst_to_dic(lst1, lst2))

"""
Problem: 774
Write a Python program to get the value of a specific key from a dictionary, or return a default value if the key is not found.
"""

def main(dic, key_to_find):
    return dic.get(key_to_find, None)

dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
key_to_find = "job"
print(main(dic, key_to_find))
key_to_find = "unknown" 
print(main(dic, key_to_find)) 

def value_of_specific_key(dic, target):
    return dic.get(target, "Default value")
    
dic = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "job": "Engineer"
}
target = "age"
print(value_of_specific_key(dic, target))

def value_of_specific_key(dic, target):
    for key, value in dic.items():
        if key == target:
            return value
    return None 
    
dic = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "job": "Engineer"
}
target = "age"
print(value_of_specific_key(dic, target))

"""
Problem: 775
Write a Python program to merge two dictionaries into one.
"""

def main(dic1, dic2):
    merge_dic = dic1.copy()  
    for key, value in dic2.items():
        if key in merge_dic:
            merge_dic[key] = [merge_dic[key], value]
        else:
            merge_dic[key] = value
    return merge_dic

dic1 = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}

dic2 = {
    "name": 2,
    "age": 2,
    "cities": 2,
    "jobless": 2
}

print(main(dic1, dic2))

def merge_dicts(dic1, dic2):
    merged_dict = {**dic1, **dic2}
    return merged_dict

dic1 = {
    "name": "Steven",
    "age": 56,
    "city": "New York",
    "job": "Engineer"
}
dic2 = {
    "named": "Alice",
    "aged": 30,
    "cities": "New York",
    "jobless": "Engineer"
}
print(merge_dicts(dic1, dic2))

"""
Problem: 776
Write a Python program to remove a key from a dictionary.
"""

def remove_key(dic, key_to_remove):
    if key_to_remove in dic:
        del dic[key_to_remove]
    return dic

dic = {
    "name": "Steven",
    "age": 56,
    "city": "New York",
    "job": "Engineer"
}
key_to_remove = "age"
print(remove_key(dic, key_to_remove))

def main(dic, target):
    result = {}
    for key, value in dic.items():
        if key != target:
            result[key] = value
    return result
    
dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
target = "job"
print(main(dic, target))
"""
Problem: 777
Write a Python program to iterate over the keys and values of a dictionary and print them in the format `key: value`.
"""

def print_dict_items(dic):
    for key, value in dic.items():
        print(f"{key}: {value}")

dic = {
    "name": "Steven",
    "age": 56,
    "city": "New York",
    "job": "Engineer"
}
print_dict_items(dic)

def main(dic):
    result = ""
    for key, value in dic.items():
        result += f"{key}: {value}, \n"
    print(result)
        
dic = {"apple": 1, "orange": 33, "mango": 5}
main(dic)

"""
Problem: 778
Write a Python program to check if a given key exists in a dictionary.
"""

def main(dic1):
    if target in dic1.keys():
        return True
    return False
           
dic1 = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
target = "names"
print(main(dic1))

def does_key_exist(dic, target):
    for key in dic.keys():
        if key == target:
            return "key exists" 
    return "key does not exist"

print(does_key_exist({"name": "Steven", "age": 56}, "job"))
print(does_key_exist({"name": "Steven", "age": 56}, "name")) 

"""
Problem: 779
Write a Python program to sort a dictionary by its keys.
"""

def sort_dic(dic):
    return dict(sorted(dic.items()))

dic = {
    "name": "Steven",
    "age": 56,
    "city": "New York",
    "job": "Engineer"
}
print(sort_dic(dic))

"""
Problem: 780
Write a Python program to sort a dictionary by its values.
"""

def main(dic):
    dic = dic.items()

    def sort_value(item):
        return item[1]
        
    return dict(sorted(dic, key=sort_value))
    
         
dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
print(main(dic))

def sort_values(dic):
    sorted_items = sorted(dic.items(), key=sort_key)
    return dict(sorted_items)

def sort_key(item):
    return item[1]

dic = {
    "cat": 34,
    "dog": 56,
    "rabbit": 566,
    "fish": 4
}
print(sort_values(dic))

"""
Problem: 781
Write a Python program to count the frequency of elements in a list and store the result in a dictionary.
"""

def frequency_elements(lst):
    result = {}
    for word in lst:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1   
    return result
    
lst = ["tree", "tree", "flower", "flower"]
print(frequency_elements(lst))

"""
Problem: 782
Write a Python program to create a dictionary where the keys are numbers from 1 to 5, and the values are the squares of the keys.
"""

def square_dic():
    result = {}
    for key in range(1, 6):
        result[key] = key ** 2
    return result
        
print(square_dic())

"""
Problem: 783
Write a Python program to update the value of an existing key in a dictionary.
"""

def main(dic, target):
    key_to_update, new_value = target
    if key_to_update in dic:
        dic[key_to_update] = new_value
    return dic

dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
target = ("city", 78)
print(main(dic, target))


def update_value(dic, key, new_value):
    if key in dic:
        dic[key] = new_value
    return dic

dic = {
    "name": "Steven",
    "age": 56,
    "city": "New York",
    "job": "Engineer"
}

update_value(dic, "age", 60)
print(dic)

"""
Problem: 784
Write a Python program to get all the keys from a dictionary.
"""

def get_keys(dic):
    return dic.keys()

dic = {
    "name": "Steven",
    "age": 56,
    "city": "New York",
    "job": "Engineer"
}
print(get_keys(dic))

def main(dic):
    for key in dic:
        print(key)
        
dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
print(main(dic)) 

"""
Problem: 785
Write a Python program to get all the values from a dictionary.
"""

def get_keys(dic):
    return dic.values()

dic = {
    "name": "Steven",
    "age": 56,
    "city": "New York",
    "job": "Engineer"
}
print(get_keys(dic))

"""
Problem: 786
Write a Python program to get all the values from a dictionary.
"""

def get_keys(dic):
    return dic.values()

dic = {
    "name": "Steven",
    "age": 56,
    "city": "New York",
    "job": "Engineer"
}
print(get_keys(dic))

"""
Problem: 787
Write a Python program to find the key with the largest value in a dictionary.
"""

def largest_value(dic):
    return max(dic.values())

dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
print(largest_value(dic))

"""
Problem: 788
Write a Python program to find the key with the smallest value in a dictionary.
"""

def largest_value(dic):
    return min(dic.values())

dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
print(largest_value(dic))

"""
Problem: 789
Write a Python program to convert two lists into a dictionary, where one list contains keys and the other contains values, but skip values if the lists are of unequal length.
"""

def lst_dic(lst1, lst2):
    result = {}
    min_length = min(len(lst1), len(lst2))
    
    for i in range(min_length):
        result[lst1[i]] = lst2[i]
    
    return result

lst1 = [1, 2, 3]
lst2 = ["sand", "rock", "beach", "sea"]
print(lst_dic(lst1, lst2))

"""
Problem: 790
Write a Python program to combine two dictionaries by adding values of common keys.
"""

def combine_dictionaries(dic1, dic2):
    result = {}
    for key in dic1:
        result[key] = dic1[key]
    for key, value in dic2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

dic1 = {
    "a": 1,
    "b": 2,
    "c": 3
}

dic2 = {
    "b": 3,
    "c": 4,
    "d": 5
}
print(combine_dictionaries(dic1, dic2))

def combine_dictionaries(dic1, dic2):
    result = dic1.copy()
    for key, value in dic2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

dic1 = {
    "a": 1,
    "b": 2,
    "c": 3
}

dic2 = {
    "b": 3,
    "c": 4,
    "d": 5
}
print(combine_dictionaries(dic1, dic2))

"""
Problem: 791
Write a Python program to invert the keys and values of a dictionary (i.e., make the keys the values and the values the keys).
"""

def invert_dictionary(dic):
    inverted = {}
    for key, value in dic.items():
        inverted[value] = key
    return inverted

dic = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(invert_dictionary(dic))

"""
Problem: 792
Write a Python program to remove duplicate values from a dictionary.
"""

def remove_duplicates_values(dic):
    unique_values = {}
    for key, value in dic.items():
        if value not in unique_values.values():
            unique_values[key] = value
    return unique_values

dic = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "job": "Engineer",
    "nickname": "Alice" 
}
print(remove_duplicates_values(dic))

"""
Problem: 793
Write a Python program to check if two dictionaries have the same keys.
"""

def same_keys(dic1, dic2):
    return dic1.keys() == dic2.keys()

dic1 = {
    "name": "Alice",
    "ages": 30,
    "cities": "New York",
    "job": "Engineer",
    "nickname": "Alice" 
}

dic2 = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "job": "Engineer",
    "nickname": "Alice" 
}
print(same_keys(dic1, dic2))

"""
Problem: 794
Write a Python program to multiply all the values in a dictionary by 2.
"""

def multiply_by2(dic):
    result = {}
    for key, value in dic.items():
        result[key] = value * 2 
    return result
    
dic = {"a": 2, "b": 8}    
print(multiply_by2(dic))

"""
Problem: 795
Write a Python program to find the length (i.e., number of key-value pairs) of a dictionary.
"""

def len_key_value_pair(dic):
    return len(dic)

dic = {
    "name": "Alice",
    "ages": "stop",
    "cities": "New York",
    "job": "Engineer",
    "nickname": "Alice" 
}
print(len_key_value_pair(dic))

"""
Problem: 796
Write a Python program to map a list of strings to their lengths using a dictionary.
"""

def map_lst_string_dic(lst):
    result = {}
    for word in lst:
        result[word] = len(word)
    return result

lst = ["it", "shop", "jonny"]
print(map_lst_string_dic(lst))

def len_dic(lst):
    result = {}
    for word in lst:
        count = 0
        for char in word:
            count += 1
        result[word] = count
    return result
    

lst = ["not", "house", "Jonathan"]
print(len_dic(lst))

"""
Problem: 797
Write a Python program to add a new key-value pair to an existing dictionary.
"""

def add_key_value_pair(dic):
    dic["new_key"] = "new_value"
    return dic
    
dic = {
    "name": "Alice",
    "ages": "stop",
    "cities": "New York",
    "job": "Engineer",
    "nickname": "Alice" 
}
print(add_key_value_pair(dic))

"""
Problem: 798
Write a Python program to create a dictionary with keys as numbers from 1 to 10 and values as their cubes.
"""

def value_cubes():
    result = {}
    for num in range(1, 6):
        result[num] = num ** 3
    return result
    
print(value_cubes())

"""
Problem: 799
Write a Python program to check if a dictionary is empty.
"""

def check_if_empty(dic):
    if not dic: 
        return "Dictionary is empty"
    return "Dictionary is not empty"

dic = {
    "name": "Alice",
    "ages": "stop",
    "cities": "New York",
    "job": "Engineer",
    "nickname": "Alice" 
}
print(check_if_empty(dic))

"""
Problem: 800
Write a Python program to remove a set of keys from a dictionary.
"""

def remove_set_keys(dic, keys_to_remove):
    result = {}
    for key, value in dic.items():
        if key not in keys_to_remove:
            result[key] = value
    return result

dic = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "job": "Engineer",
    "nickname": "Alice"
}
keys_to_remove = {"age", "city"}
print(remove_set_keys(dic, keys_to_remove))

"""
Problem: 801
Write a Python program to convert a dictionary into a list of tuples, where each tuple contains a key-value pair.
"""

def dic_lst_tuples(dic):
    return list(dic.items())
    
dic = {
    "name": "Alice",
    "ages": "stop",
    "cities": "New York",
    "job": "Engineer",
    "nickname": "Alice" 
}
print(dic_lst_tuples(dic))

"""
Problem: 802
Write a Python program to find all keys in a dictionary that map to a given value.
"""

def main(dic):
    result = {}
    
    for key, value in dic.items():
        if value == 1:
            result[key] = value
    return tuple(result.keys())
    
dic = {
    "name": 1,
    "age": 56,
    "city": 34,
    "job": 1
}
print(main(dic))

def map_value(dic, target_value):
    result = {}
    for key, value in dic.items():
        if value == target_value:
            result[key] = value
    return result

dic = {
    "name": "Alice",
    "ages": "Alice",
    "cities": "New York",
    "job": "Engineer",
    "nickname": "Alice" 
}
target_value = "Alice"
print(map_value(dic, target_value))

"""
Problem: 803
Write a Python program to replace the value of a key in a dictionary with a list of values if the value is not already a list.
"""

def replace_value(dic, list_values):
    for key in dic:
        if not isinstance(dic[key], list):
            dic[key] = list_values
    return dic

dic = {
    "name": "Alice",
    "ages": "Alice",
    "cities": "New York",
    "job": "Engineer",
    "nickname": "Alice" 
}
list_values = ["one", "two", "three", "four", "five"]
print(replace_value(dic, list_values))

"""
Problem: 804
Write a Python program to create a nested dictionary where keys are numbers and values are dictionaries containing the squares and cubes of the keys.
"""

def nested_dic():
    result = {}
    for key in range(1, 6):
        result[key] = {'square': key ** 2, 'cube': key ** 3}
    return result

print(nested_dic())

def nested_dic():
    result = {}
    for key in range(1, 6):
        result[key] = {'square': key ** 2, 'cube': key ** 3}
    return result

result = nested_dic()
for key, value in result.items():
    print(f"{key}: {value}")

"""
Problem: 805
Write a Python program to create a dictionary from a string where the keys are characters and the values are the number of occurrences of each character.
"""

def string_dic(string):
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

string = "what's happening today?"
print(string_dic(string))

#new line
def string_dic(string):
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

string = "what's happening today?"
result = string_dic(string)

for key, value in result.items():
    print(f"{key}: {value}")

#sort keys    
def string_dic(string):
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

string = "what's happening today?"
result = string_dic(string)

for key in sorted(result):
    print(f"{key}: {result[key]}")


"""
Problem: 806
Write a Python program to sort a dictionary by its values in descending order.
"""

def sort_dic(dic):
    
    def value_sort(item):
        return item[1]
    
    return dict(sorted(dic.items(), key=value_sort, reverse=True))

dic = {
    "name": "Alice",
    "ages": "Alice",
    "cities": "New York",
    "job": "Engineer",
    "nickname": "Alice"
}
print(sort_dic(dic))

"""
Problem: 807
Write a Python program to create a dictionary from a list of tuples.
"""

def lst_tuples(lst):
    return dict(lst)

lst = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]
print(lst_tuples(lst))

"""
Problem: 808
Write a Python program to filter out keys from a dictionary that have a value less than 10.
"""


    
def less_then_10(dic):
    result = {}
    for key, value in dic.items():
        if value >= 10:
            result[key] = value
    return result
    
dic = {
    "name": 3,
    "ages": 6,
    "cities": 46,
    "job": 12,
    "nickname": 7 
}
print(less_then_10(dic))

"""
Problem: 809
Write a Python program to print the dictionary in a readable, formatted way (pretty printing).
"""

def print_readable(dic):
    result = ""
    for key, value in dic.items():
        result += f"{key}: {value}\n"
    return result

dic = {
    "name": 3,
    "ages": 6,
    "cities": 46,
    "job": 12,
    "nickname": 7 
}
print(print_readable(dic))

"""
Problem: 810
Write a Python program to create a dictionary of students and their grades, and print all students who scored more than 75.
"""

def students_grades(dic):
    result = {}
    for key, value in dic.items():
        if value >= 70:
            result[key] = value
    return list(result)
    
dic = {
    "Bob": 50,
    "Alex": 72,
    "Fred": 87,
    "Mike": 60,
    "Liz": 90 
}
print(students_grades(dic))

"""
Problem: 811
Write a Python program to create a dictionary of words and their lengths from a given sentence.
"""

def word_len(string):
    words = string.split()
    result = {}
    for word in words:
        result[word] = len(word)
    return result

string = "today we are going to the beach"
print(word_len(string))

"""
Problem: 812
Write a Python program to create a dictionary of words and their lengths from a given sentence.
"""

def word_len(string):
    words = string.split()
    result = {}
    for word in words:
        result[word] = len(word)
    return result

string = "today we are going to the beach"
print(word_len(string))

"""
Problem: 813
Write a Python program to group words in a dictionary based on their starting letter.
"""

def starting_letter(dic):
    result = {}
    for key in dic.keys():
        first_letter = key[0]
        if first_letter not in result:
            result[first_letter] = []
        result[first_letter].append(key)
    return result

dic = {
    "Bob": 50,
    "Alex": 72,
    "Fred": 87,
    "Mike": 60,
    "Liz": 90 
}
print(starting_letter(dic))

def main(dic):
    result = {}
    for key, value in dic.items():
        first_letter = key[0]
        result[first_letter] = key
    return result
    

dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
print(main(dic))

"""
Problem: 814
Write a Python program to iterate through a dictionary and change the case of all keys (upper or lower).
"""

def upper_keys(dic):
    result = {}
    for key, value in dic.items():
        result[key.upper()] = value
    return result
    
dic = {
    "Bob": 50,
    "Alex": 72,
    "Fred": 87,
    "Mike": 60,
    "Liz": 90 
}
print(upper_keys(dic))

"""
Problem: 815
Write a Python program to find the intersection of two dictionaries (i.e., keys that are common in both dictionaries).
"""

def intersection(dic1, dic2):
    result = {}
    for key in dic1:
        if key in dic2:
            result[key] = dic1[key]
    return result

dic1 = {
    "Bob": 500,
    "Alex": 72,
    "Fred": 89,
    "Mike": 61,
    "Liz": 90 
}

dic2 = {
    "Bob": 50,
    "Alexander": 72,
    "Freddy": 87,
    "Zac": 60,
    "Liz": 90 
}
print(intersection(dic1, dic2))

"""
Problem: 816
Write a Python program to count how many times each vowel occurs in a given sentence using a dictionary.
"""

def count_vowels(string):
    vowels = "aeiou"
    result = {}
    
    for vowel in vowels:
        result[vowel] = 0
    
    for char in string.lower():
        if char in vowels:
            result[char] += 1
    
    return result

string = "word how many times vowels? How many times many times many"
print(count_vowels(string))

"""
Problem: 817
Write a Python program to remove all key-value pairs from a dictionary where the value is None.
"""

def remove_value_is_none(dic):
    result = {}
    for key, value in dic.items():
        if value is not None:
            result[key] = value
    return result

dic1 = {
    "Bob": None,
    "Alex": None,
    "Fred": 89,
    "Mike": 61,
    "Liz": 90 
}
print(remove_value_is_none(dic1))

"""
Problem: 818
Write a Python program to check if a dictionary contains a specific key and value pair.
"""

def check_key_value(dic, target):
    for key, value in dic.items():
        if key in target and dic[key] == target[key]:
            return True
    return False

dic1 = {
    "Bob": 500,
    "Alex": 72,
    "Fred": 89,
    "Mike": 61,
    "Liz": 90 
}
target = {"Liz": 90}
print(check_key_value(dic1, target))

"""
Problem: 819
Write a Python program to convert a dictionary to JSON format using `json.dumps()`.
"""

import json

def dict_to_json(dic):
    return json.dumps(dic)

dic1 = {
    "Bob": 500,
    "Alex": 72,
    "Fred": 89,
    "Mike": 61,
    "Liz": 90
}
print(dict_to_json(dic1))

"""
Problem: 820
Write a Python program to merge multiple dictionaries into one.
"""

def merge_dicts(dic1, dic2):
    merged_dict = {**dic1, **dic2}
    return merged_dict

dic1 = {
    "name": "Steven",
    "age": 56,
    "city": "New York",
    "job": "Engineer"
}
dic2 = {
    "named": "Alice",
    "aged": 30,
    "cities": "New York",
    "jobless": "Engineer"
}
print(merge_dicts(dic1, dic2))

"""
Problem: 821
Write a Python program to iterate through a dictionary and calculate the product of all its values.
"""

def product_values(dic):
    product = 1
    for value in dic.values():
        product *= value
    return product

dic = {
    "named": 2,
    "aged": 2,
    "cities": 2,
    "jobless": 2
}
print(product_values(dic))

"""
Problem: 822
Write a Python program to calculate the average of all values in a dictionary.
"""

def average_values(dic):
    sum_values = sum(dic.values())
    len_values = len(dic)
    average = sum_values / len_values
    return average

dic = {
    "named": 200,
    "aged": 257,
    "cities": 230,
    "jobless": 280
}
print(average_values(dic))

"""
Problem: 823
Write a Python program to swap the values of two keys in a dictionary.
"""

def main(dic):
    dic["city"] = 1
    dic["job"] = 34
    return dic
        
dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
target = ("city", "job")
print(main(dic))

def main(dic, x, y):
    result = {}
    reverse_values = dic[x], dic[y] = dic[y], dic[x]

    for key, value in dic.items():
        if reverse_values not in result:
            result[key] = value
    return result
        
dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
print(main(dic, "name", "job"))

def main(dic, change_keys):
    result = {}
    change_keys = dic["name"], dic["job"] = dic["job"], dic["name"]

    for key, value in dic.items():
        if change_keys not in result:
            result[key] = value
    return result
        
dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
change_keys = {"name", "job"}
print(main(dic, change_keys))

def swap_values(dic, key1, key2):
    dic[key1], dic[key2] = dic[key2], dic[key1]
    return dic

dic = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(swap_values(dic, "a", "c"))

"""
Problem: 824
Write a Python program to find the key with the largest value in a dictionary. Do not use max().
"""

def largest_value(dic):
    largest_key = None
    largest_val = float('-inf')
    
    for key, value in dic.items():
        if value > largest_val:
            largest_val = value
            largest_key = key
    
    return largest_key

dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
print(largest_value(dic))

"""
Problem: 825
Write a Python program to find the key with the largest value in a dictionary. Do not use min().
"""

def smallest_value(dic):
    smallest_key = None
    smallest_val = float('inf')
    
    for key, value in dic.items():
        if value < smallest_val:
            smallest_val = value
            smallest_key = key
    
    return smallest_key

dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
print(smallest_value(dic))

"""
Problem: 826
Write a Python program to add multiple new key-value pair to an existing dictionary.
"""

def main(dic):
    dic["first"] = 1
    dic["second"] = 2
    return dic
    

dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
print(main(dic))


def add_multiple_pairs(dic, new_pairs):
    dic.update(new_pairs)
    return dic

dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}

new_pairs = {
    "status": "unemployed",
    "country": "USA",
    "hobby": "coding"
}

print(add_multiple_pairs(dic, new_pairs))

"""
Problem: 827
Write a Python program that prints numbers from 1 to 10 using a while loop.
"""

i = 1
while i <= 10:
    print(i)
    i += 1

"""
Problem: 828
Write a Python program that prints even numbers between 1 and 20 using a while loop.
"""

i = 2
while i <= 20:
    print(i)
    i += 2

"""
Problem: 829
Write a Python program to print all the numbers from 10 to 1 (in reverse order) using a while loop.
"""

i = 10
while i >= 1:
    print(i)
    i -= 1

"""
Problem: 830
Write a Python program that asks the user for a number and keeps printing “Hello” that many times using a while loop.
"""

count = int(input("Enter a number: "))
i = 0
while i < count:
    print("Hello")
    i += 1

"""
Problem: 831
Write a Python program that keeps asking the user for input until they type “exit”.
"""

user_input = ""
while user_input != "exit":
    user_input = input("Enter something (type 'exit' to stop): ")

"""
Problem: 831
Write a Python program to sum all numbers from 1 to 100 using a while loop.
"""

i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print(total)

"""
Problem: 832
Write a Python program that keeps doubling a number (starting from 1) until it exceeds 1000 using a while loop.
"""

number = 1
while number <= 1000:
    print(number)
    number *= 2

"""
Problem: 833
Write a Python program that prints the multiplication table of 5 using a while loop.
"""

i = 1
while i <= 10:
    print(5 * i)
    i += 1

"""
Problem: 834
Write a Python program that asks the user for numbers and stops when the sum exceeds 50 using a while loop.
"""

total = 0
while total <= 50:
    number = int(input("Enter a number: "))
    total += number
print(total)

"""
Problem: 835
Write a Python program that keeps asking the user for input until they enter an even number using a while loop.
"""

number = 1
while number % 2 != 0:
    number = int(input("Enter an even number: "))

"""
Problem: 836
Write a Python program that asks the user to input numbers, and prints the sum when they input the number 0 using a while loop.
"""

total = 0
number = None
while number != 0:
    number = int(input("Enter a number (0 to stop): "))
    total += number
print(total)

"""
Problem: 837
Write a Python program that prints the Fibonacci sequence up to the 10th number using a while loop.
"""

a, b = 0, 1
i = 0
while i < 10:
    print(a)
    a, b = b, a + b
    i += 1

"""
Problem: 838
Write a Python program that keeps asking the user to guess a secret number between 1 and 10 until they guess it correctly using a while loop.
"""

secret_number = 7
guess = 0
while guess != secret_number:
    guess = int(input("Guess the secret number (between 1 and 10): "))

"""
Problem: 839
Write a Python program that counts the number of vowels in a user-provided string using a while loop.
"""

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
i = 0
count = 0
while i < len(string):
    if string[i] in vowels:
        count += 1
    i += 1
print(count)

"""
Problem: 840
Write a Python program that asks the user to input a string and keeps removing the last character of the string until it’s empty using a while loop.
"""

string = input("Enter a string: ")
while string:
    print(string)
    string = string[:-1]

"""
Problem: 841
Write a Python program to count down from a user-provided number to 0 using a while loop.
"""

number = int(input("Enter a number: "))
while number >= 0:
    print(number)
    number -= 1

"""
Problem: 842
Write a Python program to keep asking the user for positive numbers and print the sum when a negative number is entered using a while loop.
"""

total = 0
num = int(input("Enter a positive number: "))
while num >= 0:
    total += num
    num = int(input("Enter another number: "))
print(total)

"""
Problem: 843
Write a Python program that asks the user to input numbers and finds the largest number entered using a while loop. Stop when the user types “stop”
"""

largest = float('-inf')
while True:
    user_input = input("Enter a number (type 'stop' to end): ")
    if user_input == "stop":
        break
    num = int(user_input)
    if num > largest:
        largest = num
print(largest)

"""
Problem: 844
Write a Python program that asks the user for a password and keeps asking until the correct password (“python”) is entered using a while loop.
"""

password = ""
while password != "python":
    password = input("Enter the password: ")

"""
Problem: 845
Write a Python program that multiplies a number by itself until it exceeds 10,000 using a while loop.
"""

num = 2
while num <= 10000:
    print(num)
    num *= num

"""
Problem: 846
Write a Python program to reverse the digits of a number using a while loop.
"""

num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

"""
Problem: 847
Write a Python program that asks the user to input numbers and prints the average when they type “done” using a while loop.
"""

total = 0
count = 0
while True:
    user_input = input("Enter a number (type 'done' to end): ")
    if user_input == "done":
        break
    total += int(user_input)
    count += 1
if count != 0:
    print(total / count)

"""
Problem: 848
Write a Python program that asks the user to input a positive number and keeps subtracting 1 until it reaches zero using a while loop.
"""

num = int(input("Enter a positive number: "))
while num > 0:
    print(num)
    num -= 1

"""
Problem: 849
Write a Python program that generates random numbers between 1 and 100 and stops when it generates a number divisible by 7 using a while loop.
"""

import random
num = random.randint(1, 100)
while num % 7 != 0:
    print(num)
    num = random.randint(1, 100)

"""
Problem: 850
Write a Python program to keep asking the user for a number and print whether it is prime or not. Stop when the user types “exit”.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    user_input = input("Enter a number (type 'exit' to stop): ")
    if user_input == "exit":
        break
    num = int(user_input)
    if is_prime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

"""
Problem: 851
Write a Python program that prints all the letters of a string except the vowels using a while loop.
"""

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
i = 0
while i < len(string):
    if string[i] not in vowels:
        print(string[i], end="")
    i += 1
"""
Problem: 852
Write a Python program to count the number of digits in a number using a while loop.
"""

num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print(count)

"""
Problem: 853
Write a Python program to keep adding numbers to a list until the list contains 10 elements using a while loop.
"""

lst = []
while len(lst) < 10:
    lst.append(int(input("Enter a number: ")))
print(lst)

"""
Problem: 854
Write a Python program that keeps dividing a number by 2 until it is smaller than 1 using a while loop.
"""

num = int(input("Enter a number: "))
while num >= 1:
    print(num)
    num /= 2

"""
Problem: 855
Write a Python program that keeps asking the user for input and adds it to a list until the user types “stop”. Then print the list using a while loop.
"""

lst = []
while True:
    user_input = input("Enter something (type 'stop' to end): ")
    if user_input == "stop":
        break
    lst.append(user_input)
print(lst)

"""
Problem: 856
Write a Python program that asks the user for a number and keeps printing its square until the square exceeds 1000 using a while loop.
"""

num = int(input("Enter a number: "))
while num ** 2 <= 1000:
    print(num ** 2)
    num += 1

"""
Problem: 857
Write a Python program that prints all the numbers from 1 to 50, skipping multiples of 3, using a while loop.
"""

num = 1
while num <= 50:
    if num % 3 != 0:
        print(num)
    num += 1

"""
Problem: 858
Write a Python program that keeps adding 5 to a number starting from 0 until the number is greater than 100 using a while loop.
"""

num = 0
while num <= 100:
    print(num)
    num += 5

"""
Problem: 859
Write a Python program that prints all the elements of a list using a while loop.
"""

lst = [1, 2, 3, 4, 5]
i = 0
while i < len(lst):
    print(lst[i])
    i += 1

"""
Problem: 860
Write a Python program to sum all the odd numbers from 1 to 100 using a while loop.
"""

num = 1
total = 0
while num <= 100:
    if num % 2 != 0:
        total += num
    num += 1
print(total)

"""
Problem: 861
Write a Python program that keeps doubling a number (starting from 2) and prints how many times it doubled before exceeding 1000 using a while loop.
"""

num = 2
count = 0
while num <= 1000:
    num *= 2
    count += 1
print(count)

"""
Problem: 862
Write a Python program that keeps asking the user for a number and prints whether it is a palindrome. Stop when the user types “quit”.
"""

user = None
while user != "quit":
    user = input("type num: ")
    if user == user[::-1]:
        print("palindrome")

while True:
    user_input = input("Enter a number (type 'quit' to stop): ")
    if user_input == "quit":
        break
    if user_input == user_input[::-1]:
        print(f"{user_input} is a palindrome")
    else:
        print(f"{user_input} is not a palindrome")

"""
Problem: 863
Write a Python program that simulates a countdown timer by printing the numbers from 10 to 1, and then “Lift off!” using a while loop.
"""

num = 10
while num > 0:
    print(num)
    num -= 1
print("Lift off!")

"""
Problem: 864
Write a Python program that keeps asking the user for a string and prints its length until the user types “exit”.
"""

while True:
    user_input = input("Enter a string (type 'exit' to stop): ")
    if user_input == "exit":
        break
    print(len(user_input))

"""
Problem: 865
Write a Python program that asks the user to input 5 numbers and calculates their product using a while loop.
"""

i = 0
product = 1
while i < 5:
    num = int(input("Enter a number: "))
    product *= num
    i += 1
print(product)

"""
Problem: 866
Write a Python program to create a dictionary from two lists, one containing keys and the other containing values. Use zip()
"""

def main(lst1, lst2):
    result = {}
    for x, y in zip(lst1, lst2):
        result[x] = y
    return result
    
lst1 = [1, 3, 8]
lst2 = ["9", "2", "7"]
main(lst1, lst2)

"""
Problem: 867
Write a Python program to create a dictionary from two lists, one containing keys and the other containing values. Do not use zip().
"""

def create_dictionary(keys, values):

    dictionary = {}
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]
    return dictionary

keys = ["apple", "banana", "cherry"]
values = [1, 2, 3]

result = create_dictionary(keys, values)
print(result)  

"""
Problem: 868
Write a Python program that defines a function `capitalize_words()` which contains a nested function `capitalize()` that capitalizes a word. The `capitalize_words()` function should return a list with each word capitalized.
"""

def capitalize_words(lst):
    def capitalize(name):
        return name.capitalize()
    return list(map(capitalize, lst))

lst = ["jonathan", "sam", "mimi"]
capitalize_words(lst)

"""
Problem: 869
Write a Python program to unpack a list of three elements into three variables.
"""

numbers = [1, 2, 3]
a, b, c = numbers
print(a, b, c)  # Expected output: 1 2 3


"""
Problem: 870
Write a Python program to unpack the first and last elements of a list while collecting the middle elements in another variable.
"""

numbers = [10, 20, 30, 40, 50]
first, *middle, last = numbers
print(first, middle, last)  # Expected output: 10 [20, 30, 40] 50


"""
Problem: 871
Write a Python program to swap two variables using unpacking.
"""

x, y = 5, 10
x, y = y, x
print(x, y)  # Expected output: 10 5


"""
Problem: 872
Write a Python program to unpack the keys and values of a dictionary.
"""

data = {"name": "Alice", "age": 25, "city": "New York"}
keys, values = zip(*data.items())
print(keys, values)  # Expected output: ('name', 'age', 'city') ('Alice', 25, 'New York')


"""
Problem: 873
Write a Python program to assign multiple return values from a function to separate variables using unpacking.
"""

def get_coordinates():
    return (5, 10)

x, y = get_coordinates()
print(x, y)  # Expected output: 5 10


"""
Problem: 874
Write a Python program to extract the first two characters and the rest of a string using unpacking.
"""

word = "Python"
first, second, *rest = word
print(first, second, "".join(rest))  # Expected output: P y thon


"""
Problem: 875
Write a Python program to extract the first and last elements of a tuple using unpacking.
"""

values = (100, 200, 300, 400, 500)
first, *_, last = values
print(first, last)  # Expected output: 100 500


"""
Problem: 876
Write a Python program to unpack a nested list into separate variables.
"""

nested_list = [[1, 2], [3, 4]]
(a, b), (c, d) = nested_list
print(a, b, c, d)  # Expected output: 1 2 3 4


"""
Problem: 877
Write a Python program to unpack a range into separate variables.
"""

a, b, c = range(3)
print(a, b, c)  # Expected output: 0 1 2


"""
Problem: 878
Write a Python program to split a full name into first and last name using unpacking.
"""

full_name = "John Doe"
first_name, last_name = full_name.split()
print(first_name, last_name)  # Expected output: John Doe


"""
Problem: 879
Write a Python program to assign function arguments using unpacking.
"""

def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

person = ("Alice", 30)
greet(*person)  # Expected output: Hello, Alice. You are 30 years old.


"""
Problem: 880
Write a Python program to merge two lists using unpacking.
"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = [*list1, *list2]
print(merged)  # Expected output: [1, 2, 3, 4, 5, 6]


"""
Problem: 881
Write a Python program to merge two dictionaries using unpacking.
"""

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Expected output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


"""
Problem: 882
Write a Python program to unpack and ignore certain values using `_`.
"""

values = (1, 2, 3, 4, 5)
first, _, third, _, last = values
print(first, third, last)  # Expected output: 1 3 5


"""
Problem: 883
Write a Python program to unpack a list into positional function arguments.
"""

def add(a, b, c):
    return a + b + c

numbers = [2, 4, 6]
result = add(*numbers)
print(result)  # Expected output: 12


"""
Problem: 884
Write a Python program to unpack a dictionary into keyword function arguments.
"""

def describe(name, age, city):
    return f"{name} is {age} years old and lives in {city}."

person = {"name": "Emma", "age": 28, "city": "London"}
print(describe(**person))  # Expected output: Emma is 28 years old and lives in London.


"""
Problem: 885
Write a Python program to extract individual characters from a string using unpacking.
"""

word = "ABC"
a, b, c = word
print(a, b, c)  # Expected output: A B C


"""
Problem: 886
Write a Python program to unpack a list with unknown length using the starred expression.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, *middle, last = numbers
print(first, middle, last)  # Expected output: 1 [2, 3, 4, 5, 6, 7, 8] 9


"""
Problem: 887
Write a Python program to use unpacking inside a loop to iterate through a list of tuples.
"""

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
for number, letter in pairs:
    print(number, letter)

# Expected output:
# 1 a
# 2 b
# 3 c


"""
Problem: 888
Write a Python program to unpack a tuple returned from a function.
"""

def get_user():
    return "Alice", 25

name, age = get_user()
print(name, age)  # Expected output: Alice 25

"""
Problem: 888
Write a Python program to unpack a list of lists and sum corresponding elements using the `zip()` function.
"""

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
summed = [sum(x) for x in zip(*lists)]
print(summed)  # Expected output: [12, 15, 18]


"""
Problem: 889
Write a Python program to unpack a list of lists and sum corresponding elements using the `zip()` function. Use list comprehension.
"""

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
summed = [sum(x) for x in zip(*lists)]
print(summed)  # Expected output: [12, 15, 18]


"""
Problem: 890
Write a Python program to unpack a dictionary’s items and reformat them as key-value pairs.
"""

data = {"name": "Alice", "age": 25, "city": "New York"}
formatted = [f"{key}: {value}" for key, value in data.items()]
print(formatted)  # Expected output: ['name: Alice', 'age: 25', 'city: New York']


"""
Problem: 891
Write a Python program to use unpacking to split a sentence into words and capture the first and last words separately.
"""

sentence = "Python is a powerful programming language"
first, *middle, last = sentence.split()
print(first, middle, last)  # Expected output: Python ['is', 'a', 'powerful', 'programming'] language


"""
Problem: 892
Write a Python program to unpack only the vowels from a given word using list comprehension.
"""

word = "unpacking"
vowels = [c for c in word if c in "aeiou"]
print(vowels)  # Expected output: ['u', 'a', 'i']


"""
Problem: 893
Write a Python program to unpack a tuple containing mixed data types.
"""

data = ("Alice", 30, 5.8, True)
name, age, height, is_student = data
print(name, age, height, is_student)  # Expected output: Alice 30 5.8 True


"""
Problem: 894
Write a Python program to unpack and sort a list of tuples by the second element.
"""

tuples = [(1, 3), (4, 1), (2, 2)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)  # Expected output: [(4, 1), (2, 2), (1, 3)]


"""
Problem: 895
Write a Python program to extract only even numbers from a list using unpacking inside list comprehension.
"""

numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # Expected output: [2, 4, 6]


"""
Problem: 896
Write a Python program to swap three variables using unpacking.
"""

a, b, c = 1, 2, 3
a, b, c = c, a, b
print(a, b, c)  # Expected output: 3 1 2


"""
Problem: 897
Write a Python program to unpack a range of numbers into three variables and collect the remaining in another variable.
"""

first, second, *remaining = range(10)
print(first, second, remaining)  # Expected output: 0 1 [2, 3, 4, 5, 6, 7, 8, 9]


"""
Problem: 898
Write a Python program to use unpacking inside a lambda function to add three numbers.
"""

add_three = lambda x, y, z: x + y + z
numbers = (4, 5, 6)
print(add_three(*numbers))  # Expected output: 15


"""
Problem: 899
Write a Python program to extract and reverse the digits of a number using unpacking.
"""

num = 12345
digits = list(str(num))
reversed_digits = digits[::-1]
print(reversed_digits)  # Expected output: ['5', '4', '3', '2', '1']

num = 123456
str_num = str(num)[::-1]
lst_num = list(str_num)
print(lst_num)

"""
Problem: 900
Write a Python program to use unpacking in a function that returns the minimum and maximum of a list.
"""

def min_max(lst):
    return min(lst), max(lst)

numbers = [4, 1, 7, 9, 2]
minimum, maximum = min_max(numbers)
print(minimum, maximum)  # Expected output: 1 9


"""
Problem: 901
Write a Python program to unpack a list of tuples and extract the first elements using list comprehension.
"""

tuples = [(10, "a"), (20, "b"), (30, "c")]
first_elements = [x for x, _ in tuples]
print(first_elements)  # Expected output: [10, 20, 30]


"""
Problem: 902
Write a Python program to unpack a list of dictionaries and extract all the values under a specific key.
"""

def main(lst_dic):
    ages = [value["age"] for value in lst_dic]
    return ages
    
lst_dic = [{"name": "jon", "age": 55}, {"name": "sam", "age": 8}]
main(lst_dic)

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
]

ages = [person["age"] for person in people]
print(ages)  # Expected output: [25, 30, 35]


"""
Problem: 903
Write a Python program to use unpacking to separate numbers in a mathematical expression.
"""

expression = "3 + 5 - 2 * 4"
a, op1, b, op2, c, op3, d = expression.split()
print(a, op1, b, op2, c, op3, d)  # Expected output: 3 + 5 - 2 * 4


"""
Problem: 904
Write a Python program to unpack and reassign dictionary values dynamically.
"""

data = {"x": 10, "y": 20, "z": 30}
x, y, z = data.values()
x, y, z = z, x, y
print(x, y, z)  # Expected output: 30 10 20


"""
Problem: 905
Write a Python program to use unpacking to extract domain and subdomain from an email address.
"""

email = "john.doe@example.com"
user, domain = email.split("@")
print(user, domain)  # Expected output: john.doe example.com


"""
Problem: 906
Write a Python program to unpack nested tuples inside a list.
"""

nested_tuples = [(1, (2, 3)), (4, (5, 6))]
for a, (b, c) in nested_tuples:
    print(a, b, c)

# Expected output:
# 1 2 3
# 4 5 6

"""
Problem: 907
Write a Python program to unpack values returned from `divmod()`.
"""

quotient, remainder = divmod(17, 5)
print(quotient, remainder)  # Expected output: 3 2

"""
Problem: 908
Write a Python program to generate a random integer between 1 and 100.
"""

import random

num = random.randint(1, 100)
print(num)  # Expected output: A random number between 1 and 100


"""
Problem: 909
Write a Python program to generate a random floating-point number between 0 and 1.
"""

import random

num = random.random()
print(num)  # Expected output: A random float between 0 and 1


"""
Problem: 910
Write a Python program to generate a random even integer between 10 and 50.
"""

import random

num = random.randrange(10, 51, 2)
print(num)  # Expected output: A random even number between 10 and 50


"""
Problem: 911
Write a Python program to randomly select an element from a given list.
"""

import random

colors = ["red", "blue", "green", "yellow", "purple"]
selected = random.choice(colors)
print(selected)  # Expected output: A random color from the list


"""
Problem: 912
Write a Python program to shuffle a list randomly.
"""

import random

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # Expected output: A shuffled version of the list


"""
Problem: 913
Write a Python program to select 3 unique random numbers from a list.
"""

import random

numbers = list(range(1, 21))
selected = random.sample(numbers, 3)
print(selected)  # Expected output: 3 unique numbers from 1 to 20


"""
Problem: 914
Write a Python program to generate a random floating-point number between 5 and 10.
"""

import random

num = random.uniform(5, 10)
print(num)  # Expected output: A random float between 5 and 10


"""
Problem: 915
Write a Python program to generate a random letter from the English alphabet.
"""

import random
import string

letter = random.choice(string.ascii_letters)
print(letter)  # Expected output: A random letter from a-z or A-Z


"""
Problem: 916
Write a Python program to simulate the rolling of a six-sided die.
"""

import random

roll = random.randint(1, 6)
print(roll)  # Expected output: A number between 1 and 6


"""
Problem: 917
Write a Python program to simulate flipping a coin.
"""

import random

flip = random.choice(["Heads", "Tails"])
print(flip)  # Expected output: Heads or Tails


"""
Problem: 918
Write a Python program to randomly select a first name and last name from separate lists and combine them.
"""

import random

first_names = ["Alice", "Bob", "Charlie", "David"]
last_names = ["Smith", "Johnson", "Brown", "Williams"]

full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
print(full_name)  # Expected output: A random full name


"""
Problem: 919
Write a Python program to generate a random password with 8 characters including letters, digits, and special characters.
"""

import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.sample(characters, 8))
print(password)  # Expected output: A random 8-character password


"""
Problem: 920
Write a Python program to generate a random boolean value (True or False).
"""

import random

boolean_value = random.choice([True, False])
print(boolean_value)  # Expected output: True or False


"""
Problem: 921
Write a Python program to generate 5 random numbers between 1 and 100 and store them in a list.
"""

import random

numbers = [random.randint(1, 100) for _ in range(5)]
print(numbers)  # Expected output: A list of 5 random numbers between 1 and 100


"""
Problem: 922
Write a Python program to select a random subset of 4 elements from a list.
"""

import random

items = list(range(1, 11))
subset = random.sample(items, 4)
print(subset)  # Expected output: A random selection of 4 numbers from 1 to 10


"""
Problem: 923
Write a Python program to generate a random date within the year 2023.
"""

import random
import datetime

start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 12, 31)
random_days = random.randint(0, (end_date - start_date).days)
random_date = start_date + datetime.timedelta(days=random_days)
print(random_date)  # Expected output: A random date in 2023


"""
Problem: 924
Write a Python program to randomly pick an element from a set.
"""

import random

fruits = {"apple", "banana", "cherry", "date"}
random_fruit = random.choice(list(fruits))
print(random_fruit)  # Expected output: A random fruit from the set


"""
Problem: 925
Write a Python program to randomly generate a 6-digit verification code.
"""

import random

code = random.randint(100000, 999999)
print(code)  # Expected output: A 6-digit random number


"""
Problem: 926
Write a Python program to generate a random hexadecimal color code.
"""

import random

hex_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
print(hex_color)  # Expected output: A random hex color


"""
Problem: 927
Write a Python program to generate a random phone number in the format (XXX) XXX-XXXX.
"""

import random

phone_number = f"({random.randint(100, 999)}) {random.randint(100, 999)}-{random.randint(1000, 9999)}"
print(phone_number)  # Expected output: A random phone number


"""
Problem: 928
Write a Python program to generate a random 4-digit PIN code.
"""

import random

pin = f"{random.randint(1000, 9999)}"
print(pin)  # Expected output: A 4-digit random PIN


"""
Problem: 929
Write a Python program to simulate a random dice roll with two six-sided dice.
"""

import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
print(dice1, dice2)  # Expected output: Two random numbers between 1 and 6


"""
Problem: 930
Write a Python program to generate a random IP address.
"""

import random

ip_address = ".".join(str(random.randint(0, 255)) for _ in range(4))
print(ip_address)  # Expected output: A random IP address


"""
Problem: 931
Write a Python program to generate a random strong password of 12 characters.
"""

import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choices(characters, k=12))
print(password)  # Expected output: A random 12-character password


"""
Problem: 932
Write a Python program to randomly pick an item from a tuple.
"""

import random

animals = ("dog", "cat", "elephant", "lion")
random_animal = random.choice(animals)
print(random_animal)  # Expected output: A random animal from the tuple

"""
Problem: 933
Write a Python program to handle division by zero exception when dividing two numbers.
"""

try:
    a, b = 10, 0
    result = a / b
except ZeroDivisionError:
    result = "Cannot divide by zero"
    
print(result)  # Expected output: Cannot divide by zero


"""
Problem: 934
Write a Python program to handle an IndexError when accessing an out-of-range list index.
"""

try:
    lst = [1, 2, 3]
    value = lst[5]
except IndexError:
    value = "Index out of range"

print(value)  # Expected output: Index out of range


"""
Problem: 935
Write a Python program to handle a KeyError when accessing a non-existent key in a dictionary.
"""

try:
    d = {"name": "Alice"}
    value = d["age"]
except KeyError:
    value = "Key not found"

print(value)  # Expected output: Key not found


"""
Problem: 936
Write a Python program to handle a ValueError when converting an invalid string to an integer.
"""

try:
    num = int("abc")
except ValueError:
    num = "Invalid integer conversion"

print(num)  # Expected output: Invalid integer conversion


"""
Problem: 937
Write a Python program to handle a TypeError when trying to concatenate a string with an integer.
"""

try:
    result = "Age: " + 25
except TypeError:
    result = "Type mismatch error"

print(result)  # Expected output: Type mismatch error


"""
Problem: 938
Write a Python program to handle a FileNotFoundError when trying to open a non-existent file.
"""

try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    content = "File not found"

print(content)  # Expected output: File not found


"""
Problem: 939
Write a Python program to catch an AttributeError when accessing a non-existent attribute of an object.
"""

class Person:
    def __init__(self, name):
        self.name = name

try:
    p = Person("Alice")
    age = p.age
except AttributeError:
    age = "Attribute not found"

print(age)  # Expected output: Attribute not found


"""
Problem: 940
Write a Python program to catch a NameError when accessing an undefined variable.
"""

try:
    result = x + 10
except NameError:
    result = "Variable not defined"

print(result)  # Expected output: Variable not defined


"""
Problem: 941
Write a Python program to handle a PermissionError when trying to write to a read-only file.
"""

try:
    with open("/root/protected.txt", "w") as file:
        file.write("Test")
except PermissionError:
    result = "Permission denied"

print(result)  # Expected output: Permission denied


"""
Problem: 942
Write a Python program to use a try-except-else block to catch errors in division.
"""

try:
    a, b = 10, 2
    result = a / b
except ZeroDivisionError:
    result = "Cannot divide by zero"
else:
    result = f"Division successful: {result}"

print(result)  # Expected output: Division successful: 5.0


"""
Problem: 943
Write a Python program to use a finally block to always print a message after exception handling.
"""

try:
    result = 10 / 0
except ZeroDivisionError:
    result = "Cannot divide by zero"
finally:
    print("Execution completed")

print(result)  # Expected output: Cannot divide by zero
               # Execution completed


"""
Problem: 944
Write a Python program to raise a custom exception if a number is negative.
"""

class NegativeNumberError(Exception):
    pass

def check_number(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed")

try:
    check_number(-5)
except NegativeNumberError as e:
    print(e)  # Expected output: Negative numbers are not allowed


"""
Problem: 945
Write a Python program to handle a multiple exception scenario (ZeroDivisionError and TypeError).
"""

try:
    num = "10" / 2
except (ZeroDivisionError, TypeError):
    result = "An error occurred"

print(result)  # Expected output: An error occurred


"""
Problem: 946
Write a Python program to use the `assert` statement to raise an AssertionError if a condition is false.
"""

try:
    x = -1
    assert x >= 0, "Negative number not allowed"
except AssertionError as e:
    print(e)  # Expected output: Negative number not allowed


"""
Problem: 947
Write a Python program to handle a MemoryError by attempting to allocate excessive memory.
"""

try:
    lst = [0] * (10**9)
except MemoryError:
    print("Memory limit exceeded")  # Expected output: Memory limit exceeded


"""
Problem: 948
Write a Python program to catch a RecursionError when a function calls itself infinitely.
"""

def infinite_recursion():
    return infinite_recursion()

try:
    infinite_recursion()
except RecursionError:
    print("Recursion limit exceeded")  # Expected output: Recursion limit exceeded


"""
Problem: 949
Write a Python program to catch a ModuleNotFoundError when trying to import a non-existent module.
"""

try:
    import nonexistent_module
except ModuleNotFoundError:
    print("Module not found")  # Expected output: Module not found


"""
Problem: 950
Write a Python program to catch an IOError when trying to read a file that does not exist.
"""

try:
    with open("missingfile.txt", "r") as f:
        data = f.read()
except IOError:
    print("Error reading file")  # Expected output: Error reading file


"""
Problem: 951
Write a Python program to catch a KeyboardInterrupt exception when the user manually stops the script.
"""

try:
    while True:
        pass  # Infinite loop to simulate long-running process
except KeyboardInterrupt:
    print("Process interrupted by user")  # Expected output: Process interrupted by user

"""
Problem: 952
Write a Python program to convert a string to uppercase using a built-in method.
"""

text = "hello world"
upper_text = text.upper()
print(upper_text)  # Expected output: HELLO WORLD


"""
Problem: 953
Write a Python program to count the occurrences of a specific character in a string using a method.
"""

text = "banana"
count_a = text.count("a")
print(count_a)  # Expected output: 3


"""
Problem: 954
Write a Python program to check if a string starts with a specific prefix using a method.
"""

text = "hello world"
result = text.startswith("hello")
print(result)  # Expected output: True


"""
Problem: 955
Write a Python program to replace all occurrences of a word in a string using a method.
"""

text = "I love apples. Apples are delicious."
new_text = text.replace("Apples", "Bananas")
print(new_text)  # Expected output: I love apples. Bananas are delicious.


"""
Problem: 956
Write a Python program to split a sentence into words using a method.
"""

sentence = "Python is amazing"
words = sentence.split()
print(words)  # Expected output: ['Python', 'is', 'amazing']


"""
Problem: 957
Write a Python program to join a list of words into a sentence using a method.
"""

words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)  # Expected output: Python is fun


"""
Problem: 958
Write a Python program to remove leading and trailing spaces from a string using a method.
"""

text = "   hello world   "
trimmed_text = text.strip()
print(trimmed_text)  # Expected output: hello world


"""
Problem: 959
Write a Python program to find the index of a specific element in a list using a method.
"""

numbers = [10, 20, 30, 40, 50]
index_30 = numbers.index(30)
print(index_30)  # Expected output: 2


"""
Problem: 960
Write a Python program to sort a list of numbers in ascending order using a method.
"""

numbers = [5, 2, 8, 1, 3]
numbers.sort()
print(numbers)  # Expected output: [1, 2, 3, 5, 8]


"""
Problem: 961
Write a Python program to reverse the order of elements in a list using a method.
"""

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # Expected output: [5, 4, 3, 2, 1]


"""
Problem: 962
Write a Python program to add an element at the end of a list using a method.
"""

numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # Expected output: [1, 2, 3, 4]


"""
Problem: 963
Write a Python program to remove the last element from a list using a method.
"""

numbers = [10, 20, 30]
last_item = numbers.pop()
print(numbers)  # Expected output: [10, 20]
print(last_item)  # Expected output: 30


"""
Problem: 964
Write a Python program to remove a specific element from a list using a method.
"""

numbers = [5, 10, 15, 20]
numbers.remove(10)
print(numbers)  # Expected output: [5, 15, 20]


"""
Problem: 965
Write a Python program to get all the keys from a dictionary using a method.
"""

person = {"name": "Alice", "age": 25, "city": "New York"}
keys = person.keys()
print(list(keys))  # Expected output: ['name', 'age', 'city']


"""
Problem: 966
Write a Python program to get all the values from a dictionary using a method.
"""

person = {"name": "Alice", "age": 25, "city": "New York"}
values = person.values()
print(list(values))  # Expected output: ['Alice', 25, 'New York']


"""
Problem: 967
Write a Python program to merge two dictionaries using a method.
"""

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)  # Expected output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


"""
Problem: 968
Write a Python program to remove an item from a dictionary using a method.
"""

person = {"name": "Alice", "age": 25, "city": "New York"}
person.pop("age")
print(person)  # Expected output: {'name': 'Alice', 'city': 'New York'}


"""
Problem: 969
Write a Python program to check if a set contains a specific element using a method.
"""

numbers = {1, 2, 3, 4, 5}
result = 3 in numbers
print(result)  # Expected output: True


"""
Problem: 970
Write a Python program to remove and return an arbitrary element from a set using a method. 
"""

numbers = {10, 20, 30, 40}
removed_element = numbers.pop()
print(removed_element)  # Expected output: A random element from the set
print(numbers)  # Expected output: The set without the removed element


"""
Problem: 971
Write a Python program to clear all elements from a list using a method.
"""

numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  # Expected output: []

"""
Problem: 972
Write a Python program to parse an integer from a string.
"""

num_str = "42"
num = int(num_str)
print(num)  # Expected output: 42


"""
Problem: 973
Write a Python program to parse a float from a string.
"""

num_str = "3.14"
num = float(num_str)
print(num)  # Expected output: 3.14


"""
Problem: 974
Write a Python program to parse a boolean from a string.
"""

bool_str = "True"
boolean_value = bool_str.lower() == "true"
print(boolean_value)  # Expected output: True


"""
Problem: 975
Write a Python program to parse multiple integers from a comma-separated string.
"""

num_str = "10,20,30,40"
numbers = list(map(int, num_str.split(",")))
print(numbers)  # Expected output: [10, 20, 30, 40]


"""
Problem: 976
Write a Python program to parse a date from a string in the format 'YYYY-MM-DD'.
"""

from datetime import datetime

date_str = "2024-03-22"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
print(parsed_date)  # Expected output: 2024-03-22 00:00:00


"""
Problem: 977
Write a Python program to extract numbers from a mixed string.
"""

import re

text = "My order number is 12345 and tracking ID is 67890."
numbers = re.findall(r"\d+", text)
print(numbers)  # Expected output: ['12345', '67890']


"""
Problem: 978
Write a Python program to parse a JSON string into a Python dictionary.
"""

import json

json_str = '{"name": "Alice", "age": 25, "city": "New York"}'
data = json.loads(json_str)
print(data)  # Expected output: {'name': 'Alice', 'age': 25, 'city': 'New York'}


"""
Problem: 979
Write a Python program to convert a dictionary to a JSON string.
"""

import json

data = {"name": "Bob", "age": 30, "city": "London"}
json_str = json.dumps(data)
print(json_str)  # Expected output: '{"name": "Bob", "age": 30, "city": "London"}'


"""
Problem: 980
Write a Python program to parse an XML string and extract specific data.
"""

import xml.etree.ElementTree as ET

xml_str = "<person><name>Charlie</name><age>28</age></person>"
root = ET.fromstring(xml_str)
name = root.find("name").text
print(name)  # Expected output: Charlie


"""
Problem: 981
Write a Python program to parse key-value pairs from a query string.
"""

from urllib.parse import parse_qs

query_str = "name=David&age=35&city=Paris"
parsed_data = parse_qs(query_str)
print(parsed_data)  # Expected output: {'name': ['David'], 'age': ['35'], 'city': ['Paris']}


"""
Problem: 982
Write a Python program to parse a CSV string into a list of lists.
"""

import csv
from io import StringIO

csv_str = "name,age,city\nAlice,25,New York\nBob,30,London"
csv_file = StringIO(csv_str)
reader = csv.reader(csv_file)
data = list(reader)
print(data)  
# Expected output: [['name', 'age', 'city'], ['Alice', '25', 'New York'], ['Bob', '30', 'London']]


"""
Problem: 983
Write a Python program to parse HTML and extract all links.
"""

from bs4 import BeautifulSoup

html = '<a href="https://example.com">Example</a> <a href="https://google.com">Google</a>'
soup = BeautifulSoup(html, "html.parser")
links = [a["href"] for a in soup.find_all("a")]
print(links)  # Expected output: ['https://example.com', 'https://google.com']


"""
Problem: 984
Write a Python program to parse a time string in the format 'HH:MM:SS' into a `datetime.time` object.
"""

from datetime import datetime

time_str = "14:30:45"
parsed_time = datetime.strptime(time_str, "%H:%M:%S").time()
print(parsed_time)  # Expected output: 14:30:45


"""
Problem: 985
Write a Python program to parse a hexadecimal number string into an integer.
"""

hex_str = "0x1A"
num = int(hex_str, 16)
print(num)  # Expected output: 26


"""
Problem: 986
Write a Python program to parse a binary number string into an integer.
"""

binary_str = "1010"
num = int(binary_str, 2)
print(num)  # Expected output: 10


"""
Problem: 987
Write a Python program to parse a scientific notation string into a float.
"""

sci_str = "3.5e4"
num = float(sci_str)
print(num)  # Expected output: 35000.0


"""
Problem: 988
Write a Python program to parse a configuration file (.ini format) and extract a setting.
"""

import configparser

config_str = "[Settings]\nusername=admin\npassword=1234"
config = configparser.ConfigParser()
config.read_string(config_str)
username = config["Settings"]["username"]
print(username)  # Expected output: admin


"""
Problem: 989
Write a Python program to parse a markdown string and extract the text from a header.
"""

import re

markdown = "# Hello World\nThis is a markdown file."
header = re.findall(r"^# (.+)", markdown, re.MULTILINE)
print(header)  # Expected output: ['Hello World']


"""
Problem: 990
Write a Python program to parse a YAML string into a Python dictionary.
"""

import yaml

yaml_str = "name: Alice\nage: 25\ncity: New York"
data = yaml.safe_load(yaml_str)
print(data)  # Expected output: {'name': 'Alice', 'age': 25, 'city': 'New York'}


"""
Problem: 991
Write a Python program to parse a JSON array into a Python list.
"""

import json

json_str = '[1, 2, 3, 4, 5]'
data = json.loads(json_str)
print(data)  # Expected output: [1, 2, 3, 4, 5]


"""
Problem: 992
Write a Python program to parse a currency string and extract the numeric value.
"""

import re

currency_str = "$123.45"
value = float(re.sub(r"[^\d.]", "", currency_str))
print(value)  # Expected output: 123.45


"""
Problem: 993
Write a Python program to parse command-line arguments.
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", type=str, default="User")
args = parser.parse_args(args=["--name", "Alice"])
print(args.name)  # Expected output: Alice

"""
Problem: 994
Write a Python program to slice the first 5 characters from a string.
"""

text = "Hello, world!"
sliced_text = text[:5]
print(sliced_text)  # Expected output: Hello


"""
Problem: 995
Write a Python program to slice the last 4 characters from a string.
"""

text = "Programming"
sliced_text = text[-4:]
print(sliced_text)  # Expected output: ming


"""
Problem: 996
Write a Python program to slice all elements from a list except the first two.
"""

numbers = [10, 20, 30, 40, 50]
sliced_list = numbers[2:]
print(sliced_list)  # Expected output: [30, 40, 50]


"""
Problem: 997
Write a Python program to slice the last 3 elements from a list.
"""

numbers = [1, 2, 3, 4, 5, 6]
sliced_list = numbers[-3:]
print(sliced_list)  # Expected output: [4, 5, 6]


"""
Problem: 998
Write a Python program to extract only the even-indexed characters from a string using slicing.
"""

text = "PythonSlicing"
sliced_text = text[::2]
print(sliced_text)  # Expected output: PtoSln


"""
Problem: 999
Write a Python program to extract only the odd-indexed characters from a string using slicing.
"""

text = "PythonSlicing"
sliced_text = text[1::2]
print(sliced_text)  # Expected output: yhnicig


"""
Problem: 1000
Write a Python program to reverse a string using slicing.
"""

text = "abcdef"
reversed_text = text[::-1]
print(reversed_text)  # Expected output: fedcba





















