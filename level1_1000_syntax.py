# Syntax documentation
"""
Problem 501:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Bird:
    
        def fly(self):
            return 'I can fly!'
    class Penguin(Bird):
    
        def fly(self):
            return 'Cannot fly'
    generic_bird = Bird()
    print(generic_bird.fly())
    penguin = Penguin()
    print(penguin.fly())
#
class Bird:  # defines a new type
    def fly(self):  # method of Bird
        return 'I can fly!'  # method of Bird
class Penguin(Bird):  # defines a new type
    def fly(self):  # method of Penguin
        return 'Cannot fly'  # method of Penguin
#
# Built-in functions: Bird, Penguin()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Bird:  # class definition stored
class Penguin(Bird):  # class definition stored
generic_bird = ...  # assigns a value to the variable
print(generic_bird.fly(...))
penguin = ...  # assigns a value to the variable
print(penguin.fly(...))
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Bird(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Penguin, Bird are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → generic_bird = ...  # stored in memory
#   → print(generic_bird.fly(...))
#   → penguin = ...  # stored in memory
#   → print(penguin.fly(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Bird(...))

"""

"""
Problem 502:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Book:
    
        def __init__(self, title, author):
            self.title = title
            self.author = author
    class EBook(Book):
    
        def __init__(self, title, author, file_size):
            super().__init__(title, author)
            self.file_size = file_size
    ebook = EBook('Python Programming', 'John Doe', 2.5)
    print(f'Title: {ebook.title}, Author: {ebook.author}, File Size: {ebook.file_size}MB')
#
class Book:  # defines a new type
    def __init__(self, title, author):  # method of Book
        self.title = title  # method of Book
        self.author = author  # method of Book
class EBook(Book):  # defines a new type
    def __init__(self, title, author, file_size):  # method of EBook
        super().__init__(title, author)  # method of EBook
        self.file_size = file_size  # method of EBook
class Computer:  # defines a new type
#
# Built-in functions: Book, EBook, super()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Book:  # class definition stored
class EBook(Book):  # class definition stored
ebook = ...  # assigns a value to the variable
print(?)
from dataclasses import dataclass
class Computer:  # class definition stored
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Book(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Computer, Book, EBook are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → ebook = ...  # stored in memory
#   → print(?)
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Book(...))

"""

"""
Problem 503:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Instrument:
    
        def play(self):
            return 'Playing an instrument.'
    class Guitar(Instrument):
    
        def play(self):
            return 'Strum'
    generic_instrument = Instrument()
    print(generic_instrument.play())
    guitar = Guitar()
    print(guitar.play())
#
class Instrument:  # defines a new type
    def play(self):  # method of Instrument
        return 'Playing an instrument.'  # method of Instrument
class Guitar(Instrument):  # defines a new type
    def play(self):  # method of Guitar
        return 'Strum'  # method of Guitar
#
# Built-in functions: Guitar, Instrument()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Instrument:  # class definition stored
class Guitar(Instrument):  # class definition stored
generic_instrument = ...  # assigns a value to the variable
print(generic_instrument.play(...))
guitar = ...  # assigns a value to the variable
print(guitar.play(...))
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Instrument(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Instrument, Guitar are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → generic_instrument = ...  # stored in memory
#   → print(generic_instrument.play(...))
#   → guitar = ...  # stored in memory
#   → print(guitar.play(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Instrument(...))

"""

"""
Problem 504:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Game:
    
        def start(self):
            return 'Starting the game.'
    class Chess(Game):
    
        def start(self):
            return 'Start Chess'
    generic_game = Game()
    print(generic_game.start())
    chess_game = Chess()
    print(chess_game.start())
#
class Game:  # defines a new type
    def start(self):  # method of Game
        return 'Starting the game.'  # method of Game
class Chess(Game):  # defines a new type
    def start(self):  # method of Chess
        return 'Start Chess'  # method of Chess
#
# Built-in functions: Chess, Game()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Game:  # class definition stored
class Chess(Game):  # class definition stored
generic_game = ...  # assigns a value to the variable
print(generic_game.start(...))
chess_game = ...  # assigns a value to the variable
print(chess_game.start(...))
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Game(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Chess, Game are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → generic_game = ...  # stored in memory
#   → print(generic_game.start(...))
#   → chess_game = ...  # stored in memory
#   → print(chess_game.start(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Game(...))

"""

"""
Problem 505:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
class Vehicle:  # defines a new type
    def drive(self):  # method of Vehicle
        return 'Are you ready to drive?'  # method of Vehicle
class Bicycle(Vehicle):  # defines a new type
    def drive(self):  # method of Bicycle
        return 'Pedal'  # method of Bicycle
#
# Built-in functions: Bicycle, Vehicle()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Vehicle:  # class definition stored
class Bicycle(Vehicle):  # class definition stored
bicycle = ...  # assigns a value to the variable
print(bicycle.drive(...))
obj = ...  # assigns a value to the variable
print(obj)
print(Vehicle(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Vehicle, Bicycle are defined — methods stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → bicycle = ...  # stored in memory
#   → print(bicycle.drive(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Vehicle(...))

"""

"""
Problem 506:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Computer:
    
        def __init__(self, brand, processor):
            self.brand = brand
            self.processor = processor
    class Laptop(Computer):
    
        def __init__(self, brand, processor, weight):
            super().__init__(brand, processor)
            self.weight = weight
    laptop = Laptop('Dell', 'Intel i7', 2.3)
    print(f'Brand: {laptop.brand}, Processor: {laptop.processor}, Weight: {laptop.weight}kg')
#
class Computer:  # defines a new type
    def __init__(self, brand, processor):  # method of Computer
        self.brand = brand  # method of Computer
        self.processor = processor  # method of Computer
class Laptop(Computer):  # defines a new type
    def __init__(self, brand, processor, weight):  # method of Laptop
        super().__init__(brand, processor)  # method of Laptop
        self.weight = weight  # method of Laptop
class Computer:  # defines a new type
#
# Built-in functions: Computer, Laptop, super()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Computer:  # class definition stored
class Laptop(Computer):  # class definition stored
laptop = ...  # assigns a value to the variable
print(?)
from dataclasses import dataclass
class Computer:  # class definition stored
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Computer(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Computer, Laptop are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → laptop = ...  # stored in memory
#   → print(?)
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Computer(...))

"""

"""
Problem 507:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Device:
    
        def turn_on(self):
            return 'Device is now on.'
    class Smartphone(Device):
    
        def __init__(self, apps):
            self.apps = apps
    phone = Smartphone(['WhatsApp', 'Instagram', 'Spotify'])
    print(phone.turn_on())
    print(f"Installed apps: {', '.join(phone.apps)}")
#
class Device:  # defines a new type
    def turn_on(self):  # method of Device
        return 'Device is now on.'  # method of Device
class Smartphone(Device):  # defines a new type
    def __init__(self, apps):  # method of Smartphone
        self.apps = apps  # method of Smartphone
#
# Built-in functions: Device, Smartphone()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Device:  # class definition stored
class Smartphone(Device):  # class definition stored
phone = ...  # assigns a value to the variable
print(phone.turn_on(...))
print(?)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Device(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Smartphone, Device are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → phone = ...  # stored in memory
#   → print(phone.turn_on(...))
#   → print(?)
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Device(...))

"""

"""
Problem 508:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Parent:
    
        def display(self):
            return 'This is the parent.'
    class Child(Parent):
    
        def display(self):
            return 'This is a child'
    parent = Parent()
    print(parent.display())
    child = Child()
    print(child.display())
#
class Parent:  # defines a new type
    def display(self):  # method of Parent
        return 'This is the parent.'  # method of Parent
class Child(Parent):  # defines a new type
    def display(self):  # method of Child
        return 'This is a child'  # method of Child
#
# Built-in functions: Child, Parent()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Parent:  # class definition stored
class Child(Parent):  # class definition stored
parent = ...  # assigns a value to the variable
print(parent.display(...))
child = ...  # assigns a value to the variable
print(child.display(...))
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Parent(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Child, Parent are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → parent = ...  # stored in memory
#   → print(parent.display(...))
#   → child = ...  # stored in memory
#   → print(child.display(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Parent(...))

"""

"""
Problem 509:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Building:
    
        def __init__(self, floors, address):
            self.floors = floors
            self.address = address
    class Skyscraper(Building):
    
        def __init__(self, floors, address, height):
            super().__init__(floors, address)
            self.height = height
    skyscraper = Skyscraper(50, '123 High Street', 200)
    print(f'Floors: {skyscraper.floors}, Address: {skyscraper.address}, Height: {skyscraper.height} meters')
#
class Building:  # defines a new type
    def __init__(self, floors, address):  # method of Building
        self.floors = floors  # method of Building
        self.address = address  # method of Building
class Skyscraper(Building):  # defines a new type
    def __init__(self, floors, address, height):  # method of Skyscraper
        super().__init__(floors, address)  # method of Skyscraper
        self.height = height  # method of Skyscraper
class Computer:  # defines a new type
#
# Built-in functions: Building, Skyscraper, super()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Building:  # class definition stored
class Skyscraper(Building):  # class definition stored
skyscraper = ...  # assigns a value to the variable
print(?)
from dataclasses import dataclass
class Computer:  # class definition stored
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Building(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Building, Computer, Skyscraper are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → skyscraper = ...  # stored in memory
#   → print(?)
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Building(...))

"""

"""
Problem 510:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Plant:
    
        def grow(self):
            return 'The plant is growing.'
    class Flower(Plant):
    
        def grow(self):
            return 'Bloom'
    plant = Plant()
    print(plant.grow())
    flower = Flower()
    print(flower.grow())
#
class Plant:  # defines a new type
    def grow(self):  # method of Plant
        return 'The plant is growing.'  # method of Plant
class Flower(Plant):  # defines a new type
    def grow(self):  # method of Flower
        return 'Bloom'  # method of Flower
#
# Built-in functions: Flower, Plant()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Plant:  # class definition stored
class Flower(Plant):  # class definition stored
plant = ...  # assigns a value to the variable
print(plant.grow(...))
flower = ...  # assigns a value to the variable
print(flower.grow(...))
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Plant(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Plant, Flower are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → plant = ...  # stored in memory
#   → print(plant.grow(...))
#   → flower = ...  # stored in memory
#   → print(flower.grow(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Plant(...))

"""

"""
Problem 511:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Teacher:
    
        def __init__(self, name, subject):
            self.name = name
            self.subject = subject
    
        def __str__(self):
            return f'Name: {self.name}, Subject: {self.subject}'
    class MathTeacher(Teacher):
    
        def __init__(self, name):
            super().__init__(name, 'Math')
    
        def teach_math(self):
            return 'Teaching math concepts.'
#
class Teacher:  # defines a new type
    def __init__(self, name, subject):  # method of Teacher
        self.name = name  # method of Teacher
        self.subject = subject  # method of Teacher
    def __str__(self):  # method of Teacher
        return f'Name: {self.name}, Subject: {self.subject}'  # method of Teacher
class MathTeacher(Teacher):  # defines a new type
    def __init__(self, name):  # method of MathTeacher
        super().__init__(name, 'Math')  # method of MathTeacher
    def teach_math(self):  # method of MathTeacher
        return 'Teaching math concepts.'  # method of MathTeacher
#
# Built-in functions: MathTeacher, Teacher, super()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Teacher:  # class definition stored
class MathTeacher(Teacher):  # class definition stored
teacher = ...  # assigns a value to the variable
print(teacher)
math_teacher = ...  # assigns a value to the variable
print(math_teacher)
print(math_teacher.teach_math(...))
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Teacher(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes MathTeacher, Teacher are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → teacher = ...  # stored in memory
#   → print(teacher)
#   → math_teacher = ...  # stored in memory
#   → print(math_teacher)
#   → print(math_teacher.teach_math(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Teacher(...))

"""

"""
Problem 512:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Writer:
    
        def __init__(self, name, genre):
            self.name = name
            self.genre = genre
    
        def __str__(self):
            return f'Name: {self.name}, Genre: {self.genre}'
    class Poet(Writer):
    
        def __init__(self, name):
            super().__init__(name, 'Poetry')
#
class Writer:  # defines a new type
    def __init__(self, name, genre):  # method of Writer
        self.name = name  # method of Writer
        self.genre = genre  # method of Writer
    def __str__(self):  # method of Writer
        return f'Name: {self.name}, Genre: {self.genre}'  # method of Writer
class Poet(Writer):  # defines a new type
    def __init__(self, name):  # method of Poet
        super().__init__(name, 'Poetry')  # method of Poet
#
# Built-in functions: Poet, Writer, super()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Writer:  # class definition stored
class Poet(Writer):  # class definition stored
writer = ...  # assigns a value to the variable
print(writer)
poet = ...  # assigns a value to the variable
print(poet)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Writer(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Writer, Poet are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → writer = ...  # stored in memory
#   → print(writer)
#   → poet = ...  # stored in memory
#   → print(poet)
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Writer(...))

"""

"""
Problem 513:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Appliance:
    
        def use(self):
            return 'Using the appliance.'
    class Oven(Appliance):
    
        def use(self):
            return 'Bake'
    appliance = Appliance()
    print(appliance.use())
    oven = Oven()
    print(oven.use())
#
class Appliance:  # defines a new type
    def use(self):  # method of Appliance
        return 'Using the appliance.'  # method of Appliance
class Oven(Appliance):  # defines a new type
    def use(self):  # method of Oven
        return 'Bake'  # method of Oven
#
# Built-in functions: Appliance, Oven()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Appliance:  # class definition stored
class Oven(Appliance):  # class definition stored
appliance = ...  # assigns a value to the variable
print(appliance.use(...))
oven = ...  # assigns a value to the variable
print(oven.use(...))
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Appliance(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Appliance, Oven are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → appliance = ...  # stored in memory
#   → print(appliance.use(...))
#   → oven = ...  # stored in memory
#   → print(oven.use(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Appliance(...))

"""

"""
Problem 514:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Artist:
    
        def __init__(self, name, medium):
            self.name = name
            self.medium = medium
    
        def __str__(self):
            return f'Name: {self.name}, Medium: {self.medium}'
    class Painter(Artist):
    
        def paint(self):
            return 'Painting with ' + self.medium
#
class Artist:  # defines a new type
    def __init__(self, name, medium):  # method of Artist
        self.name = name  # method of Artist
        self.medium = medium  # method of Artist
    def __str__(self):  # method of Artist
        return f'Name: {self.name}, Medium: {self.medium}'  # method of Artist
class Painter(Artist):  # defines a new type
    def paint(self):  # method of Painter
        return 'Painting with ' + self.medium  # method of Painter
#
# Operators: +
# Built-in functions: Artist, Painter()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
'Painting with ' + self.medium  # 'Painting with ' → then self.medium → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Artist:  # class definition stored
class Painter(Artist):  # class definition stored
artist = ...  # assigns a value to the variable
print(artist)
painter = ...  # assigns a value to the variable
print(painter)
print(painter.paint(...))
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Artist(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Painter, Artist are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → artist = ...  # stored in memory
#   → print(artist)
#   → painter = ...  # stored in memory
#   → print(painter)
#   → print(painter.paint(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Artist(...))

"""

"""
Problem 515:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Worker:
    
        def work(self):
            return 'Working on general tasks.'
    class Electrician(Worker):
    
        def work(self):
            return 'Fix wires'
#
class Worker:  # defines a new type
    def work(self):  # method of Worker
        return 'Working on general tasks.'  # method of Worker
class Electrician(Worker):  # defines a new type
    def work(self):  # method of Electrician
        return 'Fix wires'  # method of Electrician
#
# Built-in functions: Electrician, Worker()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Worker:  # class definition stored
class Electrician(Worker):  # class definition stored
worker = ...  # assigns a value to the variable
print(worker.work(...))
electrician = ...  # assigns a value to the variable
print(electrician.work(...))
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Worker(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Electrician, Worker are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → worker = ...  # stored in memory
#   → print(worker.work(...))
#   → electrician = ...  # stored in memory
#   → print(electrician.work(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Worker(...))

"""

"""
Problem 516:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Animal:
    
        def eat(self):
            return 'Eating food.'
    class Lion(Animal):
    
        def eat(self):
            return 'Eat meat'
#
class Animal:  # defines a new type
    def eat(self):  # method of Animal
        return 'Eating food.'  # method of Animal
class Lion(Animal):  # defines a new type
    def eat(self):  # method of Lion
        return 'Eat meat'  # method of Lion
#
# Built-in functions: Animal, Lion()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Animal:  # class definition stored
class Lion(Animal):  # class definition stored
animal = ...  # assigns a value to the variable
print(animal.eat(...))
lion = ...  # assigns a value to the variable
print(lion.eat(...))
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Animal(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Animal, Lion are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → animal = ...  # stored in memory
#   → print(animal.eat(...))
#   → lion = ...  # stored in memory
#   → print(lion.eat(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Animal(...))

"""

"""
Problem 517:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Appliance:
    
        def run(self):
            return 'Running appliance.'
    class Fan(Appliance):
    
        def run(self):
            return 'Spin blades'
#
class Appliance:  # defines a new type
    def run(self):  # method of Appliance
        return 'Running appliance.'  # method of Appliance
class Fan(Appliance):  # defines a new type
    def run(self):  # method of Fan
        return 'Spin blades'  # method of Fan
#
# Built-in functions: Appliance, Fan()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Appliance:  # class definition stored
class Fan(Appliance):  # class definition stored
appliance = ...  # assigns a value to the variable
print(appliance.run(...))
fan = ...  # assigns a value to the variable
print(fan.run(...))
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Appliance(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Appliance, Fan are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → appliance = ...  # stored in memory
#   → print(appliance.run(...))
#   → fan = ...  # stored in memory
#   → print(fan.run(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Appliance(...))

"""

"""
Problem 518:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Employee:
    
        def get_salary(self):
            return 5000
    class Intern(Employee):
    
        def get_salary(self):
            return 2000
#
class Employee:  # defines a new type
    def get_salary(self):  # method of Employee
        return 5000  # method of Employee
class Intern(Employee):  # defines a new type
    def get_salary(self):  # method of Intern
        return 2000  # method of Intern
#
# Built-in functions: Employee, Intern()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Employee:  # class definition stored
class Intern(Employee):  # class definition stored
employee = ...  # assigns a value to the variable
print(?)
intern = ...  # assigns a value to the variable
print(?)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Employee(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Employee, Intern are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → employee = ...  # stored in memory
#   → print(?)
#   → intern = ...  # stored in memory
#   → print(?)
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Employee(...))

"""

"""
Problem 519:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Vehicle:
    
        def __init__(self, wheels):
            self.wheels = wheels
    
        def __str__(self):
            return f'Wheels: {self.wheels}'
    class Motorcycle(Vehicle):
    
        def __init__(self):
            super().__init__(2)
#
class Vehicle:  # defines a new type
    def __init__(self, wheels):  # method of Vehicle
        self.wheels = wheels  # method of Vehicle
    def __str__(self):  # method of Vehicle
        return f'Wheels: {self.wheels}'  # method of Vehicle
class Motorcycle(Vehicle):  # defines a new type
    def __init__(self):  # method of Motorcycle
        super().__init__(2)  # method of Motorcycle
#
# Built-in functions: Motorcycle, Vehicle, super()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Vehicle:  # class definition stored
class Motorcycle(Vehicle):  # class definition stored
vehicle = ...  # assigns a value to the variable
print(vehicle)
motorcycle = ...  # assigns a value to the variable
print(motorcycle)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Vehicle(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Vehicle, Motorcycle are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → vehicle = ...  # stored in memory
#   → print(vehicle)
#   → motorcycle = ...  # stored in memory
#   → print(motorcycle)
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Vehicle(...))

"""

"""
Problem 520:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Tool:
    
        def use(self):
            return 'Using the tool.'
    class Hammer(Tool):
    
        def use(self):
            return 'Hammer nails'
#
class Tool:  # defines a new type
    def use(self):  # method of Tool
        return 'Using the tool.'  # method of Tool
class Hammer(Tool):  # defines a new type
    def use(self):  # method of Hammer
        return 'Hammer nails'  # method of Hammer
#
# Built-in functions: Hammer, Tool()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Tool:  # class definition stored
class Hammer(Tool):  # class definition stored
tool = ...  # assigns a value to the variable
print(tool.use(...))
hammer = ...  # assigns a value to the variable
print(hammer.use(...))
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Tool(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Hammer, Tool are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → tool = ...  # stored in memory
#   → print(tool.use(...))
#   → hammer = ...  # stored in memory
#   → print(hammer.use(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Tool(...))

"""

"""
Problem 521:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class BankAccount:
    
        def __init__(self, balance, owner):
            self.balance = balance
            self.owner = owner
    
        def __str__(self):
            return f'Owner: {self.owner}, Balance: ${self.balance}'
    class SavingsAccount(BankAccount):
    
        def __init__(self, balance, owner, interest_rate):
            super().__init__(balance, owner)
            self.interest_rate = interest_rate
    
        def __str__(self):
            return f'Owner: {self.owner}, Balance: ${self.balance}, Interest Rate: {self.interest_rate}%'
#
class BankAccount:  # defines a new type
    def __init__(self, balance, owner):  # method of BankAccount
        self.balance = balance  # method of BankAccount
        self.owner = owner  # method of BankAccount
    def __str__(self):  # method of BankAccount
        return f'Owner: {self.owner}, Balance: ${self.balance}'  # method of BankAccount
class SavingsAccount(BankAccount):  # defines a new type
    def __init__(self, balance, owner, interest_rate):  # method of SavingsAccount
        super().__init__(balance, owner)  # method of SavingsAccount
        self.interest_rate = interest_rate  # method of SavingsAccount
    def __str__(self):  # method of SavingsAccount
        return f'Owner: {self.owner}, Balance: ${self.balance}, Interest Rate: {self.interest_rate}%'  # method of SavingsAccount
#
# Built-in functions: BankAccount, SavingsAccount, super()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class BankAccount:  # class definition stored
class SavingsAccount(BankAccount):  # class definition stored
account = ...  # assigns a value to the variable
print(account)
savings = ...  # assigns a value to the variable
print(savings)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(BankAccount(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes BankAccount, SavingsAccount are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → account = ...  # stored in memory
#   → print(account)
#   → savings = ...  # stored in memory
#   → print(savings)
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(BankAccount(...))

"""

"""
Problem 522:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Weapon:
    
        def attack(self):
            return 'Weapon attack'
    class Sword(Weapon):
    
        def attack(self):
            return 'Slash'
#
class Weapon:  # defines a new type
    def attack(self):  # method of Weapon
        return 'Weapon attack'  # method of Weapon
class Sword(Weapon):  # defines a new type
    def attack(self):  # method of Sword
        return 'Slash'  # method of Sword
#
# Built-in functions: Sword, Weapon()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Weapon:  # class definition stored
class Sword(Weapon):  # class definition stored
weapon = ...  # assigns a value to the variable
print(weapon.attack(...))
sword = ...  # assigns a value to the variable
print(sword.attack(...))
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Weapon(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Weapon, Sword are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → weapon = ...  # stored in memory
#   → print(weapon.attack(...))
#   → sword = ...  # stored in memory
#   → print(sword.attack(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Weapon(...))

"""

"""
Problem 523:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Appliance:
    
        def __init__(self, power):
            self.power = power
    
        def __str__(self):
            return f'Power: {self.power} watts'
    class Microwave(Appliance):
    
        def __init__(self, power):
            super().__init__(power)
    
        def heat_food(self):
            return 'Heating food'
#
class Appliance:  # defines a new type
    def __init__(self, power):  # method of Appliance
        self.power = power  # method of Appliance
    def __str__(self):  # method of Appliance
        return f'Power: {self.power} watts'  # method of Appliance
class Microwave(Appliance):  # defines a new type
    def __init__(self, power):  # method of Microwave
        super().__init__(power)  # method of Microwave
    def heat_food(self):  # method of Microwave
        return 'Heating food'  # method of Microwave
#
# Built-in functions: Appliance, Microwave, super()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Appliance:  # class definition stored
class Microwave(Appliance):  # class definition stored
appliance = ...  # assigns a value to the variable
print(appliance)
microwave = ...  # assigns a value to the variable
print(microwave)
print(microwave.heat_food(...))
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Appliance(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Appliance, Microwave are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → appliance = ...  # stored in memory
#   → print(appliance)
#   → microwave = ...  # stored in memory
#   → print(microwave)
#   → print(microwave.heat_food(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Appliance(...))

"""

"""
Problem 524:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Vehicle:
    
        def start(self):
            return 'Starting vehicle'
    class ElectricCar(Vehicle):
    
        def start(self):
            return 'Silent start'
#
class Vehicle:  # defines a new type
    def start(self):  # method of Vehicle
        return 'Starting vehicle'  # method of Vehicle
class ElectricCar(Vehicle):  # defines a new type
    def start(self):  # method of ElectricCar
        return 'Silent start'  # method of ElectricCar
#
# Built-in functions: ElectricCar, Vehicle()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Vehicle:  # class definition stored
class ElectricCar(Vehicle):  # class definition stored
vehicle = ...  # assigns a value to the variable
print(vehicle.start(...))
electric_car = ...  # assigns a value to the variable
print(electric_car.start(...))
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Vehicle(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Vehicle, ElectricCar are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → vehicle = ...  # stored in memory
#   → print(vehicle.start(...))
#   → electric_car = ...  # stored in memory
#   → print(electric_car.start(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Vehicle(...))

"""

"""
Problem 525:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Pet:
    
        def make_sound(self):
            return 'Some generic pet sound'
    class Cat(Pet):
    
        def make_sound(self):
            return 'Meow'
#
class Pet:  # defines a new type
    def make_sound(self):  # method of Pet
        return 'Some generic pet sound'  # method of Pet
class Cat(Pet):  # defines a new type
    def make_sound(self):  # method of Cat
        return 'Meow'  # method of Cat
#
# Built-in functions: Cat, Pet()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Pet:  # class definition stored
class Cat(Pet):  # class definition stored
pet = ...  # assigns a value to the variable
print(pet.make_sound(...))
cat = ...  # assigns a value to the variable
print(cat.make_sound(...))
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Pet(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Pet, Cat are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → pet = ...  # stored in memory
#   → print(pet.make_sound(...))
#   → cat = ...  # stored in memory
#   → print(cat.make_sound(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Pet(...))

"""

"""
Problem 526:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Chef:
    
        def cook(self):
            return 'Cook food'
    class PastryChef(Chef):
    
        def cook(self):
            return 'Bake cake'
#
class Chef:  # defines a new type
    def cook(self):  # method of Chef
        return 'Cook food'  # method of Chef
class PastryChef(Chef):  # defines a new type
    def cook(self):  # method of PastryChef
        return 'Bake cake'  # method of PastryChef
#
# Built-in functions: Chef, PastryChef()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Chef:  # class definition stored
class PastryChef(Chef):  # class definition stored
chef = ...  # assigns a value to the variable
print(chef.cook(...))
pastry_chef = ...  # assigns a value to the variable
print(pastry_chef.cook(...))
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Chef(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Chef, PastryChef are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → chef = ...  # stored in memory
#   → print(chef.cook(...))
#   → pastry_chef = ...  # stored in memory
#   → print(pastry_chef.cook(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Chef(...))

"""

"""
Problem 527:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def create_chair(material, color, legs):  # defines a function with parameters material, color, legs
    class Furniture:
    
        def __init__(self, material, color):
            self.material = material
            self.color = color
    class Chair(Furniture):
    
        def __init__(self, material, color, legs):
            super().__init__(material, color)
            self.legs = legs
    return Chair(material, color, legs)  # return sends the result back to the caller
#
# Built-in functions: Chair, super()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
create_chair('wood', 'brown', 4)  # arguments evaluated first, then function body runs
create_chair(material, color, legs)  # arguments evaluated first, then function body runs
print(create_chair(25, 25, 25))  # create_chair() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def create_chair(material, color, legs):  # stored in memory, not executed yet
my_chair = ...  # assigns a value to the variable
def create_chair(material, color, legs):  # stored in memory, not executed yet
def create_chair(material, color, legs):  # stored in memory, not executed yet
material = ...  # assigns a value to the variable
color = ...  # assigns a value to the variable
legs = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(create_chair(...))  # create_chair() runs with material=25, color=25, legs=25
#   → return Chair(material, color, legs)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only create_chair is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → my_chair = ...  # stored in memory
#   → material = ...  # stored in memory
#   → color = ...  # stored in memory
#   → legs = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(create_chair(...))  # create_chair() runs first → value goes to print()

"""

"""
Problem 528:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Game:
    
        def __init__(self, players):
            self.players = players
    
        def __str__(self):
            return f'Players: {self.players}'
    class Soccer(Game):
    
        def __init__(self):
            super().__init__(players=22)
#
class Game:  # defines a new type
    def __init__(self, players):  # method of Game
        self.players = players  # method of Game
    def __str__(self):  # method of Game
        return f'Players: {self.players}'  # method of Game
class Soccer(Game):  # defines a new type
    def __init__(self):  # method of Soccer
        super().__init__(players=22)  # method of Soccer
#
# Built-in functions: Game, Soccer, super()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Game:  # class definition stored
class Soccer(Game):  # class definition stored
game = ...  # assigns a value to the variable
print(game)
soccer = ...  # assigns a value to the variable
print(soccer)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Game(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Soccer, Game are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → game = ...  # stored in memory
#   → print(game)
#   → soccer = ...  # stored in memory
#   → print(soccer)
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Game(...))

"""

"""
Problem 529:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Musician:
    
        def play_instrument(self):
            return 'Play instrument'
    class Pianist(Musician):
    
        def play_instrument(self):
            return 'Play piano'
#
class Musician:  # defines a new type
    def play_instrument(self):  # method of Musician
        return 'Play instrument'  # method of Musician
class Pianist(Musician):  # defines a new type
    def play_instrument(self):  # method of Pianist
        return 'Play piano'  # method of Pianist
#
# Built-in functions: Musician, Pianist()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Musician:  # class definition stored
class Pianist(Musician):  # class definition stored
musician = ...  # assigns a value to the variable
print(musician.play_instrument(...))
pianist = ...  # assigns a value to the variable
print(pianist.play_instrument(...))
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Musician(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Musician, Pianist are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → musician = ...  # stored in memory
#   → print(musician.play_instrument(...))
#   → pianist = ...  # stored in memory
#   → print(pianist.play_instrument(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Musician(...))

"""

"""
Problem 530:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Company:
    
        def __init__(self, name, location):
            self.name = name
            self.location = location
    
        def __str__(self):
            return f'Name: {self.name}, Location: {self.location}'
    class TechCompany(Company):
    
        def __init__(self, name, location, products):
            super().__init__(name, location)
            self.products = products
    
        def __str__(self):
            return f"Name: {self.name}, Location: {self.location}, Products: {', '.join(self.products)}"
#
class Company:  # defines a new type
    def __init__(self, name, location):  # method of Company
        self.name = name  # method of Company
        self.location = location  # method of Company
    def __str__(self):  # method of Company
        return f'Name: {self.name}, Location: {self.location}'  # method of Company
class TechCompany(Company):  # defines a new type
    def __init__(self, name, location, products):  # method of TechCompany
        super().__init__(name, location)  # method of TechCompany
        self.products = products  # method of TechCompany
    def __str__(self):  # method of TechCompany
        return f"Name: {self.name}, Location: {self.location}, Products: {', '.join(self.products)}"  # method of TechCompany
#
# Built-in functions: Company, TechCompany, super()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Company:  # class definition stored
class TechCompany(Company):  # class definition stored
company = ...  # assigns a value to the variable
print(company)
tech_company = ...  # assigns a value to the variable
print(tech_company)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Company(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Company, TechCompany are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → company = ...  # stored in memory
#   → print(company)
#   → tech_company = ...  # stored in memory
#   → print(tech_company)
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Company(...))

"""

"""
Problem 531:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Gadget:
    
        def operate(self):
            return 'Operate gadget'
    class Smartwatch(Gadget):
    
        def __init__(self, heart_rate_monitor):
            super().__init__()
            self.heart_rate_monitor = heart_rate_monitor
    
        def __str__(self):
            return f"Heart Rate Monitor: {('Enabled' if self.heart_rate_monitor else 'Disabled')}"
#
class Gadget:  # defines a new type
    def operate(self):  # method of Gadget
        return 'Operate gadget'  # method of Gadget
class Smartwatch(Gadget):  # defines a new type
    def __init__(self, heart_rate_monitor):  # method of Smartwatch
        super().__init__()  # method of Smartwatch
        self.heart_rate_monitor = heart_rate_monitor  # method of Smartwatch
    def __str__(self):  # method of Smartwatch
        return f"Heart Rate Monitor: {('Enabled' if self.heart_rate_monitor else 'Disabled')}"  # method of Smartwatch
#
# Built-in functions: Gadget, Smartwatch, super()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Gadget:  # class definition stored
class Smartwatch(Gadget):  # class definition stored
gadget = ...  # assigns a value to the variable
print(gadget.operate(...))
smartwatch = ...  # assigns a value to the variable
print(smartwatch.operate(...))
print(smartwatch)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Gadget(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Smartwatch, Gadget are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → gadget = ...  # stored in memory
#   → print(gadget.operate(...))
#   → smartwatch = ...  # stored in memory
#   → print(smartwatch.operate(...))
#   → print(smartwatch)
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Gadget(...))

"""

"""
Problem 532:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Trainer:
    
        def train(self):
            return 'Training session'
    class FitnessTrainer(Trainer):
    
        def train(self):
            print('Train body')
#
class Trainer:  # defines a new type
    def train(self):  # method of Trainer
        return 'Training session'  # method of Trainer
class FitnessTrainer(Trainer):  # defines a new type
    def train(self):  # method of FitnessTrainer
        print('Train body')  # method of FitnessTrainer
#
# Built-in functions: FitnessTrainer, Trainer()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Trainer:  # class definition stored
class FitnessTrainer(Trainer):  # class definition stored
trainer = ...  # assigns a value to the variable
print(trainer.train(...))
fitness_trainer = ...  # assigns a value to the variable
fitness_trainer.train()
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Trainer(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes FitnessTrainer, Trainer are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → trainer = ...  # stored in memory
#   → print(trainer.train(...))
#   → fitness_trainer = ...  # stored in memory
#   → fitness_trainer.train()
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Trainer(...))

"""

"""
Problem 533:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Book:
    
        def read(self):
            return 'Read the book'
    class ComicBook(Book):
    
        def read(self):
            print('Read with pictures')
#
class Book:  # defines a new type
    def read(self):  # method of Book
        return 'Read the book'  # method of Book
class ComicBook(Book):  # defines a new type
    def read(self):  # method of ComicBook
        print('Read with pictures')  # method of ComicBook
#
# Built-in functions: Book, ComicBook()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Book:  # class definition stored
class ComicBook(Book):  # class definition stored
book = ...  # assigns a value to the variable
print(book.read(...))
comic_book = ...  # assigns a value to the variable
comic_book.read()
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Book(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Book, ComicBook are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → book = ...  # stored in memory
#   → print(book.read(...))
#   → comic_book = ...  # stored in memory
#   → comic_book.read()
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Book(...))

"""

"""
Problem 534:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Software:
    
        def __init__(self, name, version):
            self.name = name
            self.version = version
    
        def __str__(self):
            return f'Name: {self.name}, Version: {self.version}'
    class GameSoftware(Software):
    
        def __init__(self, name, version, genre):
            super().__init__(name, version)
            self.genre = genre
    
        def __str__(self):
            return f'Name: {self.name}, Version: {self.version}, Genre: {self.genre}'
#
class Software:  # defines a new type
    def __init__(self, name, version):  # method of Software
        self.name = name  # method of Software
        self.version = version  # method of Software
    def __str__(self):  # method of Software
        return f'Name: {self.name}, Version: {self.version}'  # method of Software
class GameSoftware(Software):  # defines a new type
    def __init__(self, name, version, genre):  # method of GameSoftware
        super().__init__(name, version)  # method of GameSoftware
        self.genre = genre  # method of GameSoftware
    def __str__(self):  # method of GameSoftware
        return f'Name: {self.name}, Version: {self.version}, Genre: {self.genre}'  # method of GameSoftware
#
# Built-in functions: GameSoftware, Software, super()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Software:  # class definition stored
class GameSoftware(Software):  # class definition stored
software = ...  # assigns a value to the variable
print(software)
game_software = ...  # assigns a value to the variable
print(game_software)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Software(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes GameSoftware, Software are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → software = ...  # stored in memory
#   → print(software)
#   → game_software = ...  # stored in memory
#   → print(game_software)
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Software(...))

"""

"""
Problem 535:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_letter(s):  # defines a function with parameters s
    return s.count('a')  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
# Built-in functions: sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_letter(string))  # count_letter() runs first, then print() outputs the result
count_letter(s)  # arguments evaluated first, then function body runs
print(count_letter(10))  # count_letter() runs first, then print() outputs the result
c == 'a'  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_letter(s):  # stored in memory, not executed yet
string = ...  # assigns a value to the variable
print(count_letter(...))  # count_letter() runs with s=string
#   → count = 0
#   → for c in s:
#   →     if c == 'a':
#   →         count += 1
#   → return count
def count_letter(s):  # stored in memory, not executed yet
def count_letter(s):  # stored in memory, not executed yet
s = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_letter(...))  # count_letter() runs with s=10
#   → count = 0
#   → for c in s:
#   →     if c == 'a':
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_letter is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → print(count_letter(...))  # count_letter() runs first → value goes to print()
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_letter(...))  # count_letter() runs first → value goes to print()
#
# Loop: takes one item from s, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 536:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_number(num):  # defines a function with parameters num
    return num.count(5)  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
# Built-in functions: sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_number(number))  # count_number() runs first, then print() outputs the result
count_number(num)  # arguments evaluated first, then function body runs
print(count_number(25))  # count_number() runs first, then print() outputs the result
c == 5  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_number(num):  # stored in memory, not executed yet
number = ...  # assigns a value to the variable
print(count_number(...))  # count_number() runs with num=number
#   → count = 0
#   → for c in num:
#   →     if c == 5:
#   →         count += 1
#   → return count
def count_number(num):  # stored in memory, not executed yet
def count_number(num):  # stored in memory, not executed yet
num = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_number(...))  # count_number() runs with num=25
#   → count = 0
#   → for c in num:
#   →     if c == 5:
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_number is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → number = ...  # stored in memory
#   → print(count_number(...))  # count_number() runs first → value goes to print()
#   → num = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_number(...))  # count_number() runs first → value goes to print()
#
# Loop: takes one item from num, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 537:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_hello(string):  # defines a function with parameters string
    return string.count('hello')  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
# Built-in functions: sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_hello(string))  # count_hello() runs first, then print() outputs the result
print(count_hello('world'))  # count_hello() runs first, then print() outputs the result
c == 'hello'  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_hello(string):  # stored in memory, not executed yet
string = ...  # assigns a value to the variable
print(count_hello(...))  # count_hello() runs with string=string
#   → count = 0
#   → for c in string:
#   →     if c == 'hello':
#   →         count += 1
#   → return count
def count_hello(string):  # stored in memory, not executed yet
def count_hello(string):  # stored in memory, not executed yet
string = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_hello(...))  # count_hello() runs with string='world'
#   → count = 0
#   → for c in string:
#   →     if c == 'hello':
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_hello is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → print(count_hello(...))  # count_hello() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_hello(...))  # count_hello() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 538:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count(string):  # defines a function with parameters string
    return string.count('#')  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
# Built-in functions: sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count(string))  # count() runs first, then print() outputs the result
print(count('world'))  # count() runs first, then print() outputs the result
c == '#'  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count(string):  # stored in memory, not executed yet
string = ...  # assigns a value to the variable
print(count(...))  # count() runs with string=string
#   → count = 0
#   → for c in string:
#   →     if c == '#':
#   →         count += 1
#   → return count
def count(string):  # stored in memory, not executed yet
def count(string):  # stored in memory, not executed yet
string = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count(...))  # count() runs with string='world'
#   → count = 0
#   → for c in string:
#   →     if c == '#':
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → print(count(...))  # count() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count(...))  # count() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 540:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_number(num):  # defines a function with parameters num
    return num.count(0)  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
# Built-in functions: str, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_number(num))  # count_number() runs first, then print() outputs the result
main(lst)  # arguments evaluated first, then function body runs
print(count_number(25))  # count_number() runs first, then print() outputs the result
c == 0  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_number(num):  # stored in memory, not executed yet
num = ...  # assigns a value to the variable
print(count_number(...))  # count_number() runs with num=num
#   → count = 0
#   → for c in num:
#   →     if c == 0:
#   →         count += 1
#   → return count
def main(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
main(lst)  # calls main with lst=lst
#   → total = 0
#   → for num in lst:
#   →     total += str(num).count('0')
#   → print(total)
def count_number(num):  # stored in memory, not executed yet
def count_number(num):  # stored in memory, not executed yet
num = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_number(...))  # count_number() runs with num=25
#   → count = 0
#   → for c in num:
#   →     if c == 0:
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — count_number, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → print(count_number(...))  # count_number() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → main(lst)  # jumps into main(), runs body, returns
#   → num = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_number(...))  # count_number() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 544:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_letters(lst):  # defines a function with parameters lst
    total_count = 0
    for word in lst:
        total_count += word.count('e')
    return total_count  # return sends the result back to the caller
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_letters(lst))  # count_letters() runs first, then print() outputs the result
print(count_letters(?))  # count_letters() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_letters(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(count_letters(...))  # count_letters() runs with lst=lst
#   → return total_count
def count_letters(lst):  # stored in memory, not executed yet
def count_letters(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_letters(...))  # count_letters() runs with lst=[1, 3, 5, 7]
#   → return total_count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_letters is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(count_letters(...))  # count_letters() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_letters(...))  # count_letters() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done

"""

"""
Problem 545:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_elements_in_lst(lst, element):  # defines a function with parameters lst, element
    return lst.count(element)  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
# Built-in functions: sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_elements_in_lst(lst, element))  # count_elements_in_lst() runs first, then print() outputs the result
print(count_elements_in_lst(?, 25))  # count_elements_in_lst() runs first, then print() outputs the result
c == element  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_elements_in_lst(lst, element):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
element = ...  # assigns a value to the variable
print(count_elements_in_lst(...))  # count_elements_in_lst() runs with lst=lst, element=element
#   → count = 0
#   → for c in lst:
#   →     if c == element:
#   →         count += 1
#   → return count
def count_elements_in_lst(lst, element):  # stored in memory, not executed yet
def count_elements_in_lst(lst, element):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
element = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_elements_in_lst(...))  # count_elements_in_lst() runs with lst=[1, 3, 5, 7], element=25
#   → count = 0
#   → for c in lst:
#   →     if c == element:
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_elements_in_lst is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → element = ...  # stored in memory
#   → print(count_elements_in_lst(...))  # count_elements_in_lst() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → element = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_elements_in_lst(...))  # count_elements_in_lst() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 546:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_test_occurrences(s):  # defines a function with parameters s
    return s.count('test')  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
# Built-in functions: sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_test_occurrences(s))  # count_test_occurrences() runs first, then print() outputs the result
print(count_test_occurrences(10))  # count_test_occurrences() runs first, then print() outputs the result
c == 'test'  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_test_occurrences(s):  # stored in memory, not executed yet
s = ...  # assigns a value to the variable
print(count_test_occurrences(...))  # count_test_occurrences() runs with s=s
#   → count = 0
#   → for c in s:
#   →     if c == 'test':
#   →         count += 1
#   → return count
def count_test_occurrences(s):  # stored in memory, not executed yet
def count_test_occurrences(s):  # stored in memory, not executed yet
s = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_test_occurrences(...))  # count_test_occurrences() runs with s=10
#   → count = 0
#   → for c in s:
#   →     if c == 'test':
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_test_occurrences is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → s = ...  # stored in memory
#   → print(count_test_occurrences(...))  # count_test_occurrences() runs first → value goes to print()
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_test_occurrences(...))  # count_test_occurrences() runs first → value goes to print()
#
# Loop: takes one item from s, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 547:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_floating_numbers(lst, number):  # defines a function with parameters lst, number
    return lst.count(number)  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
# Built-in functions: sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_floating_numbers(?, 1.5))  # count_floating_numbers() runs first, then print() outputs the result
count_floating_numbers(lst, number)  # arguments evaluated first, then function body runs
print(count_floating_numbers(?, 25))  # count_floating_numbers() runs first, then print() outputs the result
c == number  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_floating_numbers(lst, number):  # stored in memory, not executed yet
print(count_floating_numbers(...))  # count_floating_numbers() runs with lst=[1.5, 2.0, 1.5, 3.5], number=1.5
#   → count = 0
#   → for c in lst:
#   →     if c == number:
#   →         count += 1
#   → return count
def count_floating_numbers(lst, number):  # stored in memory, not executed yet
def count_floating_numbers(lst, number):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
number = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_floating_numbers(...))  # count_floating_numbers() runs with lst=[1, 3, 5, 7], number=25
#   → count = 0
#   → for c in lst:
#   →     if c == number:
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_floating_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(count_floating_numbers(...))  # count_floating_numbers() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_floating_numbers(...))  # count_floating_numbers() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 548:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_floating_numbers(lst, number):  # defines a function with parameters lst, number
    return lst.count(number)  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
# Built-in functions: sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_floating_numbers(lst, number))  # count_floating_numbers() runs first, then print() outputs the result
print(count_floating_numbers(?, 25))  # count_floating_numbers() runs first, then print() outputs the result
c == number  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_floating_numbers(lst, number):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
number = ...  # assigns a value to the variable
print(count_floating_numbers(...))  # count_floating_numbers() runs with lst=lst, number=number
#   → count = 0
#   → for c in lst:
#   →     if c == number:
#   →         count += 1
#   → return count
def count_floating_numbers(lst, number):  # stored in memory, not executed yet
def count_floating_numbers(lst, number):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
number = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_floating_numbers(...))  # count_floating_numbers() runs with lst=[1, 3, 5, 7], number=25
#   → count = 0
#   → for c in lst:
#   →     if c == number:
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_floating_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → number = ...  # stored in memory
#   → print(count_floating_numbers(...))  # count_floating_numbers() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_floating_numbers(...))  # count_floating_numbers() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 549:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_uppercase(string):  # defines a function with parameters string
    total_uppercase = 0
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        total_uppercase += string.count(char)
    return total_uppercase  # return sends the result back to the caller
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_uppercase(string))  # count_uppercase() runs first, then print() outputs the result
print(count_uppercase('world'))  # count_uppercase() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_uppercase(string):  # stored in memory, not executed yet
string = ...  # assigns a value to the variable
print(count_uppercase(...))  # count_uppercase() runs with string=string
#   → return total_uppercase
def count_uppercase(string):  # stored in memory, not executed yet
def count_uppercase(string):  # stored in memory, not executed yet
string = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_uppercase(...))  # count_uppercase() runs with string='world'
#   → return total_uppercase
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_uppercase is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → print(count_uppercase(...))  # count_uppercase() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_uppercase(...))  # count_uppercase() runs first → value goes to print()
#
# Loop: takes one item from 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', runs body, repeats until done

"""

"""
Problem 550:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_digit(num, digit):  # defines a function with parameters num, digit
    return str(num).count(str(digit))  # return sends the result back to the caller
#
# Built-in functions: str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_digit(12345, 3))  # count_digit() runs first, then print() outputs the result
count_digit(num, digit)  # arguments evaluated first, then function body runs
print(count_digit(25, 25))  # count_digit() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_digit(num, digit):  # stored in memory, not executed yet
print(count_digit(...))  # count_digit() runs with num=12345, digit=3
#   → return str(num).count(str(digit))
def count_digit(num, digit):  # stored in memory, not executed yet
def count_digit(num, digit):  # stored in memory, not executed yet
num = ...  # assigns a value to the variable
digit = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_digit(...))  # count_digit() runs with num=25, digit=25
#   → return str(num).count(str(digit))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_digit is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(count_digit(...))  # count_digit() runs first → value goes to print()
#   → num = ...  # stored in memory
#   → digit = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_digit(...))  # count_digit() runs first → value goes to print()

"""

"""
Problem 551:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_letters(string):  # defines a function with parameters string
    letter_count = {}
    for letter in string.lower():
        letter_count[letter] = string.lower().count(letter)
    return letter_count  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: input()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_letters(string))  # count_letters() runs first, then print() outputs the result
print(count_letters('world'))  # count_letters() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_letters(string):  # stored in memory, not executed yet
string = ...  # assigns a value to the variable
print(count_letters(...))  # count_letters() runs with string=string
#   → return letter_count
def count_letters(string):  # stored in memory, not executed yet
def count_letters(string):  # stored in memory, not executed yet
string = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_letters(...))  # count_letters() runs with string='world'
#   → return letter_count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_letters is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → print(count_letters(...))  # count_letters() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_letters(...))  # count_letters() runs first → value goes to print()
#
# Loop: takes one item from string.lower(...), runs body, repeats until done

"""

"""
Problem 552:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_text(string):  # defines a function with parameters string
    string = string.lower()
    return string.count('python')  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
# Built-in functions: sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_text(string))  # count_text() runs first, then print() outputs the result
print(count_text('world'))  # count_text() runs first, then print() outputs the result
c == 'python'  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_text(string):  # stored in memory, not executed yet
string = ...  # assigns a value to the variable
print(count_text(...))  # count_text() runs with string=string
#   → count = 0
#   → for c in string:
#   →     if c == 'python':
#   →         count += 1
#   → return count
def count_text(string):  # stored in memory, not executed yet
def count_text(string):  # stored in memory, not executed yet
string = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_text(...))  # count_text() runs with string='world'
#   → count = 0
#   → for c in string:
#   →     if c == 'python':
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_text is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → print(count_text(...))  # count_text() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_text(...))  # count_text() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 553:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_item_in_dict_list(dict_list, item):  # defines a function with parameters dict_list, item
    return dict_list.count(item)  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
# Built-in functions: sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_item_in_dict_list(dict_list, ?))  # count_item_in_dict_list() runs first, then print() outputs the result
count_item_in_dict_list(dict_list, item)  # arguments evaluated first, then function body runs
print(count_item_in_dict_list(?, 25))  # count_item_in_dict_list() runs first, then print() outputs the result
c == item  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_item_in_dict_list(dict_list, item):  # stored in memory, not executed yet
dict_list = ...  # assigns a value to the variable
print(count_item_in_dict_list(...))  # count_item_in_dict_list() runs with dict_list=dict_list, item=?
#   → count = 0
#   → for c in dict_list:
#   →     if c == item:
#   →         count += 1
#   → return count
def count_item_in_dict_list(dict_list, item):  # stored in memory, not executed yet
def count_item_in_dict_list(dict_list, item):  # stored in memory, not executed yet
dict_list = ...  # assigns a value to the variable
item = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_item_in_dict_list(...))  # count_item_in_dict_list() runs with dict_list=[4, 1, 8, 6, 3], item=25
#   → count = 0
#   → for c in dict_list:
#   →     if c == item:
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_item_in_dict_list is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dict_list = ...  # stored in memory
#   → print(count_item_in_dict_list(...))  # count_item_in_dict_list() runs first → value goes to print()
#   → dict_list = ...  # stored in memory
#   → item = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_item_in_dict_list(...))  # count_item_in_dict_list() runs first → value goes to print()
#
# Loop: takes one item from dict_list, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 554:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_letters(lst):  # defines a function with parameters lst
    total_count = 0
    for string in lst:
        total_count += string.count('z')
    return total_count  # return sends the result back to the caller
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_letters(lst))  # count_letters() runs first, then print() outputs the result
print(count_letters(?))  # count_letters() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_letters(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(count_letters(...))  # count_letters() runs with lst=lst
#   → return total_count
def count_letters(lst):  # stored in memory, not executed yet
def count_letters(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_letters(...))  # count_letters() runs with lst=[1, 3, 5, 7]
#   → return total_count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_letters is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(count_letters(...))  # count_letters() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_letters(...))  # count_letters() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done

"""

"""
Problem 555:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_asterisks(s):  # defines a function with parameters s
    return s.count('*')  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
# Built-in functions: sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_asterisks(s))  # count_asterisks() runs first, then print() outputs the result
print(count_asterisks(10))  # count_asterisks() runs first, then print() outputs the result
c == '*'  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_asterisks(s):  # stored in memory, not executed yet
s = ...  # assigns a value to the variable
print(count_asterisks(...))  # count_asterisks() runs with s=s
#   → count = 0
#   → for c in s:
#   →     if c == '*':
#   →         count += 1
#   → return count
def count_asterisks(s):  # stored in memory, not executed yet
def count_asterisks(s):  # stored in memory, not executed yet
s = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_asterisks(...))  # count_asterisks() runs with s=10
#   → count = 0
#   → for c in s:
#   →     if c == '*':
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_asterisks is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → s = ...  # stored in memory
#   → print(count_asterisks(...))  # count_asterisks() runs first → value goes to print()
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_asterisks(...))  # count_asterisks() runs first → value goes to print()
#
# Loop: takes one item from s, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 556:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_substring(s, substring):  # defines a function with parameters s, substring
    return s.count(substring)  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
# Built-in functions: sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_substring(s, substring))  # count_substring() runs first, then print() outputs the result
print(count_substring(10, 'world'))  # count_substring() runs first, then print() outputs the result
c == substring  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_substring(s, substring):  # stored in memory, not executed yet
s = ...  # assigns a value to the variable
substring = ...  # assigns a value to the variable
print(count_substring(...))  # count_substring() runs with s=s, substring=substring
#   → count = 0
#   → for c in s:
#   →     if c == substring:
#   →         count += 1
#   → return count
def count_substring(s, substring):  # stored in memory, not executed yet
def count_substring(s, substring):  # stored in memory, not executed yet
s = ...  # assigns a value to the variable
substring = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_substring(...))  # count_substring() runs with s=10, substring='world'
#   → count = 0
#   → for c in s:
#   →     if c == substring:
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_substring is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → s = ...  # stored in memory
#   → substring = ...  # stored in memory
#   → print(count_substring(...))  # count_substring() runs first → value goes to print()
#   → s = ...  # stored in memory
#   → substring = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_substring(...))  # count_substring() runs first → value goes to print()
#
# Loop: takes one item from s, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 557:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_lines_with_word(filename, word):  # defines a function with parameters filename, word
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if line.lower().count(word.lower()) > 0:
                count += 1
    return count  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: >
# Built-in functions: len, open, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_lines_with_word(filename, word))  # count_lines_with_word() runs first, then print() outputs the result
print(count_lines_with_word(25, 'coding'))  # count_lines_with_word() runs first, then print() outputs the result
line.lower(...).count(...) > 0  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_lines_with_word(filename, word):  # stored in memory, not executed yet
filename = ...  # assigns a value to the variable
word = ...  # assigns a value to the variable
print(count_lines_with_word(...))  # count_lines_with_word() runs with filename=filename, word=word
#   → return len([line for line in file if line.lower().count(word.lower()) > 0])
def count_lines_with_word(filename, word):  # stored in memory, not executed yet
def count_lines_with_word(filename, word):  # stored in memory, not executed yet
filename = ...  # assigns a value to the variable
word = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_lines_with_word(...))  # count_lines_with_word() runs with filename=25, word='coding'
#   → return len([line for line in file if line.lower().count(word.lower()) > 0])
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_lines_with_word is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → filename = ...  # stored in memory
#   → word = ...  # stored in memory
#   → print(count_lines_with_word(...))  # count_lines_with_word() runs first → value goes to print()
#   → filename = ...  # stored in memory
#   → word = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_lines_with_word(...))  # count_lines_with_word() runs first → value goes to print()
#
# Loop: takes one item from file, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 558:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_email_domain(email_list, domain):  # defines a function with parameters email_list, domain
    count = 0
    for email in email_list:
        email_domain = email.split('@')[-1]
        if email_domain == domain:
            count += 1
    return count  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
# Built-in functions: len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_email_domain(email_list, domain))  # count_email_domain() runs first, then print() outputs the result
print(count_email_domain(?, 25))  # count_email_domain() runs first, then print() outputs the result
email_domain == domain  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_email_domain(email_list, domain):  # stored in memory, not executed yet
email_list = ...  # assigns a value to the variable
domain = ...  # assigns a value to the variable
print(count_email_domain(...))  # count_email_domain() runs with email_list=email_list, domain=domain
#   → return len([email for email in email_list if email_domain == domain])
def count_email_domain(email_list, domain):  # stored in memory, not executed yet
def count_email_domain(email_list, domain):  # stored in memory, not executed yet
email_list = ...  # assigns a value to the variable
domain = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_email_domain(...))  # count_email_domain() runs with email_list=[4, 1, 8, 6, 3], domain=25
#   → return len([email for email in email_list if email_domain == domain])
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_email_domain is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → email_list = ...  # stored in memory
#   → domain = ...  # stored in memory
#   → print(count_email_domain(...))  # count_email_domain() runs first → value goes to print()
#   → email_list = ...  # stored in memory
#   → domain = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_email_domain(...))  # count_email_domain() runs first → value goes to print()
#
# Loop: takes one item from email_list, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 559:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_word(sentences):  # defines a function with parameters sentences
    count = 0
    for sentence in sentences:
        count += sentence.count('happy')
    return count  # return sends the result back to the caller
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_word(sentences))  # count_word() runs first, then print() outputs the result
print(count_word(?))  # count_word() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_word(sentences):  # stored in memory, not executed yet
sentences = ...  # assigns a value to the variable
print(count_word(...))  # count_word() runs with sentences=sentences
#   → return count
def count_word(sentences):  # stored in memory, not executed yet
def count_word(sentences):  # stored in memory, not executed yet
sentences = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_word(...))  # count_word() runs with sentences=[4, 1, 8, 6, 3]
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_word is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → sentences = ...  # stored in memory
#   → print(count_word(...))  # count_word() runs first → value goes to print()
#   → sentences = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_word(...))  # count_word() runs first → value goes to print()
#
# Loop: takes one item from sentences, runs body, repeats until done

"""

"""
Problem 560:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_exclamations(lst):  # defines a function with parameters lst
    count = 0
    for string in lst:
        count += string.count('!')
    return count  # return sends the result back to the caller
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_exclamations(lst))  # count_exclamations() runs first, then print() outputs the result
print(count_exclamations(?))  # count_exclamations() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_exclamations(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(count_exclamations(...))  # count_exclamations() runs with lst=lst
#   → return count
def count_exclamations(lst):  # stored in memory, not executed yet
def count_exclamations(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_exclamations(...))  # count_exclamations() runs with lst=[1, 3, 5, 7]
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_exclamations is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(count_exclamations(...))  # count_exclamations() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_exclamations(...))  # count_exclamations() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done

"""

"""
Problem 562:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_word_occurrences(lst, word):  # defines a function with parameters lst, word
    return lst.count(word)  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
# Built-in functions: sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_word_occurrences(words, word_to_count))  # count_word_occurrences() runs first, then print() outputs the result
count_word_occurrences(lst, word)  # arguments evaluated first, then function body runs
print(count_word_occurrences(?, 'coding'))  # count_word_occurrences() runs first, then print() outputs the result
c == word  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_word_occurrences(lst, word):  # stored in memory, not executed yet
words = ...  # assigns a value to the variable
word_to_count = ...  # assigns a value to the variable
print(count_word_occurrences(...))  # count_word_occurrences() runs with lst=words, word=word_to_count
#   → count = 0
#   → for c in lst:
#   →     if c == word:
#   →         count += 1
#   → return count
def count_word_occurrences(lst, word):  # stored in memory, not executed yet
def count_word_occurrences(lst, word):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
word = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_word_occurrences(...))  # count_word_occurrences() runs with lst=[1, 3, 5, 7], word='coding'
#   → count = 0
#   → for c in lst:
#   →     if c == word:
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_word_occurrences is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → words = ...  # stored in memory
#   → word_to_count = ...  # stored in memory
#   → print(count_word_occurrences(...))  # count_word_occurrences() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → word = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_word_occurrences(...))  # count_word_occurrences() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 563:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_x_in_mixed_list(lst):  # defines a function with parameters lst
    count = 0
    for item in lst:
        if isinstance(item, str):
            count += item.count('x')
    return count  # return sends the result back to the caller
#
# Keywords: for | if/else
# Built-in functions: isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_x_in_mixed_list(mixed_list))  # count_x_in_mixed_list() runs first, then print() outputs the result
count_x_in_mixed_list(lst)  # arguments evaluated first, then function body runs
print(count_x_in_mixed_list(?))  # count_x_in_mixed_list() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_x_in_mixed_list(lst):  # stored in memory, not executed yet
mixed_list = ...  # assigns a value to the variable
print(count_x_in_mixed_list(...))  # count_x_in_mixed_list() runs with lst=mixed_list
#   → return count
def count_x_in_mixed_list(lst):  # stored in memory, not executed yet
def count_x_in_mixed_list(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_x_in_mixed_list(...))  # count_x_in_mixed_list() runs with lst=[1, 3, 5, 7]
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_x_in_mixed_list is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → mixed_list = ...  # stored in memory
#   → print(count_x_in_mixed_list(...))  # count_x_in_mixed_list() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_x_in_mixed_list(...))  # count_x_in_mixed_list() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 565:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def square_lst(lst):  # defines a function with parameters lst
    return list(map(square, lst))  # return sends the result back to the caller
#
# Operators: **
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(square_lst(lst))  # square_lst() runs first, then print() outputs the result
print(square_lst(?))  # square_lst() runs first, then print() outputs the result
num ** 2  # num → then 2 → then **
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def square_lst(lst):  # stored in memory, not executed yet
def square(num):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(square_lst(...))  # square_lst() runs with lst=lst
#   → return list(map(square, lst))
def square_lst(lst):  # stored in memory, not executed yet
def square_lst(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(square_lst(...))  # square_lst() runs with lst=[1, 3, 5, 7]
#   → return list(map(square, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — square, square_lst are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(square_lst(...))  # square_lst() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(square_lst(...))  # square_lst() runs first → value goes to print()

"""

"""
Problem 566:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def filter_odd_numbers(lst):  # defines a function with parameters lst
    return list(filter(is_odd, lst))  # return sends the result back to the caller
#
# Operators: % !=
# Built-in functions: filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(filter_odd_numbers(lst))  # filter_odd_numbers() runs first, then print() outputs the result
print(filter_odd_numbers(?))  # filter_odd_numbers() runs first, then print() outputs the result
? != 0  # evaluated as True or False → picks which branch
x % 2  # x → then 2 → then %
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def filter_odd_numbers(lst):  # stored in memory, not executed yet
def is_odd(x):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(filter_odd_numbers(...))  # filter_odd_numbers() runs with lst=lst
#   → return list(filter(is_odd, lst))
def filter_odd_numbers(lst):  # stored in memory, not executed yet
def filter_odd_numbers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(filter_odd_numbers(...))  # filter_odd_numbers() runs with lst=[1, 3, 5, 7]
#   → return list(filter(is_odd, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — filter_odd_numbers, is_odd are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(filter_odd_numbers(...))  # filter_odd_numbers() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_odd_numbers(...))  # filter_odd_numbers() runs first → value goes to print()

"""

"""
Problem 567:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def even_num(num):  # defines a function with parameters num
    return num % 2 == 0  # return sends the result back to the caller
#
# Operators: % ==
# Built-in functions: filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(filters_even_numbers(?))  # filters_even_numbers() runs first, then print() outputs the result
even_num(num)  # arguments evaluated first, then function body runs
print(even_num(25))  # even_num() runs first, then print() outputs the result
? == 0  # evaluated as True or False → picks which branch
num % 2  # num → then 2 → then %
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def even_num(num):  # stored in memory, not executed yet
def filters_even_numbers(lst):  # stored in memory, not executed yet
print(filters_even_numbers(...))  # filters_even_numbers() runs with lst=[1, 2, 3, 4, 5, 6]
#   → return list(filter(even_num, lst))
def even_num(num):  # stored in memory, not executed yet
def even_num(num):  # stored in memory, not executed yet
num = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(even_num(...))  # even_num() runs with num=25
#   → return num % 2 == 0
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — even_num, filters_even_numbers are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(filters_even_numbers(...))  # filters_even_numbers() runs first → value goes to print()
#   → num = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(even_num(...))  # even_num() runs first → value goes to print()

"""

"""
Problem 568:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def convert_to_uppercase(lst):  # defines a function with parameters lst
    return list(map(str.upper, lst))  # return sends the result back to the caller
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(convert_to_uppercase(lst))  # convert_to_uppercase() runs first, then print() outputs the result
print(convert_to_uppercase(?))  # convert_to_uppercase() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def convert_to_uppercase(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(convert_to_uppercase(...))  # convert_to_uppercase() runs with lst=lst
#   → return list(map(str.upper, lst))
def convert_to_uppercase(lst):  # stored in memory, not executed yet
def convert_to_uppercase(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(convert_to_uppercase(...))  # convert_to_uppercase() runs with lst=[1, 3, 5, 7]
#   → return list(map(str.upper, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only convert_to_uppercase is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(convert_to_uppercase(...))  # convert_to_uppercase() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(convert_to_uppercase(...))  # convert_to_uppercase() runs first → value goes to print()

"""

"""
Problem 569:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def empty_strings(lst):  # defines a function with parameters lst
    return list(filter(call_filter, lst))  # return sends the result back to the caller
#
# Operators: !=
# Built-in functions: filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(empty_strings(lst))  # empty_strings() runs first, then print() outputs the result
print(empty_strings(?))  # empty_strings() runs first, then print() outputs the result
string.strip(...) != ''  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def empty_strings(lst):  # stored in memory, not executed yet
def call_filter(string):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(empty_strings(...))  # empty_strings() runs with lst=lst
#   → return list(filter(call_filter, lst))
def empty_strings(lst):  # stored in memory, not executed yet
def empty_strings(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(empty_strings(...))  # empty_strings() runs with lst=[1, 3, 5, 7]
#   → return list(filter(call_filter, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — call_filter, empty_strings are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(empty_strings(...))  # empty_strings() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(empty_strings(...))  # empty_strings() runs first → value goes to print()

"""

"""
Problem 570:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def multiply_lst(lst):  # defines a function with parameters lst
    def multiply_by_five(x):
        return x * 5
    return list(map(multiply_by_five, lst))  # return sends the result back to the caller
#
# Keywords: for
# Operators: *
# Built-in functions: list, map, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(multiply_lst(lst))  # multiply_lst() runs first, then print() outputs the result
print(multiply_lst(?))  # multiply_lst() runs first, then print() outputs the result
x * 5  # x → then 5 → then *
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def multiply_lst(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(multiply_lst(...))  # multiply_lst() runs with lst=lst
#   → return pow(x, 5)
def multiply_lst(lst):  # stored in memory, not executed yet
def multiply_lst(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(multiply_lst(...))  # multiply_lst() runs with lst=[1, 3, 5, 7]
#   → return pow(x, 5)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only multiply_lst is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(multiply_lst(...))  # multiply_lst() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(multiply_lst(...))  # multiply_lst() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done

"""

"""
Problem 571:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_of_string(lst):  # defines a function with parameters lst
    def len_string(word):
        return len(word)
    return list(map(len_string, lst))  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: len, list, map, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_of_string(lst))  # lst_of_string() runs first, then print() outputs the result
print(lst_of_string(?))  # lst_of_string() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_of_string(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_of_string(...))  # lst_of_string() runs with lst=lst
#   → return sum((1 for _ in word))
def lst_of_string(lst):  # stored in memory, not executed yet
def lst_of_string(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_of_string(...))  # lst_of_string() runs with lst=[1, 3, 5, 7]
#   → return sum((1 for _ in word))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_of_string is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_of_string(...))  # lst_of_string() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_of_string(...))  # lst_of_string() runs first → value goes to print()
#
# Loop: takes one item from word, runs body, repeats until done

"""

"""
Problem 572:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def palindromes(lst):  # defines a function with parameters lst
    def is_palindrome(word):
        return word == word[::-1]
    return list(filter(is_palindrome, lst))  # return sends the result back to the caller
#
# Operators: ==
# Built-in functions: filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(palindromes(?))  # palindromes() runs first, then print() outputs the result
palindromes(lst)  # arguments evaluated first, then function body runs
word == ?  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def palindromes(lst):  # stored in memory, not executed yet
print(palindromes(...))  # palindromes() runs with lst=['radar', 'hello', 'level', 'world']
#   → return word == word[::-1]
def palindromes(lst):  # stored in memory, not executed yet
def palindromes(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(palindromes(...))  # palindromes() runs with lst=[1, 3, 5, 7]
#   → return word == word[::-1]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only palindromes is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(palindromes(...))  # palindromes() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(palindromes(...))  # palindromes() runs first → value goes to print()

"""

"""
Problem 573:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sum_of_lst(lst):  # defines a function with parameters lst
    def add(x, y):
        return x + y
    return reduce(add, lst)  # return sends the result back to the caller
#
# Operators: +
# Built-in functions: reduce, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(sum_of_list(lst))  # sum_of_list() runs first, then print() outputs the result
sum_of_lst(lst)  # arguments evaluated first, then function body runs
print(sum_of_lst(?))  # sum_of_lst() runs first, then print() outputs the result
x + y  # x → then y → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from functools import reduce
def sum_of_lst(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(sum_of_list(...))  # sum_of_list() runs with lst=lst
#   → return reduce(add, lst)
def add(x, y):  # stored in memory, not executed yet
def sum_of_list(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(sum_of_list(...))  # sum_of_list() runs with lst=lst
#   → return reduce(add, lst)
def sum_of_lst(lst):  # stored in memory, not executed yet
def sum_of_lst(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sum_of_lst(...))  # sum_of_lst() runs with lst=[1, 3, 5, 7]
#   → import operator
#   → return operator.add(x, y)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — add, sum_of_list, sum_of_lst are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(sum_of_list(...))  # sum_of_list() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(sum_of_list(...))  # sum_of_list() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum_of_lst(...))  # sum_of_lst() runs first → value goes to print()

"""

"""
Problem 574:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sum_of_lst(lst):  # defines a function with parameters lst
    def add(x, y):
        return x * y
    return reduce(add, lst)  # return sends the result back to the caller
#
# Keywords: for
# Operators: *
# Built-in functions: pow, range, reduce, sum_of_list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(product_of_list(lst))  # product_of_list() runs first, then print() outputs the result
sum_of_lst(lst)  # arguments evaluated first, then function body runs
print(sum_of_lst(?))  # sum_of_lst() runs first, then print() outputs the result
x * y  # x → then y → then *
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from functools import reduce
def sum_of_lst(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(sum_of_list(...))
def multiply(x, y):  # stored in memory, not executed yet
def product_of_list(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(product_of_list(...))  # product_of_list() runs with lst=lst
#   → return reduce(multiply, lst)
def sum_of_lst(lst):  # stored in memory, not executed yet
def sum_of_lst(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sum_of_lst(...))  # sum_of_lst() runs with lst=[1, 3, 5, 7]
#   → return pow(x, y)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — multiply, product_of_list, sum_of_lst are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(sum_of_list(...))
#   → lst = ...  # stored in memory
#   → print(product_of_list(...))  # product_of_list() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum_of_lst(...))  # sum_of_lst() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done

"""

"""
Problem 575:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def capitalize_string(lst):  # defines a function with parameters lst
    return list(map(str.capitalize, lst))  # return sends the result back to the caller
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
capitalize_string(lst)  # arguments evaluated first, then function body runs
print(lst_strings(lst))  # lst_strings() runs first, then print() outputs the result
print(capitalize_string(?))  # capitalize_string() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def capitalize_string(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
capitalize_string(lst)  # calls capitalize_string with lst=lst
#   → return list(map(str.capitalize, lst))
def lst_strings(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_strings(...))  # lst_strings() runs with lst=lst
#   → def capitalize_lst(word):
#   →     word = word.capitalize()
#   →     return word
#   → return list(map(capitalize_lst, lst))
def capitalize_string(lst):  # stored in memory, not executed yet
def capitalize_string(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(capitalize_string(...))  # capitalize_string() runs with lst=[1, 3, 5, 7]
#   → return list(map(str.capitalize, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — capitalize_string, lst_strings are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → capitalize_string(lst)  # jumps into capitalize_string(), runs body, returns
#   → lst = ...  # stored in memory
#   → print(lst_strings(...))  # lst_strings() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(capitalize_string(...))  # capitalize_string() runs first → value goes to print()

"""

"""
Problem 576:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def min_number(x, y):  # defines a function with parameters x, y
    return x if x < y else y  # return sends the result back to the caller
#
# Operators: <
# Built-in functions: reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(number_lst(lst))  # number_lst() runs first, then print() outputs the result
min_number(x, y)  # arguments evaluated first, then function body runs
print(min_number(3, 14))  # min_number() runs first, then print() outputs the result
x < y  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from functools import reduce
def min_number(x, y):  # stored in memory, not executed yet
def number_lst(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(number_lst(...))  # number_lst() runs with lst=lst
#   → return reduce(min_number, lst)
def min_number(x, y):  # stored in memory, not executed yet
def min_number(x, y):  # stored in memory, not executed yet
x = ...  # assigns a value to the variable
y = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(min_number(...))  # min_number() runs with x=3, y=14
#   → return x if x < y else y
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — min_number, number_lst are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(number_lst(...))  # number_lst() runs first → value goes to print()
#   → x = ...  # stored in memory
#   → y = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(min_number(...))  # min_number() runs first → value goes to print()

"""

"""
Problem 577:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def find_max(lst):  # defines a function with parameters lst
    def inner(x, y):
        if x > y:
            return x
        else:
            return y
    return reduce(inner, lst)  # return sends the result back to the caller
#
# Keywords: if/else
# Operators: >
# Built-in functions: reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(find_max(lst))  # find_max() runs first, then print() outputs the result
main(lst)  # arguments evaluated first, then function body runs
print(number_lst(lst))  # number_lst() runs first, then print() outputs the result
print(find_max(?))  # find_max() runs first, then print() outputs the result
x > y  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from functools import reduce
def find_max(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(find_max(...))  # find_max() runs with lst=lst
#   → return x
def main(lst):  # stored in memory, not executed yet
def max_num(x, y):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
main(lst)  # calls main with lst=lst
#   → return reduce(max_num, lst)
from functools import reduce
def min_number(x, y):  # stored in memory, not executed yet
def number_lst(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(number_lst(...))  # number_lst() runs with lst=lst
#   → return reduce(min_number, lst)
def find_max(lst):  # stored in memory, not executed yet
def find_max(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(find_max(...))  # find_max() runs with lst=[1, 3, 5, 7]
#   → return x
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — find_max, main, max_num, min_number, number_lst are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(find_max(...))  # find_max() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → main(lst)  # jumps into main(), runs body, returns
#   → lst = ...  # stored in memory
#   → print(number_lst(...))  # number_lst() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_max(...))  # find_max() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 578:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def list_words(lst):  # defines a function with parameters lst
    def filter_word(word):
        if len(word) > 3:
            return word
    return list(filter(filter_word, lst))  # return sends the result back to the caller
#
# Keywords: if/else
# Operators: >
# Built-in functions: filter, len, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(list_words(lst))  # list_words() runs first, then print() outputs the result
print(list_words(?))  # list_words() runs first, then print() outputs the result
len(...) > 3  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def list_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(list_words(...))  # list_words() runs with lst=lst
#   → return word
def list_words(lst):  # stored in memory, not executed yet
def list_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(list_words(...))  # list_words() runs with lst=[1, 3, 5, 7]
#   → return word
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only list_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(list_words(...))  # list_words() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(list_words(...))  # list_words() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 579:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_strings(lst):  # defines a function with parameters lst
    def concatenate_lst(x, y):
        return x + y
    return reduce(concatenate_lst, lst)  # return sends the result back to the caller
#
# Operators: % +
# Built-in functions: reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_strings(lst))  # lst_strings() runs first, then print() outputs the result
print(lst_strings(?))  # lst_strings() runs first, then print() outputs the result
'%s%s' % ?  # '%s%s' → then ? → then %
x + y  # x → then y → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from functools import reduce
def lst_strings(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_strings(...))  # lst_strings() runs with lst=lst
#   → return '%s%s' % (x, y)
def lst_strings(lst):  # stored in memory, not executed yet
def lst_strings(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_strings(...))  # lst_strings() runs with lst=[1, 3, 5, 7]
#   → return '%s%s' % (x, y)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_strings is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_strings(...))  # lst_strings() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_strings(...))  # lst_strings() runs first → value goes to print()

"""

"""
Problem 580:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def num_lst(lst):  # defines a function with parameters lst
    def is_positive(num):
        return num > 0
    return list(filter(is_positive, lst))  # return sends the result back to the caller
#
# Keywords: if/else
# Operators: > <=
# Built-in functions: filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(num_lst(?))  # num_lst() runs first, then print() outputs the result
num_lst(lst)  # arguments evaluated first, then function body runs
num > 0  # evaluated as True or False → picks which branch
num <= 0  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def num_lst(lst):  # stored in memory, not executed yet
print(num_lst(...))  # num_lst() runs with lst=[?, 0, 1, ?, 2]
#   → return not num <= 0
def num_lst(lst):  # stored in memory, not executed yet
def num_lst(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(num_lst(...))  # num_lst() runs with lst=[1, 3, 5, 7]
#   → return not num <= 0
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only num_lst is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(num_lst(...))  # num_lst() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(num_lst(...))  # num_lst() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 581:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def num_lst(lst):  # defines a function with parameters lst
    def cubed_num(num):
        return num ** 3
    return list(map(cubed_num, lst))  # return sends the result back to the caller
#
# Operators: **
# Built-in functions: list, map, pow()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(num_lst(lst))  # num_lst() runs first, then print() outputs the result
print(num_lst(?))  # num_lst() runs first, then print() outputs the result
num ** 3  # num → then 3 → then **
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def num_lst(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(num_lst(...))  # num_lst() runs with lst=lst
#   → import math
#   → return math.pow(num, 3)
def num_lst(lst):  # stored in memory, not executed yet
def num_lst(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(num_lst(...))  # num_lst() runs with lst=[1, 3, 5, 7]
#   → import math
#   → return math.pow(num, 3)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only num_lst is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(num_lst(...))  # num_lst() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(num_lst(...))  # num_lst() runs first → value goes to print()

"""

"""
Problem 582:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_numbers(lst):  # defines a function with parameters lst
    def square_number(num):
        return num ** 2
    def add(x, y):
        return x + y
    squared_lst = map(square_number, lst)
    return reduce(add, squared_lst)  # return sends the result back to the caller
#
# Operators: + **
# Built-in functions: map, pow, reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_numbers(lst))  # lst_numbers() runs first, then print() outputs the result
print(lst_numbers(?))  # lst_numbers() runs first, then print() outputs the result
num ** 2  # num → then 2 → then **
x + y  # x → then y → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from functools import reduce
def lst_numbers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_numbers(...))  # lst_numbers() runs with lst=lst
#   → import math
#   → return math.pow(num, 2)
def lst_numbers(lst):  # stored in memory, not executed yet
def lst_numbers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_numbers(...))  # lst_numbers() runs with lst=[1, 3, 5, 7]
#   → import math
#   → return math.pow(num, 2)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_numbers(...))  # lst_numbers() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_numbers(...))  # lst_numbers() runs first → value goes to print()

"""

"""
Problem 583:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_2(lst1, lst2):  # defines a function with parameters lst1, lst2
    def combine_names(first_last):
        return f'{first_last[0]} {first_last[1]}'
    return list(map(combine_names, zip(lst1, lst2)))  # return sends the result back to the caller
#
# Built-in functions: list, map, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_2(lst1, lst2))  # lst_2() runs first, then print() outputs the result
print(lst_2(?, ?))  # lst_2() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_2(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
print(lst_2(...))  # lst_2() runs with lst1=lst1, lst2=lst2
#   → return f'{first_last[0]} {first_last[1]}'
def lst_2(lst1, lst2):  # stored in memory, not executed yet
def lst_2(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_2(...))  # lst_2() runs with lst1=[2, 4, 6], lst2=[1, 3, 5]
#   → return f'{first_last[0]} {first_last[1]}'
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_2 is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(lst_2(...))  # lst_2() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_2(...))  # lst_2() runs first → value goes to print()

"""

"""
Problem 584:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def non_alphabetical_string(string):  # defines a function with parameters string
    def is_alpha(word):
        return word.isalpha()
    return list(filter(is_alpha, string))  # return sends the result back to the caller
#
# Built-in functions: filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(non_alphabetical_string(?))  # non_alphabetical_string() runs first, then print() outputs the result
non_alphabetical_string(string)  # arguments evaluated first, then function body runs
print(non_alphabetical_string('world'))  # non_alphabetical_string() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def non_alphabetical_string(string):  # stored in memory, not executed yet
print(non_alphabetical_string(...))  # non_alphabetical_string() runs with string=['hello', 'world', 'abc123', 'python']
#   → return word.isalpha()
def non_alphabetical_string(string):  # stored in memory, not executed yet
def non_alphabetical_string(string):  # stored in memory, not executed yet
string = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(non_alphabetical_string(...))  # non_alphabetical_string() runs with string='world'
#   → return word.isalpha()
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only non_alphabetical_string is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(non_alphabetical_string(...))  # non_alphabetical_string() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(non_alphabetical_string(...))  # non_alphabetical_string() runs first → value goes to print()

"""

"""
Problem 585:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_words(lst):  # defines a function with parameters lst
    def count_word(counts, word):
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
        return counts
    return reduce(count_word, lst, {})  # return sends the result back to the caller
#
# Keywords: if/else
# Operators: in
# Built-in functions: reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_words(lst))  # lst_words() runs first, then print() outputs the result
print(lst_words(?))  # lst_words() runs first, then print() outputs the result
word in counts  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from functools import reduce
def lst_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_words(...))  # lst_words() runs with lst=lst
#   → return counts
def lst_words(lst):  # stored in memory, not executed yet
def lst_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_words(...))  # lst_words() runs with lst=[1, 3, 5, 7]
#   → return counts
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_words(...))  # lst_words() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_words(...))  # lst_words() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 586:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def unique_words(lst):  # defines a function with parameters lst
    result = []
    for word in lst:
        if word not in result:
            result.append(word)
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: not in
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(unique_words(?))  # unique_words() runs first, then print() outputs the result
unique_words(lst)  # arguments evaluated first, then function body runs
word not in result  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def unique_words(lst):  # stored in memory, not executed yet
print(unique_words(...))  # unique_words() runs with lst=['a', 'b', 'a', 'c', 'b']
#   → return list(map(lambda word: word, lst))
def unique_words(lst):  # stored in memory, not executed yet
def unique_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(unique_words(...))  # unique_words() runs with lst=[1, 3, 5, 7]
#   → return list(map(lambda word: word, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only unique_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(unique_words(...))  # unique_words() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(unique_words(...))  # unique_words() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 587:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def word_lst(lst, n):  # defines a function with parameters lst, n
    def longer_than_n(word):
        return len(word) > n
    return list(filter(longer_than_n, lst))  # return sends the result back to the caller
#
# Operators: >
# Built-in functions: filter, len, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(word_lst(?, 3))  # word_lst() runs first, then print() outputs the result
word_lst(lst, n)  # arguments evaluated first, then function body runs
print(word_lst(?, 15))  # word_lst() runs first, then print() outputs the result
len(...) > n  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def word_lst(lst, n):  # stored in memory, not executed yet
print(word_lst(...))  # word_lst() runs with lst=['a', 'ab', 'abc', 'abcd'], n=3
#   → return len(word) > n
def word_lst(lst, n):  # stored in memory, not executed yet
def word_lst(lst, n):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
n = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(word_lst(...))  # word_lst() runs with lst=[1, 3, 5, 7], n=15
#   → return len(word) > n
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only word_lst is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(word_lst(...))  # word_lst() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(word_lst(...))  # word_lst() runs first → value goes to print()

"""

"""
Problem 588:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def apply_lsts(lst):  # defines a function with parameters lst
    def square_num(num):
        return num * num
    def filter_num(num):
        return num % 2 != 0
    squared_lst = list(map(square_num, lst))
    filtered_lst = list(filter(filter_num, squared_lst))
    return filtered_lst  # return sends the result back to the caller
#
# Keywords: for
# Operators: % * !=
# Built-in functions: filter, list, map, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(apply_lsts(lst))  # apply_lsts() runs first, then print() outputs the result
print(apply_lsts(?))  # apply_lsts() runs first, then print() outputs the result
num * num  # num → then num → then *
? != 0  # evaluated as True or False → picks which branch
num % 2  # num → then 2 → then %
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def apply_lsts(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(apply_lsts(...))  # apply_lsts() runs with lst=lst
#   → return pow(num, num)
def apply_lsts(lst):  # stored in memory, not executed yet
def apply_lsts(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(apply_lsts(...))  # apply_lsts() runs with lst=[1, 3, 5, 7]
#   → return pow(num, num)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only apply_lsts is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(apply_lsts(...))  # apply_lsts() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(apply_lsts(...))  # apply_lsts() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done

"""

"""
Problem 589:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sum_nested_list(nested_list):  # defines a function with parameters nested_list
    flattened = reduce(lambda acc, item: acc + item, nested_list, [])
    return reduce(lambda total, number: total + number, flattened, 0)  # return sends the result back to the caller
#
# Operators: +
# Built-in functions: reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(sum_nested_list(?))  # sum_nested_list() runs first, then print() outputs the result
sum_nested_list(nested_list)  # arguments evaluated first, then function body runs
acc + item  # acc → then item → then +
total + number  # total → then number → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from functools import reduce
def sum_nested_list(nested_list):  # stored in memory, not executed yet
print(sum_nested_list(...))  # sum_nested_list() runs with nested_list=[[1, 2], [3, 4], [5]]
#   → return reduce(lambda total, number: total + number, flattened, 0)
def sum_nested_list(nested_list):  # stored in memory, not executed yet
def sum_nested_list(nested_list):  # stored in memory, not executed yet
nested_list = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sum_nested_list(...))  # sum_nested_list() runs with nested_list=[4, 1, 8, 6, 3]
#   → return reduce(lambda total, number: total + number, flattened, 0)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sum_nested_list is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(sum_nested_list(...))  # sum_nested_list() runs first → value goes to print()
#   → nested_list = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum_nested_list(...))  # sum_nested_list() runs first → value goes to print()

"""

"""
Problem 590:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def fibonacci_n_numbers(n):  # defines a function with parameters n
    def fib(acc, _):
        return acc + [acc[-1] + acc[-2]]
    return reduce(fib, range(n - 2), [0, 1])[:n]  # return sends the result back to the caller
#
# Operators: + -
# Built-in functions: range, reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(fibonacci_n_numbers(10))  # fibonacci_n_numbers() runs first, then print() outputs the result
fibonacci_n_numbers(n)  # arguments evaluated first, then function body runs
print(fibonacci_n_numbers(15))  # fibonacci_n_numbers() runs first, then print() outputs the result
acc + [?]  # acc → then [?] → then +
? + ?  # ? → then ? → then +
n - 2  # n → then 2 → then -
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from functools import reduce
def fibonacci_n_numbers(n):  # stored in memory, not executed yet
print(fibonacci_n_numbers(...))  # fibonacci_n_numbers() runs with n=10
#   → return acc + [acc[-1] + acc[-2]]
def fibonacci_n_numbers(n):  # stored in memory, not executed yet
def fibonacci_n_numbers(n):  # stored in memory, not executed yet
n = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(fibonacci_n_numbers(...))  # fibonacci_n_numbers() runs with n=15
#   → return acc + [acc[-1] + acc[-2]]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only fibonacci_n_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(fibonacci_n_numbers(...))  # fibonacci_n_numbers() runs first → value goes to print()
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(fibonacci_n_numbers(...))  # fibonacci_n_numbers() runs first → value goes to print()

"""

"""
Problem 591:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_string(lst):  # defines a function with parameters lst
    def count_vowels(word):
        vowels = 'aeiou'
        count = 0
        for char in word:
            if char in vowels:
                count += 1
        return count
    return list(map(count_vowels, lst))  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: in
# Built-in functions: len, list, map, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_string(lst))  # lst_string() runs first, then print() outputs the result
print(lst_string(?))  # lst_string() runs first, then print() outputs the result
char in vowels  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_string(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_string(...))  # lst_string() runs with lst=lst
#   → return len([char for char in word if char in vowels])
def lst_string(lst):  # stored in memory, not executed yet
def lst_string(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_string(...))  # lst_string() runs with lst=[1, 3, 5, 7]
#   → return len([char for char in word if char in vowels])
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_string is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_string(...))  # lst_string() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_string(...))  # lst_string() runs first → value goes to print()
#
# Loop: takes one item from word, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 592:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sum_even_numbers(lst):  # defines a function with parameters lst
    def is_even(num):
        return num % 2 == 0
    def sum_numbers(x, y):
        return x + y
    even_numbers = filter(is_even, lst)
    return reduce(sum_numbers, even_numbers)  # return sends the result back to the caller
#
# Operators: % + ==
# Built-in functions: filter, reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(sum_even_numbers(lst))  # sum_even_numbers() runs first, then print() outputs the result
print(sum_even_numbers(?))  # sum_even_numbers() runs first, then print() outputs the result
? == 0  # evaluated as True or False → picks which branch
x + y  # x → then y → then +
num % 2  # num → then 2 → then %
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from functools import reduce
def sum_even_numbers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(sum_even_numbers(...))  # sum_even_numbers() runs with lst=lst
#   → return num % 2 == 0
def sum_even_numbers(lst):  # stored in memory, not executed yet
def sum_even_numbers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sum_even_numbers(...))  # sum_even_numbers() runs with lst=[1, 3, 5, 7]
#   → return num % 2 == 0
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sum_even_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(sum_even_numbers(...))  # sum_even_numbers() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum_even_numbers(...))  # sum_even_numbers() runs first → value goes to print()

"""

"""
Problem 593:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_string(lst):  # defines a function with parameters lst
    def longest_string(x, y):
        if len(x) > len(y):
            return x
        else:
            return y
    return reduce(longest_string, lst)  # return sends the result back to the caller
#
# Keywords: if/else
# Operators: >
# Built-in functions: len, reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_string(lst))  # lst_string() runs first, then print() outputs the result
print(lst_string(?))  # lst_string() runs first, then print() outputs the result
len(...) > len(...)  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from functools import reduce
def lst_string(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_string(...))  # lst_string() runs with lst=lst
#   → return x
def lst_string(lst):  # stored in memory, not executed yet
def lst_string(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_string(...))  # lst_string() runs with lst=[1, 3, 5, 7]
#   → return x
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_string is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_string(...))  # lst_string() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_string(...))  # lst_string() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 594:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_num(lst):  # defines a function with parameters lst
    def cumulative(x, y):
        return x + y
    return reduce(cumulative, lst)  # return sends the result back to the caller
#
# Operators: +
# Built-in functions: reduce, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_num(lst))  # lst_num() runs first, then print() outputs the result
print(lst_num(?))  # lst_num() runs first, then print() outputs the result
x + y  # x → then y → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from functools import reduce
def lst_num(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_num(...))  # lst_num() runs with lst=lst
#   → import operator
#   → return operator.add(x, y)
def lst_num(lst):  # stored in memory, not executed yet
def lst_num(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_num(...))  # lst_num() runs with lst=[1, 3, 5, 7]
#   → import operator
#   → return operator.add(x, y)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_num is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_num(...))  # lst_num() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_num(...))  # lst_num() runs first → value goes to print()

"""

"""
Problem 595:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def flatten(lst):  # defines a function with parameters lst
    def concatenate(x, y):
        return x + y
    return reduce(concatenate, lst)  # return sends the result back to the caller
#
# Operators: +
# Built-in functions: reduce, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
flatten(nested_list)  # arguments evaluated first, then function body runs
flatten(lst)  # arguments evaluated first, then function body runs
print(flatten(?))  # flatten() runs first, then print() outputs the result
x + y  # x → then y → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from functools import reduce
def flatten(lst):  # stored in memory, not executed yet
nested_list = ...  # assigns a value to the variable
flattened_list = ...  # assigns a value to the variable
print(flattened_list)
def flatten(lst):  # stored in memory, not executed yet
def flatten(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(flatten(...))  # flatten() runs with lst=[1, 3, 5, 7]
#   → import operator
#   → return operator.add(x, y)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only flatten is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → nested_list = ...  # stored in memory
#   → flattened_list = ...  # stored in memory
#   → print(flattened_list)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(flatten(...))  # flatten() runs first → value goes to print()

"""

"""
Problem 596:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_words(lst):  # defines a function with parameters lst
    def count_frequency(result, word):
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
        return result
    return reduce(count_frequency, lst, {})  # return sends the result back to the caller
#
# Keywords: if/else
# Operators: in
# Built-in functions: reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_words(lst))  # lst_words() runs first, then print() outputs the result
print(lst_words(?))  # lst_words() runs first, then print() outputs the result
word in result  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from functools import reduce
def lst_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_words(...))  # lst_words() runs with lst=lst
#   → return result
def lst_words(lst):  # stored in memory, not executed yet
def lst_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_words(...))  # lst_words() runs with lst=[1, 3, 5, 7]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_words(...))  # lst_words() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_words(...))  # lst_words() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 597:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_words(lst, target_word):  # defines a function with parameters lst, target_word
    def anagram_filter(word):
        return sorted(word) != sorted(target_word)
    return list(filter(anagram_filter, lst))  # return sends the result back to the caller
#
# Operators: !=
# Built-in functions: filter, list, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
lst_words(lst, target_word)  # arguments evaluated first, then function body runs
print(lst_words(?, ?))  # lst_words() runs first, then print() outputs the result
sorted(...) != sorted(...)  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_words(lst, target_word):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
target_word = ...  # assigns a value to the variable
filtered_words = ...  # assigns a value to the variable
print(filtered_words)
def lst_words(lst, target_word):  # stored in memory, not executed yet
def lst_words(lst, target_word):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
target_word = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_words(...))  # lst_words() runs with lst=[1, 3, 5, 7], target_word=[4, 1, 8, 6, 3]
#   → return sorted(word) != sorted(target_word)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → target_word = ...  # stored in memory
#   → filtered_words = ...  # stored in memory
#   → print(filtered_words)
#   → lst = ...  # stored in memory
#   → target_word = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_words(...))  # lst_words() runs first → value goes to print()

"""

"""
Problem 598:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def compose(func1, func2):  # defines a function with parameters func1, func2
    def composed_function(x):
        return func2(func1(x))
    return composed_function  # return sends the result back to the caller
#
# Operators: * +
# Built-in functions: composed_function, func1, func2()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
compose(add_one, multiply_by_two)  # arguments evaluated first, then function body runs
compose(func1, func2)  # arguments evaluated first, then function body runs
print(compose(25, 25))  # compose() runs first, then print() outputs the result
x + 1  # x → then 1 → then +
x * 2  # x → then 2 → then *
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def compose(func1, func2):  # stored in memory, not executed yet
def add_one(x):  # stored in memory, not executed yet
def multiply_by_two(x):  # stored in memory, not executed yet
composed_function = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
def compose(func1, func2):  # stored in memory, not executed yet
def compose(func1, func2):  # stored in memory, not executed yet
func1 = ...  # assigns a value to the variable
func2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(compose(...))  # compose() runs with func1=25, func2=25
#   → return func2(func1(x))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — add_one, compose, multiply_by_two are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → composed_function = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → func1 = ...  # stored in memory
#   → func2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(compose(...))  # compose() runs first → value goes to print()

"""

"""
Problem 599:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from functools import reduce
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# No top-level code runs — functions must be called externally

"""

"""
Problem 600:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def is_prime(n):  # defines a function with parameters n
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: % + ** <= ==
# Built-in functions: filter, int, list, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
filter_primes(numbers)  # arguments evaluated first, then function body runs
is_prime(n)  # arguments evaluated first, then function body runs
print(is_prime(15))  # is_prime() runs first, then print() outputs the result
n <= 1  # evaluated as True or False → picks which branch
int(...) + 1  # int(...) → then 1 → then +
? == 0  # evaluated as True or False → picks which branch
n % i  # n → then i → then %
n ** 0.5  # n → then 0.5 → then **
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def is_prime(n):  # stored in memory, not executed yet
def filter_primes(lst):  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
prime_numbers = ...  # assigns a value to the variable
print(prime_numbers)
def is_prime(n):  # stored in memory, not executed yet
def is_prime(n):  # stored in memory, not executed yet
n = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(is_prime(...))  # is_prime() runs with n=15
#   → return False
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — filter_primes, is_prime are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → prime_numbers = ...  # stored in memory
#   → print(prime_numbers)
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_prime(...))  # is_prime() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 601:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def map_with_index(lst, func):  # defines a function with parameters lst, func
    def indexed_func(indexed_item):
        index, item = indexed_item
        return func(index, item)
    return list(map(indexed_func, enumerate(lst)))  # return sends the result back to the caller
#
# Operators: *
# Built-in functions: enumerate, func, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
map_with_index(numbers, example_func)  # arguments evaluated first, then function body runs
map_with_index(lst, func)  # arguments evaluated first, then function body runs
print(map_with_index(?, 25))  # map_with_index() runs first, then print() outputs the result
index * value  # index → then value → then *
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def map_with_index(lst, func):  # stored in memory, not executed yet
def example_func(index, value):  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
def map_with_index(lst, func):  # stored in memory, not executed yet
def map_with_index(lst, func):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
func = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(map_with_index(...))  # map_with_index() runs with lst=[1, 3, 5, 7], func=25
#   → return func(index, item)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — example_func, map_with_index are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → lst = ...  # stored in memory
#   → func = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(map_with_index(...))  # map_with_index() runs first → value goes to print()

"""

"""
Problem 602:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def is_in_list(x, list2):  # defines a function with parameters x, list2
    return x in list2  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: == in
# Built-in functions: any, filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
intersection(list1, list2)  # arguments evaluated first, then function body runs
is_in_list(x, list2)  # arguments evaluated first, then function body runs
print(is_in_list(3, ?))  # is_in_list() runs first, then print() outputs the result
x in list2  # evaluated as True or False → picks which branch
element == x  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def is_in_list(x, list2):  # stored in memory, not executed yet
def intersection(list1, list2):  # stored in memory, not executed yet
list1 = ...  # assigns a value to the variable
list2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
def is_in_list(x, list2):  # stored in memory, not executed yet
def is_in_list(x, list2):  # stored in memory, not executed yet
x = ...  # assigns a value to the variable
list2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(is_in_list(...))  # is_in_list() runs with x=3, list2=[4, 1, 8, 6, 3]
#   → return any((element == x for element in list2))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — intersection, is_in_list are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → list1 = ...  # stored in memory
#   → list2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → x = ...  # stored in memory
#   → list2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_in_list(...))  # is_in_list() runs first → value goes to print()
#
# Loop: takes one item from list2, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 603:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def add(x, y):  # defines a function with parameters x, y
    return x + y  # return sends the result back to the caller
#
# Keywords: if/else
# Operators: + /
# Built-in functions: len, reduce, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
average(numbers)  # arguments evaluated first, then function body runs
add(x, y)  # arguments evaluated first, then function body runs
print(add(3, 14))  # add() runs first, then print() outputs the result
x + y  # x → then y → then +
total / len(...)  # total → then len(...) → then /
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from functools import reduce
def add(x, y):  # stored in memory, not executed yet
def average(lst):  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
def add(x, y):  # stored in memory, not executed yet
def add(x, y):  # stored in memory, not executed yet
x = ...  # assigns a value to the variable
y = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(add(...))  # add() runs with x=3, y=14
#   → import operator
#   → return operator.add(x, y)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — add, average are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → x = ...  # stored in memory
#   → y = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(add(...))  # add() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 604:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def compose_functions(functions, initial_value):  # defines a function with parameters functions, initial_value
    def apply_functions(x, func):
        return func(x)
    return reduce(apply_functions, functions, initial_value)  # return sends the result back to the caller
#
# Operators: * +
# Built-in functions: func, reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
compose_functions(functions, initial_value)  # arguments evaluated first, then function body runs
print(compose_functions(25, 25))  # compose_functions() runs first, then print() outputs the result
x + 1  # x → then 1 → then +
x * 2  # x → then 2 → then *
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from functools import reduce
def compose_functions(functions, initial_value):  # stored in memory, not executed yet
def add_one(x):  # stored in memory, not executed yet
def multiply_by_two(x):  # stored in memory, not executed yet
functions = ...  # assigns a value to the variable
initial_value = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
def compose_functions(functions, initial_value):  # stored in memory, not executed yet
def compose_functions(functions, initial_value):  # stored in memory, not executed yet
functions = ...  # assigns a value to the variable
initial_value = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(compose_functions(...))  # compose_functions() runs with functions=25, initial_value=25
#   → return func(x)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — add_one, compose_functions, multiply_by_two are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → functions = ...  # stored in memory
#   → initial_value = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → functions = ...  # stored in memory
#   → initial_value = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(compose_functions(...))  # compose_functions() runs first → value goes to print()

"""

"""
Problem 605:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def get_keys(dic):  # defines a function with parameters dic
    return list(dic.keys())  # return sends the result back to the caller
#
# Built-in functions: list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(get_keys(dic))  # get_keys() runs first, then print() outputs the result
get_dict_keys()  # function body runs with no arguments
print(get_keys(25))  # get_keys() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def get_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(get_keys(...))  # get_keys() runs with dic=dic
#   → return list(dic.keys())
def get_dict_keys():  # stored in memory, not executed yet
keys_list = ...  # assigns a value to the variable
print(keys_list)
def get_keys(dic):  # stored in memory, not executed yet
def get_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(get_keys(...))  # get_keys() runs with dic=25
#   → return list(dic.keys())
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — get_dict_keys, get_keys are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(get_keys(...))  # get_keys() runs first → value goes to print()
#   → keys_list = ...  # stored in memory
#   → print(keys_list)
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(get_keys(...))  # get_keys() runs first → value goes to print()

"""

"""
Problem 606:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sort_string_len(lst):  # defines a function with parameters lst
    return sorted(lst, key=len)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(sort_string_len(lst))  # sort_string_len() runs first, then print() outputs the result
print(sort_string_len(?))  # sort_string_len() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sort_string_len(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(sort_string_len(...))  # sort_string_len() runs with lst=lst
#   → return sorted(lst, key=len)
def sort_string_len(lst):  # stored in memory, not executed yet
def sort_string_len(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sort_string_len(...))  # sort_string_len() runs with lst=[1, 3, 5, 7]
#   → return sorted(lst, key=len)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_string_len is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(sort_string_len(...))  # sort_string_len() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_string_len(...))  # sort_string_len() runs first → value goes to print()

"""

"""
Problem 607:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_tuples_second(lst):  # defines a function with parameters lst
    def sort_tuples(x):
        return x[1]
    return sorted(lst, key=sort_tuples)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_tuples_second(lst))  # lst_tuples_second() runs first, then print() outputs the result
print(lst_tuples_second(?))  # lst_tuples_second() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_tuples_second(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_tuples_second(...))  # lst_tuples_second() runs with lst=lst
#   → return x[1]
def lst_tuples_second(lst):  # stored in memory, not executed yet
def lst_tuples_second(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_tuples_second(...))  # lst_tuples_second() runs with lst=[1, 3, 5, 7]
#   → return x[1]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_tuples_second is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_tuples_second(...))  # lst_tuples_second() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_tuples_second(...))  # lst_tuples_second() runs first → value goes to print()

"""

"""
Problem 608:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sort_dicts_by_key(lst, target_key):  # defines a function with parameters lst, target_key
    def get_key_value(d):
        return d[target_key]
    return sorted(lst, key=get_key_value)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
sort_dicts_by_key(dicts, target_key)  # arguments evaluated first, then function body runs
sort_dicts_by_key(lst, target_key)  # arguments evaluated first, then function body runs
print(sort_dicts_by_key(?, 25))  # sort_dicts_by_key() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sort_dicts_by_key(lst, target_key):  # stored in memory, not executed yet
dicts = ...  # assigns a value to the variable
target_key = ...  # assigns a value to the variable
sorted_dicts = ...  # assigns a value to the variable
print(sorted_dicts)
def sort_dicts_by_key(lst, target_key):  # stored in memory, not executed yet
def sort_dicts_by_key(lst, target_key):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
target_key = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sort_dicts_by_key(...))  # sort_dicts_by_key() runs with lst=[1, 3, 5, 7], target_key=25
#   → return d[target_key]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_dicts_by_key is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dicts = ...  # stored in memory
#   → target_key = ...  # stored in memory
#   → sorted_dicts = ...  # stored in memory
#   → print(sorted_dicts)
#   → lst = ...  # stored in memory
#   → target_key = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_dicts_by_key(...))  # sort_dicts_by_key() runs first → value goes to print()

"""

"""
Problem 609:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sort_last_names(names):  # defines a function with parameters names
    def get_last_name(name):
        return name.split()[-1]
    return sorted(names, key=get_last_name)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(sort_last_names(names))  # sort_last_names() runs first, then print() outputs the result
print(sort_last_names(?))  # sort_last_names() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sort_last_names(names):  # stored in memory, not executed yet
names = ...  # assigns a value to the variable
print(sort_last_names(...))  # sort_last_names() runs with names=names
#   → return name.split()[-1]
def sort_last_names(names):  # stored in memory, not executed yet
def sort_last_names(names):  # stored in memory, not executed yet
names = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sort_last_names(...))  # sort_last_names() runs with names=[4, 1, 8, 6, 3]
#   → return name.split()[-1]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_last_names is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → names = ...  # stored in memory
#   → print(sort_last_names(...))  # sort_last_names() runs first → value goes to print()
#   → names = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_last_names(...))  # sort_last_names() runs first → value goes to print()

"""

"""
Problem 610:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sort_ignore_case(strings):  # defines a function with parameters strings
    def case_insensitive_key(s):
        return s.lower()
    return sorted(strings, key=case_insensitive_key)  # return sends the result back to the caller
#
# Operators: + <=
# Built-in functions: chr, ord, sorted, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
sort_ignore_case(mixed_case_strings)  # arguments evaluated first, then function body runs
sort_ignore_case(strings)  # arguments evaluated first, then function body runs
print(sort_ignore_case(?))  # sort_ignore_case() runs first, then print() outputs the result
'A' <= c  # evaluated as True or False → picks which branch
'A' <= 'Z'  # evaluated as True or False → picks which branch
ord(...) + 32  # ord(...) → then 32 → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sort_ignore_case(strings):  # stored in memory, not executed yet
mixed_case_strings = ...  # assigns a value to the variable
sorted_strings = ...  # assigns a value to the variable
print(sorted_strings)
def sort_ignore_case(strings):  # stored in memory, not executed yet
def sort_ignore_case(strings):  # stored in memory, not executed yet
strings = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sort_ignore_case(...))  # sort_ignore_case() runs with strings=[4, 1, 8, 6, 3]
#   → return str(s).lower()
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_ignore_case is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → mixed_case_strings = ...  # stored in memory
#   → sorted_strings = ...  # stored in memory
#   → print(sorted_strings)
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_ignore_case(...))  # sort_ignore_case() runs first → value goes to print()

"""

"""
Problem 611:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def list_floats(lst):  # defines a function with parameters lst
    def sort(x):
        return x
    return sorted(lst, key=sort, reverse=True)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(list_floats(lst))  # list_floats() runs first, then print() outputs the result
print(list_floats(?))  # list_floats() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def list_floats(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(list_floats(...))  # list_floats() runs with lst=lst
#   → return x
def list_floats(lst):  # stored in memory, not executed yet
def list_floats(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(list_floats(...))  # list_floats() runs with lst=[1, 3, 5, 7]
#   → return x
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only list_floats is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(list_floats(...))  # list_floats() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(list_floats(...))  # list_floats() runs first → value goes to print()

"""

"""
Problem 612:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_words(lst):  # defines a function with parameters lst
    def sort(x):
        vowels = 'aeiou'
        count = 0
        for char in x.lower():
            if char in vowels:
                count += 1
        return count
    return sorted(lst, key=sort)  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: in
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_words(lst))  # lst_words() runs first, then print() outputs the result
print(lst_words(?))  # lst_words() runs first, then print() outputs the result
char in vowels  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_words(...))  # lst_words() runs with lst=lst
#   → return count
def lst_words(lst):  # stored in memory, not executed yet
def lst_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_words(...))  # lst_words() runs with lst=[1, 3, 5, 7]
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_words(...))  # lst_words() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_words(...))  # lst_words() runs first → value goes to print()
#
# Loop: takes one item from x.lower(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 613:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sort_people_by_age(people):  # defines a function with parameters people
    def get_age(person):
        return person['age']
    return sorted(people, key=get_age)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
sort_people_by_age(people)  # arguments evaluated first, then function body runs
print(sort_people_by_age(?))  # sort_people_by_age() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sort_people_by_age(people):  # stored in memory, not executed yet
people = ...  # assigns a value to the variable
sorted_people = ...  # assigns a value to the variable
print(sorted_people)
def sort_people_by_age(people):  # stored in memory, not executed yet
def sort_people_by_age(people):  # stored in memory, not executed yet
people = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sort_people_by_age(...))  # sort_people_by_age() runs with people=[4, 1, 8, 6, 3]
#   → return person['age']
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_people_by_age is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → people = ...  # stored in memory
#   → sorted_people = ...  # stored in memory
#   → print(sorted_people)
#   → people = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_people_by_age(...))  # sort_people_by_age() runs first → value goes to print()

"""

"""
Problem 614:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_integers(lst):  # defines a function with parameters lst
    def sort_sum(x):
        total = 0
        for digit in str(x):
            total += int(digit)
        return total
    return sorted(lst, key=sort_sum)  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: int, sorted, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
lst_integers(lst)  # arguments evaluated first, then function body runs
print(lst_integers(?))  # lst_integers() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_integers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
sorted_list = ...  # assigns a value to the variable
print(sorted_list)
def lst_integers(lst):  # stored in memory, not executed yet
def lst_integers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_integers(...))  # lst_integers() runs with lst=[1, 3, 5, 7]
#   → return total
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_integers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → sorted_list = ...  # stored in memory
#   → print(sorted_list)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_integers(...))  # lst_integers() runs first → value goes to print()
#
# Loop: takes one item from str(...), runs body, repeats until done

"""

"""
Problem 615:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_products(lst):  # defines a function with parameters lst
    def sort(product):
        return product['price']
    return sorted(lst, key=sort)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
lst_products(products)  # arguments evaluated first, then function body runs
lst_products(lst)  # arguments evaluated first, then function body runs
print(lst_products(?))  # lst_products() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_products(lst):  # stored in memory, not executed yet
products = ...  # assigns a value to the variable
sorted_products = ...  # assigns a value to the variable
print(sorted_products)
def lst_products(lst):  # stored in memory, not executed yet
def lst_products(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_products(...))  # lst_products() runs with lst=[1, 3, 5, 7]
#   → return product['price']
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_products is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → products = ...  # stored in memory
#   → sorted_products = ...  # stored in memory
#   → print(sorted_products)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_products(...))  # lst_products() runs first → value goes to print()

"""

"""
Problem 616:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sort_dates(dates):  # defines a function with parameters dates
    def date_key(date_str):
        year, month, day = map(int, date_str.split('-'))
        return (year, month, day)
    return sorted(dates, key=date_key)  # return sends the result back to the caller
#
# Built-in functions: map, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
sort_dates(date_list)  # arguments evaluated first, then function body runs
sort_dates(dates)  # arguments evaluated first, then function body runs
print(sort_dates(?))  # sort_dates() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sort_dates(dates):  # stored in memory, not executed yet
date_list = ...  # assigns a value to the variable
sorted_dates = ...  # assigns a value to the variable
print(sorted_dates)
def sort_dates(dates):  # stored in memory, not executed yet
def sort_dates(dates):  # stored in memory, not executed yet
dates = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sort_dates(...))  # sort_dates() runs with dates=[4, 1, 8, 6, 3]
#   → return (year, month, day)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_dates is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → date_list = ...  # stored in memory
#   → sorted_dates = ...  # stored in memory
#   → print(sorted_dates)
#   → dates = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_dates(...))  # sort_dates() runs first → value goes to print()

"""

"""
Problem 617:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_tuples(lst):  # defines a function with parameters lst
    def sort(tup):
        return (tup[0], tup[1])
    return sorted(lst, key=sort)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
lst_tuples(lst)  # arguments evaluated first, then function body runs
print(lst_tuples(?))  # lst_tuples() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_tuples(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
sorted_tuples = ...  # assigns a value to the variable
print(sorted_tuples)
def lst_tuples(lst):  # stored in memory, not executed yet
def lst_tuples(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_tuples(...))  # lst_tuples() runs with lst=[1, 3, 5, 7]
#   → return (tup[0], tup[1])
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_tuples is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → sorted_tuples = ...  # stored in memory
#   → print(sorted_tuples)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_tuples(...))  # lst_tuples() runs first → value goes to print()

"""

"""
Problem 618:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_names(lst):  # defines a function with parameters lst
    def sort_len_of_name(name):
        return len(name)
    return sorted(lst, key=sort_len_of_name)  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: len, sorted, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_names(lst))  # lst_names() runs first, then print() outputs the result
print(lst_names(?))  # lst_names() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_names(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_names(...))  # lst_names() runs with lst=lst
#   → return sum((1 for _ in name))
def lst_names(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_names(...))  # lst_names() runs with lst=lst
#   → return sum((1 for _ in name))
def lst_names(lst):  # stored in memory, not executed yet
def lst_names(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_names(...))  # lst_names() runs with lst=[1, 3, 5, 7]
#   → return sum((1 for _ in name))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_names is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_names(...))  # lst_names() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(lst_names(...))  # lst_names() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_names(...))  # lst_names() runs first → value goes to print()
#
# Loop: takes one item from name, runs body, repeats until done

"""

"""
Problem 619:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sort_by_hire_date(employees):  # defines a function with parameters employees
    def get_hire_date(employee):
        return employee[1]
    return sorted(employees, key=get_hire_date)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
sort_by_hire_date(employees)  # arguments evaluated first, then function body runs
print(sort_by_hire_date(?))  # sort_by_hire_date() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sort_by_hire_date(employees):  # stored in memory, not executed yet
employees = ...  # assigns a value to the variable
sorted_employees = ...  # assigns a value to the variable
print(sorted_employees)
def sort_by_hire_date(employees):  # stored in memory, not executed yet
def sort_by_hire_date(employees):  # stored in memory, not executed yet
employees = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sort_by_hire_date(...))  # sort_by_hire_date() runs with employees=[4, 1, 8, 6, 3]
#   → return employee[1]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_by_hire_date is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → employees = ...  # stored in memory
#   → sorted_employees = ...  # stored in memory
#   → print(sorted_employees)
#   → employees = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_by_hire_date(...))  # sort_by_hire_date() runs first → value goes to print()

"""

"""
Problem 621:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def frequency_first_letter(words):  # defines a function with parameters words
    letter_count = {}
    for word in words:
        first_letter = word[0]
        if first_letter in letter_count:
            letter_count[first_letter] += 1
        else:
            letter_count[first_letter] = 1
    def sort(word):
        return letter_count[word[0]]
    return sorted(words, key=sort)  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: in
# Built-in functions: Counter, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(frequency_first_letter(words))  # frequency_first_letter() runs first, then print() outputs the result
print(frequency_first_letter(?))  # frequency_first_letter() runs first, then print() outputs the result
first_letter in letter_count  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def frequency_first_letter(words):  # stored in memory, not executed yet
words = ...  # assigns a value to the variable
print(frequency_first_letter(...))  # frequency_first_letter() runs with words=words
#   → return letter_count[word[0]]
from collections import Counter
def frequency_first_letter(words):  # stored in memory, not executed yet
words = ...  # assigns a value to the variable
print(frequency_first_letter(...))  # frequency_first_letter() runs with words=words
#   → return letter_count[word[0]]
def frequency_first_letter(words):  # stored in memory, not executed yet
def frequency_first_letter(words):  # stored in memory, not executed yet
words = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(frequency_first_letter(...))  # frequency_first_letter() runs with words=[4, 1, 8, 6, 3]
#   → return letter_count[word[0]]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only frequency_first_letter is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → words = ...  # stored in memory
#   → print(frequency_first_letter(...))  # frequency_first_letter() runs first → value goes to print()
#   → words = ...  # stored in memory
#   → print(frequency_first_letter(...))  # frequency_first_letter() runs first → value goes to print()
#   → words = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(frequency_first_letter(...))  # frequency_first_letter() runs first → value goes to print()
#
# Loop: takes one item from words, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 622:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_of_tuples(lst):  # defines a function with parameters lst
    def sort(x):
        return abs(x[0])
    return sorted(lst, key=sort)  # return sends the result back to the caller
#
# Built-in functions: abs, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_of_tuples(lst))  # lst_of_tuples() runs first, then print() outputs the result
print(lst_of_tuples(?))  # lst_of_tuples() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_of_tuples(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_of_tuples(...))  # lst_of_tuples() runs with lst=lst
#   → return abs(x[0])
def lst_of_tuples(lst):  # stored in memory, not executed yet
def lst_of_tuples(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_of_tuples(...))  # lst_of_tuples() runs with lst=[1, 3, 5, 7]
#   → return abs(x[0])
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_of_tuples is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_of_tuples(...))  # lst_of_tuples() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_of_tuples(...))  # lst_of_tuples() runs first → value goes to print()

"""

"""
Problem 623:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def reverse_order(lst):  # defines a function with parameters lst
    def sort(word):
        return word
    return sorted(lst, key=sort, reverse=True)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(reverse_order(lst))  # reverse_order() runs first, then print() outputs the result
print(reverse_order(?))  # reverse_order() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def reverse_order(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(reverse_order(...))  # reverse_order() runs with lst=lst
#   → return word
def reverse_order(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(reverse_order(...))  # reverse_order() runs with lst=lst
#   → return word
def reverse_order(lst):  # stored in memory, not executed yet
def reverse_order(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(reverse_order(...))  # reverse_order() runs with lst=[1, 3, 5, 7]
#   → return word
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only reverse_order is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(reverse_order(...))  # reverse_order() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(reverse_order(...))  # reverse_order() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(reverse_order(...))  # reverse_order() runs first → value goes to print()

"""

"""
Problem 624:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def temperture(lst):  # defines a function with parameters lst
    def sort(celsius):
        fahrenheit = 9 / 5 * celsius + 32
        return fahrenheit
    return sorted(lst, key=sort)  # return sends the result back to the caller
#
# Operators: * + /
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(temperture(lst))  # temperture() runs first, then print() outputs the result
print(temperture(?))  # temperture() runs first, then print() outputs the result
? + 32  # ? → then 32 → then +
? * celsius  # ? → then celsius → then *
9 / 5  # 9 → then 5 → then /
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def temperture(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(temperture(...))  # temperture() runs with lst=lst
#   → return fahrenheit
def temperture(lst):  # stored in memory, not executed yet
def temperture(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(temperture(...))  # temperture() runs with lst=[1, 3, 5, 7]
#   → return fahrenheit
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only temperture is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(temperture(...))  # temperture() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(temperture(...))  # temperture() runs first → value goes to print()

"""

"""
Problem 625:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sort_scores(scores):  # defines a function with parameters scores
    def key_function(x):
        return x
    return sorted(scores, key=key_function)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
sort_scores(scores)  # arguments evaluated first, then function body runs
print(sort_scores(?))  # sort_scores() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sort_scores(scores):  # stored in memory, not executed yet
scores = ...  # assigns a value to the variable
sorted_scores = ...  # assigns a value to the variable
print(sorted_scores)
def sort_scores(scores):  # stored in memory, not executed yet
def sort_scores(scores):  # stored in memory, not executed yet
scores = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sort_scores(...))  # sort_scores() runs with scores=[4, 1, 8, 6, 3]
#   → return x
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_scores is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → scores = ...  # stored in memory
#   → sorted_scores = ...  # stored in memory
#   → print(sorted_scores)
#   → scores = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_scores(...))  # sort_scores() runs first → value goes to print()

"""

"""
Problem 626:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sort_emails(emails):  # defines a function with parameters emails
    def get_domain(email):
        return email.split('@')[1]
    return sorted(emails, key=get_domain)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
sort_emails(emails)  # arguments evaluated first, then function body runs
print(sort_emails(?))  # sort_emails() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sort_emails(emails):  # stored in memory, not executed yet
emails = ...  # assigns a value to the variable
sorted_emails = ...  # assigns a value to the variable
print(sorted_emails)
def sort_emails(emails):  # stored in memory, not executed yet
def sort_emails(emails):  # stored in memory, not executed yet
emails = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sort_emails(...))  # sort_emails() runs with emails=[4, 1, 8, 6, 3]
#   → return email.split('@')[1]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_emails is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → emails = ...  # stored in memory
#   → sorted_emails = ...  # stored in memory
#   → print(sorted_emails)
#   → emails = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_emails(...))  # sort_emails() runs first → value goes to print()

"""

"""
Problem 627:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sort_cities_by_population(cities):  # defines a function with parameters cities
    def get_population(city):
        return city[1]
    return sorted(cities, key=get_population)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
sort_cities_by_population(cities)  # arguments evaluated first, then function body runs
print(sort_cities_by_population(?))  # sort_cities_by_population() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sort_cities_by_population(cities):  # stored in memory, not executed yet
cities = ...  # assigns a value to the variable
sorted_cities = ...  # assigns a value to the variable
print(sorted_cities)
def sort_cities_by_population(cities):  # stored in memory, not executed yet
def sort_cities_by_population(cities):  # stored in memory, not executed yet
cities = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sort_cities_by_population(...))  # sort_cities_by_population() runs with cities=[4, 1, 8, 6, 3]
#   → return city[1]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_cities_by_population is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → cities = ...  # stored in memory
#   → sorted_cities = ...  # stored in memory
#   → print(sorted_cities)
#   → cities = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_cities_by_population(...))  # sort_cities_by_population() runs first → value goes to print()

"""

"""
Problem 628:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def last_letter(lst):  # defines a function with parameters lst
    def sort(word):
        return word[-1]
    return sorted(lst, key=sort)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(last_letter(lst))  # last_letter() runs first, then print() outputs the result
print(last_letter(?))  # last_letter() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def last_letter(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(last_letter(...))  # last_letter() runs with lst=lst
#   → return word[-1]
def last_letter(lst):  # stored in memory, not executed yet
def last_letter(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(last_letter(...))  # last_letter() runs with lst=[1, 3, 5, 7]
#   → return word[-1]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only last_letter is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(last_letter(...))  # last_letter() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(last_letter(...))  # last_letter() runs first → value goes to print()

"""

"""
Problem 629:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_of_numbers(lst):  # defines a function with parameters lst
    frequency = {}
    for number in lst:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    def sort(number):
        return frequency[number]
    return sorted(lst, key=sort)  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: in
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_of_numbers(lst))  # lst_of_numbers() runs first, then print() outputs the result
print(lst_of_numbers(?))  # lst_of_numbers() runs first, then print() outputs the result
number in frequency  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_of_numbers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_of_numbers(...))  # lst_of_numbers() runs with lst=lst
#   → return frequency[number]
def lst_of_numbers(lst):  # stored in memory, not executed yet
def lst_of_numbers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_of_numbers(...))  # lst_of_numbers() runs with lst=[1, 3, 5, 7]
#   → return frequency[number]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_of_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_of_numbers(...))  # lst_of_numbers() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_of_numbers(...))  # lst_of_numbers() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 630:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sort_students_by_grades(students):  # defines a function with parameters students
    def get_grade(student):
        return student[1]
    return sorted(students, key=get_grade)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(sort_students_by_grades(students))  # sort_students_by_grades() runs first, then print() outputs the result
print(sort_students_by_grades(?))  # sort_students_by_grades() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sort_students_by_grades(students):  # stored in memory, not executed yet
students = ...  # assigns a value to the variable
print(sort_students_by_grades(...))  # sort_students_by_grades() runs with students=students
#   → return student[1]
def sort_students_by_grades(students):  # stored in memory, not executed yet
def sort_students_by_grades(students):  # stored in memory, not executed yet
students = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sort_students_by_grades(...))  # sort_students_by_grades() runs with students=[4, 1, 8, 6, 3]
#   → return student[1]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_students_by_grades is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → students = ...  # stored in memory
#   → print(sort_students_by_grades(...))  # sort_students_by_grades() runs first → value goes to print()
#   → students = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_students_by_grades(...))  # sort_students_by_grades() runs first → value goes to print()

"""

"""
Problem 631:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sort_books_by_year(books):  # defines a function with parameters books
    def get_year(book):
        return book[1]
    return sorted(books, key=get_year)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(sort_books_by_year(books))  # sort_books_by_year() runs first, then print() outputs the result
print(sort_books_by_year(?))  # sort_books_by_year() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sort_books_by_year(books):  # stored in memory, not executed yet
books = ...  # assigns a value to the variable
print(sort_books_by_year(...))  # sort_books_by_year() runs with books=books
#   → return book[1]
def sort_books_by_year(books):  # stored in memory, not executed yet
def sort_books_by_year(books):  # stored in memory, not executed yet
books = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sort_books_by_year(...))  # sort_books_by_year() runs with books=[4, 1, 8, 6, 3]
#   → return book[1]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_books_by_year is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → books = ...  # stored in memory
#   → print(sort_books_by_year(...))  # sort_books_by_year() runs first → value goes to print()
#   → books = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_books_by_year(...))  # sort_books_by_year() runs first → value goes to print()

"""

"""
Problem 632:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sort_files_by_extension(files):  # defines a function with parameters files
    def get_extension(file):
        return file.split('.')[-1]
    return sorted(files, key=get_extension)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(sort_files_by_extension(files))  # sort_files_by_extension() runs first, then print() outputs the result
print(sort_files_by_extension(?))  # sort_files_by_extension() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sort_files_by_extension(files):  # stored in memory, not executed yet
files = ...  # assigns a value to the variable
print(sort_files_by_extension(...))  # sort_files_by_extension() runs with files=files
#   → return file.split('.')[-1]
def sort_files_by_extension(files):  # stored in memory, not executed yet
def sort_files_by_extension(files):  # stored in memory, not executed yet
files = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sort_files_by_extension(...))  # sort_files_by_extension() runs with files=[4, 1, 8, 6, 3]
#   → return file.split('.')[-1]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_files_by_extension is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → files = ...  # stored in memory
#   → print(sort_files_by_extension(...))  # sort_files_by_extension() runs first → value goes to print()
#   → files = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_files_by_extension(...))  # sort_files_by_extension() runs first → value goes to print()

"""

"""
Problem 633:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sort_movies_by_release_date(movies):  # defines a function with parameters movies
    def get_release_date(movie):
        return movie['release_date']
    return sorted(movies, key=get_release_date)  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
sort_movies_by_release_date(movies)  # arguments evaluated first, then function body runs
print(sort_movies_by_release_date(?))  # sort_movies_by_release_date() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sort_movies_by_release_date(movies):  # stored in memory, not executed yet
movies = ...  # assigns a value to the variable
sorted_movies = ...  # assigns a value to the variable
for movie in sorted_movies:  # loops once per item
  print(?)
def sort_movies_by_release_date(movies):  # stored in memory, not executed yet
def sort_movies_by_release_date(movies):  # stored in memory, not executed yet
movies = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sort_movies_by_release_date(...))  # sort_movies_by_release_date() runs with movies=[4, 1, 8, 6, 3]
#   → return movie['release_date']
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_movies_by_release_date is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → movies = ...  # stored in memory
#   → sorted_movies = ...  # stored in memory
#   → for movie in sorted_movies  # runs body once per item
#   → movies = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_movies_by_release_date(...))  # sort_movies_by_release_date() runs first → value goes to print()
#
# Loop: takes one item from sorted_movies, runs body, repeats until done

"""

"""
Problem 634:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sort_sentences_by_unique_words(sentences):  # defines a function with parameters sentences
    def count_unique_words(sentence):
        words = sentence.split()
        unique_words = set(words)
        return len(unique_words)
    return sorted(sentences, key=count_unique_words)  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: len, set, sorted, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
sort_sentences_by_unique_words(sentences)  # arguments evaluated first, then function body runs
print(sort_sentences_by_unique_words(?))  # sort_sentences_by_unique_words() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sort_sentences_by_unique_words(sentences):  # stored in memory, not executed yet
sentences = ...  # assigns a value to the variable
sorted_sentences = ...  # assigns a value to the variable
for sentence in sorted_sentences:  # loops once per item
  print(sentence)
def sort_sentences_by_unique_words(sentences):  # stored in memory, not executed yet
def sort_sentences_by_unique_words(sentences):  # stored in memory, not executed yet
sentences = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sort_sentences_by_unique_words(...))  # sort_sentences_by_unique_words() runs with sentences=[4, 1, 8, 6, 3]
#   → return sum((1 for _ in unique_words))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_sentences_by_unique_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → sentences = ...  # stored in memory
#   → sorted_sentences = ...  # stored in memory
#   → for sentence in sorted_sentences  # runs body once per item
#   → sentences = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_sentences_by_unique_words(...))  # sort_sentences_by_unique_words() runs first → value goes to print()
#
# Loop: takes one item from sorted_sentences, runs body, repeats until done

"""

"""
Problem 635:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def get_keys_from_dictionary(dic):  # defines a function with parameters dic
    return list(dic.keys())  # return sends the result back to the caller
#
# Built-in functions: list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
get_keys_from_dictionary(example_dict)  # arguments evaluated first, then function body runs
get_keys_from_dictionary(dic)  # arguments evaluated first, then function body runs
print(get_keys_from_dictionary(25))  # get_keys_from_dictionary() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def get_keys_from_dictionary(dic):  # stored in memory, not executed yet
example_dict = ...  # assigns a value to the variable
keys = ...  # assigns a value to the variable
print(keys)
def get_keys_from_dictionary(dic):  # stored in memory, not executed yet
def get_keys_from_dictionary(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(get_keys_from_dictionary(...))  # get_keys_from_dictionary() runs with dic=25
#   → return list(dic.keys())
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only get_keys_from_dictionary is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → example_dict = ...  # stored in memory
#   → keys = ...  # stored in memory
#   → print(keys)
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(get_keys_from_dictionary(...))  # get_keys_from_dictionary() runs first → value goes to print()

"""

"""
Problem 636:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def dic_keys(dic):  # defines a function with parameters dic
    result = []
    for key, value in dic.items():
        if value > 10:
            result.append(key)
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: >
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(dic_keys(dic))  # dic_keys() runs first, then print() outputs the result
print(dic_keys(25))  # dic_keys() runs first, then print() outputs the result
value > 10  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def dic_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(dic_keys(...))  # dic_keys() runs with dic=dic
#   → return result
def dic_keys(dic):  # stored in memory, not executed yet
def dic_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(dic_keys(...))  # dic_keys() runs with dic=25
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only dic_keys is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(dic_keys(...))  # dic_keys() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(dic_keys(...))  # dic_keys() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 637:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def print_fruit_keys(fruit_prices):  # defines a function with parameters fruit_prices
    return list(fruit_prices.keys())  # return sends the result back to the caller
#
# Built-in functions: list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(print_fruit_keys(fruit_prices))  # print_fruit_keys() runs first, then print() outputs the result
print(print_fruit_keys(25))  # print_fruit_keys() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def print_fruit_keys(fruit_prices):  # stored in memory, not executed yet
fruit_prices = ...  # assigns a value to the variable
print(print_fruit_keys(...))  # print_fruit_keys() runs with fruit_prices=fruit_prices
#   → return list(fruit_prices.keys())
def print_fruit_keys(fruit_prices):  # stored in memory, not executed yet
def print_fruit_keys(fruit_prices):  # stored in memory, not executed yet
fruit_prices = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(print_fruit_keys(...))  # print_fruit_keys() runs with fruit_prices=25
#   → return list(fruit_prices.keys())
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only print_fruit_keys is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → fruit_prices = ...  # stored in memory
#   → print(print_fruit_keys(...))  # print_fruit_keys() runs first → value goes to print()
#   → fruit_prices = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_fruit_keys(...))  # print_fruit_keys() runs first → value goes to print()

"""

"""
Problem 638:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def max_key(dic):  # defines a function with parameters dic
    return max(dic.keys())  # return sends the result back to the caller
#
# Built-in functions: max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(max_key(example_dict))  # max_key() runs first, then print() outputs the result
max_key(dic)  # arguments evaluated first, then function body runs
print(max_key(?))  # max_key() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def max_key(dic):  # stored in memory, not executed yet
example_dict = ...  # assigns a value to the variable
print(max_key(...))  # max_key() runs with dic=example_dict
#   → return max(dic.keys())
def max_key(dic):  # stored in memory, not executed yet
def max_key(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(max_key(...))  # max_key() runs with dic=[4, 1, 8, 6, 3]
#   → return max(dic.keys())
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only max_key is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → example_dict = ...  # stored in memory
#   → print(max_key(...))  # max_key() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(max_key(...))  # max_key() runs first → value goes to print()

"""

"""
Problem 639:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def name_age(dic):  # defines a function with parameters dic
    def sort_key(name):
        return dic[name]
    sorted_keys = sorted(dic.keys(), key=sort_key)
    return sorted_keys  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(name_age(dic))  # name_age() runs first, then print() outputs the result
print(name_age(?))  # name_age() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def name_age(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(name_age(...))  # name_age() runs with dic=dic
#   → return dic[name]
def name_age(dic):  # stored in memory, not executed yet
def name_age(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(name_age(...))  # name_age() runs with dic=[4, 1, 8, 6, 3]
#   → return dic[name]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only name_age is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(name_age(...))  # name_age() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(name_age(...))  # name_age() runs first → value goes to print()

"""

"""
Problem 640:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def concatenate_keys(dic):  # defines a function with parameters dic
    result = ''
    for key in dic.keys():
        result += str(key)
    return result  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(concatenate_keys(dic))  # concatenate_keys() runs first, then print() outputs the result
print(concatenate_keys(?))  # concatenate_keys() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def concatenate_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(concatenate_keys(...))  # concatenate_keys() runs with dic=dic
#   → return result
def concatenate_keys(dic):  # stored in memory, not executed yet
def concatenate_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(concatenate_keys(...))  # concatenate_keys() runs with dic=[4, 1, 8, 6, 3]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only concatenate_keys is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(concatenate_keys(...))  # concatenate_keys() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(concatenate_keys(...))  # concatenate_keys() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done

"""

"""
Problem 641:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def print_countries_and_capitals(dic):  # defines a function with parameters dic
    for country, capital in dic.items():
        print(f'{country}: {capital}')
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print_countries_and_capitals(countries_capitals)  # arguments evaluated first, then function body runs
print_countries_and_capitals(dic)  # arguments evaluated first, then function body runs
print(print_countries_and_capitals(25))  # print_countries_and_capitals() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def print_countries_and_capitals(dic):  # stored in memory, not executed yet
countries_capitals = ...  # assigns a value to the variable
print_countries_and_capitals(countries_capitals)  # calls print_countries_and_capitals with dic=countries_capitals
#   → for country, capital in dic.items():
#   →     print(f'{country}: {capital}')
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(print_countries_and_capitals(...))  # print_countries_and_capitals() runs with dic=25
#   → for country, capital in dic.items():
#   →     print(f'{country}: {capital}')
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — print_countries_and_capitals, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → countries_capitals = ...  # stored in memory
#   → print_countries_and_capitals(countries_capitals)  # jumps into print_countries_and_capitals(), runs body, returns
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_countries_and_capitals(...))  # print_countries_and_capitals() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done

"""

"""
Problem 642:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_key(dic):  # defines a function with parameters dic
    count = 0
    for key in dic.keys():
        count += 1
    return count  # return sends the result back to the caller
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_key(dic))  # count_key() runs first, then print() outputs the result
print(count_key(?))  # count_key() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_key(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(count_key(...))  # count_key() runs with dic=dic
#   → return count
def count_key(dic):  # stored in memory, not executed yet
def count_key(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_key(...))  # count_key() runs with dic=[4, 1, 8, 6, 3]
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_key is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(count_key(...))  # count_key() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_key(...))  # count_key() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done

"""

"""
Problem 643:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_key(dic, letter):  # defines a function with parameters dic, letter
    result = []
    for key in dic.keys():
        if key.startswith(letter):
            result.append(key)
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_key(dic, 'a'))  # count_key() runs first, then print() outputs the result
count_key(dic, letter)  # arguments evaluated first, then function body runs
print(count_key(?, 25))  # count_key() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_key(dic, letter):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(count_key(...))  # count_key() runs with dic=dic, letter='a'
#   → return result
def count_key(dic, letter):  # stored in memory, not executed yet
def count_key(dic, letter):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
letter = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_key(...))  # count_key() runs with dic=[4, 1, 8, 6, 3], letter=25
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_key is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(count_key(...))  # count_key() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → letter = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_key(...))  # count_key() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 644:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sorted_students_grades(dic):  # defines a function with parameters dic
    return sorted(dic.keys())  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(sorted_students_grades(students_grades))  # sorted_students_grades() runs first, then print() outputs the result
sorted_students_grades(dic)  # arguments evaluated first, then function body runs
print(sorted_students_grades(?))  # sorted_students_grades() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sorted_students_grades(dic):  # stored in memory, not executed yet
students_grades = ...  # assigns a value to the variable
print(sorted_students_grades(...))  # sorted_students_grades() runs with dic=students_grades
#   → return sorted(dic.keys())
def sorted_students_grades(dic):  # stored in memory, not executed yet
def sorted_students_grades(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sorted_students_grades(...))  # sorted_students_grades() runs with dic=[4, 1, 8, 6, 3]
#   → return sorted(dic.keys())
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sorted_students_grades is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → students_grades = ...  # stored in memory
#   → print(sorted_students_grades(...))  # sorted_students_grades() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sorted_students_grades(...))  # sorted_students_grades() runs first → value goes to print()

"""

"""
Problem 645:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def list_dictionary(lst1, lst2):  # defines a function with parameters lst1, lst2
    dic = {}
    for key, value in zip(lst1, lst2):
        dic[key] = value
    return dic  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(list_dictionary(lst1, lst2))  # list_dictionary() runs first, then print() outputs the result
print(list_dictionary(?, ?))  # list_dictionary() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def list_dictionary(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
print(list_dictionary(...))  # list_dictionary() runs with lst1=lst1, lst2=lst2
#   → return dic
def list_dictionary(lst1, lst2):  # stored in memory, not executed yet
def list_dictionary(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(list_dictionary(...))  # list_dictionary() runs with lst1=[2, 4, 6], lst2=[1, 3, 5]
#   → return dic
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only list_dictionary is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(list_dictionary(...))  # list_dictionary() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(list_dictionary(...))  # list_dictionary() runs first → value goes to print()
#
# Loop: takes one item from zip(...), runs body, repeats until done

"""

"""
Problem 646:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def reverse_keys(dic):  # defines a function with parameters dic
    return list(dic.keys())[::-1]  # return sends the result back to the caller
#
# Built-in functions: list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(reverse_keys(colors))  # reverse_keys() runs first, then print() outputs the result
reverse_keys(dic)  # arguments evaluated first, then function body runs
print(reverse_keys(25))  # reverse_keys() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def reverse_keys(dic):  # stored in memory, not executed yet
colors = ...  # assigns a value to the variable
print(reverse_keys(...))  # reverse_keys() runs with dic=colors
#   → return list(dic.keys())[::-1]
def reverse_keys(dic):  # stored in memory, not executed yet
def reverse_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(reverse_keys(...))  # reverse_keys() runs with dic=25
#   → return list(dic.keys())[::-1]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only reverse_keys is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → colors = ...  # stored in memory
#   → print(reverse_keys(...))  # reverse_keys() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(reverse_keys(...))  # reverse_keys() runs first → value goes to print()

"""

"""
Problem 647:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def first_key(dic):  # defines a function with parameters dic
    return next(iter(dic))  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: iter, next()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(first_key(example_dict))  # first_key() runs first, then print() outputs the result
first_key(dic)  # arguments evaluated first, then function body runs
print(first_key(25))  # first_key() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def first_key(dic):  # stored in memory, not executed yet
example_dict = ...  # assigns a value to the variable
print(first_key(...))  # first_key() runs with dic=example_dict
#   → return next(iter(dic))
def first_key(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
first_key(dic)  # calls first_key with dic=dic
#   → return next(iter(dic))
def first_key(dic):  # stored in memory, not executed yet
def first_key(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(first_key(...))  # first_key() runs with dic=25
#   → return next(iter(dic))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only first_key is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → example_dict = ...  # stored in memory
#   → print(first_key(...))  # first_key() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → first_key(dic)  # jumps into first_key(), runs body, returns
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(first_key(...))  # first_key() runs first → value goes to print()
#
# Loop: takes one item from dic, runs body, repeats until done

"""

"""
Problem 648:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def shopping_cart_items(cart):  # defines a function with parameters cart
    for item in cart.keys():
        print(item)
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
shopping_cart_items(cart)  # arguments evaluated first, then function body runs
print(shopping_cart_items(?))  # shopping_cart_items() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def shopping_cart_items(cart):  # stored in memory, not executed yet
cart = ...  # assigns a value to the variable
shopping_cart_items(cart)  # calls shopping_cart_items with cart=cart
#   → for item in cart.keys():
#   →     print(item)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
cart = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(shopping_cart_items(...))  # shopping_cart_items() runs with cart=[4, 1, 8, 6, 3]
#   → for item in cart.keys():
#   →     print(item)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — shopping_cart_items, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → cart = ...  # stored in memory
#   → shopping_cart_items(cart)  # jumps into shopping_cart_items(), runs body, returns
#   → cart = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(shopping_cart_items(...))  # shopping_cart_items() runs first → value goes to print()
#
# Loop: takes one item from cart.keys(...), runs body, repeats until done

"""

"""
Problem 649:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def check_key_exists(dic, key):  # defines a function with parameters dic, key
    if key in dic:
        return True
    else:
        return False
#
# Keywords: if/else
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(check_key_exists(example_dict, key_to_check))  # check_key_exists() runs first, then print() outputs the result
check_key_exists(dic, key)  # arguments evaluated first, then function body runs
print(check_key_exists(25, 'value'))  # check_key_exists() runs first, then print() outputs the result
key in dic  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def check_key_exists(dic, key):  # stored in memory, not executed yet
example_dict = ...  # assigns a value to the variable
key_to_check = ...  # assigns a value to the variable
print(check_key_exists(...))  # check_key_exists() runs with dic=example_dict, key=key_to_check
#   → return True
key_to_check = ...  # assigns a value to the variable
print(check_key_exists(...))  # check_key_exists() runs with dic=example_dict, key=key_to_check
#   → return True
def check_key_exists(dic, key):  # stored in memory, not executed yet
def check_key_exists(dic, key):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
key = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(check_key_exists(...))  # check_key_exists() runs with dic=25, key='value'
#   → return True
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only check_key_exists is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → example_dict = ...  # stored in memory
#   → key_to_check = ...  # stored in memory
#   → print(check_key_exists(...))  # check_key_exists() runs first → value goes to print()
#   → key_to_check = ...  # stored in memory
#   → print(check_key_exists(...))  # check_key_exists() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → key = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(check_key_exists(...))  # check_key_exists() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 650:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def print_keys_greater_than_five(dic):  # defines a function with parameters dic
    for item, quantity in dic.items():
        if quantity > 5:
            print(item)
#
# Keywords: for | if/else
# Operators: >
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print_keys_greater_than_five(items_dict)  # arguments evaluated first, then function body runs
print_keys_greater_than_five(dic)  # arguments evaluated first, then function body runs
print(print_keys_greater_than_five(25))  # print_keys_greater_than_five() runs first, then print() outputs the result
quantity > 5  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def print_keys_greater_than_five(dic):  # stored in memory, not executed yet
items_dict = ...  # assigns a value to the variable
print_keys_greater_than_five(items_dict)  # calls print_keys_greater_than_five with dic=items_dict
#   → for item, quantity in dic.items():
#   →     if quantity > 5:
#   →         print(item)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(print_keys_greater_than_five(...))  # print_keys_greater_than_five() runs with dic=25
#   → for item, quantity in dic.items():
#   →     if quantity > 5:
#   →         print(item)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — print_keys_greater_than_five, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → items_dict = ...  # stored in memory
#   → print_keys_greater_than_five(items_dict)  # jumps into print_keys_greater_than_five(), runs body, returns
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_keys_greater_than_five(...))  # print_keys_greater_than_five() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 651:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def returns_strings(dic):  # defines a function with parameters dic
    result = []
    for key in dic.keys():
        if isinstance(key, str):
            result.append(key)
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Built-in functions: isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(returns_strings(example_dict))  # returns_strings() runs first, then print() outputs the result
returns_strings(dic)  # arguments evaluated first, then function body runs
print(returns_strings(?))  # returns_strings() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def returns_strings(dic):  # stored in memory, not executed yet
example_dict = ...  # assigns a value to the variable
print(returns_strings(...))  # returns_strings() runs with dic=example_dict
#   → return result
def returns_strings(dic):  # stored in memory, not executed yet
def returns_strings(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(returns_strings(...))  # returns_strings() runs with dic=[4, 1, 8, 6, 3]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only returns_strings is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → example_dict = ...  # stored in memory
#   → print(returns_strings(...))  # returns_strings() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(returns_strings(...))  # returns_strings() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 652:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sports_by_popularity(sports_dict):  # defines a function with parameters sports_dict
    def get_ranking(sport):
        return sports_dict[sport]
    return sorted(sports_dict, key=get_ranking)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(sports_by_popularity(sports_dict))  # sports_by_popularity() runs first, then print() outputs the result
print(sports_by_popularity(?))  # sports_by_popularity() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sports_by_popularity(sports_dict):  # stored in memory, not executed yet
sports_dict = ...  # assigns a value to the variable
print(sports_by_popularity(...))  # sports_by_popularity() runs with sports_dict=sports_dict
#   → return sports_dict[sport]
def sports_by_popularity(sports_dict):  # stored in memory, not executed yet
def sports_by_popularity(sports_dict):  # stored in memory, not executed yet
sports_dict = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sports_by_popularity(...))  # sports_by_popularity() runs with sports_dict=[4, 1, 8, 6, 3]
#   → return sports_dict[sport]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sports_by_popularity is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → sports_dict = ...  # stored in memory
#   → print(sports_by_popularity(...))  # sports_by_popularity() runs first → value goes to print()
#   → sports_dict = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sports_by_popularity(...))  # sports_by_popularity() runs first → value goes to print()

"""

"""
Problem 653:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(dic):  # defines a function with parameters dic
    result = {}
    for key, value in dic.items():
        if isinstance(value, int):
            result[key] = value
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Built-in functions: isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
main(dic)  # arguments evaluated first, then function body runs
print(main(25))  # main() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
main(dic)  # calls main with dic=dic
#   → return result
data = ...  # assigns a value to the variable
integer_keys = ...  # assigns a value to the variable
print(integer_keys)
def main(dic):  # stored in memory, not executed yet
def main(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with dic=25
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only main is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → main(dic)  # jumps into main(), runs body, returns
#   → data = ...  # stored in memory
#   → integer_keys = ...  # stored in memory
#   → print(integer_keys)
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 654:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def books_authors(dic):  # defines a function with parameters dic
    for index, book in enumerate(dic.keys(), start=1):
        print(f'{index}. {book}')
#
# Keywords: for
# Built-in functions: enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
books_authors(dic)  # arguments evaluated first, then function body runs
print(books_authors(25))  # books_authors() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def books_authors(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
books_authors(dic)  # calls books_authors with dic=dic
#   → for index, book in enumerate(dic.keys(), start=1):
#   →     print(f'{index}. {book}')
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(books_authors(...))  # books_authors() runs with dic=25
#   → for index, book in enumerate(dic.keys(), start=1):
#   →     print(f'{index}. {book}')
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — books_authors, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → books_authors(dic)  # jumps into books_authors(), runs body, returns
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(books_authors(...))  # books_authors() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done

"""

"""
Problem 655:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def palindromic_keys(dic):  # defines a function with parameters dic
    result = []
    for key in dic.keys():
        if key == key[::-1]:
            result.append(key)
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(palindromic_keys(example_dict))  # palindromic_keys() runs first, then print() outputs the result
palindromic_keys(dic)  # arguments evaluated first, then function body runs
print(palindromic_keys(?))  # palindromic_keys() runs first, then print() outputs the result
key == ?  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def palindromic_keys(dic):  # stored in memory, not executed yet
example_dict = ...  # assigns a value to the variable
print(palindromic_keys(...))  # palindromic_keys() runs with dic=example_dict
#   → return result
def palindromic_keys(dic):  # stored in memory, not executed yet
def palindromic_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(palindromic_keys(...))  # palindromic_keys() runs with dic=[4, 1, 8, 6, 3]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only palindromic_keys is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → example_dict = ...  # stored in memory
#   → print(palindromic_keys(...))  # palindromic_keys() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(palindromic_keys(...))  # palindromic_keys() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 656:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def pet_owners(dic):  # defines a function with parameters dic
    result = []
    for key in dic.keys():
        if 'o' in key:
            result.append(key)
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: == in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(pet_owners(dic))  # pet_owners() runs first, then print() outputs the result
print(pet_owners(?))  # pet_owners() runs first, then print() outputs the result
'o' in key  # evaluated as True or False → picks which branch
char == 'o'  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def pet_owners(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(pet_owners(...))  # pet_owners() runs with dic=dic
#   → return result
def pet_owners(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(pet_owners(...))  # pet_owners() runs with dic=dic
#   → return result
def pet_owners(dic):  # stored in memory, not executed yet
def pet_owners(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(pet_owners(...))  # pet_owners() runs with dic=[4, 1, 8, 6, 3]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only pet_owners is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(pet_owners(...))  # pet_owners() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → print(pet_owners(...))  # pet_owners() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(pet_owners(...))  # pet_owners() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 657:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_tuple_keys(dic):  # defines a function with parameters dic
    count = 0
    for key in dic.keys():
        if isinstance(key, tuple):
            count += 1
    return count  # return sends the result back to the caller
#
# Keywords: for | if/else
# Built-in functions: isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_tuple_keys(dic))  # count_tuple_keys() runs first, then print() outputs the result
print(count_tuple_keys(?))  # count_tuple_keys() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_tuple_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(count_tuple_keys(...))  # count_tuple_keys() runs with dic=dic
#   → return count
def count_tuple_keys(dic):  # stored in memory, not executed yet
def count_tuple_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_tuple_keys(...))  # count_tuple_keys() runs with dic=[4, 1, 8, 6, 3]
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_tuple_keys is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(count_tuple_keys(...))  # count_tuple_keys() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_tuple_keys(...))  # count_tuple_keys() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 658:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def movies(dic):  # defines a function with parameters dic
    return sorted(dic.keys())  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(movies(dic))  # movies() runs first, then print() outputs the result
print(movies(?))  # movies() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def movies(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(movies(...))  # movies() runs with dic=dic
#   → return sorted(dic.keys())
def movies(dic):  # stored in memory, not executed yet
def movies(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(movies(...))  # movies() runs with dic=[4, 1, 8, 6, 3]
#   → return sorted(dic.keys())
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only movies is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(movies(...))  # movies() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(movies(...))  # movies() runs first → value goes to print()

"""

"""
Problem 659:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(dic):  # defines a function with parameters dic
    for key, value in dic.items():
        if isinstance(value, list):
            return key
#
# Keywords: for | if/else
# Built-in functions: isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
main(dic)  # arguments evaluated first, then function body runs
print(keys_with_list_values(dic))  # keys_with_list_values() runs first, then print() outputs the result
print(main(25))  # main() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
main(dic)  # calls main with dic=dic
#   → return key
def keys_with_list_values(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(keys_with_list_values(...))  # keys_with_list_values() runs with dic=dic
#   → result = []
#   → for key, value in dic.items():
#   →     if isinstance(value, list):
#   →         result.append(key)
#   → return result
def main(dic):  # stored in memory, not executed yet
def main(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with dic=25
#   → return key
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — keys_with_list_values, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → main(dic)  # jumps into main(), runs body, returns
#   → dic = ...  # stored in memory
#   → print(keys_with_list_values(...))  # keys_with_list_values() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 660:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def print_car_brands(dic):  # defines a function with parameters dic
    print('Car Brands:')
    for index, brand in enumerate(dic.keys(), start=1):
        print(f'{index}. {brand}')
#
# Keywords: for
# Built-in functions: enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print_car_brands(car_brands)  # arguments evaluated first, then function body runs
print_car_brands(dic)  # arguments evaluated first, then function body runs
print(print_car_brands(25))  # print_car_brands() runs first, then print() outputs the result
print_car_brands(car_brands_2)  # arguments evaluated first, then function body runs
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def print_car_brands(dic):  # stored in memory, not executed yet
car_brands = ...  # assigns a value to the variable
print_car_brands(car_brands)  # calls print_car_brands with dic=car_brands
#   → print('Car Brands:')
#   → for index, brand in enumerate(dic.keys(), start=1):
#   →     print(f'{index}. {brand}')
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(print_car_brands(...))  # print_car_brands() runs with dic=25
#   → print('Car Brands:')
#   → for index, brand in enumerate(dic.keys(), start=1):
#   →     print(f'{index}. {brand}')
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — print_car_brands, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → car_brands = ...  # stored in memory
#   → print_car_brands(car_brands)  # jumps into print_car_brands(), runs body, returns
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_car_brands(...))  # print_car_brands() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done

"""

"""
Problem 661:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def second_key(dic):  # defines a function with parameters dic
    keys_list = list(dic.keys())
    return keys_list[1] if len(keys_list) > 1 else None  # return sends the result back to the caller
#
# Operators: >
# Built-in functions: len, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(second_key(dic))  # second_key() runs first, then print() outputs the result
print(second_key(25))  # second_key() runs first, then print() outputs the result
len(...) > 1  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def second_key(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(second_key(...))  # second_key() runs with dic=dic
#   → return keys_list[1] if len(keys_list) > 1 else None
def second_key(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(second_key(...))  # second_key() runs with dic=dic
#   → return keys_list[1] if len(keys_list) > 1 else None
def second_key(dic):  # stored in memory, not executed yet
def second_key(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(second_key(...))  # second_key() runs with dic=25
#   → return keys_list[1] if len(keys_list) > 1 else None
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only second_key is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(second_key(...))  # second_key() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → print(second_key(...))  # second_key() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(second_key(...))  # second_key() runs first → value goes to print()

"""

"""
Problem 662:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def temperature(dic):  # defines a function with parameters dic
    upper_keys = []
    for key in dic.keys():
        upper_keys.append(key.upper())
    return upper_keys  # return sends the result back to the caller
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(temperature(dic))  # temperature() runs first, then print() outputs the result
print(temperature(?))  # temperature() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def temperature(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(temperature(...))  # temperature() runs with dic=dic
#   → return upper_keys
def temperature(dic):  # stored in memory, not executed yet
def temperature(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(temperature(...))  # temperature() runs with dic=[4, 1, 8, 6, 3]
#   → return upper_keys
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only temperature is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(temperature(...))  # temperature() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(temperature(...))  # temperature() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done

"""

"""
Problem 663:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def keys_in_list(dic, given_list):  # defines a function with parameters dic, given_list
    result = []
    for key in dic.keys():
        if key in given_list:
            result.append(key)
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(keys_in_list(dic, given_list))  # keys_in_list() runs first, then print() outputs the result
print(keys_in_list(?, ?))  # keys_in_list() runs first, then print() outputs the result
key in given_list  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def keys_in_list(dic, given_list):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
given_list = ...  # assigns a value to the variable
print(keys_in_list(...))  # keys_in_list() runs with dic=dic, given_list=given_list
#   → return result
def keys_in_list(dic, given_list):  # stored in memory, not executed yet
def keys_in_list(dic, given_list):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
given_list = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(keys_in_list(...))  # keys_in_list() runs with dic=[4, 1, 8, 6, 3], given_list=[4, 1, 8, 6, 3]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only keys_in_list is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → given_list = ...  # stored in memory
#   → print(keys_in_list(...))  # keys_in_list() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → given_list = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(keys_in_list(...))  # keys_in_list() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 664:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main():  # defines a function with no parameters
    devices = {'Phone': 999, 'Headphones': 50, 'Keyboard': 80, 'Mouse': 25, 'Charger': 15}
    affordable = [device for device, price in devices.items() if price < 100]
    for device in affordable:
        print(device)
#
# Keywords: for | if/else
# Operators: <
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
main()  # function body runs with no arguments
price < 100  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
devices = ...  # assigns a value to the variable
for (device, price) in devices.items(...):  # loops once per item
def main():  # stored in memory, not executed yet
main()  # calls main()
#   → devices = {'Phone': 999, 'Headphones': 50, 'Keyboard': 80, 'Mouse': 25, 'Charger': 15}
#   → affordable = [device for device, price in devices.items() if price < 100]
#   → for device in affordable:
#   →     print(device)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
devices = ...  # assigns a value to the variable
affordable = ...  # assigns a value to the variable
for device in affordable:  # loops once per item
  print(device)
devices = ...  # assigns a value to the variable
affordable = ...  # assigns a value to the variable
for device in affordable:  # loops once per item
  print(device)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → devices = ...  # stored in memory
#   → for (device, price) in devices.items(...)  # runs body once per item
#   → main()  # jumps into main(), runs body, returns
#   → devices = ...  # stored in memory
#   → affordable = ...  # stored in memory
#   → for device in affordable  # runs body once per item
#   → devices = ...  # stored in memory
#   → affordable = ...  # stored in memory
#   → for device in affordable  # runs body once per item
#
# Loop: takes one item from devices.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 665:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def keys_with_values_greater_than_10(dic):  # defines a function with parameters dic
    result = []
    for key in dic.keys():
        if dic[key] > 10:
            result.append(key)
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: >
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(keys_with_values_greater_than_10(dic))  # keys_with_values_greater_than_10() runs first, then print() outputs the result
print(get_dict_keys(my_dict))  # get_dict_keys() runs first, then print() outputs the result
print(keys_with_values_greater_than_10(?))  # keys_with_values_greater_than_10() runs first, then print() outputs the result
? > 10  # evaluated as True or False → picks which branch
value > 10  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def keys_with_values_greater_than_10(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(keys_with_values_greater_than_10(...))  # keys_with_values_greater_than_10() runs with dic=dic
#   → return result
def get_dict_keys(dic):  # stored in memory, not executed yet
my_dict = ...  # assigns a value to the variable
print(get_dict_keys(...))  # get_dict_keys() runs with dic=my_dict
#   → result = []
#   → for key, value in dic.items():
#   →     if value > 10:
#   →         result.append(key)
#   → return result
def keys_with_values_greater_than_10(dic):  # stored in memory, not executed yet
def keys_with_values_greater_than_10(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(keys_with_values_greater_than_10(...))  # keys_with_values_greater_than_10() runs with dic=[4, 1, 8, 6, 3]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — get_dict_keys, keys_with_values_greater_than_10 are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(keys_with_values_greater_than_10(...))  # keys_with_values_greater_than_10() runs first → value goes to print()
#   → my_dict = ...  # stored in memory
#   → print(get_dict_keys(...))  # get_dict_keys() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(keys_with_values_greater_than_10(...))  # keys_with_values_greater_than_10() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 666:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def print_fruit_keys(fruits):  # defines a function with parameters fruits
    for key in fruits.keys():
        print(key)
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print_fruit_keys(fruits)  # arguments evaluated first, then function body runs
print(print_fruit_keys(?))  # print_fruit_keys() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def print_fruit_keys(fruits):  # stored in memory, not executed yet
fruits = ...  # assigns a value to the variable
print_fruit_keys(fruits)  # calls print_fruit_keys with fruits=fruits
#   → for key in fruits.keys():
#   →     print(key)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
fruits = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(print_fruit_keys(...))  # print_fruit_keys() runs with fruits=[4, 1, 8, 6, 3]
#   → for key in fruits.keys():
#   →     print(key)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — print_fruit_keys, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → fruits = ...  # stored in memory
#   → print_fruit_keys(fruits)  # jumps into print_fruit_keys(), runs body, returns
#   → fruits = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_fruit_keys(...))  # print_fruit_keys() runs first → value goes to print()
#
# Loop: takes one item from fruits.keys(...), runs body, repeats until done

"""

"""
Problem 667:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def name_age(dic):  # defines a function with parameters dic
    def sort_age(x):
        for keys, values in x:
            return values
    return sorted(dic, key=sort_age)  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(name_age(dic))  # name_age() runs first, then print() outputs the result
print(name_age(?))  # name_age() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def name_age(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(name_age(...))  # name_age() runs with dic=dic
#   → return values
def name_age(dic):  # stored in memory, not executed yet
def name_age(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(name_age(...))  # name_age() runs with dic=[4, 1, 8, 6, 3]
#   → return values
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only name_age is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(name_age(...))  # name_age() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(name_age(...))  # name_age() runs first → value goes to print()
#
# Loop: takes one item from x, runs body, repeats until done

"""

"""
Problem 668:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def concatenate(dic):  # defines a function with parameters dic
    result = ''
    for key in dic.keys():
        result += str(key)
    return result  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(concatenate(dic))  # concatenate() runs first, then print() outputs the result
print(concatenate(?))  # concatenate() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def concatenate(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(concatenate(...))  # concatenate() runs with dic=dic
#   → return result
def concatenate(dic):  # stored in memory, not executed yet
def concatenate(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(concatenate(...))  # concatenate() runs with dic=[4, 1, 8, 6, 3]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only concatenate is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(concatenate(...))  # concatenate() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(concatenate(...))  # concatenate() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done

"""

"""
Problem 670:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_keys(dic):  # defines a function with parameters dic
    return len(dic)  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_keys(dic))  # count_keys() runs first, then print() outputs the result
print(count_keys(25))  # count_keys() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(count_keys(...))  # count_keys() runs with dic=dic
#   → return sum((1 for _ in dic))
def count_keys(dic):  # stored in memory, not executed yet
def count_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_keys(...))  # count_keys() runs with dic=25
#   → return sum((1 for _ in dic))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_keys is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(count_keys(...))  # count_keys() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_keys(...))  # count_keys() runs first → value goes to print()
#
# Loop: takes one item from dic, runs body, repeats until done

"""

"""
Problem 671:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def keys_starting_with(dic, letter):  # defines a function with parameters dic, letter
    result = []
    for key in dic.keys():
        if key.startswith(letter):
            result.append(key)
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(keys_starting_with(dic, 'a'))  # keys_starting_with() runs first, then print() outputs the result
keys_starting_with(dic, letter)  # arguments evaluated first, then function body runs
print(keys_starting_with(?, 25))  # keys_starting_with() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def keys_starting_with(dic, letter):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(keys_starting_with(...))  # keys_starting_with() runs with dic=dic, letter='a'
#   → return result
def keys_starting_with(dic, letter):  # stored in memory, not executed yet
def keys_starting_with(dic, letter):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
letter = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(keys_starting_with(...))  # keys_starting_with() runs with dic=[4, 1, 8, 6, 3], letter=25
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only keys_starting_with is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(keys_starting_with(...))  # keys_starting_with() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → letter = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(keys_starting_with(...))  # keys_starting_with() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 672:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def students_grades(dic):  # defines a function with parameters dic
    sorted_keys = sorted(dic.keys())
    for key in sorted_keys:
        print(key)
#
# Keywords: for
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
students_grades(dic)  # arguments evaluated first, then function body runs
print(students_grades(?))  # students_grades() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def students_grades(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
students_grades(dic)  # calls students_grades with dic=dic
#   → sorted_keys = sorted(dic.keys())
#   → for key in sorted_keys:
#   →     print(key)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(students_grades(...))  # students_grades() runs with dic=[4, 1, 8, 6, 3]
#   → sorted_keys = sorted(dic.keys())
#   → for key in sorted_keys:
#   →     print(key)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — solve, students_grades are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → students_grades(dic)  # jumps into students_grades(), runs body, returns
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(students_grades(...))  # students_grades() runs first → value goes to print()
#
# Loop: takes one item from sorted_keys, runs body, repeats until done

"""

"""
Problem 673:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def two_lst(lst1, lst2):  # defines a function with parameters lst1, lst2
    result = {}
    for key, value in zip(lst1, lst2):
        result[key] = value
    return result  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(two_lst(lst1, lst2))  # two_lst() runs first, then print() outputs the result
print(two_lst(?, ?))  # two_lst() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def two_lst(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
print(two_lst(...))  # two_lst() runs with lst1=lst1, lst2=lst2
#   → return result
def two_lst(lst1, lst2):  # stored in memory, not executed yet
def two_lst(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(two_lst(...))  # two_lst() runs with lst1=[2, 4, 6], lst2=[1, 3, 5]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only two_lst is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(two_lst(...))  # two_lst() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(two_lst(...))  # two_lst() runs first → value goes to print()
#
# Loop: takes one item from zip(...), runs body, repeats until done

"""

"""
Problem 674:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def colors_hex(dic):  # defines a function with parameters dic
    keys_in_reverse = list(dic.keys())[::-1]
    for key in keys_in_reverse:
        print(key)
#
# Keywords: for
# Built-in functions: list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
colors_hex(colors_dict)  # arguments evaluated first, then function body runs
colors_hex(dic)  # arguments evaluated first, then function body runs
print(colors_hex(25))  # colors_hex() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def colors_hex(dic):  # stored in memory, not executed yet
colors_dict = ...  # assigns a value to the variable
colors_hex(colors_dict)  # calls colors_hex with dic=colors_dict
#   → return list(dic.keys())[::-1]
def colors_hex(dic):  # stored in memory, not executed yet
colors_dict = ...  # assigns a value to the variable
colors_hex(colors_dict)  # calls colors_hex with dic=colors_dict
#   → return list(dic.keys())[::-1]
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(colors_hex(...))  # colors_hex() runs with dic=25
#   → return list(dic.keys())[::-1]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — colors_hex, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → colors_dict = ...  # stored in memory
#   → colors_hex(colors_dict)  # jumps into colors_hex(), runs body, returns
#   → colors_dict = ...  # stored in memory
#   → colors_hex(colors_dict)  # jumps into colors_hex(), runs body, returns
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(colors_hex(...))  # colors_hex() runs first → value goes to print()
#
# Loop: takes one item from keys_in_reverse, runs body, repeats until done

"""

"""
Problem 675:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def first_key(dic):  # defines a function with parameters dic
    return next(iter(dic))  # return sends the result back to the caller
#
# Built-in functions: iter, next()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(first_key(example_dict))  # first_key() runs first, then print() outputs the result
first_key(dic)  # arguments evaluated first, then function body runs
print(first_key(25))  # first_key() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def first_key(dic):  # stored in memory, not executed yet
example_dict = ...  # assigns a value to the variable
print(first_key(...))  # first_key() runs with dic=example_dict
#   → return next(iter(dic))
def first_key(dic):  # stored in memory, not executed yet
def first_key(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(first_key(...))  # first_key() runs with dic=25
#   → return next(iter(dic))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only first_key is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → example_dict = ...  # stored in memory
#   → print(first_key(...))  # first_key() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(first_key(...))  # first_key() runs first → value goes to print()

"""

"""
Problem 676:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def print_cart_items(cart):  # defines a function with parameters cart
    for item in cart.keys():
        print(item)
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print_cart_items(shopping_cart)  # arguments evaluated first, then function body runs
print_cart_items(cart)  # arguments evaluated first, then function body runs
print(print_cart_items(?))  # print_cart_items() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def print_cart_items(cart):  # stored in memory, not executed yet
shopping_cart = ...  # assigns a value to the variable
print_cart_items(shopping_cart)  # calls print_cart_items with cart=shopping_cart
#   → for item in cart.keys():
#   →     print(item)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
cart = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(print_cart_items(...))  # print_cart_items() runs with cart=[4, 1, 8, 6, 3]
#   → for item in cart.keys():
#   →     print(item)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — print_cart_items, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → shopping_cart = ...  # stored in memory
#   → print_cart_items(shopping_cart)  # jumps into print_cart_items(), runs body, returns
#   → cart = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_cart_items(...))  # print_cart_items() runs first → value goes to print()
#
# Loop: takes one item from cart.keys(...), runs body, repeats until done

"""

"""
Problem 678:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def items_with_high_quantity(dic):  # defines a function with parameters dic
    result = []
    for item, quantity in dic.items():
        if quantity > 5:
            result.append(item)
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: >
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
items_with_high_quantity(inventory)  # arguments evaluated first, then function body runs
items_with_high_quantity(dic)  # arguments evaluated first, then function body runs
print(items_with_high_quantity(25))  # items_with_high_quantity() runs first, then print() outputs the result
quantity > 5  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def items_with_high_quantity(dic):  # stored in memory, not executed yet
inventory = ...  # assigns a value to the variable
high_quantity_items = ...  # assigns a value to the variable
print('Items with quantities greater than 5:')
for item in high_quantity_items:  # loops once per item
  print(item)
def items_with_high_quantity(dic):  # stored in memory, not executed yet
def items_with_high_quantity(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(items_with_high_quantity(...))  # items_with_high_quantity() runs with dic=25
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only items_with_high_quantity is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → inventory = ...  # stored in memory
#   → high_quantity_items = ...  # stored in memory
#   → print('Items with quantities greater than 5:')
#   → for item in high_quantity_items  # runs body once per item
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(items_with_high_quantity(...))  # items_with_high_quantity() runs first → value goes to print()
#
# Loop: takes one item from high_quantity_items, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 679:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def string_keys(dic):  # defines a function with parameters dic
    result = []
    for key in dic.keys():
        if isinstance(key, str):
            result.append(key)
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Built-in functions: isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
string_keys(example_dict)  # arguments evaluated first, then function body runs
string_keys(dic)  # arguments evaluated first, then function body runs
print(string_keys(?))  # string_keys() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def string_keys(dic):  # stored in memory, not executed yet
example_dict = ...  # assigns a value to the variable
string_keys_list = ...  # assigns a value to the variable
print('Keys that are strings:', string_keys_list)
def string_keys(dic):  # stored in memory, not executed yet
def string_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(string_keys(...))  # string_keys() runs with dic=[4, 1, 8, 6, 3]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only string_keys is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → example_dict = ...  # stored in memory
#   → string_keys_list = ...  # stored in memory
#   → print('Keys that are strings:', string_keys_list)
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(string_keys(...))  # string_keys() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 680:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sports_by_popularity(sports_dict):  # defines a function with parameters sports_dict
    def get_ranking(sport):
        return sports_dict[sport]
    return sorted(sports_dict.keys(), key=get_ranking)  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(sports_by_popularity(sports_dict))  # sports_by_popularity() runs first, then print() outputs the result
print(sports_by_popularity(?))  # sports_by_popularity() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sports_by_popularity(sports_dict):  # stored in memory, not executed yet
sports_dict = ...  # assigns a value to the variable
print(sports_by_popularity(...))  # sports_by_popularity() runs with sports_dict=sports_dict
#   → return sports_dict[sport]
def sports_by_popularity(sports_dict):  # stored in memory, not executed yet
def sports_by_popularity(sports_dict):  # stored in memory, not executed yet
sports_dict = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sports_by_popularity(...))  # sports_by_popularity() runs with sports_dict=[4, 1, 8, 6, 3]
#   → return sports_dict[sport]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sports_by_popularity is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → sports_dict = ...  # stored in memory
#   → print(sports_by_popularity(...))  # sports_by_popularity() runs first → value goes to print()
#   → sports_dict = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sports_by_popularity(...))  # sports_by_popularity() runs first → value goes to print()

"""

"""
Problem 681:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def retrieve_integer_keys(dic):  # defines a function with parameters dic
    result = []
    for key in dic.keys():
        if isinstance(key, int):
            result.append(key)
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Built-in functions: isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(retrieve_integer_keys(example_dict))  # retrieve_integer_keys() runs first, then print() outputs the result
retrieve_integer_keys(dic)  # arguments evaluated first, then function body runs
print(retrieve_integer_keys(?))  # retrieve_integer_keys() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def retrieve_integer_keys(dic):  # stored in memory, not executed yet
example_dict = ...  # assigns a value to the variable
print(retrieve_integer_keys(...))  # retrieve_integer_keys() runs with dic=example_dict
#   → return result
def retrieve_integer_keys(dic):  # stored in memory, not executed yet
def retrieve_integer_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(retrieve_integer_keys(...))  # retrieve_integer_keys() runs with dic=[4, 1, 8, 6, 3]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only retrieve_integer_keys is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → example_dict = ...  # stored in memory
#   → print(retrieve_integer_keys(...))  # retrieve_integer_keys() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(retrieve_integer_keys(...))  # retrieve_integer_keys() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 682:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def print_numbered_books(dic):  # defines a function with parameters dic
    for index, items in enumerate(dic.keys(), start=1):
        print(f'{index}. {items}')
#
# Keywords: for
# Built-in functions: enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print_numbered_books(books)  # arguments evaluated first, then function body runs
print_numbered_books(dic)  # arguments evaluated first, then function body runs
print(print_numbered_books(25))  # print_numbered_books() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def print_numbered_books(dic):  # stored in memory, not executed yet
books = ...  # assigns a value to the variable
print_numbered_books(books)  # calls print_numbered_books with dic=books
#   → for index, items in enumerate(dic.keys(), start=1):
#   →     print(f'{index}. {items}')
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(print_numbered_books(...))  # print_numbered_books() runs with dic=25
#   → for index, items in enumerate(dic.keys(), start=1):
#   →     print(f'{index}. {items}')
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — print_numbered_books, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → books = ...  # stored in memory
#   → print_numbered_books(books)  # jumps into print_numbered_books(), runs body, returns
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_numbered_books(...))  # print_numbered_books() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done

"""

"""
Problem 683:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def palindrome_keys(dic):  # defines a function with parameters dic
    result = []
    for key in dic.keys():
        if str(key) == str(key)[::-1]:
            result.append(key)
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
# Built-in functions: str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(palindrome_keys(example_dict))  # palindrome_keys() runs first, then print() outputs the result
palindrome_keys(dic)  # arguments evaluated first, then function body runs
print(palindrome_keys(?))  # palindrome_keys() runs first, then print() outputs the result
str(...) == ?  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def palindrome_keys(dic):  # stored in memory, not executed yet
example_dict = ...  # assigns a value to the variable
print(palindrome_keys(...))  # palindrome_keys() runs with dic=example_dict
#   → return result
def palindrome_keys(dic):  # stored in memory, not executed yet
def palindrome_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(palindrome_keys(...))  # palindrome_keys() runs with dic=[4, 1, 8, 6, 3]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only palindrome_keys is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → example_dict = ...  # stored in memory
#   → print(palindrome_keys(...))  # palindrome_keys() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(palindrome_keys(...))  # palindrome_keys() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 684:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def pets_with_o(dic):  # defines a function with parameters dic
    result = []
    for key in dic.keys():
        if 'o' in key:
            result.append(key)
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(pets_with_o(pets_dict))  # pets_with_o() runs first, then print() outputs the result
pets_with_o(dic)  # arguments evaluated first, then function body runs
print(pets_with_o(?))  # pets_with_o() runs first, then print() outputs the result
'o' in key  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def pets_with_o(dic):  # stored in memory, not executed yet
pets_dict = ...  # assigns a value to the variable
print(pets_with_o(...))  # pets_with_o() runs with dic=pets_dict
#   → return result
def pets_with_o(dic):  # stored in memory, not executed yet
def pets_with_o(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(pets_with_o(...))  # pets_with_o() runs with dic=[4, 1, 8, 6, 3]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only pets_with_o is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → pets_dict = ...  # stored in memory
#   → print(pets_with_o(...))  # pets_with_o() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(pets_with_o(...))  # pets_with_o() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 685:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_list_keys(dic):  # defines a function with parameters dic
    count = 0
    for key in dic.keys():
        if isinstance(key, list):
            count += 1
    return count  # return sends the result back to the caller
#
# Keywords: for | if/else
# Built-in functions: isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_list_keys(example_dict))  # count_list_keys() runs first, then print() outputs the result
count_list_keys(dic)  # arguments evaluated first, then function body runs
print(count_list_keys(?))  # count_list_keys() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_list_keys(dic):  # stored in memory, not executed yet
example_dict = ...  # assigns a value to the variable
print(count_list_keys(...))  # count_list_keys() runs with dic=example_dict
#   → return count
def count_list_keys(dic):  # stored in memory, not executed yet
def count_list_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_list_keys(...))  # count_list_keys() runs with dic=[4, 1, 8, 6, 3]
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_list_keys is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → example_dict = ...  # stored in memory
#   → print(count_list_keys(...))  # count_list_keys() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_list_keys(...))  # count_list_keys() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 686:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sorted_movie_titles(movies):  # defines a function with parameters movies
    return sorted(movies.keys())  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(sorted_movie_titles(movies_dict))  # sorted_movie_titles() runs first, then print() outputs the result
sorted_movie_titles(movies)  # arguments evaluated first, then function body runs
print(sorted_movie_titles(?))  # sorted_movie_titles() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sorted_movie_titles(movies):  # stored in memory, not executed yet
movies_dict = ...  # assigns a value to the variable
print(sorted_movie_titles(...))  # sorted_movie_titles() runs with movies=movies_dict
#   → return sorted(movies.keys())
def sorted_movie_titles(movies):  # stored in memory, not executed yet
def sorted_movie_titles(movies):  # stored in memory, not executed yet
movies = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sorted_movie_titles(...))  # sorted_movie_titles() runs with movies=[4, 1, 8, 6, 3]
#   → return sorted(movies.keys())
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sorted_movie_titles is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → movies_dict = ...  # stored in memory
#   → print(sorted_movie_titles(...))  # sorted_movie_titles() runs first → value goes to print()
#   → movies = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sorted_movie_titles(...))  # sorted_movie_titles() runs first → value goes to print()

"""

"""
Problem 687:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def keys_with_list_values(dic):  # defines a function with parameters dic
    result = []
    for key, value in dic.items():
        if isinstance(value, list):
            result.append(key)
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Built-in functions: isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(keys_with_list_values(example_dict))  # keys_with_list_values() runs first, then print() outputs the result
keys_with_list_values(dic)  # arguments evaluated first, then function body runs
print(keys_with_list_values(25))  # keys_with_list_values() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def keys_with_list_values(dic):  # stored in memory, not executed yet
example_dict = ...  # assigns a value to the variable
print(keys_with_list_values(...))  # keys_with_list_values() runs with dic=example_dict
#   → return result
def keys_with_list_values(dic):  # stored in memory, not executed yet
def keys_with_list_values(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(keys_with_list_values(...))  # keys_with_list_values() runs with dic=25
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only keys_with_list_values is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → example_dict = ...  # stored in memory
#   → print(keys_with_list_values(...))  # keys_with_list_values() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(keys_with_list_values(...))  # keys_with_list_values() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 688:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def print_car_brands(dic):  # defines a function with parameters dic
    for brand in dic.keys():
        print(f'Brand: {brand}')
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print_car_brands(car_brands)  # arguments evaluated first, then function body runs
print_car_brands(dic)  # arguments evaluated first, then function body runs
print(print_car_brands(?))  # print_car_brands() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def print_car_brands(dic):  # stored in memory, not executed yet
car_brands = ...  # assigns a value to the variable
print_car_brands(car_brands)  # calls print_car_brands with dic=car_brands
#   → for brand in dic.keys():
#   →     print(f'Brand: {brand}')
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(print_car_brands(...))  # print_car_brands() runs with dic=[4, 1, 8, 6, 3]
#   → for brand in dic.keys():
#   →     print(f'Brand: {brand}')
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — print_car_brands, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → car_brands = ...  # stored in memory
#   → print_car_brands(car_brands)  # jumps into print_car_brands(), runs body, returns
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_car_brands(...))  # print_car_brands() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done

"""

"""
Problem 689:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def second_key(dic):  # defines a function with parameters dic
    return list(dic.keys())[1]  # return sends the result back to the caller
#
# Built-in functions: list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(second_key(example_dict))  # second_key() runs first, then print() outputs the result
second_key(dic)  # arguments evaluated first, then function body runs
print(second_key(25))  # second_key() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def second_key(dic):  # stored in memory, not executed yet
example_dict = ...  # assigns a value to the variable
print(second_key(...))  # second_key() runs with dic=example_dict
#   → return list(dic.keys())[1]
def second_key(dic):  # stored in memory, not executed yet
def second_key(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(second_key(...))  # second_key() runs with dic=25
#   → return list(dic.keys())[1]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only second_key is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → example_dict = ...  # stored in memory
#   → print(second_key(...))  # second_key() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(second_key(...))  # second_key() runs first → value goes to print()

"""

"""
Problem 690:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def uppercase_keys(dic):  # defines a function with parameters dic
    result = []
    for key in dic.keys():
        result.append(key.upper())
    return result  # return sends the result back to the caller
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(uppercase_keys(dic))  # uppercase_keys() runs first, then print() outputs the result
print(uppercase_keys(?))  # uppercase_keys() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def uppercase_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(uppercase_keys(...))  # uppercase_keys() runs with dic=dic
#   → return result
def uppercase_keys(dic):  # stored in memory, not executed yet
def uppercase_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(uppercase_keys(...))  # uppercase_keys() runs with dic=[4, 1, 8, 6, 3]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only uppercase_keys is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(uppercase_keys(...))  # uppercase_keys() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(uppercase_keys(...))  # uppercase_keys() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done

"""

"""
Problem 691:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def key_max(dic):  # defines a function with parameters dic
    return max(dic)  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: > is or
# Built-in functions: max, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(key_max(dic))  # key_max() runs first, then print() outputs the result
print(key_max(?))  # key_max() runs first, then print() outputs the result
item > result  # evaluated as True or False → picks which branch
max_key_lower  None  # evaluated as True or False → picks which branch
key_lower > max_key_lower  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def key_max(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(key_max(...))  # key_max() runs with dic=dic
#   → result = dic[0]
#   → for item in dic:
#   →     if item > result:
#   →         result = item
#   → return result
def key_max(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(key_max(...))  # key_max() runs with dic=dic
#   → result = dic[0]
#   → for item in dic:
#   →     if item > result:
#   →         result = item
#   → return result
def key_max(dic):  # stored in memory, not executed yet
def key_max(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(key_max(...))  # key_max() runs with dic=[4, 1, 8, 6, 3]
#   → result = dic[0]
#   → for item in dic:
#   →     if item > result:
#   →         result = item
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only key_max is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(key_max(...))  # key_max() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → print(key_max(...))  # key_max() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(key_max(...))  # key_max() runs first → value goes to print()
#
# Loop: takes one item from dic, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 692:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def square_numbers(lst):  # defines a function with parameters lst
    def square(num):
        return num ** 2
    return list(map(square, lst))  # return sends the result back to the caller
#
# Operators: **
# Built-in functions: list, map, pow()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(square_numbers(numbers))  # square_numbers() runs first, then print() outputs the result
square_numbers(lst)  # arguments evaluated first, then function body runs
print(square_numbers(?))  # square_numbers() runs first, then print() outputs the result
num ** 2  # num → then 2 → then **
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def square_numbers(lst):  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
print(square_numbers(...))  # square_numbers() runs with lst=numbers
#   → import math
#   → return math.pow(num, 2)
def square_numbers(lst):  # stored in memory, not executed yet
def square_numbers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(square_numbers(...))  # square_numbers() runs with lst=[1, 3, 5, 7]
#   → import math
#   → return math.pow(num, 2)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only square_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print(square_numbers(...))  # square_numbers() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(square_numbers(...))  # square_numbers() runs first → value goes to print()

"""

"""
Problem 693:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def string_lengths(lst):  # defines a function with parameters lst
    def length(string):
        return len(string)
    return list(map(length, lst))  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: len, list, map, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(string_lengths(strings))  # string_lengths() runs first, then print() outputs the result
string_lengths(lst)  # arguments evaluated first, then function body runs
print(string_lengths(?))  # string_lengths() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def string_lengths(lst):  # stored in memory, not executed yet
strings = ...  # assigns a value to the variable
print(string_lengths(...))  # string_lengths() runs with lst=strings
#   → return sum((1 for _ in string))
def string_lengths(lst):  # stored in memory, not executed yet
def string_lengths(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(string_lengths(...))  # string_lengths() runs with lst=[1, 3, 5, 7]
#   → return sum((1 for _ in string))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only string_lengths is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → strings = ...  # stored in memory
#   → print(string_lengths(...))  # string_lengths() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(string_lengths(...))  # string_lengths() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done

"""

"""
Problem 694:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_words(lst):  # defines a function with parameters lst
    def word_len(word):
        return word.upper()
    return list(map(word_len, lst))  # return sends the result back to the caller
#
# Operators: - <=
# Built-in functions: chr, list, map, ord, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_words(lst))  # lst_words() runs first, then print() outputs the result
print(lst_words(?))  # lst_words() runs first, then print() outputs the result
'a' <= c  # evaluated as True or False → picks which branch
'a' <= 'z'  # evaluated as True or False → picks which branch
ord(...) - 32  # ord(...) → then 32 → then -
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_words(...))  # lst_words() runs with lst=lst
#   → return str(word).upper()
def lst_words(lst):  # stored in memory, not executed yet
def lst_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_words(...))  # lst_words() runs with lst=[1, 3, 5, 7]
#   → return str(word).upper()
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_words(...))  # lst_words() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_words(...))  # lst_words() runs first → value goes to print()

"""

"""
Problem 695:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_numbers(lst):  # defines a function with parameters lst
    def round_two_decimals(x):
        return round(x, 2)
    return list(map(round_two_decimals, lst))  # return sends the result back to the caller
#
# Built-in functions: list, map, round()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_numbers(lst))  # lst_numbers() runs first, then print() outputs the result
print(lst_numbers(?))  # lst_numbers() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_numbers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_numbers(...))  # lst_numbers() runs with lst=lst
#   → return round(x, 2)
def lst_numbers(lst):  # stored in memory, not executed yet
def lst_numbers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_numbers(...))  # lst_numbers() runs with lst=[1, 3, 5, 7]
#   → return round(x, 2)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_numbers(...))  # lst_numbers() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_numbers(...))  # lst_numbers() runs first → value goes to print()

"""

"""
Problem 696:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def celsius_to_fahrenheit(lst):  # defines a function with parameters lst
    def convert(celsius):
        return celsius * 9 / 5 + 32
    return list(map(convert, lst))  # return sends the result back to the caller
#
# Operators: * + /
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
celsius_to_fahrenheit(celsius_temps)  # arguments evaluated first, then function body runs
celsius_to_fahrenheit(lst)  # arguments evaluated first, then function body runs
print(celsius_to_fahrenheit(?))  # celsius_to_fahrenheit() runs first, then print() outputs the result
? + 32  # ? → then 32 → then +
? / 5  # ? → then 5 → then /
celsius * 9  # celsius → then 9 → then *
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def celsius_to_fahrenheit(lst):  # stored in memory, not executed yet
celsius_temps = ...  # assigns a value to the variable
fahrenheit_temps = ...  # assigns a value to the variable
print(fahrenheit_temps)
def celsius_to_fahrenheit(lst):  # stored in memory, not executed yet
def celsius_to_fahrenheit(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(celsius_to_fahrenheit(...))  # celsius_to_fahrenheit() runs with lst=[1, 3, 5, 7]
#   → return celsius * 9 / 5 + 32
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only celsius_to_fahrenheit is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → celsius_temps = ...  # stored in memory
#   → fahrenheit_temps = ...  # stored in memory
#   → print(fahrenheit_temps)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(celsius_to_fahrenheit(...))  # celsius_to_fahrenheit() runs first → value goes to print()

"""

"""
Problem 697:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def numbers_to_ascii(lst):  # defines a function with parameters lst
    def to_ascii(number):
        return chr(number)
    return list(map(to_ascii, lst))  # return sends the result back to the caller
#
# Built-in functions: chr, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
numbers_to_ascii(numbers)  # arguments evaluated first, then function body runs
numbers_to_ascii(lst)  # arguments evaluated first, then function body runs
print(numbers_to_ascii(?))  # numbers_to_ascii() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def numbers_to_ascii(lst):  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
ascii_characters = ...  # assigns a value to the variable
print(ascii_characters)
def numbers_to_ascii(lst):  # stored in memory, not executed yet
def numbers_to_ascii(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(numbers_to_ascii(...))  # numbers_to_ascii() runs with lst=[1, 3, 5, 7]
#   → return chr(number)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only numbers_to_ascii is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → ascii_characters = ...  # stored in memory
#   → print(ascii_characters)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(numbers_to_ascii(...))  # numbers_to_ascii() runs first → value goes to print()

"""

"""
Problem 698:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_words(lst):  # defines a function with parameters lst
    def reverse_word(word):
        return word[::-1]
    return list(map(reverse_word, lst))  # return sends the result back to the caller
#
# Keywords: for
# Operators: +
# Built-in functions: list, map, reversed()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_words(lst))  # lst_words() runs first, then print() outputs the result
print(lst_words(?))  # lst_words() runs first, then print() outputs the result
char + result  # char → then result → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_words(...))  # lst_words() runs with lst=lst
#   → result = ''
#   → for char in word:
#   →     result = char + result
#   → return result
def lst_words(lst):  # stored in memory, not executed yet
def lst_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_words(...))  # lst_words() runs with lst=[1, 3, 5, 7]
#   → result = ''
#   → for char in word:
#   →     result = char + result
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_words(...))  # lst_words() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_words(...))  # lst_words() runs first → value goes to print()
#
# Loop: takes one item from word, runs body, repeats until done

"""

"""
Problem 700:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_integers(lst):  # defines a function with parameters lst
    def double_num(number):
        return number * 2
    return list(map(double_num, lst))  # return sends the result back to the caller
#
# Keywords: for
# Operators: *
# Built-in functions: list, map, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_integers(lst))  # lst_integers() runs first, then print() outputs the result
print(lst_integers(?))  # lst_integers() runs first, then print() outputs the result
number * 2  # number → then 2 → then *
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_integers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_integers(...))  # lst_integers() runs with lst=lst
#   → return pow(number, 2)
def lst_integers(lst):  # stored in memory, not executed yet
def lst_integers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_integers(...))  # lst_integers() runs with lst=[1, 3, 5, 7]
#   → return pow(number, 2)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_integers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_integers(...))  # lst_integers() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_integers(...))  # lst_integers() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done

"""

"""
Problem 701:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_words(lst):  # defines a function with parameters lst
    def first_char(word):
        return word[0]
    return list(map(first_char, lst))  # return sends the result back to the caller
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_words(lst))  # lst_words() runs first, then print() outputs the result
print(lst_words(?))  # lst_words() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_words(...))  # lst_words() runs with lst=lst
#   → return word[0]
def lst_words(lst):  # stored in memory, not executed yet
def lst_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_words(...))  # lst_words() runs with lst=[1, 3, 5, 7]
#   → return word[0]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_words(...))  # lst_words() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_words(...))  # lst_words() runs first → value goes to print()

"""

"""
Problem 702:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_words(lst):  # defines a function with parameters lst
    def binary(word):
        return int(word, 2)
    return list(map(binary, lst))  # return sends the result back to the caller
#
# Built-in functions: int, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_words(lst))  # lst_words() runs first, then print() outputs the result
print(lst_words(?))  # lst_words() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_words(...))  # lst_words() runs with lst=lst
#   → return int(word, 2)
def lst_words(lst):  # stored in memory, not executed yet
def lst_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_words(...))  # lst_words() runs with lst=[1, 3, 5, 7]
#   → return int(word, 2)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_words(...))  # lst_words() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_words(...))  # lst_words() runs first → value goes to print()

"""

"""
Problem 703:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_mixed_case(lst):  # defines a function with parameters lst
    def lowercase(string):
        return string.lower()
    return list(map(lowercase, lst))  # return sends the result back to the caller
#
# Operators: + <=
# Built-in functions: chr, list, map, ord, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_mixed_case(lst))  # lst_mixed_case() runs first, then print() outputs the result
print(lst_mixed_case(?))  # lst_mixed_case() runs first, then print() outputs the result
'A' <= c  # evaluated as True or False → picks which branch
'A' <= 'Z'  # evaluated as True or False → picks which branch
ord(...) + 32  # ord(...) → then 32 → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_mixed_case(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_mixed_case(...))  # lst_mixed_case() runs with lst=lst
#   → return str(string).lower()
def lst_mixed_case(lst):  # stored in memory, not executed yet
def lst_mixed_case(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_mixed_case(...))  # lst_mixed_case() runs with lst=[1, 3, 5, 7]
#   → return str(string).lower()
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_mixed_case is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_mixed_case(...))  # lst_mixed_case() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_mixed_case(...))  # lst_mixed_case() runs first → value goes to print()

"""

"""
Problem 704:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_integers(lst1, lst2):  # defines a function with parameters lst1, lst2
    def multiply(num1, num2):
        return num1 * num2
    return list(map(multiply, lst1, lst2))  # return sends the result back to the caller
#
# Keywords: for
# Operators: *
# Built-in functions: list, map, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_integers(lst1, lst2))  # lst_integers() runs first, then print() outputs the result
print(lst_integers(?, ?))  # lst_integers() runs first, then print() outputs the result
num1 * num2  # num1 → then num2 → then *
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_integers(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
print(lst_integers(...))  # lst_integers() runs with lst1=lst1, lst2=lst2
#   → return pow(num1, num2)
def lst_integers(lst1, lst2):  # stored in memory, not executed yet
def lst_integers(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_integers(...))  # lst_integers() runs with lst1=[2, 4, 6], lst2=[1, 3, 5]
#   → return pow(num1, num2)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_integers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(lst_integers(...))  # lst_integers() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_integers(...))  # lst_integers() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done

"""

"""
Problem 705:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def euclidean_distances(points):  # defines a function with parameters points
    def distance(point):
        return math.sqrt(point[0] ** 2 + point[1] ** 2)
    return list(map(distance, points))  # return sends the result back to the caller
#
# Operators: + **
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(euclidean_distances(points))  # euclidean_distances() runs first, then print() outputs the result
print(euclidean_distances(25))  # euclidean_distances() runs first, then print() outputs the result
? + ?  # ? → then ? → then +
? ** 2  # ? → then 2 → then **
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import math
def euclidean_distances(points):  # stored in memory, not executed yet
points = ...  # assigns a value to the variable
print(euclidean_distances(...))  # euclidean_distances() runs with points=points
#   → return math.sqrt(point[0] ** 2 + point[1] ** 2)
def euclidean_distances(points):  # stored in memory, not executed yet
def euclidean_distances(points):  # stored in memory, not executed yet
points = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(euclidean_distances(...))  # euclidean_distances() runs with points=25
#   → return math.sqrt(point[0] ** 2 + point[1] ** 2)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only euclidean_distances is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → points = ...  # stored in memory
#   → print(euclidean_distances(...))  # euclidean_distances() runs first → value goes to print()
#   → points = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(euclidean_distances(...))  # euclidean_distances() runs first → value goes to print()

"""

"""
Problem 706:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_emails(lst):  # defines a function with parameters lst
    def domain(string):
        return string.split('@')[1]
    return list(map(domain, lst))  # return sends the result back to the caller
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_emails(lst))  # lst_emails() runs first, then print() outputs the result
print(lst_emails(?))  # lst_emails() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_emails(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_emails(...))  # lst_emails() runs with lst=lst
#   → return string.split('@')[1]
def lst_emails(lst):  # stored in memory, not executed yet
def lst_emails(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_emails(...))  # lst_emails() runs with lst=[1, 3, 5, 7]
#   → return string.split('@')[1]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_emails is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_emails(...))  # lst_emails() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_emails(...))  # lst_emails() runs first → value goes to print()

"""

"""
Problem 707:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_integers(lst):  # defines a function with parameters lst
    def even_odd(number):
        if number % 2 == 0:
            return 'Even'
        else:
            return 'Odd'
    return list(map(even_odd, lst))  # return sends the result back to the caller
#
# Keywords: if/else
# Operators: % ==
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_integers(lst))  # lst_integers() runs first, then print() outputs the result
print(lst_integers(?))  # lst_integers() runs first, then print() outputs the result
? == 0  # evaluated as True or False → picks which branch
number % 2  # number → then 2 → then %
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_integers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_integers(...))  # lst_integers() runs with lst=lst
#   → return 'Even'
def lst_integers(lst):  # stored in memory, not executed yet
def lst_integers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_integers(...))  # lst_integers() runs with lst=[1, 3, 5, 7]
#   → return 'Even'
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_integers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_integers(...))  # lst_integers() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_integers(...))  # lst_integers() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 708:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def negate_bool(value):  # defines a function with parameters value
    return not value  # return sends the result back to the caller
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
negate_bool(value)  # arguments evaluated first, then function body runs
print(negate_bool(25))  # negate_bool() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def negate_bool(value):  # stored in memory, not executed yet
bool_list = ...  # assigns a value to the variable
negated_list = ...  # assigns a value to the variable
print(negated_list)
def negate_bool(value):  # stored in memory, not executed yet
def negate_bool(value):  # stored in memory, not executed yet
value = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(negate_bool(...))  # negate_bool() runs with value=25
#   → return not value
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only negate_bool is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → bool_list = ...  # stored in memory
#   → negated_list = ...  # stored in memory
#   → print(negated_list)
#   → value = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(negate_bool(...))  # negate_bool() runs first → value goes to print()

"""

"""
Problem 709:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def negate_bool(bool_list):  # defines a function with parameters bool_list
    def inner(value):
        return not value
    return list(map(inner, bool_list))  # return sends the result back to the caller
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
negate_bool(bool_list)  # arguments evaluated first, then function body runs
print(negate_bool(?))  # negate_bool() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def negate_bool(bool_list):  # stored in memory, not executed yet
bool_list = ...  # assigns a value to the variable
negate_bool(bool_list)  # calls negate_bool with bool_list=bool_list
#   → return not value
def negate_bool(value):  # stored in memory, not executed yet
bool_list = ...  # assigns a value to the variable
negated_list = ...  # assigns a value to the variable
print(negated_list)
def negate_bool(bool_list):  # stored in memory, not executed yet
def negate_bool(bool_list):  # stored in memory, not executed yet
bool_list = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(negate_bool(...))  # negate_bool() runs with bool_list=[4, 1, 8, 6, 3]
#   → return not value
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only negate_bool is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → bool_list = ...  # stored in memory
#   → negate_bool(bool_list)  # jumps into negate_bool(), runs body, returns
#   → bool_list = ...  # stored in memory
#   → negated_list = ...  # stored in memory
#   → print(negated_list)
#   → bool_list = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(negate_bool(...))  # negate_bool() runs first → value goes to print()

"""

"""
Problem 710:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def negate_booleans(lst):  # defines a function with parameters lst
    def negate(value):
        return not value
    return list(map(negate, lst))  # return sends the result back to the caller
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(negate_booleans(lst))  # negate_booleans() runs first, then print() outputs the result
print(negate_booleans(?))  # negate_booleans() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def negate_booleans(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(negate_booleans(...))  # negate_booleans() runs with lst=lst
#   → return not value
def negate_booleans(lst):  # stored in memory, not executed yet
def negate_booleans(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(negate_booleans(...))  # negate_booleans() runs with lst=[1, 3, 5, 7]
#   → return not value
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only negate_booleans is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(negate_booleans(...))  # negate_booleans() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(negate_booleans(...))  # negate_booleans() runs first → value goes to print()

"""

"""
Problem 712:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_sentence(lst):  # defines a function with parameters lst
    def cap(word):
        word = word.capitalize()
        return word
    return list(map(cap, lst))  # return sends the result back to the caller
#
# Built-in functions: list, map, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_sentence(lst))  # lst_sentence() runs first, then print() outputs the result
print(lst_sentence(?))  # lst_sentence() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_sentence(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_sentence(...))  # lst_sentence() runs with lst=lst
#   → return str(word).capitalize()
def lst_sentence(lst):  # stored in memory, not executed yet
def lst_sentence(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_sentence(...))  # lst_sentence() runs with lst=[1, 3, 5, 7]
#   → return str(word).capitalize()
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_sentence is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_sentence(...))  # lst_sentence() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_sentence(...))  # lst_sentence() runs first → value goes to print()

"""

"""
Problem 713:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_sentence(lst):  # defines a function with parameters lst
    def remove_spaces(word):
        return word.replace(' ', '')
    return list(map(remove_spaces, lst))  # return sends the result back to the caller
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_sentence(lst))  # lst_sentence() runs first, then print() outputs the result
print(lst_sentence(?))  # lst_sentence() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_sentence(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_sentence(...))  # lst_sentence() runs with lst=lst
#   → return word.replace(' ', '')
def lst_sentence(lst):  # stored in memory, not executed yet
def lst_sentence(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_sentence(...))  # lst_sentence() runs with lst=[1, 3, 5, 7]
#   → return word.replace(' ', '')
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_sentence is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_sentence(...))  # lst_sentence() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_sentence(...))  # lst_sentence() runs first → value goes to print()

"""

"""
Problem 714:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_of_tuples(lst):  # defines a function with parameters lst
    def area_lst(dimensions):
        width, height = dimensions
        area = width * height
        return area
    return list(map(area_lst, lst))  # return sends the result back to the caller
#
# Keywords: for
# Operators: *
# Built-in functions: list, map, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_of_tuples(lst))  # lst_of_tuples() runs first, then print() outputs the result
print(lst_of_tuples(?))  # lst_of_tuples() runs first, then print() outputs the result
width * height  # width → then height → then *
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_of_tuples(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_of_tuples(...))  # lst_of_tuples() runs with lst=lst
#   → return pow(width, height)
def lst_of_tuples(lst):  # stored in memory, not executed yet
def lst_of_tuples(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_of_tuples(...))  # lst_of_tuples() runs with lst=[1, 3, 5, 7]
#   → return pow(width, height)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_of_tuples is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_of_tuples(...))  # lst_of_tuples() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_of_tuples(...))  # lst_of_tuples() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done

"""

"""
Problem 715:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def extract_domain(lst):  # defines a function with parameters lst
    def domain(url):
        return url.split('//')[-1].split('/')[0]
    return list(map(domain, lst))  # return sends the result back to the caller
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(extract_domain(urls))  # extract_domain() runs first, then print() outputs the result
extract_domain(lst)  # arguments evaluated first, then function body runs
print(extract_domain(?))  # extract_domain() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def extract_domain(lst):  # stored in memory, not executed yet
urls = ...  # assigns a value to the variable
print(extract_domain(...))  # extract_domain() runs with lst=urls
#   → return url.split('//')[-1].split('/')[0]
def extract_domain(lst):  # stored in memory, not executed yet
def extract_domain(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(extract_domain(...))  # extract_domain() runs with lst=[1, 3, 5, 7]
#   → return url.split('//')[-1].split('/')[0]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only extract_domain is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → urls = ...  # stored in memory
#   → print(extract_domain(...))  # extract_domain() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(extract_domain(...))  # extract_domain() runs first → value goes to print()

"""

"""
Problem 716:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def pair_elements(numbers, strings):  # defines a function with parameters numbers, strings
    def pair(num, string):
        return (num, string)
    return list(map(pair, numbers, strings))  # return sends the result back to the caller
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(pair_elements(numbers, strings))  # pair_elements() runs first, then print() outputs the result
print(pair_elements(?, 'world'))  # pair_elements() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def pair_elements(numbers, strings):  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
strings = ...  # assigns a value to the variable
print(pair_elements(...))  # pair_elements() runs with numbers=numbers, strings=strings
#   → return (num, string)
def pair_elements(numbers, strings):  # stored in memory, not executed yet
def pair_elements(numbers, strings):  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
strings = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(pair_elements(...))  # pair_elements() runs with numbers=[4, 1, 8, 6, 3], strings='world'
#   → return (num, string)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only pair_elements is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → strings = ...  # stored in memory
#   → print(pair_elements(...))  # pair_elements() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(pair_elements(...))  # pair_elements() runs first → value goes to print()

"""

"""
Problem 717:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lowercase_to_uppercase(lst):  # defines a function with parameters lst
    def to_uppercase(letter):
        return letter.upper()
    return list(map(to_uppercase, lst))  # return sends the result back to the caller
#
# Operators: - <=
# Built-in functions: chr, list, map, ord, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lowercase_to_uppercase(lst))  # lowercase_to_uppercase() runs first, then print() outputs the result
print(lowercase_to_uppercase(?))  # lowercase_to_uppercase() runs first, then print() outputs the result
'a' <= c  # evaluated as True or False → picks which branch
'a' <= 'z'  # evaluated as True or False → picks which branch
ord(...) - 32  # ord(...) → then 32 → then -
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lowercase_to_uppercase(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lowercase_to_uppercase(...))  # lowercase_to_uppercase() runs with lst=lst
#   → return str(letter).upper()
def lowercase_to_uppercase(lst):  # stored in memory, not executed yet
def lowercase_to_uppercase(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lowercase_to_uppercase(...))  # lowercase_to_uppercase() runs with lst=[1, 3, 5, 7]
#   → return str(letter).upper()
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lowercase_to_uppercase is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lowercase_to_uppercase(...))  # lowercase_to_uppercase() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lowercase_to_uppercase(...))  # lowercase_to_uppercase() runs first → value goes to print()

"""

"""
Problem 718:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def factorial_lst(lst):  # defines a function with parameters lst
    def factorial(num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result
    return list(map(factorial, lst))  # return sends the result back to the caller
#
# Keywords: for
# Operators: +
# Built-in functions: list, map, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(factorial_lst(lst))  # factorial_lst() runs first, then print() outputs the result
print(factorial_lst(?))  # factorial_lst() runs first, then print() outputs the result
num + 1  # num → then 1 → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def factorial_lst(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(factorial_lst(...))  # factorial_lst() runs with lst=lst
#   → return result
import math
def factorial_lst(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(factorial_lst(...))  # factorial_lst() runs with lst=lst
#   → return result
def factorial_lst(lst):  # stored in memory, not executed yet
def factorial_lst(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(factorial_lst(...))  # factorial_lst() runs with lst=[1, 3, 5, 7]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only factorial_lst is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(factorial_lst(...))  # factorial_lst() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(factorial_lst(...))  # factorial_lst() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(factorial_lst(...))  # factorial_lst() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done

"""

"""
Problem 719:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def reverse_words_in_sentences(lst):  # defines a function with parameters lst
    def reverse_sentence(sentence):
        words = sentence.split()
        reversed_words = []
        for word in words:
            reversed_words.append(word[::-1])
        return ' '.join(reversed_words)
    return list(map(reverse_sentence, lst))  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(reverse_words_in_sentences(lst))  # reverse_words_in_sentences() runs first, then print() outputs the result
print(reverse_words_in_sentences(?))  # reverse_words_in_sentences() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def reverse_words_in_sentences(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(reverse_words_in_sentences(...))  # reverse_words_in_sentences() runs with lst=lst
#   → return list(map(lambda word: word[::-1], words))
def reverse_words_in_sentences(lst):  # stored in memory, not executed yet
def reverse_words_in_sentences(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(reverse_words_in_sentences(...))  # reverse_words_in_sentences() runs with lst=[1, 3, 5, 7]
#   → return list(map(lambda word: word[::-1], words))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only reverse_words_in_sentences is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(reverse_words_in_sentences(...))  # reverse_words_in_sentences() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(reverse_words_in_sentences(...))  # reverse_words_in_sentences() runs first → value goes to print()
#
# Loop: takes one item from words, runs body, repeats until done

"""

"""
Problem 720:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_strings(lst):  # defines a function with parameters lst
    def alpha_only(word):
        if word.isalpha():
            return True
        else:
            return False
    return list(map(alpha_only, lst))  # return sends the result back to the caller
#
# Keywords: if/else
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_strings(lst))  # lst_strings() runs first, then print() outputs the result
print(lst_strings(?))  # lst_strings() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_strings(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_strings(...))  # lst_strings() runs with lst=lst
#   → return True
def lst_strings(lst):  # stored in memory, not executed yet
def lst_strings(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_strings(...))  # lst_strings() runs with lst=[1, 3, 5, 7]
#   → return True
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_strings is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_strings(...))  # lst_strings() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_strings(...))  # lst_strings() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 721:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def square_floats(lst):  # defines a function with parameters lst
    def square(num):
        return num * num
    return list(map(square, lst))  # return sends the result back to the caller
#
# Keywords: for
# Operators: *
# Built-in functions: list, map, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(square_floats(lst))  # square_floats() runs first, then print() outputs the result
print(square_floats(?))  # square_floats() runs first, then print() outputs the result
num * num  # num → then num → then *
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def square_floats(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(square_floats(...))  # square_floats() runs with lst=lst
#   → return pow(num, num)
def square_floats(lst):  # stored in memory, not executed yet
def square_floats(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(square_floats(...))  # square_floats() runs with lst=[1, 3, 5, 7]
#   → return pow(num, num)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only square_floats is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(square_floats(...))  # square_floats() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(square_floats(...))  # square_floats() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done

"""

"""
Problem 722:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def format_phone_numbers(lst):  # defines a function with parameters lst
    def format_number(number):
        return f'+1-{number}'
    return list(map(format_number, lst))  # return sends the result back to the caller
#
# Operators: %
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(format_phone_numbers(lst))  # format_phone_numbers() runs first, then print() outputs the result
print(format_phone_numbers(?))  # format_phone_numbers() runs first, then print() outputs the result
'+1-%s' % number  # '+1-%s' → then number → then %
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def format_phone_numbers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(format_phone_numbers(...))  # format_phone_numbers() runs with lst=lst
#   → return '+1-%s' % number
def format_phone_numbers(lst):  # stored in memory, not executed yet
def format_phone_numbers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(format_phone_numbers(...))  # format_phone_numbers() runs with lst=[1, 3, 5, 7]
#   → return '+1-%s' % number
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only format_phone_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(format_phone_numbers(...))  # format_phone_numbers() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(format_phone_numbers(...))  # format_phone_numbers() runs first → value goes to print()

"""

"""
Problem 723:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def absolute_values(lst):  # defines a function with parameters lst
    def absolute(num):
        return abs(num)
    return list(map(absolute, lst))  # return sends the result back to the caller
#
# Built-in functions: abs, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(absolute_values(lst))  # absolute_values() runs first, then print() outputs the result
print(absolute_values(?))  # absolute_values() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def absolute_values(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(absolute_values(...))  # absolute_values() runs with lst=lst
#   → return abs(num)
def absolute_values(lst):  # stored in memory, not executed yet
def absolute_values(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(absolute_values(...))  # absolute_values() runs with lst=[1, 3, 5, 7]
#   → return abs(num)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only absolute_values is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(absolute_values(...))  # absolute_values() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(absolute_values(...))  # absolute_values() runs first → value goes to print()

"""

"""
Problem 724:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def pair_lists(lst1, lst2):  # defines a function with parameters lst1, lst2
    def pair_numbers(num1, num2):
        return (num1, num2)
    return list(map(pair_numbers, lst1, lst2))  # return sends the result back to the caller
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(pair_lists(lst1, lst2))  # pair_lists() runs first, then print() outputs the result
print(pair_lists(?, ?))  # pair_lists() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def pair_lists(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
print(pair_lists(...))  # pair_lists() runs with lst1=lst1, lst2=lst2
#   → return (num1, num2)
def pair_lists(lst1, lst2):  # stored in memory, not executed yet
def pair_lists(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(pair_lists(...))  # pair_lists() runs with lst1=[2, 4, 6], lst2=[1, 3, 5]
#   → return (num1, num2)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only pair_lists is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(pair_lists(...))  # pair_lists() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(pair_lists(...))  # pair_lists() runs first → value goes to print()

"""

"""
Problem 725:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def cartesian_to_polar(lst):  # defines a function with parameters lst
    def to_polar(coords):
        x, y = coords
        r = math.sqrt(x ** 2 + y ** 2)
        theta = math.atan2(y, x)
        return (r, theta)
    return list(map(to_polar, lst))  # return sends the result back to the caller
#
# Operators: + **
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(cartesian_to_polar(coordinates))  # cartesian_to_polar() runs first, then print() outputs the result
cartesian_to_polar(lst)  # arguments evaluated first, then function body runs
print(cartesian_to_polar(?))  # cartesian_to_polar() runs first, then print() outputs the result
? + ?  # ? → then ? → then +
x ** 2  # x → then 2 → then **
y ** 2  # y → then 2 → then **
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import math
def cartesian_to_polar(lst):  # stored in memory, not executed yet
coordinates = ...  # assigns a value to the variable
print(cartesian_to_polar(...))  # cartesian_to_polar() runs with lst=coordinates
#   → return (r, theta)
def cartesian_to_polar(lst):  # stored in memory, not executed yet
def cartesian_to_polar(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(cartesian_to_polar(...))  # cartesian_to_polar() runs with lst=[1, 3, 5, 7]
#   → return (r, theta)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only cartesian_to_polar is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → coordinates = ...  # stored in memory
#   → print(cartesian_to_polar(...))  # cartesian_to_polar() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(cartesian_to_polar(...))  # cartesian_to_polar() runs first → value goes to print()

"""

"""
Problem 726:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_cubes(lst):  # defines a function with parameters lst
    def cube(num):
        return num ** 3
    return list(map(cube, lst))  # return sends the result back to the caller
#
# Operators: **
# Built-in functions: list, map, pow()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_cubes(numbers))  # lst_cubes() runs first, then print() outputs the result
lst_cubes(lst)  # arguments evaluated first, then function body runs
print(lst_cubes(?))  # lst_cubes() runs first, then print() outputs the result
num ** 3  # num → then 3 → then **
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_cubes(lst):  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
print(lst_cubes(...))  # lst_cubes() runs with lst=numbers
#   → import math
#   → return math.pow(num, 3)
def lst_cubes(lst):  # stored in memory, not executed yet
def lst_cubes(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_cubes(...))  # lst_cubes() runs with lst=[1, 3, 5, 7]
#   → import math
#   → return math.pow(num, 3)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_cubes is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print(lst_cubes(...))  # lst_cubes() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_cubes(...))  # lst_cubes() runs first → value goes to print()

"""

"""
Problem 727:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_squares_and_cubes(lst):  # defines a function with parameters lst
    def square_and_cube(num):
        return (num ** 2, num ** 3)
    return list(map(square_and_cube, lst))  # return sends the result back to the caller
#
# Operators: **
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_squares_and_cubes(lst))  # lst_squares_and_cubes() runs first, then print() outputs the result
print(lst_squares_and_cubes(?))  # lst_squares_and_cubes() runs first, then print() outputs the result
num ** 2  # num → then 2 → then **
num ** 3  # num → then 3 → then **
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_squares_and_cubes(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_squares_and_cubes(...))  # lst_squares_and_cubes() runs with lst=lst
#   → return (num ** 2, num ** 3)
def lst_squares_and_cubes(lst):  # stored in memory, not executed yet
def lst_squares_and_cubes(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_squares_and_cubes(...))  # lst_squares_and_cubes() runs with lst=[1, 3, 5, 7]
#   → return (num ** 2, num ** 3)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_squares_and_cubes is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_squares_and_cubes(...))  # lst_squares_and_cubes() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_squares_and_cubes(...))  # lst_squares_and_cubes() runs first → value goes to print()

"""

"""
Problem 728:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def rgb_to_hex(lst):  # defines a function with parameters lst
    def to_hex(rgb):
        return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
    return list(map(to_hex, lst))  # return sends the result back to the caller
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(rgb_to_hex(lst))  # rgb_to_hex() runs first, then print() outputs the result
print(rgb_to_hex(?))  # rgb_to_hex() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def rgb_to_hex(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(rgb_to_hex(...))  # rgb_to_hex() runs with lst=lst
#   → return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
def rgb_to_hex(lst):  # stored in memory, not executed yet
def rgb_to_hex(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(rgb_to_hex(...))  # rgb_to_hex() runs with lst=[1, 3, 5, 7]
#   → return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only rgb_to_hex is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(rgb_to_hex(...))  # rgb_to_hex() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(rgb_to_hex(...))  # rgb_to_hex() runs first → value goes to print()

"""

"""
Problem 729:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def mixed_case_string(lst):  # defines a function with parameters lst
    def second_uppercase(word):
        return word[0] + word[1].upper() + word[2:]
    return list(map(second_uppercase, lst))  # return sends the result back to the caller
#
# Operators: +
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(mixed_case_string(lst))  # mixed_case_string() runs first, then print() outputs the result
print(mixed_case_string(?))  # mixed_case_string() runs first, then print() outputs the result
? + ?  # ? → then ? → then +
? + ?.upper(...)  # ? → then ?.upper(...) → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def mixed_case_string(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(mixed_case_string(...))  # mixed_case_string() runs with lst=lst
#   → return word[0] + word[1].upper() + word[2:]
def mixed_case_string(lst):  # stored in memory, not executed yet
def mixed_case_string(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(mixed_case_string(...))  # mixed_case_string() runs with lst=[1, 3, 5, 7]
#   → return word[0] + word[1].upper() + word[2:]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only mixed_case_string is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(mixed_case_string(...))  # mixed_case_string() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(mixed_case_string(...))  # mixed_case_string() runs first → value goes to print()

"""

"""
Problem 730:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def convert_dates(date_list):  # defines a function with parameters date_list
    def parse_date(date_string):
        return datetime.strptime(date_string, '%Y-%m-%d')
    return list(map(parse_date, date_list))  # return sends the result back to the caller
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(convert_dates(date_list))  # convert_dates() runs first, then print() outputs the result
print(convert_dates(?))  # convert_dates() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from datetime import datetime
def convert_dates(date_list):  # stored in memory, not executed yet
date_list = ...  # assigns a value to the variable
print(convert_dates(...))  # convert_dates() runs with date_list=date_list
#   → return datetime.strptime(date_string, '%Y-%m-%d')
def convert_dates(date_list):  # stored in memory, not executed yet
def convert_dates(date_list):  # stored in memory, not executed yet
date_list = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(convert_dates(...))  # convert_dates() runs with date_list=[4, 1, 8, 6, 3]
#   → return datetime.strptime(date_string, '%Y-%m-%d')
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only convert_dates is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → date_list = ...  # stored in memory
#   → print(convert_dates(...))  # convert_dates() runs first → value goes to print()
#   → date_list = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(convert_dates(...))  # convert_dates() runs first → value goes to print()

"""

"""
Problem 731:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def calculate_square_roots(numbers):  # defines a function with parameters numbers
    def square_root(x):
        return math.sqrt(x)
    return list(map(square_root, numbers))  # return sends the result back to the caller
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(calculate_square_roots(numbers))  # calculate_square_roots() runs first, then print() outputs the result
print(calculate_square_roots(?))  # calculate_square_roots() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import math
def calculate_square_roots(numbers):  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
print(calculate_square_roots(...))  # calculate_square_roots() runs with numbers=numbers
#   → return math.sqrt(x)
def calculate_square_roots(numbers):  # stored in memory, not executed yet
def calculate_square_roots(numbers):  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(calculate_square_roots(...))  # calculate_square_roots() runs with numbers=[4, 1, 8, 6, 3]
#   → return math.sqrt(x)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only calculate_square_roots is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print(calculate_square_roots(...))  # calculate_square_roots() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(calculate_square_roots(...))  # calculate_square_roots() runs first → value goes to print()

"""

"""
Problem 732:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def calculate_percentage(scores, max_score):  # defines a function with parameters scores, max_score
    def percentage(score):
        return score / max_score * 100
    return list(map(percentage, scores))  # return sends the result back to the caller
#
# Operators: * /
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(calculate_percentage(scores, max_score))  # calculate_percentage() runs first, then print() outputs the result
print(calculate_percentage(25, 25))  # calculate_percentage() runs first, then print() outputs the result
? * 100  # ? → then 100 → then *
score / max_score  # score → then max_score → then /
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def calculate_percentage(scores, max_score):  # stored in memory, not executed yet
scores = ...  # assigns a value to the variable
max_score = ...  # assigns a value to the variable
print(calculate_percentage(...))  # calculate_percentage() runs with scores=scores, max_score=max_score
#   → return score / max_score * 100
def calculate_percentage(scores, max_score):  # stored in memory, not executed yet
def calculate_percentage(scores, max_score):  # stored in memory, not executed yet
scores = ...  # assigns a value to the variable
max_score = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(calculate_percentage(...))  # calculate_percentage() runs with scores=25, max_score=25
#   → return score / max_score * 100
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only calculate_percentage is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → scores = ...  # stored in memory
#   → max_score = ...  # stored in memory
#   → print(calculate_percentage(...))  # calculate_percentage() runs first → value goes to print()
#   → scores = ...  # stored in memory
#   → max_score = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(calculate_percentage(...))  # calculate_percentage() runs first → value goes to print()

"""

"""
Problem 733:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def add(a, b):  # defines a function with parameters a, b
    return a + b  # return sends the result back to the caller
#
# Keywords: for
# Operators: +
# Built-in functions: sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
sum_list(numbers)  # arguments evaluated first, then function body runs
add(a, b)  # arguments evaluated first, then function body runs
print(add(20, 30))  # add() runs first, then print() outputs the result
a + b  # a → then b → then +
add(total, number)  # arguments evaluated first, then function body runs
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def add(a, b):  # stored in memory, not executed yet
def sum_list(numbers):  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
def add(a, b):  # stored in memory, not executed yet
def add(a, b):  # stored in memory, not executed yet
a = ...  # assigns a value to the variable
b = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(add(...))  # add() runs with a=20, b=30
#   → import operator
#   → return operator.add(a, b)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — add, sum_list are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(add(...))  # add() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done

"""

"""
Problem 734:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def is_even(n):  # defines a function with parameters n
    return n % 2 == 0  # return sends the result back to the caller
#
# Operators: % ==
# Built-in functions: filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
filter_even_numbers(numbers)  # arguments evaluated first, then function body runs
is_even(n)  # arguments evaluated first, then function body runs
print(is_even(15))  # is_even() runs first, then print() outputs the result
? == 0  # evaluated as True or False → picks which branch
n % 2  # n → then 2 → then %
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def is_even(n):  # stored in memory, not executed yet
def filter_even_numbers(numbers):  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
even_numbers = ...  # assigns a value to the variable
print(even_numbers)
def is_even(n):  # stored in memory, not executed yet
def is_even(n):  # stored in memory, not executed yet
n = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(is_even(...))  # is_even() runs with n=15
#   → return n % 2 == 0
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — filter_even_numbers, is_even are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → even_numbers = ...  # stored in memory
#   → print(even_numbers)
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_even(...))  # is_even() runs first → value goes to print()

"""

"""
Problem 735:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def capitalize_first_letter(word):  # defines a function with parameters word
    return word.capitalize()  # return sends the result back to the caller
#
# Built-in functions: list, map, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(word_list(lst))  # word_list() runs first, then print() outputs the result
capitalize_first_letter(word)  # arguments evaluated first, then function body runs
print(capitalize_first_letter('coding'))  # capitalize_first_letter() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def capitalize_first_letter(word):  # stored in memory, not executed yet
def word_list(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(word_list(...))  # word_list() runs with lst=lst
#   → return list(map(capitalize_first_letter, lst))
def word_list(lst):  # stored in memory, not executed yet
def capitalize_first_letter(word):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(word_list(...))  # word_list() runs with lst=lst
#   → return list(map(capitalize_first_letter, lst))
def capitalize_first_letter(word):  # stored in memory, not executed yet
def capitalize_first_letter(word):  # stored in memory, not executed yet
word = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(capitalize_first_letter(...))  # capitalize_first_letter() runs with word='coding'
#   → return str(word).capitalize()
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — capitalize_first_letter, word_list are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(word_list(...))  # word_list() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(word_list(...))  # word_list() runs first → value goes to print()
#   → word = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(capitalize_first_letter(...))  # capitalize_first_letter() runs first → value goes to print()

"""

"""
Problem 736:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_numbers(lst):  # defines a function with parameters lst
    return find_max(lst)  # return sends the result back to the caller
#
# Built-in functions: max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_numbers(lst))  # lst_numbers() runs first, then print() outputs the result
print(lst_numbers(?))  # lst_numbers() runs first, then print() outputs the result
find_max(lst)  # arguments evaluated first, then function body runs
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_numbers(lst):  # stored in memory, not executed yet
def find_max(numbers):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_numbers(...))  # lst_numbers() runs with lst=lst
#   → return find_max(lst)
def lst_numbers(lst):  # stored in memory, not executed yet
def lst_numbers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_numbers(...))  # lst_numbers() runs with lst=[1, 3, 5, 7]
#   → return find_max(lst)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — find_max, lst_numbers are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_numbers(...))  # lst_numbers() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_numbers(...))  # lst_numbers() runs first → value goes to print()

"""

"""
Problem 737:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_tempertures(lst):  # defines a function with parameters lst
    return list(map(convert_to_celsius, lst))  # return sends the result back to the caller
#
# Operators: - /
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_tempertures(lst))  # lst_tempertures() runs first, then print() outputs the result
print(lst_tempertures(?))  # lst_tempertures() runs first, then print() outputs the result
? / 1.8  # ? → then 1.8 → then /
fahrenheit - 32  # fahrenheit → then 32 → then -
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_tempertures(lst):  # stored in memory, not executed yet
def convert_to_celsius(fahrenheit):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_tempertures(...))  # lst_tempertures() runs with lst=lst
#   → return list(map(convert_to_celsius, lst))
def lst_tempertures(lst):  # stored in memory, not executed yet
def lst_tempertures(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_tempertures(...))  # lst_tempertures() runs with lst=[1, 3, 5, 7]
#   → return list(map(convert_to_celsius, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — convert_to_celsius, lst_tempertures are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_tempertures(...))  # lst_tempertures() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_tempertures(...))  # lst_tempertures() runs first → value goes to print()

"""

"""
Problem 738:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def string_lst(lst):  # defines a function with parameters lst
    return list(map(reverse_string, lst))  # return sends the result back to the caller
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(string_lst(lst))  # string_lst() runs first, then print() outputs the result
print(string_lst(?))  # string_lst() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def string_lst(lst):  # stored in memory, not executed yet
def reverse_string(word):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(string_lst(...))  # string_lst() runs with lst=lst
#   → return list(map(reverse_string, lst))
def string_lst(lst):  # stored in memory, not executed yet
def string_lst(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(string_lst(...))  # string_lst() runs with lst=[1, 3, 5, 7]
#   → return list(map(reverse_string, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — reverse_string, string_lst are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(string_lst(...))  # string_lst() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(string_lst(...))  # string_lst() runs first → value goes to print()

"""

"""
Problem 739:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_words(lst):  # defines a function with parameters lst
    return max(lst, key=count_vowels)  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: in
# Built-in functions: max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_words(lst))  # lst_words() runs first, then print() outputs the result
print(lst_words(?))  # lst_words() runs first, then print() outputs the result
char.lower(...) in vowels  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_words(lst):  # stored in memory, not executed yet
def count_vowels(word):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_words(...))  # lst_words() runs with lst=lst
#   → return max(lst, key=count_vowels)
def lst_words(lst):  # stored in memory, not executed yet
def lst_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_words(...))  # lst_words() runs with lst=[1, 3, 5, 7]
#   → return max(lst, key=count_vowels)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — count_vowels, lst_words are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_words(...))  # lst_words() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_words(...))  # lst_words() runs first → value goes to print()
#
# Loop: takes one item from word, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 740:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_of_word(lst):  # defines a function with parameters lst
    return list(filter(is_palindrome, lst))  # return sends the result back to the caller
#
# Operators: ==
# Built-in functions: filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_of_word(lst))  # lst_of_word() runs first, then print() outputs the result
print(lst_of_word(?))  # lst_of_word() runs first, then print() outputs the result
word == ?  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_of_word(lst):  # stored in memory, not executed yet
def is_palindrome(word):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_of_word(...))  # lst_of_word() runs with lst=lst
#   → return list(filter(is_palindrome, lst))
def lst_of_word(lst):  # stored in memory, not executed yet
def lst_of_word(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_of_word(...))  # lst_of_word() runs with lst=[1, 3, 5, 7]
#   → return list(filter(is_palindrome, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — is_palindrome, lst_of_word are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_of_word(...))  # lst_of_word() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_of_word(...))  # lst_of_word() runs first → value goes to print()

"""

"""
Problem 741:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_of_radii(lst):  # defines a function with parameters lst
    return list(map(calculate_area, lst))  # return sends the result back to the caller
#
# Operators: * **
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_of_radii(lst))  # lst_of_radii() runs first, then print() outputs the result
print(lst_of_radii(?))  # lst_of_radii() runs first, then print() outputs the result
3.14159 * ?  # 3.14159 → then ? → then *
radius ** 2  # radius → then 2 → then **
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_of_radii(lst):  # stored in memory, not executed yet
def calculate_area(radius):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_of_radii(...))  # lst_of_radii() runs with lst=lst
#   → return list(map(calculate_area, lst))
def lst_of_radii(lst):  # stored in memory, not executed yet
def lst_of_radii(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_of_radii(...))  # lst_of_radii() runs with lst=[1, 3, 5, 7]
#   → return list(map(calculate_area, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — calculate_area, lst_of_radii are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_of_radii(...))  # lst_of_radii() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_of_radii(...))  # lst_of_radii() runs first → value goes to print()

"""

"""
Problem 742:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_numbers(lst):  # defines a function with parameters lst
    return list(map(sqaure_number, lst))  # return sends the result back to the caller
#
# Operators: *
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_numbers(lst))  # lst_numbers() runs first, then print() outputs the result
print(lst_numbers(?))  # lst_numbers() runs first, then print() outputs the result
num * num  # num → then num → then *
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_numbers(lst):  # stored in memory, not executed yet
def sqaure_number(num):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_numbers(...))  # lst_numbers() runs with lst=lst
#   → return list(map(sqaure_number, lst))
def lst_numbers(lst):  # stored in memory, not executed yet
def lst_numbers(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_numbers(...))  # lst_numbers() runs with lst=[1, 3, 5, 7]
#   → return list(map(sqaure_number, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — lst_numbers, sqaure_number are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_numbers(...))  # lst_numbers() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_numbers(...))  # lst_numbers() runs first → value goes to print()

"""

"""
Problem 743:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def get_first_n_elements(lst, num):  # defines a function with parameters lst, num
    return lst[:num]  # return sends the result back to the caller
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main())  # main() runs first, then print() outputs the result
get_first_n_elements(lst, num)  # arguments evaluated first, then function body runs
print(get_first_n_elements(?, 25))  # get_first_n_elements() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def get_first_n_elements(lst, num):  # stored in memory, not executed yet
def main():  # stored in memory, not executed yet
print(main(...))  # main() runs with 
#   → lst = [1, 2, 3, 4, 5, 6]
#   → num = 3
#   → return get_first_n_elements(lst, num)
def get_first_n_elements(lst, num):  # stored in memory, not executed yet
def get_first_n_elements(lst, num):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
num = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(get_first_n_elements(...))  # get_first_n_elements() runs with lst=[1, 3, 5, 7], num=25
#   → return lst[:num]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — get_first_n_elements, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(main(...))  # main() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → num = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(get_first_n_elements(...))  # get_first_n_elements() runs first → value goes to print()

"""

"""
Problem 744:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def merge_dicts(dict1, dict2):  # defines a function with parameters dict1, dict2
    return {**dict1, **dict2}  # return sends the result back to the caller
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(combine_dicts(dicts))  # combine_dicts() runs first, then print() outputs the result
merge_dicts(dict1, dict2)  # arguments evaluated first, then function body runs
print(merge_dicts(?, ?))  # merge_dicts() runs first, then print() outputs the result
merge_dicts(result, d)  # arguments evaluated first, then function body runs
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def merge_dicts(dict1, dict2):  # stored in memory, not executed yet
def combine_dicts(dicts):  # stored in memory, not executed yet
dicts = ...  # assigns a value to the variable
print(combine_dicts(...))  # combine_dicts() runs with dicts=dicts
#   → result = {}
#   → for d in dicts:
#   →     result = merge_dicts(result, d)
#   → return result
def merge_dicts(dict1, dict2):  # stored in memory, not executed yet
def merge_dicts(dict1, dict2):  # stored in memory, not executed yet
dict1 = ...  # assigns a value to the variable
dict2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(merge_dicts(...))  # merge_dicts() runs with dict1=?, dict2=?
#   → return {**dict1, **dict2}
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — combine_dicts, merge_dicts are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dicts = ...  # stored in memory
#   → print(combine_dicts(...))  # combine_dicts() runs first → value goes to print()
#   → dict1 = ...  # stored in memory
#   → dict2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(merge_dicts(...))  # merge_dicts() runs first → value goes to print()
#
# Loop: takes one item from dicts, runs body, repeats until done

"""

"""
Problem 745:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def format_name(first_name, last_name):  # defines a function with parameters first_name, last_name
    return f'{first_name} {last_name}'  # return sends the result back to the caller
#
# Operators: %
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
format_names(names)  # arguments evaluated first, then function body runs
format_name(first_name, last_name)  # arguments evaluated first, then function body runs
print(format_name('world', 'world'))  # format_name() runs first, then print() outputs the result
'%s %s' % ?  # '%s %s' → then ? → then %
format_name(?, ?)  # arguments evaluated first, then function body runs
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def format_name(first_name, last_name):  # stored in memory, not executed yet
def format_names(lst):  # stored in memory, not executed yet
names = ...  # assigns a value to the variable
formatted_names = ...  # assigns a value to the variable
print(formatted_names)
def format_name(first_name, last_name):  # stored in memory, not executed yet
def format_name(first_name, last_name):  # stored in memory, not executed yet
first_name = ...  # assigns a value to the variable
last_name = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(format_name(...))  # format_name() runs with first_name='world', last_name='world'
#   → return '%s %s' % (first_name, last_name)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — format_name, format_names are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → names = ...  # stored in memory
#   → formatted_names = ...  # stored in memory
#   → print(formatted_names)
#   → first_name = ...  # stored in memory
#   → last_name = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(format_name(...))  # format_name() runs first → value goes to print()

"""

"""
Problem 746:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def find_gcd(a, b):  # defines a function with parameters a, b
    while b:
        a, b = (b, a % b)
    return a  # return sends the result back to the caller
#
# Keywords: while
# Operators: %
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
gcd_of_pairs(pairs)  # arguments evaluated first, then function body runs
find_gcd(a, b)  # arguments evaluated first, then function body runs
print(find_gcd(20, 30))  # find_gcd() runs first, then print() outputs the result
find_gcd(?, ?)  # arguments evaluated first, then function body runs
a % b  # a → then b → then %
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def find_gcd(a, b):  # stored in memory, not executed yet
def gcd_of_pairs(lst):  # stored in memory, not executed yet
pairs = ...  # assigns a value to the variable
gcd_results = ...  # assigns a value to the variable
print(gcd_results)
def find_gcd(a, b):  # stored in memory, not executed yet
def find_gcd(a, b):  # stored in memory, not executed yet
a = ...  # assigns a value to the variable
b = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(find_gcd(...))  # find_gcd() runs with a=20, b=30
#   → return a
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — find_gcd, gcd_of_pairs are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → pairs = ...  # stored in memory
#   → gcd_results = ...  # stored in memory
#   → print(gcd_results)
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_gcd(...))  # find_gcd() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 747:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_elements(lst):  # defines a function with parameters lst
    element = 'tree'
    return count_occurrences(lst, element)  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_elements(lst))  # lst_elements() runs first, then print() outputs the result
print(lst_elements(?))  # lst_elements() runs first, then print() outputs the result
count_occurrences(lst, element)  # arguments evaluated first, then function body runs
item == element  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_elements(lst):  # stored in memory, not executed yet
def count_occurrences(lst, element):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_elements(...))  # lst_elements() runs with lst=lst
#   → return count_occurrences(lst, element)
def lst_elements(lst):  # stored in memory, not executed yet
def lst_elements(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_elements(...))  # lst_elements() runs with lst=[1, 3, 5, 7]
#   → return count_occurrences(lst, element)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — count_occurrences, lst_elements are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_elements(...))  # lst_elements() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_elements(...))  # lst_elements() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 748:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_words(lst1, lst2):  # defines a function with parameters lst1, lst2
    return (sort_lst(lst1), sort_lst(lst2))  # return sends the result back to the caller
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
lst_words(lst1, lst2)  # arguments evaluated first, then function body runs
print(lst_words(?, ?))  # lst_words() runs first, then print() outputs the result
sort_lst(lst1)  # arguments evaluated first, then function body runs
sort_lst(lst2)  # arguments evaluated first, then function body runs
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_words(lst1, lst2):  # stored in memory, not executed yet
def sort_lst(lst):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
sorted_lists = ...  # assigns a value to the variable
print(sorted_lists)
def lst_words(lst1, lst2):  # stored in memory, not executed yet
def lst_words(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_words(...))  # lst_words() runs with lst1=[2, 4, 6], lst2=[1, 3, 5]
#   → return (sort_lst(lst1), sort_lst(lst2))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — lst_words, sort_lst are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → sorted_lists = ...  # stored in memory
#   → print(sorted_lists)
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_words(...))  # lst_words() runs first → value goes to print()

"""

"""
Problem 749:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def domain_names(lst):  # defines a function with parameters lst
    return list(map(extract_URL, lst))  # return sends the result back to the caller
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(domain_names(lst))  # domain_names() runs first, then print() outputs the result
print(domain_names(?))  # domain_names() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def domain_names(lst):  # stored in memory, not executed yet
def extract_URL(url):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(domain_names(...))  # domain_names() runs with lst=lst
#   → return list(map(extract_URL, lst))
def domain_names(lst):  # stored in memory, not executed yet
def domain_names(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(domain_names(...))  # domain_names() runs with lst=[1, 3, 5, 7]
#   → return list(map(extract_URL, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — domain_names, extract_URL are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(domain_names(...))  # domain_names() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(domain_names(...))  # domain_names() runs first → value goes to print()

"""

"""
Problem 750:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_sites(lst):  # defines a function with parameters lst
    return remove_duplicates(lst)  # return sends the result back to the caller
#
# Built-in functions: list, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_sites(lst))  # lst_sites() runs first, then print() outputs the result
print(lst_sites(?))  # lst_sites() runs first, then print() outputs the result
remove_duplicates(lst)  # arguments evaluated first, then function body runs
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_sites(lst):  # stored in memory, not executed yet
def remove_duplicates(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_sites(...))  # lst_sites() runs with lst=lst
#   → return remove_duplicates(lst)
def lst_sites(lst):  # stored in memory, not executed yet
def lst_sites(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_sites(...))  # lst_sites() runs with lst=[1, 3, 5, 7]
#   → return remove_duplicates(lst)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — lst_sites, remove_duplicates are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_sites(...))  # lst_sites() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_sites(...))  # lst_sites() runs first → value goes to print()

"""

"""
Problem 751:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(lst):  # defines a function with parameters lst
    result = []
    for i in lst:
        for j in i:
            result.append(j)
    return result  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(lst))  # main() runs first, then print() outputs the result
print(lst_of_lists(nested_list))  # lst_of_lists() runs first, then print() outputs the result
print(main(?))  # main() runs first, then print() outputs the result
flatten_list(nested_list)  # arguments evaluated first, then function body runs
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(main(...))  # main() runs with lst=lst
#   → return list(map(lambda i: j, lst))
def lst_of_lists(nested_list):  # stored in memory, not executed yet
def flatten_list(nested_list):  # stored in memory, not executed yet
nested_list = ...  # assigns a value to the variable
print(lst_of_lists(...))  # lst_of_lists() runs with nested_list=nested_list
#   → return flatten_list(nested_list)
def main(lst):  # stored in memory, not executed yet
def main(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with lst=[1, 3, 5, 7]
#   → return list(map(lambda i: j, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — flatten_list, lst_of_lists, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → nested_list = ...  # stored in memory
#   → print(lst_of_lists(...))  # lst_of_lists() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done

"""

"""
Problem 752:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def filter_primes(lst):  # defines a function with parameters lst
    return list(filter(is_prime, lst))  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: % + ** <= ==
# Built-in functions: filter, int, list, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(filter_primes(numbers))  # filter_primes() runs first, then print() outputs the result
filter_primes(lst)  # arguments evaluated first, then function body runs
print(filter_primes(?))  # filter_primes() runs first, then print() outputs the result
n <= 1  # evaluated as True or False → picks which branch
int(...) + 1  # int(...) → then 1 → then +
? == 0  # evaluated as True or False → picks which branch
n % i  # n → then i → then %
n ** 0.5  # n → then 0.5 → then **
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def filter_primes(lst):  # stored in memory, not executed yet
def is_prime(n):  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
print(filter_primes(...))  # filter_primes() runs with lst=numbers
#   → return list(filter(is_prime, lst))
def filter_primes(lst):  # stored in memory, not executed yet
def filter_primes(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(filter_primes(...))  # filter_primes() runs with lst=[1, 3, 5, 7]
#   → return list(filter(is_prime, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — filter_primes, is_prime are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print(filter_primes(...))  # filter_primes() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_primes(...))  # filter_primes() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 753:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(lst):  # defines a function with parameters lst
    def inner(n):
        factorial = 1
        for num in range(1, n + 1):
            factorial *= num
        return factorial
    return list(map(inner, lst))  # return sends the result back to the caller
#
# Keywords: for
# Operators: +
# Built-in functions: list, map, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
main(lst)  # arguments evaluated first, then function body runs
print(lst_of_numbers(lst))  # lst_of_numbers() runs first, then print() outputs the result
print(main(?))  # main() runs first, then print() outputs the result
num + 1  # num → then 1 → then +
n + 1  # n → then 1 → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
main(lst)  # calls main with lst=lst
#   → return factorial
def lst_of_numbers(lst):  # stored in memory, not executed yet
def calculate_factorial(num):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_of_numbers(...))  # lst_of_numbers() runs with lst=lst
#   → return list(map(calculate_factorial, lst))
def main(lst):  # stored in memory, not executed yet
def main(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with lst=[1, 3, 5, 7]
#   → return factorial
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — calculate_factorial, lst_of_numbers, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → main(lst)  # jumps into main(), runs body, returns
#   → lst = ...  # stored in memory
#   → print(lst_of_numbers(...))  # lst_of_numbers() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done

"""

"""
Problem 754:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(dic):  # defines a function with parameters dic
    return sort_dict_by_value(dic)  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: dict, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(dic))  # main() runs first, then print() outputs the result
print(main(25))  # main() runs first, then print() outputs the result
sort_dict_by_value(dic)  # arguments evaluated first, then function body runs
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(dic):  # stored in memory, not executed yet
def sort_dict_by_value(d):  # stored in memory, not executed yet
def get_value(item):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(main(...))  # main() runs with dic=dic
#   → return sort_dict_by_value(dic)
def main(dic):  # stored in memory, not executed yet
def sort_dict_by_value(d):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(main(...))  # main() runs with dic=dic
#   → return sort_dict_by_value(dic)
def main(dic):  # stored in memory, not executed yet
def main(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with dic=25
#   → return sort_dict_by_value(dic)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — get_value, main, sort_dict_by_value are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from sorted_items, runs body, repeats until done

"""

"""
Problem 755:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(lst):  # defines a function with parameters lst
    return get_unique_elements(lst)  # return sends the result back to the caller
#
# Built-in functions: list, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(lst))  # main() runs first, then print() outputs the result
print(main(?))  # main() runs first, then print() outputs the result
get_unique_elements(lst)  # arguments evaluated first, then function body runs
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(lst):  # stored in memory, not executed yet
def get_unique_elements(word):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(main(...))  # main() runs with lst=lst
#   → return get_unique_elements(lst)
def main(lst):  # stored in memory, not executed yet
def main(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with lst=[1, 3, 5, 7]
#   → return get_unique_elements(lst)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — get_unique_elements, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()

"""

"""
Problem 756:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(str1, str2):  # defines a function with parameters str1, str2
    return check_anagram(str1, str2)  # return sends the result back to the caller
#
# Operators: ==
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(str1, str2))  # main() runs first, then print() outputs the result
print(main('world', 'python'))  # main() runs first, then print() outputs the result
check_anagram(str1, str2)  # arguments evaluated first, then function body runs
sorted(...) == sorted(...)  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(str1, str2):  # stored in memory, not executed yet
def check_anagram(x, y):  # stored in memory, not executed yet
str1 = ...  # assigns a value to the variable
str2 = ...  # assigns a value to the variable
print(main(...))  # main() runs with str1=str1, str2=str2
#   → return check_anagram(str1, str2)
def main(str1, str2):  # stored in memory, not executed yet
def main(str1, str2):  # stored in memory, not executed yet
str1 = ...  # assigns a value to the variable
str2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with str1='world', str2='python'
#   → return check_anagram(str1, str2)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — check_anagram, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → str1 = ...  # stored in memory
#   → str2 = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → str1 = ...  # stored in memory
#   → str2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()

"""

"""
Problem 757:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(lst1, target1):  # defines a function with parameters lst1, target1
    return find_index(lst, target1)  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
# Built-in functions: enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(lst1, target1))  # main() runs first, then print() outputs the result
print(main(?, 25))  # main() runs first, then print() outputs the result
find_index(lst, target1)  # arguments evaluated first, then function body runs
word == target  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(lst1, target1):  # stored in memory, not executed yet
def find_index(lst, target):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
target1 = ...  # assigns a value to the variable
print(main(...))  # main() runs with lst1=lst1, target1=target1
#   → return find_index(lst, target1)
def main(lst1, target1):  # stored in memory, not executed yet
def main(lst1, target1):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
target1 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with lst1=[2, 4, 6], target1=25
#   → return find_index(lst, target1)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — find_index, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → target1 = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → target1 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 758:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(n):  # defines a function with parameters n
    return generate_fibonacci(n)  # return sends the result back to the caller
#
# Keywords: for
# Operators: +
# Built-in functions: range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(n))  # main() runs first, then print() outputs the result
print(main(15))  # main() runs first, then print() outputs the result
generate_fibonacci(n)  # arguments evaluated first, then function body runs
a + b  # a → then b → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(n):  # stored in memory, not executed yet
def generate_fibonacci(n):  # stored in memory, not executed yet
n = ...  # assigns a value to the variable
print(main(...))  # main() runs with n=n
#   → return generate_fibonacci(n)
def main(n):  # stored in memory, not executed yet
def main(n):  # stored in memory, not executed yet
n = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with n=15
#   → return generate_fibonacci(n)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — generate_fibonacci, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → n = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done

"""

"""
Problem 759:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(lst1, lst2):  # defines a function with parameters lst1, lst2
    avg1 = calculate_average(lst1)
    avg2 = calculate_average(lst2)
    return (avg1, avg2)  # return sends the result back to the caller
#
# Operators: /
# Built-in functions: len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(list1, list2))  # main() runs first, then print() outputs the result
main(lst1, lst2)  # arguments evaluated first, then function body runs
print(main(?, ?))  # main() runs first, then print() outputs the result
calculate_average(lst1)  # arguments evaluated first, then function body runs
calculate_average(lst2)  # arguments evaluated first, then function body runs
total / length_lst  # total → then length_lst → then /
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(lst1, lst2):  # stored in memory, not executed yet
def calculate_average(lst):  # stored in memory, not executed yet
list1 = ...  # assigns a value to the variable
list2 = ...  # assigns a value to the variable
print(main(...))  # main() runs with lst1=list1, lst2=list2
#   → return (avg1, avg2)
def main(lst1, lst2):  # stored in memory, not executed yet
def main(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with lst1=[2, 4, 6], lst2=[1, 3, 5]
#   → return (avg1, avg2)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — calculate_average, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → list1 = ...  # stored in memory
#   → list2 = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()

"""

"""
Problem 760:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(lst):  # defines a function with parameters lst
    return list(map(convert_to_kilometers, lst))  # return sends the result back to the caller
#
# Operators: *
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(lst))  # main() runs first, then print() outputs the result
print(main(?))  # main() runs first, then print() outputs the result
miles * miles_to_km  # miles → then miles_to_km → then *
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(lst):  # stored in memory, not executed yet
def convert_to_kilometers(miles):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(main(...))  # main() runs with lst=lst
#   → return list(map(convert_to_kilometers, lst))
def main(lst):  # stored in memory, not executed yet
def main(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with lst=[1, 3, 5, 7]
#   → return list(map(convert_to_kilometers, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — convert_to_kilometers, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()

"""

"""
Problem 761:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(lst, n):  # defines a function with parameters lst, n
    return get_last_n_elements(lst, n)  # return sends the result back to the caller
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(lst, n))  # main() runs first, then print() outputs the result
print(main(?, 15))  # main() runs first, then print() outputs the result
get_last_n_elements(lst, n)  # arguments evaluated first, then function body runs
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(lst, n):  # stored in memory, not executed yet
def get_last_n_elements(lst, n):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
n = ...  # assigns a value to the variable
print(main(...))  # main() runs with lst=lst, n=n
#   → return get_last_n_elements(lst, n)
def main(lst, n):  # stored in memory, not executed yet
def main(lst, n):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
n = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with lst=[1, 3, 5, 7], n=15
#   → return get_last_n_elements(lst, n)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — get_last_n_elements, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → n = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()

"""

"""
Problem 763:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(lst):  # defines a function with parameters lst
    return list(filter(get_positive_numbers, lst))  # return sends the result back to the caller
#
# Operators: >
# Built-in functions: filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(lst))  # main() runs first, then print() outputs the result
print(main(?))  # main() runs first, then print() outputs the result
number > 0  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(lst):  # stored in memory, not executed yet
def get_positive_numbers(number):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(main(...))  # main() runs with lst=lst
#   → return list(filter(get_positive_numbers, lst))
def main(lst):  # stored in memory, not executed yet
def main(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with lst=[1, 3, 5, 7]
#   → return list(filter(get_positive_numbers, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — get_positive_numbers, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()

"""

"""
Problem 764:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def get_common_elements(lst1, lst2):  # defines a function with parameters lst1, lst2
    common_word = []
    for word in lst1:
        if word in lst2:
            common_word.append(word)
    return common_word  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: in and not in
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(get_common_elements(lst1, lst2))  # get_common_elements() runs first, then print() outputs the result
print(main(lst1, lst2))  # main() runs first, then print() outputs the result
print(get_common_elements(?, ?))  # get_common_elements() runs first, then print() outputs the result
word in lst2  # evaluated as True or False → picks which branch
item in y  # evaluated as True or False → picks which branch
item not in duplicates  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def get_common_elements(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
print(get_common_elements(...))  # get_common_elements() runs with lst1=lst1, lst2=lst2
#   → return list(map(lambda word: word, lst1))
def main(lst1, lst2):  # stored in memory, not executed yet
def get_common_elements(x, y):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
print(main(...))  # main() runs with lst1=lst1, lst2=lst2
#   → return get_common_elements(lst1, lst2)
def get_common_elements(lst1, lst2):  # stored in memory, not executed yet
def get_common_elements(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(get_common_elements(...))  # get_common_elements() runs with lst1=[2, 4, 6], lst2=[1, 3, 5]
#   → return list(map(lambda word: word, lst1))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — get_common_elements, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(get_common_elements(...))  # get_common_elements() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(get_common_elements(...))  # get_common_elements() runs first → value goes to print()
#
# Loop: takes one item from lst1, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 765:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(lst):  # defines a function with parameters lst
    return list(map(check_even_odd, lst))  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: % ==
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(lst))  # main() runs first, then print() outputs the result
print(main(?))  # main() runs first, then print() outputs the result
? == 0  # evaluated as True or False → picks which branch
n % 2  # n → then 2 → then %
check_even_odd(number)  # arguments evaluated first, then function body runs
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(lst):  # stored in memory, not executed yet
def check_even_odd(n):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(main(...))  # main() runs with lst=lst
#   → return list(map(check_even_odd, lst))
def main(lst):  # stored in memory, not executed yet
def check_even_odd(n):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(main(...))  # main() runs with lst=lst
#   → return list(map(check_even_odd, lst))
def main(lst):  # stored in memory, not executed yet
def main(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with lst=[1, 3, 5, 7]
#   → return list(map(check_even_odd, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — check_even_odd, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 766:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(lst):  # defines a function with parameters lst
    return list(map(convert_to_uppercase, lst))  # return sends the result back to the caller
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(lst))  # main() runs first, then print() outputs the result
print(main(?))  # main() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(lst):  # stored in memory, not executed yet
def convert_to_uppercase(word):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(main(...))  # main() runs with lst=lst
#   → return list(map(convert_to_uppercase, lst))
def main(lst):  # stored in memory, not executed yet
def main(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with lst=[1, 3, 5, 7]
#   → return list(map(convert_to_uppercase, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — convert_to_uppercase, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()

"""

"""
Problem 767:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(lst_str):  # defines a function with parameters lst_str
    return list(map(count_characters, lst_str))  # return sends the result back to the caller
#
# Built-in functions: len, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_characters(lst_str))  # count_characters() runs first, then print() outputs the result
print(main(lst_str))  # main() runs first, then print() outputs the result
print(main('world'))  # main() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(lst_str):  # stored in memory, not executed yet
def count_characters(s):  # stored in memory, not executed yet
lst_str = ...  # assigns a value to the variable
print(count_characters(...))  # count_characters() runs with s=lst_str
#   → return len(s)
def main(lst_str):  # stored in memory, not executed yet
def count_characters(s):  # stored in memory, not executed yet
lst_str = ...  # assigns a value to the variable
print(main(...))  # main() runs with lst_str=lst_str
#   → return list(map(count_characters, lst_str))
def main(lst_str):  # stored in memory, not executed yet
def main(lst_str):  # stored in memory, not executed yet
lst_str = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with lst_str='world'
#   → return list(map(count_characters, lst_str))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — count_characters, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst_str = ...  # stored in memory
#   → print(count_characters(...))  # count_characters() runs first → value goes to print()
#   → lst_str = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → lst_str = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()

"""

"""
Problem 768:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(lst):  # defines a function with parameters lst
    return list(map(remove_special_characters, lst))  # return sends the result back to the caller
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(lst))  # main() runs first, then print() outputs the result
print(main(?))  # main() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(lst):  # stored in memory, not executed yet
def remove_special_characters(s):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(main(...))  # main() runs with lst=lst
#   → return list(map(remove_special_characters, lst))
def main(lst):  # stored in memory, not executed yet
def main(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with lst=[1, 3, 5, 7]
#   → return list(map(remove_special_characters, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, remove_special_characters are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()

"""

"""
Problem 769:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(lst):  # defines a function with parameters lst
    results = []
    for pair in lst:
        results.append(is_substring(pair[0], pair[1]))
    return results  # return sends the result back to the caller
#
# Keywords: for
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(lst))  # main() runs first, then print() outputs the result
print(main(?))  # main() runs first, then print() outputs the result
s1 in s2  # evaluated as True or False → picks which branch
is_substring(?, ?)  # arguments evaluated first, then function body runs
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(lst):  # stored in memory, not executed yet
def is_substring(s1, s2):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(main(...))  # main() runs with lst=lst
#   → return results
def main(lst):  # stored in memory, not executed yet
def main(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with lst=[1, 3, 5, 7]
#   → return results
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — is_substring, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done

"""

"""
Problem 770:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(lst):  # defines a function with parameters lst
    return sum_of_list(lst)  # return sends the result back to the caller
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(lst))  # main() runs first, then print() outputs the result
print(main(?))  # main() runs first, then print() outputs the result
sum_of_list(lst)  # arguments evaluated first, then function body runs
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(lst):  # stored in memory, not executed yet
def sum_of_list(n):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(main(...))  # main() runs with lst=lst
#   → return sum_of_list(lst)
def main(lst):  # stored in memory, not executed yet
def main(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with lst=[1, 3, 5, 7]
#   → return sum_of_list(lst)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, sum_of_list are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done

"""

"""
Problem 771:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(lst):  # defines a function with parameters lst
    return list(filter(get_even_numbers, lst))  # return sends the result back to the caller
#
# Operators: % ==
# Built-in functions: filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(lst))  # main() runs first, then print() outputs the result
print(main(?))  # main() runs first, then print() outputs the result
? == 0  # evaluated as True or False → picks which branch
n % 2  # n → then 2 → then %
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(lst):  # stored in memory, not executed yet
def get_even_numbers(n):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(main(...))  # main() runs with lst=lst
#   → return list(filter(get_even_numbers, lst))
def main(lst):  # stored in memory, not executed yet
def main(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with lst=[1, 3, 5, 7]
#   → return list(filter(get_even_numbers, lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — get_even_numbers, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()

"""

"""
Problem 772:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(lst1, lst2):  # defines a function with parameters lst1, lst2
    return merge_sorted_lists(lst1, lst2)  # return sends the result back to the caller
#
# Operators: +
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(lst1, lst2))  # main() runs first, then print() outputs the result
print(main(?, ?))  # main() runs first, then print() outputs the result
merge_sorted_lists(lst1, lst2)  # arguments evaluated first, then function body runs
x + y  # x → then y → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(lst1, lst2):  # stored in memory, not executed yet
def merge_sorted_lists(x, y):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
print(main(...))  # main() runs with lst1=lst1, lst2=lst2
#   → return merge_sorted_lists(lst1, lst2)
def main(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
main(lst1, lst2)  # calls main with lst1=lst1, lst2=lst2
#   → return merge_sorted_lists(lst1, lst2)
def main(lst1, lst2):  # stored in memory, not executed yet
def main(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with lst1=[2, 4, 6], lst2=[1, 3, 5]
#   → return merge_sorted_lists(lst1, lst2)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, merge_sorted_lists are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → main(lst1, lst2)  # jumps into main(), runs body, returns
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()

"""

"""
Problem 773:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_to_dic(lst1, lst2):  # defines a function with parameters lst1, lst2
    result = {}
    for x, y in zip(lst1, lst2):
        result[x] = y
    return result  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: len, range, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_to_dic(lst1, lst2))  # lst_to_dic() runs first, then print() outputs the result
print(lst_to_dic(?, ?))  # lst_to_dic() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_to_dic(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
print(lst_to_dic(...))  # lst_to_dic() runs with lst1=lst1, lst2=lst2
#   → return result
def lst_to_dic(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
print(lst_to_dic(...))  # lst_to_dic() runs with lst1=lst1, lst2=lst2
#   → return result
def lst_to_dic(lst1, lst2):  # stored in memory, not executed yet
def lst_to_dic(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_to_dic(...))  # lst_to_dic() runs with lst1=[2, 4, 6], lst2=[1, 3, 5]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_to_dic is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(lst_to_dic(...))  # lst_to_dic() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(lst_to_dic(...))  # lst_to_dic() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_to_dic(...))  # lst_to_dic() runs first → value goes to print()
#
# Loop: takes one item from zip(...), runs body, repeats until done

"""

"""
Problem 774:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(dic, key_to_find):  # defines a function with parameters dic, key_to_find
    return dic.get(key_to_find, None)  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(dic, key_to_find))  # main() runs first, then print() outputs the result
print(value_of_specific_key(dic, target))  # value_of_specific_key() runs first, then print() outputs the result
print(main(25, 25))  # main() runs first, then print() outputs the result
key == target  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(dic, key_to_find):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
key_to_find = ...  # assigns a value to the variable
print(main(...))  # main() runs with dic=dic, key_to_find=key_to_find
#   → return dic.get(key_to_find, None)
key_to_find = ...  # assigns a value to the variable
print(main(...))  # main() runs with dic=dic, key_to_find=key_to_find
#   → return dic.get(key_to_find, None)
def value_of_specific_key(dic, target):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
target = ...  # assigns a value to the variable
print(value_of_specific_key(...))  # value_of_specific_key() runs with dic=dic, target=target
#   → for key, value in dic.items():
#   →     if key == target:
#   →         return value
#   → return None
def value_of_specific_key(dic, target):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
target = ...  # assigns a value to the variable
print(value_of_specific_key(...))  # value_of_specific_key() runs with dic=dic, target=target
#   → for key, value in dic.items():
#   →     if key == target:
#   →         return value
#   → return None
def main(dic, key_to_find):  # stored in memory, not executed yet
def main(dic, key_to_find):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
key_to_find = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with dic=25, key_to_find=25
#   → return dic.get(key_to_find, None)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, value_of_specific_key are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → key_to_find = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → key_to_find = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → target = ...  # stored in memory
#   → print(value_of_specific_key(...))  # value_of_specific_key() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → target = ...  # stored in memory
#   → print(value_of_specific_key(...))  # value_of_specific_key() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → key_to_find = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 775:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(dic1, dic2):  # defines a function with parameters dic1, dic2
    merge_dic = dic1.copy()
    for key, value in dic2.items():
        if key in merge_dic:
            merge_dic[key] = [merge_dic[key], value]
        else:
            merge_dic[key] = value
    return merge_dic  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(dic1, dic2))  # main() runs first, then print() outputs the result
print(merge_dicts(dic1, dic2))  # merge_dicts() runs first, then print() outputs the result
print(main(25, 25))  # main() runs first, then print() outputs the result
key in merge_dic  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(dic1, dic2):  # stored in memory, not executed yet
dic1 = ...  # assigns a value to the variable
dic2 = ...  # assigns a value to the variable
print(main(...))  # main() runs with dic1=dic1, dic2=dic2
#   → return merge_dic
def merge_dicts(dic1, dic2):  # stored in memory, not executed yet
dic1 = ...  # assigns a value to the variable
dic2 = ...  # assigns a value to the variable
print(merge_dicts(...))  # merge_dicts() runs with dic1=dic1, dic2=dic2
#   → merged_dict = {**dic1, **dic2}
#   → return merged_dict
def main(dic1, dic2):  # stored in memory, not executed yet
def main(dic1, dic2):  # stored in memory, not executed yet
dic1 = ...  # assigns a value to the variable
dic2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with dic1=25, dic2=25
#   → return merge_dic
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, merge_dicts are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic1 = ...  # stored in memory
#   → dic2 = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → dic1 = ...  # stored in memory
#   → dic2 = ...  # stored in memory
#   → print(merge_dicts(...))  # merge_dicts() runs first → value goes to print()
#   → dic1 = ...  # stored in memory
#   → dic2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from dic2.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 776:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def remove_key(dic, key_to_remove):  # defines a function with parameters dic, key_to_remove
    if key_to_remove in dic:
        del dic[key_to_remove]
    return dic  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: != in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(remove_key(dic, key_to_remove))  # remove_key() runs first, then print() outputs the result
print(main(dic, target))  # main() runs first, then print() outputs the result
print(remove_key(?, 25))  # remove_key() runs first, then print() outputs the result
key_to_remove in dic  # evaluated as True or False → picks which branch
key != target  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def remove_key(dic, key_to_remove):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
key_to_remove = ...  # assigns a value to the variable
print(remove_key(...))  # remove_key() runs with dic=dic, key_to_remove=key_to_remove
#   → return dic
def main(dic, target):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
target = ...  # assigns a value to the variable
print(main(...))  # main() runs with dic=dic, target=target
#   → result = {}
#   → for key, value in dic.items():
#   →     if key != target:
#   →         result[key] = value
#   → return result
def remove_key(dic, key_to_remove):  # stored in memory, not executed yet
def remove_key(dic, key_to_remove):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
key_to_remove = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(remove_key(...))  # remove_key() runs with dic=[4, 1, 8, 6, 3], key_to_remove=25
#   → return dic
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, remove_key are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → key_to_remove = ...  # stored in memory
#   → print(remove_key(...))  # remove_key() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → target = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → key_to_remove = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(remove_key(...))  # remove_key() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 778:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(dic1):  # defines a function with parameters dic1
    if target in dic1.keys():
        return True
    return False  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: == in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(dic1))  # main() runs first, then print() outputs the result
print(does_key_exist(?, 'job'))  # does_key_exist() runs first, then print() outputs the result
print(does_key_exist(?, 'name'))  # does_key_exist() runs first, then print() outputs the result
print(main(25))  # main() runs first, then print() outputs the result
target in dic1.keys(...)  # evaluated as True or False → picks which branch
key == target  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(dic1):  # stored in memory, not executed yet
dic1 = ...  # assigns a value to the variable
target = ...  # assigns a value to the variable
print(main(...))  # main() runs with dic1=dic1
#   → return True
def does_key_exist(dic, target):  # stored in memory, not executed yet
print(does_key_exist(...))  # does_key_exist() runs with dic=?, target='job'
#   → for key in dic.keys():
#   →     if key == target:
#   →         return 'key exists'
#   → return 'key does not exist'
print(does_key_exist(...))  # does_key_exist() runs with dic=?, target='name'
#   → for key in dic.keys():
#   →     if key == target:
#   →         return 'key exists'
#   → return 'key does not exist'
def main(dic1):  # stored in memory, not executed yet
def main(dic1):  # stored in memory, not executed yet
dic1 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with dic1=25
#   → return True
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — does_key_exist, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic1 = ...  # stored in memory
#   → target = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → print(does_key_exist(...))  # does_key_exist() runs first → value goes to print()
#   → print(does_key_exist(...))  # does_key_exist() runs first → value goes to print()
#   → dic1 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 779:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sort_dic(dic):  # defines a function with parameters dic
    return dict(sorted(dic.items()))  # return sends the result back to the caller
#
# Built-in functions: dict, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(sort_dic(dic))  # sort_dic() runs first, then print() outputs the result
print(sort_dic(?))  # sort_dic() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sort_dic(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(sort_dic(...))  # sort_dic() runs with dic=dic
#   → return dict(sorted(dic.items()))
def sort_dic(dic):  # stored in memory, not executed yet
def sort_dic(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sort_dic(...))  # sort_dic() runs with dic=[4, 1, 8, 6, 3]
#   → return dict(sorted(dic.items()))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_dic is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(sort_dic(...))  # sort_dic() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_dic(...))  # sort_dic() runs first → value goes to print()

"""

"""
Problem 780:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(dic):  # defines a function with parameters dic
    dic = dic.items()
    def sort_value(item):
        return item[1]
    return dict(sorted(dic, key=sort_value))  # return sends the result back to the caller
#
# Built-in functions: dict, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(dic))  # main() runs first, then print() outputs the result
print(sort_values(dic))  # sort_values() runs first, then print() outputs the result
print(main(?))  # main() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(main(...))  # main() runs with dic=dic
#   → return item[1]
def sort_values(dic):  # stored in memory, not executed yet
def sort_key(item):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(sort_values(...))  # sort_values() runs with dic=dic
#   → sorted_items = sorted(dic.items(), key=sort_key)
#   → return dict(sorted_items)
def main(dic):  # stored in memory, not executed yet
def main(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with dic=[4, 1, 8, 6, 3]
#   → return item[1]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, sort_key, sort_values are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → print(sort_values(...))  # sort_values() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()

"""

"""
Problem 781:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def frequency_elements(lst):  # defines a function with parameters lst
    result = {}
    for word in lst:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(frequency_elements(lst))  # frequency_elements() runs first, then print() outputs the result
print(frequency_elements(?))  # frequency_elements() runs first, then print() outputs the result
word in result  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def frequency_elements(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(frequency_elements(...))  # frequency_elements() runs with lst=lst
#   → return result
def frequency_elements(lst):  # stored in memory, not executed yet
def frequency_elements(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(frequency_elements(...))  # frequency_elements() runs with lst=[1, 3, 5, 7]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only frequency_elements is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(frequency_elements(...))  # frequency_elements() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(frequency_elements(...))  # frequency_elements() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 782:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def square_dic():  # defines a function with no parameters
    result = {}
    for key in range(1, 6):
        result[key] = key ** 2
    return result  # return sends the result back to the caller
#
# Keywords: for
# Operators: **
# Built-in functions: range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(square_dic())  # square_dic() runs first, then print() outputs the result
key ** 2  # key → then 2 → then **
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def square_dic():  # stored in memory, not executed yet
print(square_dic(...))  # square_dic() runs with 
#   → return result
def square_dic():  # stored in memory, not executed yet
def square_dic():  # stored in memory, not executed yet
result = ...  # assigns a value to the variable
for key in range(...):  # loops once per item
  ? = ...
result = ...  # assigns a value to the variable
print(result)
result = ...  # assigns a value to the variable
for key in range(...):  # loops once per item
  ? = ...
result = ...  # assigns a value to the variable
print(result)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only square_dic is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(square_dic(...))  # square_dic() runs first → value goes to print()
#   → result = ...  # stored in memory
#   → for key in range(...)  # runs body once per item
#   → result = ...  # stored in memory
#   → print(result)
#   → result = ...  # stored in memory
#   → for key in range(...)  # runs body once per item
#   → result = ...  # stored in memory
#   → print(result)
#
# Loop: takes one item from range(...), runs body, repeats until done

"""

"""
Problem 783:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(dic, target):  # defines a function with parameters dic, target
    key_to_update, new_value = target
    if key_to_update in dic:
        dic[key_to_update] = new_value
    return dic  # return sends the result back to the caller
#
# Keywords: if/else
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(dic, target))  # main() runs first, then print() outputs the result
update_value(dic, 'age', 60)  # arguments evaluated first, then function body runs
print(main(?, 'goal'))  # main() runs first, then print() outputs the result
key_to_update in dic  # evaluated as True or False → picks which branch
key in dic  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(dic, target):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
target = ...  # assigns a value to the variable
print(main(...))  # main() runs with dic=dic, target=target
#   → return dic
def update_value(dic, key, new_value):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
update_value(dic, 'age', 60)  # calls update_value with dic=dic, key='age', new_value=60
#   → if key in dic:
#   →     dic[key] = new_value
#   → return dic
print(dic)
def main(dic, target):  # stored in memory, not executed yet
def main(dic, target):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
target = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with dic=[4, 1, 8, 6, 3], target='goal'
#   → return dic
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, update_value are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → target = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → update_value(dic, 'age', 60)  # jumps into update_value(), runs body, returns
#   → print(dic)
#   → dic = ...  # stored in memory
#   → target = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 784:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def get_keys(dic):  # defines a function with parameters dic
    return dic.keys()  # return sends the result back to the caller
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(get_keys(dic))  # get_keys() runs first, then print() outputs the result
print(main(dic))  # main() runs first, then print() outputs the result
print(get_keys(25))  # get_keys() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def get_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(get_keys(...))  # get_keys() runs with dic=dic
#   → return dic.keys()
def main(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(main(...))  # main() runs with dic=dic
#   → for key in dic:
#   →     print(key)
def get_keys(dic):  # stored in memory, not executed yet
def get_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(get_keys(...))  # get_keys() runs with dic=25
#   → return dic.keys()
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — get_keys, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(get_keys(...))  # get_keys() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(get_keys(...))  # get_keys() runs first → value goes to print()
#
# Loop: takes one item from dic, runs body, repeats until done

"""

"""
Problem 785:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def get_keys(dic):  # defines a function with parameters dic
    return dic.values()  # return sends the result back to the caller
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(get_keys(dic))  # get_keys() runs first, then print() outputs the result
print(get_keys(25))  # get_keys() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def get_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(get_keys(...))  # get_keys() runs with dic=dic
#   → return dic.values()
def get_keys(dic):  # stored in memory, not executed yet
def get_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(get_keys(...))  # get_keys() runs with dic=25
#   → return dic.values()
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only get_keys is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(get_keys(...))  # get_keys() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(get_keys(...))  # get_keys() runs first → value goes to print()

"""

"""
Problem 786:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def get_keys(dic):  # defines a function with parameters dic
    return dic.values()  # return sends the result back to the caller
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(get_keys(dic))  # get_keys() runs first, then print() outputs the result
print(get_keys(25))  # get_keys() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def get_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(get_keys(...))  # get_keys() runs with dic=dic
#   → return dic.values()
def get_keys(dic):  # stored in memory, not executed yet
def get_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(get_keys(...))  # get_keys() runs with dic=25
#   → return dic.values()
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only get_keys is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(get_keys(...))  # get_keys() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(get_keys(...))  # get_keys() runs first → value goes to print()

"""

"""
Problem 787:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def largest_value(dic):  # defines a function with parameters dic
    return max(dic.values())  # return sends the result back to the caller
#
# Built-in functions: max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(largest_value(dic))  # largest_value() runs first, then print() outputs the result
print(largest_value(?))  # largest_value() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def largest_value(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(largest_value(...))  # largest_value() runs with dic=dic
#   → return max(dic.values())
def largest_value(dic):  # stored in memory, not executed yet
def largest_value(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(largest_value(...))  # largest_value() runs with dic=[4, 1, 8, 6, 3]
#   → return max(dic.values())
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only largest_value is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(largest_value(...))  # largest_value() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(largest_value(...))  # largest_value() runs first → value goes to print()

"""

"""
Problem 788:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def largest_value(dic):  # defines a function with parameters dic
    return min(dic.values())  # return sends the result back to the caller
#
# Built-in functions: min()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(largest_value(dic))  # largest_value() runs first, then print() outputs the result
print(largest_value(?))  # largest_value() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def largest_value(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(largest_value(...))  # largest_value() runs with dic=dic
#   → return min(dic.values())
def largest_value(dic):  # stored in memory, not executed yet
def largest_value(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(largest_value(...))  # largest_value() runs with dic=[4, 1, 8, 6, 3]
#   → return min(dic.values())
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only largest_value is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(largest_value(...))  # largest_value() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(largest_value(...))  # largest_value() runs first → value goes to print()

"""

"""
Problem 789:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_dic(lst1, lst2):  # defines a function with parameters lst1, lst2
    result = {}
    min_length = min(len(lst1), len(lst2))
    for i in range(min_length):
        result[lst1[i]] = lst2[i]
    return result  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: len, min, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_dic(lst1, lst2))  # lst_dic() runs first, then print() outputs the result
print(lst_dic(?, ?))  # lst_dic() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_dic(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
print(lst_dic(...))  # lst_dic() runs with lst1=lst1, lst2=lst2
#   → return result
def lst_dic(lst1, lst2):  # stored in memory, not executed yet
def lst_dic(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_dic(...))  # lst_dic() runs with lst1=[2, 4, 6], lst2=[1, 3, 5]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_dic is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(lst_dic(...))  # lst_dic() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_dic(...))  # lst_dic() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done

"""

"""
Problem 790:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def combine_dictionaries(dic1, dic2):  # defines a function with parameters dic1, dic2
    result = {}
    for key in dic1:
        result[key] = dic1[key]
    for key, value in dic2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(combine_dictionaries(dic1, dic2))  # combine_dictionaries() runs first, then print() outputs the result
print(combine_dictionaries(?, 25))  # combine_dictionaries() runs first, then print() outputs the result
key in result  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def combine_dictionaries(dic1, dic2):  # stored in memory, not executed yet
dic1 = ...  # assigns a value to the variable
dic2 = ...  # assigns a value to the variable
print(combine_dictionaries(...))  # combine_dictionaries() runs with dic1=dic1, dic2=dic2
#   → return result
def combine_dictionaries(dic1, dic2):  # stored in memory, not executed yet
dic1 = ...  # assigns a value to the variable
dic2 = ...  # assigns a value to the variable
print(combine_dictionaries(...))  # combine_dictionaries() runs with dic1=dic1, dic2=dic2
#   → return result
def combine_dictionaries(dic1, dic2):  # stored in memory, not executed yet
def combine_dictionaries(dic1, dic2):  # stored in memory, not executed yet
dic1 = ...  # assigns a value to the variable
dic2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(combine_dictionaries(...))  # combine_dictionaries() runs with dic1=[4, 1, 8, 6, 3], dic2=25
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only combine_dictionaries is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic1 = ...  # stored in memory
#   → dic2 = ...  # stored in memory
#   → print(combine_dictionaries(...))  # combine_dictionaries() runs first → value goes to print()
#   → dic1 = ...  # stored in memory
#   → dic2 = ...  # stored in memory
#   → print(combine_dictionaries(...))  # combine_dictionaries() runs first → value goes to print()
#   → dic1 = ...  # stored in memory
#   → dic2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(combine_dictionaries(...))  # combine_dictionaries() runs first → value goes to print()
#
# Loop: takes one item from dic1, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 791:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def invert_dictionary(dic):  # defines a function with parameters dic
    inverted = {}
    for key, value in dic.items():
        inverted[value] = key
    return inverted  # return sends the result back to the caller
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(invert_dictionary(dic))  # invert_dictionary() runs first, then print() outputs the result
print(invert_dictionary(25))  # invert_dictionary() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def invert_dictionary(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(invert_dictionary(...))  # invert_dictionary() runs with dic=dic
#   → return inverted
def invert_dictionary(dic):  # stored in memory, not executed yet
def invert_dictionary(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(invert_dictionary(...))  # invert_dictionary() runs with dic=25
#   → return inverted
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only invert_dictionary is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(invert_dictionary(...))  # invert_dictionary() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(invert_dictionary(...))  # invert_dictionary() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done

"""

"""
Problem 792:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def remove_duplicates_values(dic):  # defines a function with parameters dic
    unique_values = {}
    for key, value in dic.items():
        if value not in unique_values.values():
            unique_values[key] = value
    return unique_values  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: not in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(remove_duplicates_values(dic))  # remove_duplicates_values() runs first, then print() outputs the result
print(remove_duplicates_values(25))  # remove_duplicates_values() runs first, then print() outputs the result
value not in unique_values.values(...)  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def remove_duplicates_values(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(remove_duplicates_values(...))  # remove_duplicates_values() runs with dic=dic
#   → return unique_values
def remove_duplicates_values(dic):  # stored in memory, not executed yet
def remove_duplicates_values(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(remove_duplicates_values(...))  # remove_duplicates_values() runs with dic=25
#   → return unique_values
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only remove_duplicates_values is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(remove_duplicates_values(...))  # remove_duplicates_values() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(remove_duplicates_values(...))  # remove_duplicates_values() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 793:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def same_keys(dic1, dic2):  # defines a function with parameters dic1, dic2
    return dic1.keys() == dic2.keys()  # return sends the result back to the caller
#
# Operators: ==
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(same_keys(dic1, dic2))  # same_keys() runs first, then print() outputs the result
print(same_keys(25, 25))  # same_keys() runs first, then print() outputs the result
dic1.keys(...) == dic2.keys(...)  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def same_keys(dic1, dic2):  # stored in memory, not executed yet
dic1 = ...  # assigns a value to the variable
dic2 = ...  # assigns a value to the variable
print(same_keys(...))  # same_keys() runs with dic1=dic1, dic2=dic2
#   → return dic1.keys() == dic2.keys()
def same_keys(dic1, dic2):  # stored in memory, not executed yet
def same_keys(dic1, dic2):  # stored in memory, not executed yet
dic1 = ...  # assigns a value to the variable
dic2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(same_keys(...))  # same_keys() runs with dic1=25, dic2=25
#   → return dic1.keys() == dic2.keys()
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only same_keys is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic1 = ...  # stored in memory
#   → dic2 = ...  # stored in memory
#   → print(same_keys(...))  # same_keys() runs first → value goes to print()
#   → dic1 = ...  # stored in memory
#   → dic2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(same_keys(...))  # same_keys() runs first → value goes to print()

"""

"""
Problem 794:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def multiply_by2(dic):  # defines a function with parameters dic
    result = {}
    for key, value in dic.items():
        result[key] = value * 2
    return result  # return sends the result back to the caller
#
# Keywords: for
# Operators: *
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(multiply_by2(dic))  # multiply_by2() runs first, then print() outputs the result
print(multiply_by2(25))  # multiply_by2() runs first, then print() outputs the result
value * 2  # value → then 2 → then *
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def multiply_by2(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(multiply_by2(...))  # multiply_by2() runs with dic=dic
#   → return result
def multiply_by2(dic):  # stored in memory, not executed yet
def multiply_by2(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(multiply_by2(...))  # multiply_by2() runs with dic=25
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only multiply_by2 is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(multiply_by2(...))  # multiply_by2() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(multiply_by2(...))  # multiply_by2() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done

"""

"""
Problem 795:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def len_key_value_pair(dic):  # defines a function with parameters dic
    return len(dic)  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(len_key_value_pair(dic))  # len_key_value_pair() runs first, then print() outputs the result
print(len_key_value_pair(25))  # len_key_value_pair() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def len_key_value_pair(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(len_key_value_pair(...))  # len_key_value_pair() runs with dic=dic
#   → return sum((1 for _ in dic))
def len_key_value_pair(dic):  # stored in memory, not executed yet
def len_key_value_pair(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(len_key_value_pair(...))  # len_key_value_pair() runs with dic=25
#   → return sum((1 for _ in dic))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only len_key_value_pair is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(len_key_value_pair(...))  # len_key_value_pair() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(len_key_value_pair(...))  # len_key_value_pair() runs first → value goes to print()
#
# Loop: takes one item from dic, runs body, repeats until done

"""

"""
Problem 796:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def map_lst_string_dic(lst):  # defines a function with parameters lst
    result = {}
    for word in lst:
        result[word] = len(word)
    return result  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(map_lst_string_dic(lst))  # map_lst_string_dic() runs first, then print() outputs the result
print(len_dic(lst))  # len_dic() runs first, then print() outputs the result
print(map_lst_string_dic(?))  # map_lst_string_dic() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def map_lst_string_dic(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(map_lst_string_dic(...))  # map_lst_string_dic() runs with lst=lst
#   → return result
def len_dic(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(len_dic(...))  # len_dic() runs with lst=lst
#   → result = {}
#   → for word in lst:
#   →     count = 0
#   →     for char in word:
#   →         count += 1
#   →     result[word] = count
#   → return result
def map_lst_string_dic(lst):  # stored in memory, not executed yet
def map_lst_string_dic(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(map_lst_string_dic(...))  # map_lst_string_dic() runs with lst=[1, 3, 5, 7]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — len_dic, map_lst_string_dic are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(map_lst_string_dic(...))  # map_lst_string_dic() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(len_dic(...))  # len_dic() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(map_lst_string_dic(...))  # map_lst_string_dic() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done

"""

"""
Problem 797:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def add_key_value_pair(dic):  # defines a function with parameters dic
    dic['new_key'] = 'new_value'
    return dic  # return sends the result back to the caller
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(add_key_value_pair(dic))  # add_key_value_pair() runs first, then print() outputs the result
print(add_key_value_pair(?))  # add_key_value_pair() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def add_key_value_pair(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(add_key_value_pair(...))  # add_key_value_pair() runs with dic=dic
#   → return dic
def add_key_value_pair(dic):  # stored in memory, not executed yet
def add_key_value_pair(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(add_key_value_pair(...))  # add_key_value_pair() runs with dic=[4, 1, 8, 6, 3]
#   → return dic
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only add_key_value_pair is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(add_key_value_pair(...))  # add_key_value_pair() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(add_key_value_pair(...))  # add_key_value_pair() runs first → value goes to print()

"""

"""
Problem 798:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def value_cubes():  # defines a function with no parameters
    result = {}
    for num in range(1, 6):
        result[num] = num ** 3
    return result  # return sends the result back to the caller
#
# Keywords: for
# Operators: **
# Built-in functions: range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(value_cubes())  # value_cubes() runs first, then print() outputs the result
num ** 3  # num → then 3 → then **
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def value_cubes():  # stored in memory, not executed yet
print(value_cubes(...))  # value_cubes() runs with 
#   → return result
def value_cubes():  # stored in memory, not executed yet
def value_cubes():  # stored in memory, not executed yet
result = ...  # assigns a value to the variable
for num in range(...):  # loops once per item
  ? = ...
result = ...  # assigns a value to the variable
print(result)
result = ...  # assigns a value to the variable
for num in range(...):  # loops once per item
  ? = ...
result = ...  # assigns a value to the variable
print(result)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only value_cubes is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(value_cubes(...))  # value_cubes() runs first → value goes to print()
#   → result = ...  # stored in memory
#   → for num in range(...)  # runs body once per item
#   → result = ...  # stored in memory
#   → print(result)
#   → result = ...  # stored in memory
#   → for num in range(...)  # runs body once per item
#   → result = ...  # stored in memory
#   → print(result)
#
# Loop: takes one item from range(...), runs body, repeats until done

"""

"""
Problem 799:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def check_if_empty(dic):  # defines a function with parameters dic
    if not dic:
        return 'Dictionary is empty'
    return 'Dictionary is not empty'  # return sends the result back to the caller
#
# Keywords: if/else
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(check_if_empty(dic))  # check_if_empty() runs first, then print() outputs the result
print(check_if_empty(25))  # check_if_empty() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def check_if_empty(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(check_if_empty(...))  # check_if_empty() runs with dic=dic
#   → return 'Dictionary is empty'
def check_if_empty(dic):  # stored in memory, not executed yet
def check_if_empty(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(check_if_empty(...))  # check_if_empty() runs with dic=25
#   → return 'Dictionary is empty'
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only check_if_empty is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(check_if_empty(...))  # check_if_empty() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(check_if_empty(...))  # check_if_empty() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 800:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def remove_set_keys(dic, keys_to_remove):  # defines a function with parameters dic, keys_to_remove
    result = {}
    for key, value in dic.items():
        if key not in keys_to_remove:
            result[key] = value
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: not in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(remove_set_keys(dic, keys_to_remove))  # remove_set_keys() runs first, then print() outputs the result
print(remove_set_keys(25, 25))  # remove_set_keys() runs first, then print() outputs the result
key not in keys_to_remove  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def remove_set_keys(dic, keys_to_remove):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
keys_to_remove = ...  # assigns a value to the variable
print(remove_set_keys(...))  # remove_set_keys() runs with dic=dic, keys_to_remove=keys_to_remove
#   → return result
def remove_set_keys(dic, keys_to_remove):  # stored in memory, not executed yet
def remove_set_keys(dic, keys_to_remove):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
keys_to_remove = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(remove_set_keys(...))  # remove_set_keys() runs with dic=25, keys_to_remove=25
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only remove_set_keys is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → keys_to_remove = ...  # stored in memory
#   → print(remove_set_keys(...))  # remove_set_keys() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → keys_to_remove = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(remove_set_keys(...))  # remove_set_keys() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 801:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def dic_lst_tuples(dic):  # defines a function with parameters dic
    return list(dic.items())  # return sends the result back to the caller
#
# Built-in functions: list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(dic_lst_tuples(dic))  # dic_lst_tuples() runs first, then print() outputs the result
print(dic_lst_tuples(25))  # dic_lst_tuples() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def dic_lst_tuples(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(dic_lst_tuples(...))  # dic_lst_tuples() runs with dic=dic
#   → return list(dic.items())
def dic_lst_tuples(dic):  # stored in memory, not executed yet
def dic_lst_tuples(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(dic_lst_tuples(...))  # dic_lst_tuples() runs with dic=25
#   → return list(dic.items())
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only dic_lst_tuples is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(dic_lst_tuples(...))  # dic_lst_tuples() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(dic_lst_tuples(...))  # dic_lst_tuples() runs first → value goes to print()

"""

"""
Problem 802:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(dic):  # defines a function with parameters dic
    result = {}
    for key, value in dic.items():
        if value == 1:
            result[key] = value
    return tuple(result.keys())  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: ==
# Built-in functions: tuple()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(dic))  # main() runs first, then print() outputs the result
print(map_value(dic, target_value))  # map_value() runs first, then print() outputs the result
print(main(25))  # main() runs first, then print() outputs the result
value == 1  # evaluated as True or False → picks which branch
value == target_value  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(main(...))  # main() runs with dic=dic
#   → return tuple(result.keys())
def map_value(dic, target_value):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
target_value = ...  # assigns a value to the variable
print(map_value(...))  # map_value() runs with dic=dic, target_value=target_value
#   → result = {}
#   → for key, value in dic.items():
#   →     if value == target_value:
#   →         result[key] = value
#   → return result
def main(dic):  # stored in memory, not executed yet
def main(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with dic=25
#   → return tuple(result.keys())
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, map_value are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → target_value = ...  # stored in memory
#   → print(map_value(...))  # map_value() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 803:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def replace_value(dic, list_values):  # defines a function with parameters dic, list_values
    for key in dic:
        if not isinstance(dic[key], list):
            dic[key] = list_values
    return dic  # return sends the result back to the caller
#
# Keywords: for | if/else
# Built-in functions: isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(replace_value(dic, list_values))  # replace_value() runs first, then print() outputs the result
print(replace_value(?, 25))  # replace_value() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def replace_value(dic, list_values):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
list_values = ...  # assigns a value to the variable
print(replace_value(...))  # replace_value() runs with dic=dic, list_values=list_values
#   → return dic
def replace_value(dic, list_values):  # stored in memory, not executed yet
def replace_value(dic, list_values):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
list_values = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(replace_value(...))  # replace_value() runs with dic=[4, 1, 8, 6, 3], list_values=25
#   → return dic
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only replace_value is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → list_values = ...  # stored in memory
#   → print(replace_value(...))  # replace_value() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → list_values = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(replace_value(...))  # replace_value() runs first → value goes to print()
#
# Loop: takes one item from dic, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 804:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def nested_dic():  # defines a function with no parameters
    result = {}
    for key in range(1, 6):
        result[key] = {'square': key ** 2, 'cube': key ** 3}
    return result  # return sends the result back to the caller
#
# Keywords: for
# Operators: **
# Built-in functions: range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(nested_dic())  # nested_dic() runs first, then print() outputs the result
key ** 2  # key → then 2 → then **
key ** 3  # key → then 3 → then **
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def nested_dic():  # stored in memory, not executed yet
print(nested_dic(...))  # nested_dic() runs with 
#   → return result
def nested_dic():  # stored in memory, not executed yet
result = ...  # assigns a value to the variable
for (key, value) in result.items(...):  # loops once per item
  print(?)
def nested_dic():  # stored in memory, not executed yet
def nested_dic():  # stored in memory, not executed yet
result = ...  # assigns a value to the variable
for key in range(...):  # loops once per item
  ? = ...
result = ...  # assigns a value to the variable
print(result)
result = ...  # assigns a value to the variable
for key in range(...):  # loops once per item
  ? = ...
result = ...  # assigns a value to the variable
print(result)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only nested_dic is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(nested_dic(...))  # nested_dic() runs first → value goes to print()
#   → result = ...  # stored in memory
#   → for (key, value) in result.items(...)  # runs body once per item
#   → result = ...  # stored in memory
#   → for key in range(...)  # runs body once per item
#   → result = ...  # stored in memory
#   → print(result)
#   → result = ...  # stored in memory
#   → for key in range(...)  # runs body once per item
#   → result = ...  # stored in memory
#   → print(result)
#
# Loop: takes one item from result.items(...), runs body, repeats until done

"""

"""
Problem 806:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def sort_dic(dic):  # defines a function with parameters dic
    def value_sort(item):
        return item[1]
    return dict(sorted(dic.items(), key=value_sort, reverse=True))  # return sends the result back to the caller
#
# Built-in functions: dict, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(sort_dic(dic))  # sort_dic() runs first, then print() outputs the result
print(sort_dic(?))  # sort_dic() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def sort_dic(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(sort_dic(...))  # sort_dic() runs with dic=dic
#   → return item[1]
def sort_dic(dic):  # stored in memory, not executed yet
def sort_dic(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(sort_dic(...))  # sort_dic() runs with dic=[4, 1, 8, 6, 3]
#   → return item[1]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_dic is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(sort_dic(...))  # sort_dic() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_dic(...))  # sort_dic() runs first → value goes to print()

"""

"""
Problem 807:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def lst_tuples(lst):  # defines a function with parameters lst
    return dict(lst)  # return sends the result back to the caller
#
# Built-in functions: dict()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(lst_tuples(lst))  # lst_tuples() runs first, then print() outputs the result
print(lst_tuples(?))  # lst_tuples() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def lst_tuples(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(lst_tuples(...))  # lst_tuples() runs with lst=lst
#   → return dict(lst)
def lst_tuples(lst):  # stored in memory, not executed yet
def lst_tuples(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(lst_tuples(...))  # lst_tuples() runs with lst=[1, 3, 5, 7]
#   → return dict(lst)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lst_tuples is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst_tuples(...))  # lst_tuples() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lst_tuples(...))  # lst_tuples() runs first → value goes to print()

"""

"""
Problem 808:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def less_then_10(dic):  # defines a function with parameters dic
    result = {}
    for key, value in dic.items():
        if value >= 10:
            result[key] = value
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: >=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(less_then_10(dic))  # less_then_10() runs first, then print() outputs the result
print(less_then_10(25))  # less_then_10() runs first, then print() outputs the result
value >= 10  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def less_then_10(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(less_then_10(...))  # less_then_10() runs with dic=dic
#   → return result
def less_then_10(dic):  # stored in memory, not executed yet
def less_then_10(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(less_then_10(...))  # less_then_10() runs with dic=25
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only less_then_10 is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(less_then_10(...))  # less_then_10() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(less_then_10(...))  # less_then_10() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 810:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def students_grades(dic):  # defines a function with parameters dic
    result = {}
    for key, value in dic.items():
        if value >= 70:
            result[key] = value
    return list(result)  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: >=
# Built-in functions: list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(students_grades(dic))  # students_grades() runs first, then print() outputs the result
print(students_grades(25))  # students_grades() runs first, then print() outputs the result
value >= 70  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def students_grades(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(students_grades(...))  # students_grades() runs with dic=dic
#   → return list(result)
def students_grades(dic):  # stored in memory, not executed yet
def students_grades(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(students_grades(...))  # students_grades() runs with dic=25
#   → return list(result)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only students_grades is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(students_grades(...))  # students_grades() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(students_grades(...))  # students_grades() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 811:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def word_len(string):  # defines a function with parameters string
    words = string.split()
    result = {}
    for word in words:
        result[word] = len(word)
    return result  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(word_len(string))  # word_len() runs first, then print() outputs the result
print(word_len('world'))  # word_len() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def word_len(string):  # stored in memory, not executed yet
string = ...  # assigns a value to the variable
print(word_len(...))  # word_len() runs with string=string
#   → return result
def word_len(string):  # stored in memory, not executed yet
def word_len(string):  # stored in memory, not executed yet
string = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(word_len(...))  # word_len() runs with string='world'
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only word_len is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → print(word_len(...))  # word_len() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(word_len(...))  # word_len() runs first → value goes to print()
#
# Loop: takes one item from words, runs body, repeats until done

"""

"""
Problem 812:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def word_len(string):  # defines a function with parameters string
    words = string.split()
    result = {}
    for word in words:
        result[word] = len(word)
    return result  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(word_len(string))  # word_len() runs first, then print() outputs the result
print(word_len('world'))  # word_len() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def word_len(string):  # stored in memory, not executed yet
string = ...  # assigns a value to the variable
print(word_len(...))  # word_len() runs with string=string
#   → return result
def word_len(string):  # stored in memory, not executed yet
def word_len(string):  # stored in memory, not executed yet
string = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(word_len(...))  # word_len() runs with string='world'
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only word_len is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → print(word_len(...))  # word_len() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(word_len(...))  # word_len() runs first → value goes to print()
#
# Loop: takes one item from words, runs body, repeats until done

"""

"""
Problem 813:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def starting_letter(dic):  # defines a function with parameters dic
    result = {}
    for key in dic.keys():
        first_letter = key[0]
        if first_letter not in result:
            result[first_letter] = []
        result[first_letter].append(key)
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: not in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(starting_letter(dic))  # starting_letter() runs first, then print() outputs the result
print(main(dic))  # main() runs first, then print() outputs the result
print(starting_letter(?))  # starting_letter() runs first, then print() outputs the result
first_letter not in result  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def starting_letter(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(starting_letter(...))  # starting_letter() runs with dic=dic
#   → return result
def main(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(main(...))  # main() runs with dic=dic
#   → result = {}
#   → for key, value in dic.items():
#   →     first_letter = key[0]
#   →     result[first_letter] = key
#   → return result
def starting_letter(dic):  # stored in memory, not executed yet
def starting_letter(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(starting_letter(...))  # starting_letter() runs with dic=[4, 1, 8, 6, 3]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, starting_letter are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(starting_letter(...))  # starting_letter() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(starting_letter(...))  # starting_letter() runs first → value goes to print()
#
# Loop: takes one item from dic.keys(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 814:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def upper_keys(dic):  # defines a function with parameters dic
    result = {}
    for key, value in dic.items():
        result[key.upper()] = value
    return result  # return sends the result back to the caller
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(upper_keys(dic))  # upper_keys() runs first, then print() outputs the result
print(upper_keys(25))  # upper_keys() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def upper_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(upper_keys(...))  # upper_keys() runs with dic=dic
#   → return result
def upper_keys(dic):  # stored in memory, not executed yet
def upper_keys(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(upper_keys(...))  # upper_keys() runs with dic=25
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only upper_keys is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(upper_keys(...))  # upper_keys() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(upper_keys(...))  # upper_keys() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done

"""

"""
Problem 815:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def intersection(dic1, dic2):  # defines a function with parameters dic1, dic2
    result = {}
    for key in dic1:
        if key in dic2:
            result[key] = dic1[key]
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(intersection(dic1, dic2))  # intersection() runs first, then print() outputs the result
print(intersection(?, 25))  # intersection() runs first, then print() outputs the result
key in dic2  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def intersection(dic1, dic2):  # stored in memory, not executed yet
dic1 = ...  # assigns a value to the variable
dic2 = ...  # assigns a value to the variable
print(intersection(...))  # intersection() runs with dic1=dic1, dic2=dic2
#   → return result
def intersection(dic1, dic2):  # stored in memory, not executed yet
def intersection(dic1, dic2):  # stored in memory, not executed yet
dic1 = ...  # assigns a value to the variable
dic2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(intersection(...))  # intersection() runs with dic1=[4, 1, 8, 6, 3], dic2=25
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only intersection is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic1 = ...  # stored in memory
#   → dic2 = ...  # stored in memory
#   → print(intersection(...))  # intersection() runs first → value goes to print()
#   → dic1 = ...  # stored in memory
#   → dic2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(intersection(...))  # intersection() runs first → value goes to print()
#
# Loop: takes one item from dic1, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 816:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def count_vowels(string):  # defines a function with parameters string
    vowels = 'aeiou'
    result = {}
    for vowel in vowels:
        result[vowel] = 0
    for char in string.lower():
        if char in vowels:
            result[char] += 1
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(count_vowels(string))  # count_vowels() runs first, then print() outputs the result
print(count_vowels('world'))  # count_vowels() runs first, then print() outputs the result
char in vowels  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def count_vowels(string):  # stored in memory, not executed yet
string = ...  # assigns a value to the variable
print(count_vowels(...))  # count_vowels() runs with string=string
#   → return result
def count_vowels(string):  # stored in memory, not executed yet
def count_vowels(string):  # stored in memory, not executed yet
string = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(count_vowels(...))  # count_vowels() runs with string='world'
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_vowels is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#
# Loop: takes one item from vowels, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 817:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def remove_value_is_none(dic):  # defines a function with parameters dic
    result = {}
    for key, value in dic.items():
        if value is not None:
            result[key] = value
    return result  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: is not
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(remove_value_is_none(dic1))  # remove_value_is_none() runs first, then print() outputs the result
remove_value_is_none(dic)  # arguments evaluated first, then function body runs
print(remove_value_is_none(25))  # remove_value_is_none() runs first, then print() outputs the result
value  None  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def remove_value_is_none(dic):  # stored in memory, not executed yet
dic1 = ...  # assigns a value to the variable
print(remove_value_is_none(...))  # remove_value_is_none() runs with dic=dic1
#   → return result
def remove_value_is_none(dic):  # stored in memory, not executed yet
def remove_value_is_none(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(remove_value_is_none(...))  # remove_value_is_none() runs with dic=25
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only remove_value_is_none is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic1 = ...  # stored in memory
#   → print(remove_value_is_none(...))  # remove_value_is_none() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(remove_value_is_none(...))  # remove_value_is_none() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 818:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def check_key_value(dic, target):  # defines a function with parameters dic, target
    for key, value in dic.items():
        if key in target and dic[key] == target[key]:
            return True
    return False  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: == in and
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(check_key_value(dic1, target))  # check_key_value() runs first, then print() outputs the result
check_key_value(dic, target)  # arguments evaluated first, then function body runs
print(check_key_value(?, 'goal'))  # check_key_value() runs first, then print() outputs the result
key in target  # evaluated as True or False → picks which branch
? == ?  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def check_key_value(dic, target):  # stored in memory, not executed yet
dic1 = ...  # assigns a value to the variable
target = ...  # assigns a value to the variable
print(check_key_value(...))  # check_key_value() runs with dic=dic1, target=target
#   → return True
def check_key_value(dic, target):  # stored in memory, not executed yet
def check_key_value(dic, target):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
target = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(check_key_value(...))  # check_key_value() runs with dic=[4, 1, 8, 6, 3], target='goal'
#   → return True
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only check_key_value is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic1 = ...  # stored in memory
#   → target = ...  # stored in memory
#   → print(check_key_value(...))  # check_key_value() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → target = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(check_key_value(...))  # check_key_value() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 819:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import json
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# No top-level code runs — functions must be called externally

"""

"""
Problem 820:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def merge_dicts(dic1, dic2):  # defines a function with parameters dic1, dic2
    merged_dict = {**dic1, **dic2}
    return merged_dict  # return sends the result back to the caller
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(merge_dicts(dic1, dic2))  # merge_dicts() runs first, then print() outputs the result
print(merge_dicts(25, 25))  # merge_dicts() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def merge_dicts(dic1, dic2):  # stored in memory, not executed yet
dic1 = ...  # assigns a value to the variable
dic2 = ...  # assigns a value to the variable
print(merge_dicts(...))  # merge_dicts() runs with dic1=dic1, dic2=dic2
#   → return merged_dict
def merge_dicts(dic1, dic2):  # stored in memory, not executed yet
def merge_dicts(dic1, dic2):  # stored in memory, not executed yet
dic1 = ...  # assigns a value to the variable
dic2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(merge_dicts(...))  # merge_dicts() runs with dic1=25, dic2=25
#   → return merged_dict
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only merge_dicts is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic1 = ...  # stored in memory
#   → dic2 = ...  # stored in memory
#   → print(merge_dicts(...))  # merge_dicts() runs first → value goes to print()
#   → dic1 = ...  # stored in memory
#   → dic2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(merge_dicts(...))  # merge_dicts() runs first → value goes to print()

"""

"""
Problem 821:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def product_values(dic):  # defines a function with parameters dic
    product = 1
    for value in dic.values():
        product *= value
    return product  # return sends the result back to the caller
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(product_values(dic))  # product_values() runs first, then print() outputs the result
print(product_values(?))  # product_values() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def product_values(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(product_values(...))  # product_values() runs with dic=dic
#   → return product
def product_values(dic):  # stored in memory, not executed yet
def product_values(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(product_values(...))  # product_values() runs with dic=[4, 1, 8, 6, 3]
#   → return product
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only product_values is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(product_values(...))  # product_values() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(product_values(...))  # product_values() runs first → value goes to print()
#
# Loop: takes one item from dic.values(...), runs body, repeats until done

"""

"""
Problem 822:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def average_values(dic):  # defines a function with parameters dic
    sum_values = sum(dic.values())
    len_values = len(dic)
    average = sum_values / len_values
    return average  # return sends the result back to the caller
#
# Operators: * /
# Built-in functions: Fraction, float, len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(average_values(dic))  # average_values() runs first, then print() outputs the result
print(average_values(?))  # average_values() runs first, then print() outputs the result
sum_values / len_values  # sum_values → then len_values → then /
sum_values * ?  # sum_values → then ? → then *
1 / len_values  # 1 → then len_values → then /
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def average_values(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(average_values(...))  # average_values() runs with dic=dic
#   → from fractions import Fraction
#   → return float(Fraction(sum_values, len_values))
def average_values(dic):  # stored in memory, not executed yet
def average_values(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(average_values(...))  # average_values() runs with dic=[4, 1, 8, 6, 3]
#   → from fractions import Fraction
#   → return float(Fraction(sum_values, len_values))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only average_values is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(average_values(...))  # average_values() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(average_values(...))  # average_values() runs first → value goes to print()

"""

"""
Problem 823:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(dic):  # defines a function with parameters dic
    dic['city'] = 1
    dic['job'] = 34
    return dic  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: not in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(dic))  # main() runs first, then print() outputs the result
print(main(dic, 'name', 'job'))  # main() runs first, then print() outputs the result
print(main(dic, change_keys))  # main() runs first, then print() outputs the result
print(swap_values(dic, 'a', 'c'))  # swap_values() runs first, then print() outputs the result
print(main(?))  # main() runs first, then print() outputs the result
reverse_values not in result  # evaluated as True or False → picks which branch
change_keys not in result  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
target = ...  # assigns a value to the variable
print(main(...))  # main() runs with dic=dic
#   → return dic
def main(dic, x, y):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(main(...))  # main() runs with dic=dic
#   → return dic
def main(dic, change_keys):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
change_keys = ...  # assigns a value to the variable
print(main(...))  # main() runs with dic=dic
#   → return dic
def swap_values(dic, key1, key2):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(swap_values(...))  # swap_values() runs with dic=dic, key1='a', key2='c'
#   → dic[key1], dic[key2] = (dic[key2], dic[key1])
#   → return dic
def main(dic):  # stored in memory, not executed yet
def main(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with dic=[4, 1, 8, 6, 3]
#   → return dic
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, swap_values are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → target = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → change_keys = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → print(swap_values(...))  # swap_values() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 824:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def largest_value(dic):  # defines a function with parameters dic
    largest_key = None
    largest_val = float('-inf')
    for key, value in dic.items():
        if value > largest_val:
            largest_val = value
            largest_key = key
    return largest_key  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: >
# Built-in functions: float()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(largest_value(dic))  # largest_value() runs first, then print() outputs the result
print(largest_value(25))  # largest_value() runs first, then print() outputs the result
value > largest_val  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def largest_value(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(largest_value(...))  # largest_value() runs with dic=dic
#   → return largest_key
def largest_value(dic):  # stored in memory, not executed yet
def largest_value(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(largest_value(...))  # largest_value() runs with dic=25
#   → return largest_key
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only largest_value is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(largest_value(...))  # largest_value() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(largest_value(...))  # largest_value() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 825:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def smallest_value(dic):  # defines a function with parameters dic
    smallest_key = None
    smallest_val = float('inf')
    for key, value in dic.items():
        if value < smallest_val:
            smallest_val = value
            smallest_key = key
    return smallest_key  # return sends the result back to the caller
#
# Keywords: for | if/else
# Operators: <
# Built-in functions: float()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(smallest_value(dic))  # smallest_value() runs first, then print() outputs the result
print(smallest_value(25))  # smallest_value() runs first, then print() outputs the result
value < smallest_val  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def smallest_value(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(smallest_value(...))  # smallest_value() runs with dic=dic
#   → return smallest_key
def smallest_value(dic):  # stored in memory, not executed yet
def smallest_value(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(smallest_value(...))  # smallest_value() runs with dic=25
#   → return smallest_key
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only smallest_value is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(smallest_value(...))  # smallest_value() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(smallest_value(...))  # smallest_value() runs first → value goes to print()
#
# Loop: takes one item from dic.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 826:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(dic):  # defines a function with parameters dic
    dic['first'] = 1
    dic['second'] = 2
    return dic  # return sends the result back to the caller
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(main(dic))  # main() runs first, then print() outputs the result
print(add_multiple_pairs(dic, new_pairs))  # add_multiple_pairs() runs first, then print() outputs the result
print(main(?))  # main() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
print(main(...))  # main() runs with dic=dic
#   → return dic
def add_multiple_pairs(dic, new_pairs):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
new_pairs = ...  # assigns a value to the variable
print(add_multiple_pairs(...))  # add_multiple_pairs() runs with dic=dic, new_pairs=new_pairs
#   → dic.update(new_pairs)
#   → return dic
def main(dic):  # stored in memory, not executed yet
def main(dic):  # stored in memory, not executed yet
dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with dic=[4, 1, 8, 6, 3]
#   → return dic
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — add_multiple_pairs, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → new_pairs = ...  # stored in memory
#   → print(add_multiple_pairs(...))  # add_multiple_pairs() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()

"""

"""
Problem 827:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    i = 1
    while i <= 10:
        print(i)
        i += 1
#
# Keywords: while
# Operators: <=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
i <= 10  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → i = ...  # stored in memory
#   → i = ...  # stored in memory
#   → i = ...  # stored in memory
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 828:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    i = 2
    while i <= 20:
        print(i)
        i += 2
#
# Keywords: while
# Operators: <=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
i <= 20  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → i = ...  # stored in memory
#   → i = ...  # stored in memory
#   → i = ...  # stored in memory
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 829:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    i = 10
    while i >= 1:
        print(i)
        i -= 1
#
# Keywords: while
# Operators: >=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
i >= 1  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → i = ...  # stored in memory
#   → i = ...  # stored in memory
#   → i = ...  # stored in memory
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 830:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve(number):  # defines a function with parameters number
    count = number
    i = 0
    while i < count:
        print('Hello')
        i += 1
#
# Keywords: while
# Operators: <
# Built-in functions: input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
i < count  # evaluated as True or False → picks which branch
solve(number)  # arguments evaluated first, then function body runs
print(solve(25))  # solve() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
count = ...  # assigns a value to the variable
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
def solve(number):  # stored in memory, not executed yet
def solve(number):  # stored in memory, not executed yet
number = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(solve(...))  # solve() runs with number=25
#   → count = number
#   → i = 0
#   → while i < count:
#   →     return 'Hello'
#   →     i += 1
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → count = ...  # stored in memory
#   → i = ...  # stored in memory
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(solve(...))  # solve() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 832:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    number = 1
    while number <= 1000:
        print(number)
        number *= 2
#
# Keywords: while
# Operators: <=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
number <= 1000  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
number = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
number = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
number = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → number = ...  # stored in memory
#   → number = ...  # stored in memory
#   → number = ...  # stored in memory
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 833:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    i = 1
    while i <= 10:
        print(5 * i)
        i += 1
#
# Keywords: while
# Operators: * <=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
i <= 10  # evaluated as True or False → picks which branch
5 * i  # 5 → then i → then *
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → i = ...  # stored in memory
#   → i = ...  # stored in memory
#   → i = ...  # stored in memory
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 834:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Keywords: while
# Operators: <=
# Built-in functions: input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
total <= 50  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
total = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
print(total)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → total = ...  # stored in memory
#   → print(total)
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 835:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Keywords: while
# Operators: % !=
# Built-in functions: input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
? != 0  # evaluated as True or False → picks which branch
number % 2  # number → then 2 → then %
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
number = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → number = ...  # stored in memory
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 836:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Keywords: while
# Operators: !=
# Built-in functions: input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
number != 0  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
total = ...  # assigns a value to the variable
number = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
print(total)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → total = ...  # stored in memory
#   → number = ...  # stored in memory
#   → print(total)
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 837:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    a, b = (0, 1)
    i = 0
    while i < 10:
        print(a)
        a, b = (b, a + b)
        i += 1
#
# Keywords: while
# Operators: + <
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
i < 10  # evaluated as True or False → picks which branch
a + b  # a → then b → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
? = ...  # assigns a value to the variable
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
? = ...  # assigns a value to the variable
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
? = ...  # assigns a value to the variable
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → ? = ...  # stored in memory
#   → i = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → i = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → i = ...  # stored in memory
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 838:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Keywords: while
# Operators: !=
# Built-in functions: input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
guess != secret_number  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
secret_number = ...  # assigns a value to the variable
guess = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → secret_number = ...  # stored in memory
#   → guess = ...  # stored in memory
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 839:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve(text):  # defines a function with parameters text
    string = text
    vowels = 'aeiouAEIOU'
    i = 0
    count = 0
    while i < len(string):
        if string[i] in vowels:
            count += 1
        i += 1
    print(count)
#
# Keywords: if/else | while
# Operators: < in
# Built-in functions: input, len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
i < len(...)  # evaluated as True or False → picks which branch
solve(text)  # arguments evaluated first, then function body runs
print(solve('world'))  # solve() runs first, then print() outputs the result
? in vowels  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
string = ...  # assigns a value to the variable
vowels = ...  # assigns a value to the variable
i = ...  # assigns a value to the variable
count = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
print(count)
def solve(text):  # stored in memory, not executed yet
def solve(text):  # stored in memory, not executed yet
text = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(solve(...))  # solve() runs with text='world'
#   → string = text
#   → vowels = 'aeiouAEIOU'
#   → i = 0
#   → count = 0
#   → while i < len(string):
#   →     if string[i] in vowels:
#   →         count += 1
#   →     i += 1
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → vowels = ...  # stored in memory
#   → i = ...  # stored in memory
#   → count = ...  # stored in memory
#   → print(count)
#   → text = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(solve(...))  # solve() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 840:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve(text):  # defines a function with parameters text
    string = text
    while string:
        print(string)
        string = string[:-1]
#
# Keywords: while
# Built-in functions: input()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
solve(text)  # arguments evaluated first, then function body runs
print(solve('world'))  # solve() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
string = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
def solve(text):  # stored in memory, not executed yet
def solve(text):  # stored in memory, not executed yet
text = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(solve(...))  # solve() runs with text='world'
#   → string = text
#   → while string:
#   →     return string
#   →     string = string[:-1]
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → text = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(solve(...))  # solve() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 841:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve(number):  # defines a function with parameters number
    number = number
    while number >= 0:
        print(number)
        number -= 1
#
# Keywords: while
# Operators: >=
# Built-in functions: input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
number >= 0  # evaluated as True or False → picks which branch
solve(number)  # arguments evaluated first, then function body runs
print(solve(25))  # solve() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
number = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
def solve(number):  # stored in memory, not executed yet
def solve(number):  # stored in memory, not executed yet
number = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(solve(...))  # solve() runs with number=25
#   → number = number
#   → while number >= 0:
#   →     return number
#   →     number -= 1
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → number = ...  # stored in memory
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(solve(...))  # solve() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 842:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve(number, number1):  # defines a function with parameters number, number1
    total = 0
    num = number
    while num >= 0:
        total += num
    num = number1
    print(total)
#
# Keywords: while
# Operators: >=
# Built-in functions: input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
num >= 0  # evaluated as True or False → picks which branch
solve(number, number1)  # arguments evaluated first, then function body runs
print(solve(25, 25))  # solve() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
total = ...  # assigns a value to the variable
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
print(total)
def solve(number, number1):  # stored in memory, not executed yet
def solve(number, number1):  # stored in memory, not executed yet
number = ...  # assigns a value to the variable
number1 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(solve(...))  # solve() runs with number=25, number1=25
#   → total = 0
#   → num = number
#   → while num >= 0:
#   →     total += num
#   → num = number1
#   → return total
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → total = ...  # stored in memory
#   → num = ...  # stored in memory
#   → print(total)
#   → number = ...  # stored in memory
#   → number1 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(solve(...))  # solve() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 844:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Keywords: while
# Operators: !=
# Built-in functions: input()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
password != 'python'  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
password = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → password = ...  # stored in memory
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 845:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    num = 2
    while num <= 10000:
        print(num)
        num *= num
#
# Keywords: while
# Operators: <=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
num <= 10000  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → num = ...  # stored in memory
#   → num = ...  # stored in memory
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 846:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve(number):  # defines a function with parameters number
    num = number
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    print(reversed_num)
#
# Keywords: while
# Operators: % * + >
# Built-in functions: input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
num > 0  # evaluated as True or False → picks which branch
solve(number)  # arguments evaluated first, then function body runs
print(solve(25))  # solve() runs first, then print() outputs the result
? + ?  # ? → then ? → then +
reversed_num * 10  # reversed_num → then 10 → then *
num % 10  # num → then 10 → then %
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
num = ...  # assigns a value to the variable
reversed_num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
print(reversed_num)
def solve(number):  # stored in memory, not executed yet
def solve(number):  # stored in memory, not executed yet
number = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(solve(...))  # solve() runs with number=25
#   → num = number
#   → reversed_num = 0
#   → while num > 0:
#   →     reversed_num = reversed_num * 10 + num % 10
#   →     num //= 10
#   → return reversed_num
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → reversed_num = ...  # stored in memory
#   → print(reversed_num)
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(solve(...))  # solve() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 848:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve(number):  # defines a function with parameters number
    num = number
    while num > 0:
        print(num)
        num -= 1
#
# Keywords: while
# Operators: >
# Built-in functions: input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
num > 0  # evaluated as True or False → picks which branch
solve(number)  # arguments evaluated first, then function body runs
print(solve(25))  # solve() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
def solve(number):  # stored in memory, not executed yet
def solve(number):  # stored in memory, not executed yet
number = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(solve(...))  # solve() runs with number=25
#   → num = number
#   → while num > 0:
#   →     return num
#   →     num -= 1
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(solve(...))  # solve() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 849:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    num = random.randint(1, 100)
    while num % 7 != 0:
        print(num)
        num = random.randint(1, 100)
#
# Keywords: while
# Operators: % !=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
? != 0  # evaluated as True or False → picks which branch
num % 7  # num → then 7 → then %
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
import random
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → num = ...  # stored in memory
#   → num = ...  # stored in memory
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 851:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Keywords: if/else | while
# Operators: < not in
# Built-in functions: input, len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
i < len(...)  # evaluated as True or False → picks which branch
? not in vowels  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
string = ...  # assigns a value to the variable
vowels = ...  # assigns a value to the variable
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → vowels = ...  # stored in memory
#   → i = ...  # stored in memory
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 852:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve(number):  # defines a function with parameters number
    num = number
    count = 0
    while num > 0:
        count += 1
        num //= 10
    print(count)
#
# Keywords: while
# Operators: >
# Built-in functions: input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
num > 0  # evaluated as True or False → picks which branch
solve(number)  # arguments evaluated first, then function body runs
print(solve(25))  # solve() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
num = ...  # assigns a value to the variable
count = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
print(count)
def solve(number):  # stored in memory, not executed yet
def solve(number):  # stored in memory, not executed yet
number = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(solve(...))  # solve() runs with number=25
#   → num = number
#   → count = 0
#   → while num > 0:
#   →     count += 1
#   →     num //= 10
#   → return count
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → count = ...  # stored in memory
#   → print(count)
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(solve(...))  # solve() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 853:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Keywords: while
# Operators: <
# Built-in functions: input, int, len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
len(...) < 10  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
lst = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
print(lst)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst)
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 854:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve(number):  # defines a function with parameters number
    num = number
    while num >= 1:
        print(num)
        num /= 2
#
# Keywords: while
# Operators: >=
# Built-in functions: input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
num >= 1  # evaluated as True or False → picks which branch
solve(number)  # arguments evaluated first, then function body runs
print(solve(25))  # solve() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
def solve(number):  # stored in memory, not executed yet
def solve(number):  # stored in memory, not executed yet
number = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(solve(...))  # solve() runs with number=25
#   → num = number
#   → while num >= 1:
#   →     return num
#   →     num /= 2
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(solve(...))  # solve() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 856:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve(number):  # defines a function with parameters number
    num = number
    while num ** 2 <= 1000:
        print(num ** 2)
        num += 1
#
# Keywords: while
# Operators: ** <=
# Built-in functions: input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
? <= 1000  # evaluated as True or False → picks which branch
solve(number)  # arguments evaluated first, then function body runs
print(solve(25))  # solve() runs first, then print() outputs the result
num ** 2  # num → then 2 → then **
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
def solve(number):  # stored in memory, not executed yet
def solve(number):  # stored in memory, not executed yet
number = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(solve(...))  # solve() runs with number=25
#   → num = number
#   → while num ** 2 <= 1000:
#   →     return num ** 2
#   →     num += 1
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(solve(...))  # solve() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 857:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    num = 1
    while num <= 50:
        if num % 3 != 0:
            print(num)
        num += 1
#
# Keywords: if/else | while
# Operators: % != <=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
num <= 50  # evaluated as True or False → picks which branch
? != 0  # evaluated as True or False → picks which branch
num % 3  # num → then 3 → then %
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → num = ...  # stored in memory
#   → num = ...  # stored in memory
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 858:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    num = 0
    while num <= 100:
        print(num)
        num += 5
#
# Keywords: while
# Operators: <=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
num <= 100  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → num = ...  # stored in memory
#   → num = ...  # stored in memory
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 859:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    lst = [1, 2, 3, 4, 5]
    i = 0
    while i < len(lst):
        print(lst[i])
        i += 1
#
# Keywords: while
# Operators: <
# Built-in functions: len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
i < len(...)  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
lst = ...  # assigns a value to the variable
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
lst = ...  # assigns a value to the variable
i = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → i = ...  # stored in memory
#   → lst = ...  # stored in memory
#   → i = ...  # stored in memory
#   → lst = ...  # stored in memory
#   → i = ...  # stored in memory
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 860:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    num = 1
    total = 0
    while num <= 100:
        if num % 2 != 0:
            total += num
        num += 1
    print(total)
#
# Keywords: if/else | while
# Operators: % != <=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
num <= 100  # evaluated as True or False → picks which branch
? != 0  # evaluated as True or False → picks which branch
num % 2  # num → then 2 → then %
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
num = ...  # assigns a value to the variable
total = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
print(total)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
num = ...  # assigns a value to the variable
total = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
print(total)
num = ...  # assigns a value to the variable
total = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
print(total)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → total = ...  # stored in memory
#   → print(total)
#   → num = ...  # stored in memory
#   → total = ...  # stored in memory
#   → print(total)
#   → num = ...  # stored in memory
#   → total = ...  # stored in memory
#   → print(total)
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 861:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    num = 2
    count = 0
    while num <= 1000:
        num *= 2
        count += 1
    print(count)
#
# Keywords: while
# Operators: <=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
num <= 1000  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
num = ...  # assigns a value to the variable
count = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
print(count)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
num = ...  # assigns a value to the variable
count = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
print(count)
num = ...  # assigns a value to the variable
count = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
print(count)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → count = ...  # stored in memory
#   → print(count)
#   → num = ...  # stored in memory
#   → count = ...  # stored in memory
#   → print(count)
#   → num = ...  # stored in memory
#   → count = ...  # stored in memory
#   → print(count)
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 863:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    num = 10
    while num > 0:
        print(num)
        num -= 1
    print('Lift off!')
#
# Keywords: while
# Operators: >
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
num > 0  # evaluated as True or False → picks which branch
num_2 > 0  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
print('Lift off!')
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
print('Lift off!')
num = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
print('Lift off!')
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → print('Lift off!')
#   → num = ...  # stored in memory
#   → print('Lift off!')
#   → num = ...  # stored in memory
#   → print('Lift off!')
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 865:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Keywords: while
# Operators: <
# Built-in functions: input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
i < 5  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
i = ...  # assigns a value to the variable
product = ...  # assigns a value to the variable
# while ... → repeats as long as condition is true
print(product)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → i = ...  # stored in memory
#   → product = ...  # stored in memory
#   → print(product)
#
# Loop: check condition → if True run body → check again

"""

"""
Problem 866:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(lst1, lst2):  # defines a function with parameters lst1, lst2
    result = {}
    for x, y in zip(lst1, lst2):
        result[x] = y
    return result  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
main(lst1, lst2)  # arguments evaluated first, then function body runs
print(main(?, ?))  # main() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
main(lst1, lst2)  # calls main with lst1=lst1, lst2=lst2
#   → return result
def main(lst1, lst2):  # stored in memory, not executed yet
def main(lst1, lst2):  # stored in memory, not executed yet
lst1 = ...  # assigns a value to the variable
lst2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with lst1=[2, 4, 6], lst2=[1, 3, 5]
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only main is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → main(lst1, lst2)  # jumps into main(), runs body, returns
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from zip(...), runs body, repeats until done

"""

"""
Problem 867:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def create_dictionary(keys, values):  # defines a function with parameters keys, values
    dictionary = {}
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]
    return dictionary  # return sends the result back to the caller
#
# Keywords: for
# Built-in functions: len, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
create_dictionary(keys, values)  # arguments evaluated first, then function body runs
print(create_dictionary(?, ?))  # create_dictionary() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def create_dictionary(keys, values):  # stored in memory, not executed yet
keys = ...  # assigns a value to the variable
values = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
def create_dictionary(keys, values):  # stored in memory, not executed yet
def create_dictionary(keys, values):  # stored in memory, not executed yet
keys = ...  # assigns a value to the variable
values = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(create_dictionary(...))  # create_dictionary() runs with keys=[4, 1, 8, 6, 3], values=[4, 1, 8, 6, 3]
#   → return dictionary
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only create_dictionary is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → keys = ...  # stored in memory
#   → values = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → keys = ...  # stored in memory
#   → values = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(create_dictionary(...))  # create_dictionary() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done

"""

"""
Problem 868:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def capitalize_words(lst):  # defines a function with parameters lst
    def capitalize(name):
        return name.capitalize()
    return list(map(capitalize, lst))  # return sends the result back to the caller
#
# Built-in functions: list, map, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
capitalize_words(lst)  # arguments evaluated first, then function body runs
print(capitalize_words(?))  # capitalize_words() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def capitalize_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
capitalize_words(lst)  # calls capitalize_words with lst=lst
#   → return str(name).capitalize()
def capitalize_words(lst):  # stored in memory, not executed yet
def capitalize_words(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(capitalize_words(...))  # capitalize_words() runs with lst=[1, 3, 5, 7]
#   → return str(name).capitalize()
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only capitalize_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → capitalize_words(lst)  # jumps into capitalize_words(), runs body, returns
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(capitalize_words(...))  # capitalize_words() runs first → value goes to print()

"""

"""
Problem 869:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    numbers = [1, 2, 3]
    a, b, c = numbers
    print(a, b, c)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
numbers = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(a, b, c)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(a, b, c)
numbers = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(a, b, c)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(a, b, c)
#   → numbers = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(a, b, c)
#   → numbers = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(a, b, c)

"""

"""
Problem 870:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    numbers = [10, 20, 30, 40, 50]
    first, *middle, last = numbers
    print(first, middle, last)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
numbers = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first, middle, last)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first, middle, last)
numbers = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first, middle, last)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first, middle, last)
#   → numbers = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first, middle, last)
#   → numbers = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first, middle, last)

"""

"""
Problem 871:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    x, y = (5, 10)
    x, y = (y, x)
    print(x, y)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
? = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(x, y)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
? = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(x, y)
? = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(x, y)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → ? = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(x, y)
#   → ? = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(x, y)
#   → ? = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(x, y)

"""

"""
Problem 872:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    data = {'name': 'Alice', 'age': 25, 'city': 'New York'}
    keys, values = zip(*data.items())
    print(keys, values)
#
# Built-in functions: zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
data = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(keys, values)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
data = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(keys, values)
data = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(keys, values)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → data = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(keys, values)
#   → data = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(keys, values)
#   → data = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(keys, values)

"""

"""
Problem 873:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def get_coordinates():  # defines a function with no parameters
    return (5, 10)  # return sends the result back to the caller
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
get_coordinates()  # function body runs with no arguments
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def get_coordinates():  # stored in memory, not executed yet
? = ...  # assigns a value to the variable
print(x, y)
def get_coordinates():  # stored in memory, not executed yet
def get_coordinates():  # stored in memory, not executed yet
result = ...  # assigns a value to the variable
print(result)
result = ...  # assigns a value to the variable
print(result)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only get_coordinates is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → ? = ...  # stored in memory
#   → print(x, y)
#   → result = ...  # stored in memory
#   → print(result)
#   → result = ...  # stored in memory
#   → print(result)

"""

"""
Problem 874:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
word = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first, second, ''.join(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → word = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first, second, ''.join(...))

"""

"""
Problem 875:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    values = (100, 200, 300, 400, 500)
    first, *_, last = values
    print(first, last)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
values = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first, last)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
values = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first, last)
values = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first, last)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → values = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first, last)
#   → values = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first, last)
#   → values = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first, last)

"""

"""
Problem 876:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    nested_list = [[1, 2], [3, 4]]
    (a, b), (c, d) = nested_list
    print(a, b, c, d)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
nested_list = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(a, b, c, d)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
nested_list = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(a, b, c, d)
nested_list = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(a, b, c, d)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → nested_list = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(a, b, c, d)
#   → nested_list = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(a, b, c, d)
#   → nested_list = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(a, b, c, d)

"""

"""
Problem 877:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    a, b, c = range(3)
    print(a, b, c)
#
# Built-in functions: range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
? = ...  # assigns a value to the variable
print(a, b, c)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
? = ...  # assigns a value to the variable
print(a, b, c)
? = ...  # assigns a value to the variable
print(a, b, c)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → ? = ...  # stored in memory
#   → print(a, b, c)
#   → ? = ...  # stored in memory
#   → print(a, b, c)
#   → ? = ...  # stored in memory
#   → print(a, b, c)

"""

"""
Problem 878:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    full_name = 'John Doe'
    first_name, last_name = full_name.split()
    print(first_name, last_name)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
full_name = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first_name, last_name)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
full_name = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first_name, last_name)
full_name = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first_name, last_name)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → full_name = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first_name, last_name)
#   → full_name = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first_name, last_name)
#   → full_name = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first_name, last_name)

"""

"""
Problem 879:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def greet(name, age):  # defines a function with parameters name, age
    print(f'Hello, {name}. You are {age} years old.')
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
greet(?)  # arguments evaluated first, then function body runs
greet(name, age)  # arguments evaluated first, then function body runs
print(greet('Bob', 25))  # greet() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def greet(name, age):  # stored in memory, not executed yet
person = ...  # assigns a value to the variable
greet(?)  # calls greet with name=?
#   → result = f'Hello, {name}. You are {age} years old.'
#   → return result
def greet(name, age):  # stored in memory, not executed yet
def greet(name, age):  # stored in memory, not executed yet
name = ...  # assigns a value to the variable
age = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(greet(...))  # greet() runs with name='Bob', age=25
#   → result = f'Hello, {name}. You are {age} years old.'
#   → return result
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only greet is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → person = ...  # stored in memory
#   → greet(?)  # jumps into greet(), runs body, returns
#   → name = ...  # stored in memory
#   → age = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(greet(...))  # greet() runs first → value goes to print()

"""

"""
Problem 880:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    merged = [*list1, *list2]
    print(merged)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
list1 = ...  # assigns a value to the variable
list2 = ...  # assigns a value to the variable
merged = ...  # assigns a value to the variable
print(merged)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
list1 = ...  # assigns a value to the variable
list2 = ...  # assigns a value to the variable
merged = ...  # assigns a value to the variable
print(merged)
list1 = ...  # assigns a value to the variable
list2 = ...  # assigns a value to the variable
merged = ...  # assigns a value to the variable
print(merged)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → list1 = ...  # stored in memory
#   → list2 = ...  # stored in memory
#   → merged = ...  # stored in memory
#   → print(merged)
#   → list1 = ...  # stored in memory
#   → list2 = ...  # stored in memory
#   → merged = ...  # stored in memory
#   → print(merged)
#   → list1 = ...  # stored in memory
#   → list2 = ...  # stored in memory
#   → merged = ...  # stored in memory
#   → print(merged)

"""

"""
Problem 881:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    merged_dict = {**dict1, **dict2}
    print(merged_dict)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
dict1 = ...  # assigns a value to the variable
dict2 = ...  # assigns a value to the variable
merged_dict = ...  # assigns a value to the variable
print(merged_dict)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
dict1 = ...  # assigns a value to the variable
dict2 = ...  # assigns a value to the variable
merged_dict = ...  # assigns a value to the variable
print(merged_dict)
dict1 = ...  # assigns a value to the variable
dict2 = ...  # assigns a value to the variable
merged_dict = ...  # assigns a value to the variable
print(merged_dict)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dict1 = ...  # stored in memory
#   → dict2 = ...  # stored in memory
#   → merged_dict = ...  # stored in memory
#   → print(merged_dict)
#   → dict1 = ...  # stored in memory
#   → dict2 = ...  # stored in memory
#   → merged_dict = ...  # stored in memory
#   → print(merged_dict)
#   → dict1 = ...  # stored in memory
#   → dict2 = ...  # stored in memory
#   → merged_dict = ...  # stored in memory
#   → print(merged_dict)

"""

"""
Problem 882:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    values = (1, 2, 3, 4, 5)
    first, _, third, _, last = values
    print(first, third, last)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
values = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first, third, last)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
values = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first, third, last)
values = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first, third, last)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → values = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first, third, last)
#   → values = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first, third, last)
#   → values = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first, third, last)

"""

"""
Problem 883:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def add(a, b, c):  # defines a function with parameters a, b, c
    return a + b + c  # return sends the result back to the caller
#
# Operators: +
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
add(?)  # arguments evaluated first, then function body runs
add(a, b, c)  # arguments evaluated first, then function body runs
print(add(20, 30, 10))  # add() runs first, then print() outputs the result
? + c  # ? → then c → then +
a + b  # a → then b → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def add(a, b, c):  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
def add(a, b, c):  # stored in memory, not executed yet
def add(a, b, c):  # stored in memory, not executed yet
a = ...  # assigns a value to the variable
b = ...  # assigns a value to the variable
c = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(add(...))  # add() runs with a=20, b=30, c=10
#   → return a + b + c
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only add is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → c = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(add(...))  # add() runs first → value goes to print()

"""

"""
Problem 884:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def describe(name, age, city):  # defines a function with parameters name, age, city
    return f'{name} is {age} years old and lives in {city}.'  # return sends the result back to the caller
#
# Operators: %
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
print(describe())  # describe() runs first, then print() outputs the result
describe(name, age, city)  # arguments evaluated first, then function body runs
print(describe('Bob', 25, 25))  # describe() runs first, then print() outputs the result
'%s is %s years old and lives in %s.' % ?  # '%s is %s years old and lives in %s.' → then ? → then %
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def describe(name, age, city):  # stored in memory, not executed yet
person = ...  # assigns a value to the variable
print(describe(...))  # describe() runs with 
#   → return '%s is %s years old and lives in %s.' % (name, age, city)
def describe(name, age, city):  # stored in memory, not executed yet
def describe(name, age, city):  # stored in memory, not executed yet
name = ...  # assigns a value to the variable
age = ...  # assigns a value to the variable
city = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(describe(...))  # describe() runs with name='Bob', age=25, city=25
#   → return '%s is %s years old and lives in %s.' % (name, age, city)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only describe is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → person = ...  # stored in memory
#   → print(describe(...))  # describe() runs first → value goes to print()
#   → name = ...  # stored in memory
#   → age = ...  # stored in memory
#   → city = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(describe(...))  # describe() runs first → value goes to print()

"""

"""
Problem 885:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    word = 'ABC'
    a, b, c = word
    print(a, b, c)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
word = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(a, b, c)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
word = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(a, b, c)
word = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(a, b, c)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → word = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(a, b, c)
#   → word = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(a, b, c)
#   → word = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(a, b, c)

"""

"""
Problem 886:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    first, *middle, last = numbers
    print(first, middle, last)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
numbers = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first, middle, last)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first, middle, last)
numbers = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first, middle, last)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first, middle, last)
#   → numbers = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first, middle, last)
#   → numbers = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first, middle, last)

"""

"""
Problem 887:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
    for number, letter in pairs:
        print(number, letter)
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
pairs = ...  # assigns a value to the variable
for (number, letter) in pairs:  # loops once per item
  print(number, letter)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
pairs = ...  # assigns a value to the variable
for (number, letter) in pairs:  # loops once per item
  print(number, letter)
pairs = ...  # assigns a value to the variable
for (number, letter) in pairs:  # loops once per item
  print(number, letter)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → pairs = ...  # stored in memory
#   → for (number, letter) in pairs  # runs body once per item
#   → pairs = ...  # stored in memory
#   → for (number, letter) in pairs  # runs body once per item
#   → pairs = ...  # stored in memory
#   → for (number, letter) in pairs  # runs body once per item
#
# Loop: takes one item from pairs, runs body, repeats until done

"""

"""
Problem 888:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def get_user():  # defines a function with no parameters
    return ('Alice', 25)  # return sends the result back to the caller
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
get_user()  # function body runs with no arguments
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def get_user():  # stored in memory, not executed yet
? = ...  # assigns a value to the variable
print(name, age)
def get_user():  # stored in memory, not executed yet
def get_user():  # stored in memory, not executed yet
result = ...  # assigns a value to the variable
print(result)
result = ...  # assigns a value to the variable
print(result)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only get_user is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → ? = ...  # stored in memory
#   → print(name, age)
#   → result = ...  # stored in memory
#   → print(result)
#   → result = ...  # stored in memory
#   → print(result)

"""

"""
Problem 889:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    summed = [sum(x) for x in zip(*lists)]
    print(summed)
#
# Built-in functions: sum, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
lists = ...  # assigns a value to the variable
summed = ...  # assigns a value to the variable
print(summed)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
lists = ...  # assigns a value to the variable
summed = ...  # assigns a value to the variable
print(summed)
lists = ...  # assigns a value to the variable
summed = ...  # assigns a value to the variable
print(summed)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lists = ...  # stored in memory
#   → summed = ...  # stored in memory
#   → print(summed)
#   → lists = ...  # stored in memory
#   → summed = ...  # stored in memory
#   → print(summed)
#   → lists = ...  # stored in memory
#   → summed = ...  # stored in memory
#   → print(summed)

"""

"""
Problem 890:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    data = {'name': 'Alice', 'age': 25, 'city': 'New York'}
    formatted = [f'{key}: {value}' for key, value in data.items()]
    print(formatted)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
data = ...  # assigns a value to the variable
formatted = ...  # assigns a value to the variable
print(formatted)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
data = ...  # assigns a value to the variable
formatted = ...  # assigns a value to the variable
print(formatted)
data = ...  # assigns a value to the variable
formatted = ...  # assigns a value to the variable
print(formatted)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → data = ...  # stored in memory
#   → formatted = ...  # stored in memory
#   → print(formatted)
#   → data = ...  # stored in memory
#   → formatted = ...  # stored in memory
#   → print(formatted)
#   → data = ...  # stored in memory
#   → formatted = ...  # stored in memory
#   → print(formatted)

"""

"""
Problem 891:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    sentence = 'Python is a powerful programming language'
    first, *middle, last = sentence.split()
    print(first, middle, last)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
sentence = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first, middle, last)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
sentence = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first, middle, last)
sentence = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(first, middle, last)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → sentence = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first, middle, last)
#   → sentence = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first, middle, last)
#   → sentence = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first, middle, last)

"""

"""
Problem 892:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    word = 'unpacking'
    vowels = [c for c in word if c in 'aeiou']
    print(vowels)
#
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
c in 'aeiou'  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
word = ...  # assigns a value to the variable
vowels = ...  # assigns a value to the variable
print(vowels)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
word = ...  # assigns a value to the variable
vowels = ...  # assigns a value to the variable
print(vowels)
word = ...  # assigns a value to the variable
vowels = ...  # assigns a value to the variable
print(vowels)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → word = ...  # stored in memory
#   → vowels = ...  # stored in memory
#   → print(vowels)
#   → word = ...  # stored in memory
#   → vowels = ...  # stored in memory
#   → print(vowels)
#   → word = ...  # stored in memory
#   → vowels = ...  # stored in memory
#   → print(vowels)

"""

"""
Problem 893:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    data = ('Alice', 30, 5.8, True)
    name, age, height, is_student = data
    print(name, age, height, is_student)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
data = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(name, age, height, is_student)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
data = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(name, age, height, is_student)
data = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(name, age, height, is_student)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → data = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(name, age, height, is_student)
#   → data = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(name, age, height, is_student)
#   → data = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(name, age, height, is_student)

"""

"""
Problem 894:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    tuples = [(1, 3), (4, 1), (2, 2)]
    sorted_tuples = sorted(tuples, key=lambda x: x[1])
    print(sorted_tuples)
#
# Built-in functions: sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
tuples = ...  # assigns a value to the variable
sorted_tuples = ...  # assigns a value to the variable
print(sorted_tuples)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
tuples = ...  # assigns a value to the variable
sorted_tuples = ...  # assigns a value to the variable
print(sorted_tuples)
tuples = ...  # assigns a value to the variable
sorted_tuples = ...  # assigns a value to the variable
print(sorted_tuples)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → tuples = ...  # stored in memory
#   → sorted_tuples = ...  # stored in memory
#   → print(sorted_tuples)
#   → tuples = ...  # stored in memory
#   → sorted_tuples = ...  # stored in memory
#   → print(sorted_tuples)
#   → tuples = ...  # stored in memory
#   → sorted_tuples = ...  # stored in memory
#   → print(sorted_tuples)

"""

"""
Problem 895:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    numbers = [1, 2, 3, 4, 5, 6]
    evens = [n for n in numbers if n % 2 == 0]
    print(evens)
#
# Operators: % ==
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
? == 0  # evaluated as True or False → picks which branch
n % 2  # n → then 2 → then %
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
numbers = ...  # assigns a value to the variable
evens = ...  # assigns a value to the variable
print(evens)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
evens = ...  # assigns a value to the variable
print(evens)
numbers = ...  # assigns a value to the variable
evens = ...  # assigns a value to the variable
print(evens)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → evens = ...  # stored in memory
#   → print(evens)
#   → numbers = ...  # stored in memory
#   → evens = ...  # stored in memory
#   → print(evens)
#   → numbers = ...  # stored in memory
#   → evens = ...  # stored in memory
#   → print(evens)

"""

"""
Problem 896:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    a, b, c = (1, 2, 3)
    a, b, c = (c, a, b)
    print(a, b, c)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
? = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(a, b, c)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
? = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(a, b, c)
? = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(a, b, c)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → ? = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(a, b, c)
#   → ? = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(a, b, c)
#   → ? = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(a, b, c)

"""

"""
Problem 897:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    first, second, *remaining = range(10)
    print(first, second, remaining)
#
# Built-in functions: range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
? = ...  # assigns a value to the variable
print(first, second, remaining)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
? = ...  # assigns a value to the variable
print(first, second, remaining)
? = ...  # assigns a value to the variable
print(first, second, remaining)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → ? = ...  # stored in memory
#   → print(first, second, remaining)
#   → ? = ...  # stored in memory
#   → print(first, second, remaining)
#   → ? = ...  # stored in memory
#   → print(first, second, remaining)

"""

"""
Problem 898:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Operators: +
# Built-in functions: add_three()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
? + z  # ? → then z → then +
x + y  # x → then y → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
add_three = ...  # assigns a value to the variable
numbers = ...  # assigns a value to the variable
print(add_three(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → add_three = ...  # stored in memory
#   → numbers = ...  # stored in memory
#   → print(add_three(...))

"""

"""
Problem 899:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    num = 12345
    digits = list(str(num))
    reversed_digits = digits[::-1]
    print(reversed_digits)
    num = 123456
    str_num = str(num)[::-1]
    lst_num = list(str_num)
    print(lst_num)
#
# Built-in functions: list, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
num = ...  # assigns a value to the variable
digits = ...  # assigns a value to the variable
reversed_digits = ...  # assigns a value to the variable
print(reversed_digits)
num = ...  # assigns a value to the variable
str_num = ...  # assigns a value to the variable
lst_num = ...  # assigns a value to the variable
print(lst_num)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
num = ...  # assigns a value to the variable
digits = ...  # assigns a value to the variable
reversed_digits = ...  # assigns a value to the variable
print(reversed_digits)
num = ...  # assigns a value to the variable
str_num = ...  # assigns a value to the variable
lst_num = ...  # assigns a value to the variable
print(lst_num)
num = ...  # assigns a value to the variable
digits = ...  # assigns a value to the variable
reversed_digits = ...  # assigns a value to the variable
print(reversed_digits)
num = ...  # assigns a value to the variable
str_num = ...  # assigns a value to the variable
lst_num = ...  # assigns a value to the variable
print(lst_num)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → digits = ...  # stored in memory
#   → reversed_digits = ...  # stored in memory
#   → print(reversed_digits)
#   → num = ...  # stored in memory
#   → str_num = ...  # stored in memory
#   → lst_num = ...  # stored in memory
#   → print(lst_num)
#   → num = ...  # stored in memory
#   → digits = ...  # stored in memory
#   → reversed_digits = ...  # stored in memory
#   → print(reversed_digits)
#   → num = ...  # stored in memory
#   → str_num = ...  # stored in memory
#   → lst_num = ...  # stored in memory
#   → print(lst_num)
#   → num = ...  # stored in memory
#   → digits = ...  # stored in memory
#   → reversed_digits = ...  # stored in memory
#   → print(reversed_digits)
#   → num = ...  # stored in memory
#   → str_num = ...  # stored in memory
#   → lst_num = ...  # stored in memory
#   → print(lst_num)

"""

"""
Problem 900:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def min_max(lst):  # defines a function with parameters lst
    return (min(lst), max(lst))  # return sends the result back to the caller
#
# Built-in functions: max, min()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
min_max(numbers)  # arguments evaluated first, then function body runs
min_max(lst)  # arguments evaluated first, then function body runs
print(min_max(?))  # min_max() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def min_max(lst):  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(minimum, maximum)
def min_max(lst):  # stored in memory, not executed yet
def min_max(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(min_max(...))  # min_max() runs with lst=[1, 3, 5, 7]
#   → return (min(lst), max(lst))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only min_max is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(minimum, maximum)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(min_max(...))  # min_max() runs first → value goes to print()

"""

"""
Problem 901:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main():  # defines a function with no parameters
    pass
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
main()  # function body runs with no arguments
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
tuples = ...  # assigns a value to the variable
first_elements = ...  # assigns a value to the variable
print(first_elements)
def main():  # stored in memory, not executed yet
main()  # calls main()
#   → pass
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → tuples = ...  # stored in memory
#   → first_elements = ...  # stored in memory
#   → print(first_elements)
#   → main()  # jumps into main(), runs body, returns

"""

"""
Problem 902:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main(lst_dic):  # defines a function with parameters lst_dic
    ages = [value['age'] for value in lst_dic]
    return ages  # return sends the result back to the caller
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
main(lst_dic)  # arguments evaluated first, then function body runs
print(main(?))  # main() runs first, then print() outputs the result
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def main(lst_dic):  # stored in memory, not executed yet
lst_dic = ...  # assigns a value to the variable
main(lst_dic)  # calls main with lst_dic=lst_dic
#   → return ages
people = ...  # assigns a value to the variable
ages = ...  # assigns a value to the variable
print(ages)
def main(lst_dic):  # stored in memory, not executed yet
def main(lst_dic):  # stored in memory, not executed yet
lst_dic = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(main(...))  # main() runs with lst_dic=[4, 1, 8, 6, 3]
#   → return ages
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only main is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst_dic = ...  # stored in memory
#   → main(lst_dic)  # jumps into main(), runs body, returns
#   → people = ...  # stored in memory
#   → ages = ...  # stored in memory
#   → print(ages)
#   → lst_dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()

"""

"""
Problem 903:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    expression = '3 + 5 - 2 * 4'
    a, op1, b, op2, c, op3, d = expression.split()
    print(a, op1, b, op2, c, op3, d)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
expression = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(a, op1, b, op2, c, op3, d)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
expression = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(a, op1, b, op2, c, op3, d)
expression = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(a, op1, b, op2, c, op3, d)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → expression = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(a, op1, b, op2, c, op3, d)
#   → expression = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(a, op1, b, op2, c, op3, d)
#   → expression = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(a, op1, b, op2, c, op3, d)

"""

"""
Problem 904:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    data = {'x': 10, 'y': 20, 'z': 30}
    x, y, z = data.values()
    x, y, z = (z, x, y)
    print(x, y, z)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
data = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(x, y, z)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
data = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(x, y, z)
data = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(x, y, z)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → data = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(x, y, z)
#   → data = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(x, y, z)
#   → data = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(x, y, z)

"""

"""
Problem 905:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    email = 'john.doe@example.com'
    user, domain = email.split('@')
    print(user, domain)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
email = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(user, domain)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
email = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(user, domain)
email = ...  # assigns a value to the variable
? = ...  # assigns a value to the variable
print(user, domain)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → email = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(user, domain)
#   → email = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(user, domain)
#   → email = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(user, domain)

"""

"""
Problem 906:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    nested_tuples = [(1, (2, 3)), (4, (5, 6))]
    for a, (b, c) in nested_tuples:
        print(a, b, c)
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
nested_tuples = ...  # assigns a value to the variable
for (a, (b, c)) in nested_tuples:  # loops once per item
  print(a, b, c)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
nested_tuples = ...  # assigns a value to the variable
for (a, (b, c)) in nested_tuples:  # loops once per item
  print(a, b, c)
nested_tuples = ...  # assigns a value to the variable
for (a, (b, c)) in nested_tuples:  # loops once per item
  print(a, b, c)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → nested_tuples = ...  # stored in memory
#   → for (a, (b, c)) in nested_tuples  # runs body once per item
#   → nested_tuples = ...  # stored in memory
#   → for (a, (b, c)) in nested_tuples  # runs body once per item
#   → nested_tuples = ...  # stored in memory
#   → for (a, (b, c)) in nested_tuples  # runs body once per item
#
# Loop: takes one item from nested_tuples, runs body, repeats until done

"""

"""
Problem 907:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    quotient, remainder = divmod(17, 5)
    print(quotient, remainder)
#
# Built-in functions: divmod()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
? = ...  # assigns a value to the variable
print(quotient, remainder)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
? = ...  # assigns a value to the variable
print(quotient, remainder)
? = ...  # assigns a value to the variable
print(quotient, remainder)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → ? = ...  # stored in memory
#   → print(quotient, remainder)
#   → ? = ...  # stored in memory
#   → print(quotient, remainder)
#   → ? = ...  # stored in memory
#   → print(quotient, remainder)

"""

"""
Problem 908:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    num = random.randint(1, 100)
    print(num)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
num = ...  # assigns a value to the variable
print(num)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
num = ...  # assigns a value to the variable
print(num)
import random
num = ...  # assigns a value to the variable
print(num)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → print(num)
#   → num = ...  # stored in memory
#   → print(num)
#   → num = ...  # stored in memory
#   → print(num)

"""

"""
Problem 909:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    num = random.random()
    print(num)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
num = ...  # assigns a value to the variable
print(num)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
num = ...  # assigns a value to the variable
print(num)
import random
num = ...  # assigns a value to the variable
print(num)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → print(num)
#   → num = ...  # stored in memory
#   → print(num)
#   → num = ...  # stored in memory
#   → print(num)

"""

"""
Problem 910:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    num = random.randrange(10, 51, 2)
    print(num)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
num = ...  # assigns a value to the variable
print(num)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
num = ...  # assigns a value to the variable
print(num)
import random
num = ...  # assigns a value to the variable
print(num)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → print(num)
#   → num = ...  # stored in memory
#   → print(num)
#   → num = ...  # stored in memory
#   → print(num)

"""

"""
Problem 911:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    colors = ['red', 'blue', 'green', 'yellow', 'purple']
    selected = random.choice(colors)
    print(selected)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
colors = ...  # assigns a value to the variable
selected = ...  # assigns a value to the variable
print(selected)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
colors = ...  # assigns a value to the variable
selected = ...  # assigns a value to the variable
print(selected)
import random
colors = ...  # assigns a value to the variable
selected = ...  # assigns a value to the variable
print(selected)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → colors = ...  # stored in memory
#   → selected = ...  # stored in memory
#   → print(selected)
#   → colors = ...  # stored in memory
#   → selected = ...  # stored in memory
#   → print(selected)
#   → colors = ...  # stored in memory
#   → selected = ...  # stored in memory
#   → print(selected)

"""

"""
Problem 912:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    numbers = [1, 2, 3, 4, 5]
    random.shuffle(numbers)
    print(numbers)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
numbers = ...  # assigns a value to the variable
random.shuffle(numbers)
print(numbers)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
numbers = ...  # assigns a value to the variable
random.shuffle(numbers)
print(numbers)
import random
numbers = ...  # assigns a value to the variable
random.shuffle(numbers)
print(numbers)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → random.shuffle(numbers)
#   → print(numbers)
#   → numbers = ...  # stored in memory
#   → random.shuffle(numbers)
#   → print(numbers)
#   → numbers = ...  # stored in memory
#   → random.shuffle(numbers)
#   → print(numbers)

"""

"""
Problem 913:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    numbers = list(range(1, 21))
    selected = random.sample(numbers, 3)
    print(selected)
#
# Built-in functions: list, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
numbers = ...  # assigns a value to the variable
selected = ...  # assigns a value to the variable
print(selected)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
numbers = ...  # assigns a value to the variable
selected = ...  # assigns a value to the variable
print(selected)
import random
numbers = ...  # assigns a value to the variable
selected = ...  # assigns a value to the variable
print(selected)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → selected = ...  # stored in memory
#   → print(selected)
#   → numbers = ...  # stored in memory
#   → selected = ...  # stored in memory
#   → print(selected)
#   → numbers = ...  # stored in memory
#   → selected = ...  # stored in memory
#   → print(selected)

"""

"""
Problem 914:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    num = random.uniform(5, 10)
    print(num)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
num = ...  # assigns a value to the variable
print(num)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
num = ...  # assigns a value to the variable
print(num)
import random
num = ...  # assigns a value to the variable
print(num)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → print(num)
#   → num = ...  # stored in memory
#   → print(num)
#   → num = ...  # stored in memory
#   → print(num)

"""

"""
Problem 915:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    import string
    letter = random.choice(string.ascii_letters)
    print(letter)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
import string
letter = ...  # assigns a value to the variable
print(letter)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
import string
letter = ...  # assigns a value to the variable
print(letter)
import random
import string
letter = ...  # assigns a value to the variable
print(letter)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → letter = ...  # stored in memory
#   → print(letter)
#   → letter = ...  # stored in memory
#   → print(letter)
#   → letter = ...  # stored in memory
#   → print(letter)

"""

"""
Problem 916:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    roll = random.randint(1, 6)
    print(roll)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
roll = ...  # assigns a value to the variable
print(roll)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
roll = ...  # assigns a value to the variable
print(roll)
import random
roll = ...  # assigns a value to the variable
print(roll)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → roll = ...  # stored in memory
#   → print(roll)
#   → roll = ...  # stored in memory
#   → print(roll)
#   → roll = ...  # stored in memory
#   → print(roll)

"""

"""
Problem 917:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    flip = random.choice(['Heads', 'Tails'])
    print(flip)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
flip = ...  # assigns a value to the variable
print(flip)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
flip = ...  # assigns a value to the variable
print(flip)
import random
flip = ...  # assigns a value to the variable
print(flip)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → flip = ...  # stored in memory
#   → print(flip)
#   → flip = ...  # stored in memory
#   → print(flip)
#   → flip = ...  # stored in memory
#   → print(flip)

"""

"""
Problem 918:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    first_names = ['Alice', 'Bob', 'Charlie', 'David']
    last_names = ['Smith', 'Johnson', 'Brown', 'Williams']
    full_name = f'{random.choice(first_names)} {random.choice(last_names)}'
    print(full_name)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
first_names = ...  # assigns a value to the variable
last_names = ...  # assigns a value to the variable
full_name = ...  # assigns a value to the variable
print(full_name)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
first_names = ...  # assigns a value to the variable
last_names = ...  # assigns a value to the variable
full_name = ...  # assigns a value to the variable
print(full_name)
import random
first_names = ...  # assigns a value to the variable
last_names = ...  # assigns a value to the variable
full_name = ...  # assigns a value to the variable
print(full_name)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → first_names = ...  # stored in memory
#   → last_names = ...  # stored in memory
#   → full_name = ...  # stored in memory
#   → print(full_name)
#   → first_names = ...  # stored in memory
#   → last_names = ...  # stored in memory
#   → full_name = ...  # stored in memory
#   → print(full_name)
#   → first_names = ...  # stored in memory
#   → last_names = ...  # stored in memory
#   → full_name = ...  # stored in memory
#   → print(full_name)

"""

"""
Problem 919:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.sample(characters, 8))
    print(password)
#
# Operators: +
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
? + string.punctuation  # ? → then string.punctuation → then +
string.ascii_letters + string.digits  # string.ascii_letters → then string.digits → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
import string
characters = ...  # assigns a value to the variable
password = ...  # assigns a value to the variable
print(password)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
import string
characters = ...  # assigns a value to the variable
password = ...  # assigns a value to the variable
print(password)
import random
import string
characters = ...  # assigns a value to the variable
password = ...  # assigns a value to the variable
print(password)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → characters = ...  # stored in memory
#   → password = ...  # stored in memory
#   → print(password)
#   → characters = ...  # stored in memory
#   → password = ...  # stored in memory
#   → print(password)
#   → characters = ...  # stored in memory
#   → password = ...  # stored in memory
#   → print(password)

"""

"""
Problem 920:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    boolean_value = random.choice([True, False])
    print(boolean_value)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
boolean_value = ...  # assigns a value to the variable
print(boolean_value)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
boolean_value = ...  # assigns a value to the variable
print(boolean_value)
import random
boolean_value = ...  # assigns a value to the variable
print(boolean_value)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → boolean_value = ...  # stored in memory
#   → print(boolean_value)
#   → boolean_value = ...  # stored in memory
#   → print(boolean_value)
#   → boolean_value = ...  # stored in memory
#   → print(boolean_value)

"""

"""
Problem 921:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    numbers = [random.randint(1, 100) for _ in range(5)]
    print(numbers)
#
# Built-in functions: range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
numbers = ...  # assigns a value to the variable
print(numbers)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
numbers = ...  # assigns a value to the variable
print(numbers)
import random
numbers = ...  # assigns a value to the variable
print(numbers)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print(numbers)
#   → numbers = ...  # stored in memory
#   → print(numbers)
#   → numbers = ...  # stored in memory
#   → print(numbers)

"""

"""
Problem 922:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    items = list(range(1, 11))
    subset = random.sample(items, 4)
    print(subset)
#
# Built-in functions: list, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
items = ...  # assigns a value to the variable
subset = ...  # assigns a value to the variable
print(subset)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
items = ...  # assigns a value to the variable
subset = ...  # assigns a value to the variable
print(subset)
import random
items = ...  # assigns a value to the variable
subset = ...  # assigns a value to the variable
print(subset)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → items = ...  # stored in memory
#   → subset = ...  # stored in memory
#   → print(subset)
#   → items = ...  # stored in memory
#   → subset = ...  # stored in memory
#   → print(subset)
#   → items = ...  # stored in memory
#   → subset = ...  # stored in memory
#   → print(subset)

"""

"""
Problem 923:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    import datetime
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + datetime.timedelta(days=random_days)
    print(random_date)
#
# Operators: + -
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
start_date + datetime.timedelta(...)  # start_date → then datetime.timedelta(...) → then +
end_date - start_date  # end_date → then start_date → then -
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
import datetime
start_date = ...  # assigns a value to the variable
end_date = ...  # assigns a value to the variable
random_days = ...  # assigns a value to the variable
random_date = ...  # assigns a value to the variable
print(random_date)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
import datetime
start_date = ...  # assigns a value to the variable
end_date = ...  # assigns a value to the variable
random_days = ...  # assigns a value to the variable
random_date = ...  # assigns a value to the variable
print(random_date)
import random
import datetime
start_date = ...  # assigns a value to the variable
end_date = ...  # assigns a value to the variable
random_days = ...  # assigns a value to the variable
random_date = ...  # assigns a value to the variable
print(random_date)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → start_date = ...  # stored in memory
#   → end_date = ...  # stored in memory
#   → random_days = ...  # stored in memory
#   → random_date = ...  # stored in memory
#   → print(random_date)
#   → start_date = ...  # stored in memory
#   → end_date = ...  # stored in memory
#   → random_days = ...  # stored in memory
#   → random_date = ...  # stored in memory
#   → print(random_date)
#   → start_date = ...  # stored in memory
#   → end_date = ...  # stored in memory
#   → random_days = ...  # stored in memory
#   → random_date = ...  # stored in memory
#   → print(random_date)

"""

"""
Problem 924:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    fruits = {'apple', 'banana', 'cherry', 'date'}
    random_fruit = random.choice(list(fruits))
    print(random_fruit)
#
# Built-in functions: list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
fruits = ...  # assigns a value to the variable
random_fruit = ...  # assigns a value to the variable
print(random_fruit)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
fruits = ...  # assigns a value to the variable
random_fruit = ...  # assigns a value to the variable
print(random_fruit)
import random
fruits = ...  # assigns a value to the variable
random_fruit = ...  # assigns a value to the variable
print(random_fruit)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → fruits = ...  # stored in memory
#   → random_fruit = ...  # stored in memory
#   → print(random_fruit)
#   → fruits = ...  # stored in memory
#   → random_fruit = ...  # stored in memory
#   → print(random_fruit)
#   → fruits = ...  # stored in memory
#   → random_fruit = ...  # stored in memory
#   → print(random_fruit)

"""

"""
Problem 925:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    code = random.randint(100000, 999999)
    print(code)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
code = ...  # assigns a value to the variable
print(code)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
code = ...  # assigns a value to the variable
print(code)
import random
code = ...  # assigns a value to the variable
print(code)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → code = ...  # stored in memory
#   → print(code)
#   → code = ...  # stored in memory
#   → print(code)
#   → code = ...  # stored in memory
#   → print(code)

"""

"""
Problem 926:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    hex_color = '#{:06x}'.format(random.randint(0, 16777215))
    print(hex_color)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
hex_color = ...  # assigns a value to the variable
print(hex_color)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
hex_color = ...  # assigns a value to the variable
print(hex_color)
import random
hex_color = ...  # assigns a value to the variable
print(hex_color)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → hex_color = ...  # stored in memory
#   → print(hex_color)
#   → hex_color = ...  # stored in memory
#   → print(hex_color)
#   → hex_color = ...  # stored in memory
#   → print(hex_color)

"""

"""
Problem 927:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    phone_number = f'({random.randint(100, 999)}) {random.randint(100, 999)}-{random.randint(1000, 9999)}'
    print(phone_number)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
phone_number = ...  # assigns a value to the variable
print(phone_number)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
phone_number = ...  # assigns a value to the variable
print(phone_number)
import random
phone_number = ...  # assigns a value to the variable
print(phone_number)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → phone_number = ...  # stored in memory
#   → print(phone_number)
#   → phone_number = ...  # stored in memory
#   → print(phone_number)
#   → phone_number = ...  # stored in memory
#   → print(phone_number)

"""

"""
Problem 928:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    pin = f'{random.randint(1000, 9999)}'
    print(pin)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
pin = ...  # assigns a value to the variable
print(pin)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
pin = ...  # assigns a value to the variable
print(pin)
import random
pin = ...  # assigns a value to the variable
print(pin)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → pin = ...  # stored in memory
#   → print(pin)
#   → pin = ...  # stored in memory
#   → print(pin)
#   → pin = ...  # stored in memory
#   → print(pin)

"""

"""
Problem 929:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(dice1, dice2)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
dice1 = ...  # assigns a value to the variable
dice2 = ...  # assigns a value to the variable
print(dice1, dice2)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
dice1 = ...  # assigns a value to the variable
dice2 = ...  # assigns a value to the variable
print(dice1, dice2)
import random
dice1 = ...  # assigns a value to the variable
dice2 = ...  # assigns a value to the variable
print(dice1, dice2)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dice1 = ...  # stored in memory
#   → dice2 = ...  # stored in memory
#   → print(dice1, dice2)
#   → dice1 = ...  # stored in memory
#   → dice2 = ...  # stored in memory
#   → print(dice1, dice2)
#   → dice1 = ...  # stored in memory
#   → dice2 = ...  # stored in memory
#   → print(dice1, dice2)

"""

"""
Problem 930:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    ip_address = '.'.join((str(random.randint(0, 255)) for _ in range(4)))
    print(ip_address)
#
# Built-in functions: range, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
ip_address = ...  # assigns a value to the variable
print(ip_address)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
ip_address = ...  # assigns a value to the variable
print(ip_address)
import random
ip_address = ...  # assigns a value to the variable
print(ip_address)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → ip_address = ...  # stored in memory
#   → print(ip_address)
#   → ip_address = ...  # stored in memory
#   → print(ip_address)
#   → ip_address = ...  # stored in memory
#   → print(ip_address)

"""

"""
Problem 931:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=12))
    print(password)
#
# Operators: +
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
? + string.punctuation  # ? → then string.punctuation → then +
string.ascii_letters + string.digits  # string.ascii_letters → then string.digits → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
import string
characters = ...  # assigns a value to the variable
password = ...  # assigns a value to the variable
print(password)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
import string
characters = ...  # assigns a value to the variable
password = ...  # assigns a value to the variable
print(password)
import random
import string
characters = ...  # assigns a value to the variable
password = ...  # assigns a value to the variable
print(password)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → characters = ...  # stored in memory
#   → password = ...  # stored in memory
#   → print(password)
#   → characters = ...  # stored in memory
#   → password = ...  # stored in memory
#   → print(password)
#   → characters = ...  # stored in memory
#   → password = ...  # stored in memory
#   → print(password)

"""

"""
Problem 932:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import random
    animals = ('dog', 'cat', 'elephant', 'lion')
    random_animal = random.choice(animals)
    print(random_animal)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import random
animals = ...  # assigns a value to the variable
random_animal = ...  # assigns a value to the variable
print(random_animal)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import random
animals = ...  # assigns a value to the variable
random_animal = ...  # assigns a value to the variable
print(random_animal)
import random
animals = ...  # assigns a value to the variable
random_animal = ...  # assigns a value to the variable
print(random_animal)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → animals = ...  # stored in memory
#   → random_animal = ...  # stored in memory
#   → print(random_animal)
#   → animals = ...  # stored in memory
#   → random_animal = ...  # stored in memory
#   → print(random_animal)
#   → animals = ...  # stored in memory
#   → random_animal = ...  # stored in memory
#   → print(random_animal)

"""

"""
Problem 933:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    try:
        a, b = (10, 0)
        result = a / b
    except ZeroDivisionError:
        result = 'Cannot divide by zero'
    print(result)
#
# Keywords: try/except
# Operators: /
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
a / b  # a → then b → then /
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
print(result)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
print(result)
print(result)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(result)
#   → print(result)
#   → print(result)

"""

"""
Problem 934:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    try:
        lst = [1, 2, 3]
        value = lst[5]
    except IndexError:
        value = 'Index out of range'
    print(value)
#
# Keywords: try/except
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
print(value)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
print(value)
print(value)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(value)
#   → print(value)
#   → print(value)

"""

"""
Problem 935:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    try:
        d = {'name': 'Alice'}
        value = d['age']
    except KeyError:
        value = 'Key not found'
    print(value)
#
# Keywords: try/except
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
print(value)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
print(value)
print(value)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(value)
#   → print(value)
#   → print(value)

"""

"""
Problem 936:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    try:
        num = int('abc')
    except ValueError:
        num = 'Invalid integer conversion'
    print(num)
#
# Keywords: try/except
# Built-in functions: int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
print(num)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
print(num)
print(num)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(num)
#   → print(num)
#   → print(num)

"""

"""
Problem 937:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    try:
        result = 'Age: ' + 25
    except TypeError:
        result = 'Type mismatch error'
    print(result)
#
# Keywords: try/except
# Operators: +
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
'Age: ' + 25  # 'Age: ' → then 25 → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
print(result)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
print(result)
print(result)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(result)
#   → print(result)
#   → print(result)

"""

"""
Problem 938:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    try:
        with open('nonexistent.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        content = 'File not found'
    print(content)
#
# Keywords: try/except
# Built-in functions: open()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
print(content)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
print(content)
print(content)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(content)
#   → print(content)
#   → print(content)

"""

"""
Problem 939:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    class Person:
    
        def __init__(self, name):
            self.name = name
    try:
        p = Person('Alice')
        age = p.age
    except AttributeError:
        age = 'Attribute not found'
    print(age)
#
class Person:  # defines a new type
    def __init__(self, name):  # method of Person
        self.name = name  # method of Person
#
# Keywords: try/except
# Built-in functions: Person()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class Person:  # class definition stored
print(age)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
obj = ...  # assigns a value to the variable
print(obj)
print(Person(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Person are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(age)
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Person(...))

"""

"""
Problem 940:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    try:
        result = x + 10
    except NameError:
        result = 'Variable not defined'
    print(result)
#
# Keywords: try/except
# Operators: +
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
x + 10  # x → then 10 → then +
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
print(result)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
print(result)
print(result)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(result)
#   → print(result)
#   → print(result)

"""

"""
Problem 941:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    try:
        with open('/root/protected.txt', 'w') as file:
            file.write('Test')
    except PermissionError:
        result = 'Permission denied'
    print(result)
#
# Keywords: try/except
# Built-in functions: open()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
print(result)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
print(result)
print(result)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(result)
#   → print(result)
#   → print(result)

"""

"""
Problem 942:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    try:
        a, b = (10, 2)
        result = a / b
    except ZeroDivisionError:
        result = 'Cannot divide by zero'
    else:
        result = f'Division successful: {result}'
    print(result)
#
# Keywords: try/except
# Operators: /
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
a / b  # a → then b → then /
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
print(result)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
print(result)
print(result)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(result)
#   → print(result)
#   → print(result)

"""

"""
Problem 943:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    try:
        result = 10 / 0
    except ZeroDivisionError:
        result = 'Cannot divide by zero'
    finally:
        print('Execution completed')
    print(result)
#
# Keywords: try/except
# Operators: /
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
10 / 0  # 10 → then 0 → then /
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
print(result)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
print(result)
print(result)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(result)
#   → print(result)
#   → print(result)

"""

"""
Problem 944:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def check_number(n):  # defines a function with parameters n
    if n < 0:
        raise NegativeNumberError('Negative numbers are not allowed')
#
class NegativeNumberError(Exception):  # defines a new type
#
# Keywords: if/else | try/except
# Operators: <
# Built-in functions: NegativeNumberError()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
check_number(n)  # arguments evaluated first, then function body runs
print(check_number(15))  # check_number() runs first, then print() outputs the result
n < 0  # evaluated as True or False → picks which branch
check_number(?)  # arguments evaluated first, then function body runs
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
class NegativeNumberError(Exception):  # class definition stored
def check_number(n):  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
n = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(check_number(...))  # check_number() runs with n=15
#   → if n < 0:
#   →     raise NegativeNumberError('Negative numbers are not allowed')
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes NegativeNumberError are defined — methods stored in memory
# def blocks are skipped at runtime — check_number, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(check_number(...))  # check_number() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped

"""

"""
Problem 945:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    try:
        num = '10' / 2
    except (ZeroDivisionError, TypeError):
        result = 'An error occurred'
    print(result)
#
# Keywords: try/except
# Operators: /
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
'10' / 2  # '10' → then 2 → then /
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
print(result)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
print(result)
print(result)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(result)
#   → print(result)
#   → print(result)

"""

"""
Problem 946:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    try:
        x = -1
        assert x >= 0, 'Negative number not allowed'
    except AssertionError as e:
        print(e)
#
# Keywords: try/except
# Operators: >=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
x >= 0  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):

"""

"""
Problem 947:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    try:
        raise MemoryError('simulated memory limit')
    except MemoryError:
        print('Memory limit exceeded')
#
# Keywords: try/except
# Built-in functions: MemoryError()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):

"""

"""
Problem 948:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def infinite_recursion():  # defines a function with no parameters
    return infinite_recursion()  # return sends the result back to the caller
#
# Keywords: try/except
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
infinite_recursion()  # function body runs with no arguments
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def infinite_recursion():  # stored in memory, not executed yet
def infinite_recursion():  # stored in memory, not executed yet
def infinite_recursion():  # stored in memory, not executed yet
result = ...  # assigns a value to the variable
print(result)
result = ...  # assigns a value to the variable
print(result)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only infinite_recursion is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → result = ...  # stored in memory
#   → print(result)

"""

"""
Problem 949:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    try:
        import nonexistent_module
    except ModuleNotFoundError:
        print('Module not found')
#
# Keywords: try/except
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):

"""

"""
Problem 950:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    try:
        with open('missingfile.txt', 'r') as f:
            data = f.read()
    except IOError:
        print('Error reading file')
#
# Keywords: try/except
# Built-in functions: open()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):

"""

"""
Problem 951:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    try:
        raise KeyboardInterrupt
    except KeyboardInterrupt:
        print('Process interrupted by user')
#
# Keywords: try/except
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):

"""

"""
Problem 952:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    text = 'hello world'
    upper_text = text.upper()
    print(upper_text)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
text = ...  # assigns a value to the variable
upper_text = ...  # assigns a value to the variable
print(upper_text)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
text = ...  # assigns a value to the variable
upper_text = ...  # assigns a value to the variable
print(upper_text)
text = ...  # assigns a value to the variable
upper_text = ...  # assigns a value to the variable
print(upper_text)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → text = ...  # stored in memory
#   → upper_text = ...  # stored in memory
#   → print(upper_text)
#   → text = ...  # stored in memory
#   → upper_text = ...  # stored in memory
#   → print(upper_text)
#   → text = ...  # stored in memory
#   → upper_text = ...  # stored in memory
#   → print(upper_text)

"""

"""
Problem 953:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    text = 'banana'
    count_a = text.count('a')
    print(count_a)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
text = ...  # assigns a value to the variable
count_a = ...  # assigns a value to the variable
print(count_a)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
text = ...  # assigns a value to the variable
count_a = ...  # assigns a value to the variable
print(count_a)
text = ...  # assigns a value to the variable
count_a = ...  # assigns a value to the variable
print(count_a)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → text = ...  # stored in memory
#   → count_a = ...  # stored in memory
#   → print(count_a)
#   → text = ...  # stored in memory
#   → count_a = ...  # stored in memory
#   → print(count_a)
#   → text = ...  # stored in memory
#   → count_a = ...  # stored in memory
#   → print(count_a)

"""

"""
Problem 954:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    text = 'hello world'
    result = text.startswith('hello')
    print(result)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
text = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
text = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
text = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → text = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → text = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → text = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)

"""

"""
Problem 955:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    text = 'I love apples. Apples are delicious.'
    new_text = text.replace('Apples', 'Bananas')
    print(new_text)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
text = ...  # assigns a value to the variable
new_text = ...  # assigns a value to the variable
print(new_text)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
text = ...  # assigns a value to the variable
new_text = ...  # assigns a value to the variable
print(new_text)
text = ...  # assigns a value to the variable
new_text = ...  # assigns a value to the variable
print(new_text)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → text = ...  # stored in memory
#   → new_text = ...  # stored in memory
#   → print(new_text)
#   → text = ...  # stored in memory
#   → new_text = ...  # stored in memory
#   → print(new_text)
#   → text = ...  # stored in memory
#   → new_text = ...  # stored in memory
#   → print(new_text)

"""

"""
Problem 956:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    sentence = 'Python is amazing'
    words = sentence.split()
    print(words)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
sentence = ...  # assigns a value to the variable
words = ...  # assigns a value to the variable
print(words)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
sentence = ...  # assigns a value to the variable
words = ...  # assigns a value to the variable
print(words)
sentence = ...  # assigns a value to the variable
words = ...  # assigns a value to the variable
print(words)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → sentence = ...  # stored in memory
#   → words = ...  # stored in memory
#   → print(words)
#   → sentence = ...  # stored in memory
#   → words = ...  # stored in memory
#   → print(words)
#   → sentence = ...  # stored in memory
#   → words = ...  # stored in memory
#   → print(words)

"""

"""
Problem 957:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    words = ['Python', 'is', 'fun']
    sentence = ' '.join(words)
    print(sentence)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
words = ...  # assigns a value to the variable
sentence = ...  # assigns a value to the variable
print(sentence)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
words = ...  # assigns a value to the variable
sentence = ...  # assigns a value to the variable
print(sentence)
words = ...  # assigns a value to the variable
sentence = ...  # assigns a value to the variable
print(sentence)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → words = ...  # stored in memory
#   → sentence = ...  # stored in memory
#   → print(sentence)
#   → words = ...  # stored in memory
#   → sentence = ...  # stored in memory
#   → print(sentence)
#   → words = ...  # stored in memory
#   → sentence = ...  # stored in memory
#   → print(sentence)

"""

"""
Problem 958:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    text = '   hello world   '
    trimmed_text = text.strip()
    print(trimmed_text)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
text = ...  # assigns a value to the variable
trimmed_text = ...  # assigns a value to the variable
print(trimmed_text)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
text = ...  # assigns a value to the variable
trimmed_text = ...  # assigns a value to the variable
print(trimmed_text)
text = ...  # assigns a value to the variable
trimmed_text = ...  # assigns a value to the variable
print(trimmed_text)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → text = ...  # stored in memory
#   → trimmed_text = ...  # stored in memory
#   → print(trimmed_text)
#   → text = ...  # stored in memory
#   → trimmed_text = ...  # stored in memory
#   → print(trimmed_text)
#   → text = ...  # stored in memory
#   → trimmed_text = ...  # stored in memory
#   → print(trimmed_text)

"""

"""
Problem 959:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    numbers = [10, 20, 30, 40, 50]
    index_30 = numbers.index(30)
    print(index_30)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
numbers = ...  # assigns a value to the variable
index_30 = ...  # assigns a value to the variable
print(index_30)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
index_30 = ...  # assigns a value to the variable
print(index_30)
numbers = ...  # assigns a value to the variable
index_30 = ...  # assigns a value to the variable
print(index_30)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → index_30 = ...  # stored in memory
#   → print(index_30)
#   → numbers = ...  # stored in memory
#   → index_30 = ...  # stored in memory
#   → print(index_30)
#   → numbers = ...  # stored in memory
#   → index_30 = ...  # stored in memory
#   → print(index_30)

"""

"""
Problem 960:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    numbers = [5, 2, 8, 1, 3]
    numbers.sort()
    print(numbers)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
numbers = ...  # assigns a value to the variable
numbers.sort()
print(numbers)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
numbers.sort()
print(numbers)
numbers = ...  # assigns a value to the variable
numbers.sort()
print(numbers)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → numbers.sort()
#   → print(numbers)
#   → numbers = ...  # stored in memory
#   → numbers.sort()
#   → print(numbers)
#   → numbers = ...  # stored in memory
#   → numbers.sort()
#   → print(numbers)

"""

"""
Problem 961:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    numbers = [1, 2, 3, 4, 5]
    numbers.reverse()
    print(numbers)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
numbers = ...  # assigns a value to the variable
numbers.reverse()
print(numbers)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
numbers.reverse()
print(numbers)
numbers = ...  # assigns a value to the variable
numbers.reverse()
print(numbers)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → numbers.reverse()
#   → print(numbers)
#   → numbers = ...  # stored in memory
#   → numbers.reverse()
#   → print(numbers)
#   → numbers = ...  # stored in memory
#   → numbers.reverse()
#   → print(numbers)

"""

"""
Problem 962:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    numbers = [1, 2, 3]
    numbers.append(4)
    print(numbers)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
numbers = ...  # assigns a value to the variable
numbers.append(4)
print(numbers)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
numbers.append(4)
print(numbers)
numbers = ...  # assigns a value to the variable
numbers.append(4)
print(numbers)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → numbers.append(4)
#   → print(numbers)
#   → numbers = ...  # stored in memory
#   → numbers.append(4)
#   → print(numbers)
#   → numbers = ...  # stored in memory
#   → numbers.append(4)
#   → print(numbers)

"""

"""
Problem 963:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    numbers = [10, 20, 30]
    last_item = numbers.pop()
    print(numbers)
    print(last_item)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
numbers = ...  # assigns a value to the variable
last_item = ...  # assigns a value to the variable
print(numbers)
print(last_item)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
last_item = ...  # assigns a value to the variable
print(numbers)
print(last_item)
numbers = ...  # assigns a value to the variable
last_item = ...  # assigns a value to the variable
print(numbers)
print(last_item)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → last_item = ...  # stored in memory
#   → print(numbers)
#   → print(last_item)
#   → numbers = ...  # stored in memory
#   → last_item = ...  # stored in memory
#   → print(numbers)
#   → print(last_item)
#   → numbers = ...  # stored in memory
#   → last_item = ...  # stored in memory
#   → print(numbers)
#   → print(last_item)

"""

"""
Problem 964:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    numbers = [5, 10, 15, 20]
    numbers.remove(10)
    print(numbers)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
numbers = ...  # assigns a value to the variable
numbers.remove(10)
print(numbers)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
numbers.remove(10)
print(numbers)
numbers = ...  # assigns a value to the variable
numbers.remove(10)
print(numbers)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → numbers.remove(10)
#   → print(numbers)
#   → numbers = ...  # stored in memory
#   → numbers.remove(10)
#   → print(numbers)
#   → numbers = ...  # stored in memory
#   → numbers.remove(10)
#   → print(numbers)

"""

"""
Problem 965:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Built-in functions: list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
person = ...  # assigns a value to the variable
keys = ...  # assigns a value to the variable
print(list(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → person = ...  # stored in memory
#   → keys = ...  # stored in memory
#   → print(list(...))

"""

"""
Problem 966:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Built-in functions: list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
person = ...  # assigns a value to the variable
values = ...  # assigns a value to the variable
print(list(...))
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → person = ...  # stored in memory
#   → values = ...  # stored in memory
#   → print(list(...))

"""

"""
Problem 967:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    dict1.update(dict2)
    print(dict1)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
dict1 = ...  # assigns a value to the variable
dict2 = ...  # assigns a value to the variable
dict1.update(dict2)
print(dict1)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
dict1 = ...  # assigns a value to the variable
dict2 = ...  # assigns a value to the variable
dict1.update(dict2)
print(dict1)
dict1 = ...  # assigns a value to the variable
dict2 = ...  # assigns a value to the variable
dict1.update(dict2)
print(dict1)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dict1 = ...  # stored in memory
#   → dict2 = ...  # stored in memory
#   → dict1.update(dict2)
#   → print(dict1)
#   → dict1 = ...  # stored in memory
#   → dict2 = ...  # stored in memory
#   → dict1.update(dict2)
#   → print(dict1)
#   → dict1 = ...  # stored in memory
#   → dict2 = ...  # stored in memory
#   → dict1.update(dict2)
#   → print(dict1)

"""

"""
Problem 968:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
    person.pop('age')
    print(person)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
person = ...  # assigns a value to the variable
person.pop('age')
print(person)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
person = ...  # assigns a value to the variable
person.pop('age')
print(person)
person = ...  # assigns a value to the variable
person.pop('age')
print(person)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → person = ...  # stored in memory
#   → person.pop('age')
#   → print(person)
#   → person = ...  # stored in memory
#   → person.pop('age')
#   → print(person)
#   → person = ...  # stored in memory
#   → person.pop('age')
#   → print(person)

"""

"""
Problem 969:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    numbers = {1, 2, 3, 4, 5}
    result = 3 in numbers
    print(result)
#
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
3 in numbers  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
numbers = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
numbers = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)

"""

"""
Problem 970:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    numbers = {10, 20, 30, 40}
    removed_element = numbers.pop()
    print(removed_element)
    print(numbers)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
numbers = ...  # assigns a value to the variable
removed_element = ...  # assigns a value to the variable
print(removed_element)
print(numbers)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
removed_element = ...  # assigns a value to the variable
print(removed_element)
print(numbers)
numbers = ...  # assigns a value to the variable
removed_element = ...  # assigns a value to the variable
print(removed_element)
print(numbers)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → removed_element = ...  # stored in memory
#   → print(removed_element)
#   → print(numbers)
#   → numbers = ...  # stored in memory
#   → removed_element = ...  # stored in memory
#   → print(removed_element)
#   → print(numbers)
#   → numbers = ...  # stored in memory
#   → removed_element = ...  # stored in memory
#   → print(removed_element)
#   → print(numbers)

"""

"""
Problem 971:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    numbers = [1, 2, 3, 4, 5]
    numbers.clear()
    print(numbers)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
numbers = ...  # assigns a value to the variable
numbers.clear()
print(numbers)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
numbers.clear()
print(numbers)
numbers = ...  # assigns a value to the variable
numbers.clear()
print(numbers)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → numbers.clear()
#   → print(numbers)
#   → numbers = ...  # stored in memory
#   → numbers.clear()
#   → print(numbers)
#   → numbers = ...  # stored in memory
#   → numbers.clear()
#   → print(numbers)

"""

"""
Problem 972:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    num_str = '42'
    num = int(num_str)
    print(num)
#
# Built-in functions: int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
num_str = ...  # assigns a value to the variable
num = ...  # assigns a value to the variable
print(num)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
num_str = ...  # assigns a value to the variable
num = ...  # assigns a value to the variable
print(num)
num_str = ...  # assigns a value to the variable
num = ...  # assigns a value to the variable
print(num)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num_str = ...  # stored in memory
#   → num = ...  # stored in memory
#   → print(num)
#   → num_str = ...  # stored in memory
#   → num = ...  # stored in memory
#   → print(num)
#   → num_str = ...  # stored in memory
#   → num = ...  # stored in memory
#   → print(num)

"""

"""
Problem 973:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    num_str = '3.14'
    num = float(num_str)
    print(num)
#
# Built-in functions: float()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
num_str = ...  # assigns a value to the variable
num = ...  # assigns a value to the variable
print(num)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
num_str = ...  # assigns a value to the variable
num = ...  # assigns a value to the variable
print(num)
num_str = ...  # assigns a value to the variable
num = ...  # assigns a value to the variable
print(num)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num_str = ...  # stored in memory
#   → num = ...  # stored in memory
#   → print(num)
#   → num_str = ...  # stored in memory
#   → num = ...  # stored in memory
#   → print(num)
#   → num_str = ...  # stored in memory
#   → num = ...  # stored in memory
#   → print(num)

"""

"""
Problem 974:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    bool_str = 'True'
    boolean_value = bool_str.lower() == 'true'
    print(boolean_value)
#
# Operators: ==
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
bool_str.lower(...) == 'true'  # evaluated as True or False → picks which branch
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
bool_str = ...  # assigns a value to the variable
boolean_value = ...  # assigns a value to the variable
print(boolean_value)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
bool_str = ...  # assigns a value to the variable
boolean_value = ...  # assigns a value to the variable
print(boolean_value)
bool_str = ...  # assigns a value to the variable
boolean_value = ...  # assigns a value to the variable
print(boolean_value)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → bool_str = ...  # stored in memory
#   → boolean_value = ...  # stored in memory
#   → print(boolean_value)
#   → bool_str = ...  # stored in memory
#   → boolean_value = ...  # stored in memory
#   → print(boolean_value)
#   → bool_str = ...  # stored in memory
#   → boolean_value = ...  # stored in memory
#   → print(boolean_value)

"""

"""
Problem 975:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    num_str = '10,20,30,40'
    numbers = list(map(int, num_str.split(',')))
    print(numbers)
#
# Built-in functions: list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
num_str = ...  # assigns a value to the variable
numbers = ...  # assigns a value to the variable
print(numbers)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
num_str = ...  # assigns a value to the variable
numbers = ...  # assigns a value to the variable
print(numbers)
num_str = ...  # assigns a value to the variable
numbers = ...  # assigns a value to the variable
print(numbers)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num_str = ...  # stored in memory
#   → numbers = ...  # stored in memory
#   → print(numbers)
#   → num_str = ...  # stored in memory
#   → numbers = ...  # stored in memory
#   → print(numbers)
#   → num_str = ...  # stored in memory
#   → numbers = ...  # stored in memory
#   → print(numbers)

"""

"""
Problem 976:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    from datetime import datetime
    date_str = '2024-03-22'
    parsed_date = datetime.strptime(date_str, '%Y-%m-%d')
    print(parsed_date)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from datetime import datetime
date_str = ...  # assigns a value to the variable
parsed_date = ...  # assigns a value to the variable
print(parsed_date)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
from datetime import datetime
date_str = ...  # assigns a value to the variable
parsed_date = ...  # assigns a value to the variable
print(parsed_date)
from datetime import datetime
date_str = ...  # assigns a value to the variable
parsed_date = ...  # assigns a value to the variable
print(parsed_date)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → date_str = ...  # stored in memory
#   → parsed_date = ...  # stored in memory
#   → print(parsed_date)
#   → date_str = ...  # stored in memory
#   → parsed_date = ...  # stored in memory
#   → print(parsed_date)
#   → date_str = ...  # stored in memory
#   → parsed_date = ...  # stored in memory
#   → print(parsed_date)

"""

"""
Problem 977:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import re
    text = 'My order number is 12345 and tracking ID is 67890.'
    numbers = re.findall('\\d+', text)
    print(numbers)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import re
text = ...  # assigns a value to the variable
numbers = ...  # assigns a value to the variable
print(numbers)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import re
text = ...  # assigns a value to the variable
numbers = ...  # assigns a value to the variable
print(numbers)
import re
text = ...  # assigns a value to the variable
numbers = ...  # assigns a value to the variable
print(numbers)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → text = ...  # stored in memory
#   → numbers = ...  # stored in memory
#   → print(numbers)
#   → text = ...  # stored in memory
#   → numbers = ...  # stored in memory
#   → print(numbers)
#   → text = ...  # stored in memory
#   → numbers = ...  # stored in memory
#   → print(numbers)

"""

"""
Problem 978:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import json
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# No top-level code runs — functions must be called externally

"""

"""
Problem 979:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import json
    data = {'name': 'Bob', 'age': 30, 'city': 'London'}
    json_str = json.dumps(data)
    print(json_str)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import json
data = ...  # assigns a value to the variable
json_str = ...  # assigns a value to the variable
print(json_str)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import json
data = ...  # assigns a value to the variable
json_str = ...  # assigns a value to the variable
print(json_str)
import json
data = ...  # assigns a value to the variable
json_str = ...  # assigns a value to the variable
print(json_str)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → data = ...  # stored in memory
#   → json_str = ...  # stored in memory
#   → print(json_str)
#   → data = ...  # stored in memory
#   → json_str = ...  # stored in memory
#   → print(json_str)
#   → data = ...  # stored in memory
#   → json_str = ...  # stored in memory
#   → print(json_str)

"""

"""
Problem 980:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import xml.etree.ElementTree as ET
    xml_str = '<person><name>Charlie</name><age>28</age></person>'
    root = ET.fromstring(xml_str)
    name = root.find('name').text
    print(name)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import xml.etree.ElementTree
xml_str = ...  # assigns a value to the variable
root = ...  # assigns a value to the variable
name = ...  # assigns a value to the variable
print(name)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import xml.etree.ElementTree
xml_str = ...  # assigns a value to the variable
root = ...  # assigns a value to the variable
name = ...  # assigns a value to the variable
print(name)
import xml.etree.ElementTree
xml_str = ...  # assigns a value to the variable
root = ...  # assigns a value to the variable
name = ...  # assigns a value to the variable
print(name)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → xml_str = ...  # stored in memory
#   → root = ...  # stored in memory
#   → name = ...  # stored in memory
#   → print(name)
#   → xml_str = ...  # stored in memory
#   → root = ...  # stored in memory
#   → name = ...  # stored in memory
#   → print(name)
#   → xml_str = ...  # stored in memory
#   → root = ...  # stored in memory
#   → name = ...  # stored in memory
#   → print(name)

"""

"""
Problem 981:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    from urllib.parse import parse_qs
    query_str = 'name=David&age=35&city=Paris'
    parsed_data = parse_qs(query_str)
    print(parsed_data)
#
# Built-in functions: parse_qs()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from urllib.parse import parse_qs
query_str = ...  # assigns a value to the variable
parsed_data = ...  # assigns a value to the variable
print(parsed_data)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
from urllib.parse import parse_qs
query_str = ...  # assigns a value to the variable
parsed_data = ...  # assigns a value to the variable
print(parsed_data)
from urllib.parse import parse_qs
query_str = ...  # assigns a value to the variable
parsed_data = ...  # assigns a value to the variable
print(parsed_data)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → query_str = ...  # stored in memory
#   → parsed_data = ...  # stored in memory
#   → print(parsed_data)
#   → query_str = ...  # stored in memory
#   → parsed_data = ...  # stored in memory
#   → print(parsed_data)
#   → query_str = ...  # stored in memory
#   → parsed_data = ...  # stored in memory
#   → print(parsed_data)

"""

"""
Problem 982:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import csv
from io import StringIO
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# No top-level code runs — functions must be called externally

"""

"""
Problem 983:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from html.parser import HTMLParser
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# No top-level code runs — functions must be called externally

"""

"""
Problem 984:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    from datetime import datetime
    time_str = '14:30:45'
    parsed_time = datetime.strptime(time_str, '%H:%M:%S').time()
    print(parsed_time)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
from datetime import datetime
time_str = ...  # assigns a value to the variable
parsed_time = ...  # assigns a value to the variable
print(parsed_time)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
from datetime import datetime
time_str = ...  # assigns a value to the variable
parsed_time = ...  # assigns a value to the variable
print(parsed_time)
from datetime import datetime
time_str = ...  # assigns a value to the variable
parsed_time = ...  # assigns a value to the variable
print(parsed_time)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → time_str = ...  # stored in memory
#   → parsed_time = ...  # stored in memory
#   → print(parsed_time)
#   → time_str = ...  # stored in memory
#   → parsed_time = ...  # stored in memory
#   → print(parsed_time)
#   → time_str = ...  # stored in memory
#   → parsed_time = ...  # stored in memory
#   → print(parsed_time)

"""

"""
Problem 985:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    hex_str = '0x1A'
    num = int(hex_str, 16)
    print(num)
#
# Built-in functions: int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
hex_str = ...  # assigns a value to the variable
num = ...  # assigns a value to the variable
print(num)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
hex_str = ...  # assigns a value to the variable
num = ...  # assigns a value to the variable
print(num)
hex_str = ...  # assigns a value to the variable
num = ...  # assigns a value to the variable
print(num)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → hex_str = ...  # stored in memory
#   → num = ...  # stored in memory
#   → print(num)
#   → hex_str = ...  # stored in memory
#   → num = ...  # stored in memory
#   → print(num)
#   → hex_str = ...  # stored in memory
#   → num = ...  # stored in memory
#   → print(num)

"""

"""
Problem 986:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    binary_str = '1010'
    num = int(binary_str, 2)
    print(num)
#
# Built-in functions: int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
binary_str = ...  # assigns a value to the variable
num = ...  # assigns a value to the variable
print(num)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
binary_str = ...  # assigns a value to the variable
num = ...  # assigns a value to the variable
print(num)
binary_str = ...  # assigns a value to the variable
num = ...  # assigns a value to the variable
print(num)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → binary_str = ...  # stored in memory
#   → num = ...  # stored in memory
#   → print(num)
#   → binary_str = ...  # stored in memory
#   → num = ...  # stored in memory
#   → print(num)
#   → binary_str = ...  # stored in memory
#   → num = ...  # stored in memory
#   → print(num)

"""

"""
Problem 987:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    sci_str = '3.5e4'
    num = float(sci_str)
    print(num)
#
# Built-in functions: float()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
sci_str = ...  # assigns a value to the variable
num = ...  # assigns a value to the variable
print(num)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
sci_str = ...  # assigns a value to the variable
num = ...  # assigns a value to the variable
print(num)
sci_str = ...  # assigns a value to the variable
num = ...  # assigns a value to the variable
print(num)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → sci_str = ...  # stored in memory
#   → num = ...  # stored in memory
#   → print(num)
#   → sci_str = ...  # stored in memory
#   → num = ...  # stored in memory
#   → print(num)
#   → sci_str = ...  # stored in memory
#   → num = ...  # stored in memory
#   → print(num)

"""

"""
Problem 988:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import configparser
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# No top-level code runs — functions must be called externally

"""

"""
Problem 989:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import re
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# No top-level code runs — functions must be called externally

"""

"""
Problem 991:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import json
    json_str = '[1, 2, 3, 4, 5]'
    data = json.loads(json_str)
    print(data)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import json
json_str = ...  # assigns a value to the variable
data = ...  # assigns a value to the variable
print(data)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import json
json_str = ...  # assigns a value to the variable
data = ...  # assigns a value to the variable
print(data)
import json
json_str = ...  # assigns a value to the variable
data = ...  # assigns a value to the variable
print(data)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → json_str = ...  # stored in memory
#   → data = ...  # stored in memory
#   → print(data)
#   → json_str = ...  # stored in memory
#   → data = ...  # stored in memory
#   → print(data)
#   → json_str = ...  # stored in memory
#   → data = ...  # stored in memory
#   → print(data)

"""

"""
Problem 992:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import re
    currency_str = '$123.45'
    value = float(re.sub('[^\\d.]', '', currency_str))
    print(value)
#
# Built-in functions: float()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import re
currency_str = ...  # assigns a value to the variable
value = ...  # assigns a value to the variable
print(value)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import re
currency_str = ...  # assigns a value to the variable
value = ...  # assigns a value to the variable
print(value)
import re
currency_str = ...  # assigns a value to the variable
value = ...  # assigns a value to the variable
print(value)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → currency_str = ...  # stored in memory
#   → value = ...  # stored in memory
#   → print(value)
#   → currency_str = ...  # stored in memory
#   → value = ...  # stored in memory
#   → print(value)
#   → currency_str = ...  # stored in memory
#   → value = ...  # stored in memory
#   → print(value)

"""

"""
Problem 993:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, default='User')
    args = parser.parse_args(args=['--name', 'Alice'])
    print(args.name)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
import argparse
parser = ...  # assigns a value to the variable
parser.add_argument('--name')
args = ...  # assigns a value to the variable
print(?)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
import argparse
parser = ...  # assigns a value to the variable
parser.add_argument('--name')
args = ...  # assigns a value to the variable
print(?)
import argparse
parser = ...  # assigns a value to the variable
parser.add_argument('--name')
args = ...  # assigns a value to the variable
print(?)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → parser = ...  # stored in memory
#   → parser.add_argument('--name')
#   → args = ...  # stored in memory
#   → print(?)
#   → parser = ...  # stored in memory
#   → parser.add_argument('--name')
#   → args = ...  # stored in memory
#   → print(?)
#   → parser = ...  # stored in memory
#   → parser.add_argument('--name')
#   → args = ...  # stored in memory
#   → print(?)

"""

"""
Problem 994:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main():  # defines a function with no parameters
    pass
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
main()  # function body runs with no arguments
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
text = ...  # assigns a value to the variable
sliced_text = ...  # assigns a value to the variable
print(sliced_text)
def main():  # stored in memory, not executed yet
main()  # calls main()
#   → pass
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → text = ...  # stored in memory
#   → sliced_text = ...  # stored in memory
#   → print(sliced_text)
#   → main()  # jumps into main(), runs body, returns

"""

"""
Problem 995:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    text = 'Programming'
    sliced_text = text[-4:]
    print(sliced_text)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
text = ...  # assigns a value to the variable
sliced_text = ...  # assigns a value to the variable
print(sliced_text)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
text = ...  # assigns a value to the variable
sliced_text = ...  # assigns a value to the variable
print(sliced_text)
text = ...  # assigns a value to the variable
sliced_text = ...  # assigns a value to the variable
print(sliced_text)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → text = ...  # stored in memory
#   → sliced_text = ...  # stored in memory
#   → print(sliced_text)
#   → text = ...  # stored in memory
#   → sliced_text = ...  # stored in memory
#   → print(sliced_text)
#   → text = ...  # stored in memory
#   → sliced_text = ...  # stored in memory
#   → print(sliced_text)

"""

"""
Problem 996:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    numbers = [10, 20, 30, 40, 50]
    sliced_list = numbers[2:]
    print(sliced_list)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
numbers = ...  # assigns a value to the variable
sliced_list = ...  # assigns a value to the variable
print(sliced_list)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
sliced_list = ...  # assigns a value to the variable
print(sliced_list)
numbers = ...  # assigns a value to the variable
sliced_list = ...  # assigns a value to the variable
print(sliced_list)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → sliced_list = ...  # stored in memory
#   → print(sliced_list)
#   → numbers = ...  # stored in memory
#   → sliced_list = ...  # stored in memory
#   → print(sliced_list)
#   → numbers = ...  # stored in memory
#   → sliced_list = ...  # stored in memory
#   → print(sliced_list)

"""

"""
Problem 997:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    numbers = [1, 2, 3, 4, 5, 6]
    sliced_list = numbers[-3:]
    print(sliced_list)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
numbers = ...  # assigns a value to the variable
sliced_list = ...  # assigns a value to the variable
print(sliced_list)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
numbers = ...  # assigns a value to the variable
sliced_list = ...  # assigns a value to the variable
print(sliced_list)
numbers = ...  # assigns a value to the variable
sliced_list = ...  # assigns a value to the variable
print(sliced_list)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → sliced_list = ...  # stored in memory
#   → print(sliced_list)
#   → numbers = ...  # stored in memory
#   → sliced_list = ...  # stored in memory
#   → print(sliced_list)
#   → numbers = ...  # stored in memory
#   → sliced_list = ...  # stored in memory
#   → print(sliced_list)

"""

"""
Problem 998:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    text = 'PythonSlicing'
    sliced_text = text[::2]
    print(sliced_text)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
text = ...  # assigns a value to the variable
sliced_text = ...  # assigns a value to the variable
print(sliced_text)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
text = ...  # assigns a value to the variable
sliced_text = ...  # assigns a value to the variable
print(sliced_text)
text = ...  # assigns a value to the variable
sliced_text = ...  # assigns a value to the variable
print(sliced_text)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → text = ...  # stored in memory
#   → sliced_text = ...  # stored in memory
#   → print(sliced_text)
#   → text = ...  # stored in memory
#   → sliced_text = ...  # stored in memory
#   → print(sliced_text)
#   → text = ...  # stored in memory
#   → sliced_text = ...  # stored in memory
#   → print(sliced_text)

"""

"""
Problem 999:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def main():  # defines a function with no parameters
    pass
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
main()  # function body runs with no arguments
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
text = ...  # assigns a value to the variable
sliced_text = ...  # assigns a value to the variable
print(sliced_text)
def main():  # stored in memory, not executed yet
main()  # calls main()
#   → pass
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → text = ...  # stored in memory
#   → sliced_text = ...  # stored in memory
#   → print(sliced_text)
#   → main()  # jumps into main(), runs body, returns

"""

"""
Problem 1000:
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
def solve():  # defines a function with no parameters
    text = 'abcdef'
    reversed_text = text[::-1]
    print(reversed_text)
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
text = ...  # assigns a value to the variable
reversed_text = ...  # assigns a value to the variable
print(reversed_text)
def solve():  # stored in memory, not executed yet
def solve():  # stored in memory, not executed yet
text = ...  # assigns a value to the variable
reversed_text = ...  # assigns a value to the variable
print(reversed_text)
text = ...  # assigns a value to the variable
reversed_text = ...  # assigns a value to the variable
print(reversed_text)
#
# EXECUTION FLOW:
# Execution Flow tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → text = ...  # stored in memory
#   → reversed_text = ...  # stored in memory
#   → print(reversed_text)
#   → text = ...  # stored in memory
#   → reversed_text = ...  # stored in memory
#   → print(reversed_text)
#   → text = ...  # stored in memory
#   → reversed_text = ...  # stored in memory
#   → print(reversed_text)

"""

