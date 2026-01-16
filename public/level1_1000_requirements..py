# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Bird with a method fly(). Create a derived class Penguin that overrides the fly() method to print “Cannot fly”.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 501
Create a base class Bird with a method fly(). Create a derived class Penguin that overrides the fly() method to print “Cannot fly”.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

class Bird:  # Base class definition
    def fly(self):  # Method: fly
        return "I can fly!"  # Return the result

class Penguin(Bird):  # Penguin inherits from Bird

    def fly(self):  # Method: fly
        return "Cannot fly"  # Return the result

generic_bird = Bird()
print(generic_bird.fly())

penguin = Penguin()
print(penguin.fly())

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Book with attributes title and author. Create a derived class EBook that adds an attribute file_size.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 502
Create a base class Book with attributes title and author. Create a derived class EBook that adds an attribute file_size.
"""

# SOLUTION EXPLANATION:
# This solution uses inheritance to extend a base class. The derived class
# inherits attributes from the base class using super().__init__() and adds
# additional attributes. This allows code reuse and follows the DRY principle.

class Book:  # Base class definition
    def __init__(self, title, author):  # Constructor: initializes instance attributes
        self.title = title
        self.author = author

class EBook(Book):  # EBook inherits from Book
    def __init__(self, title, author, file_size):  # Constructor: initializes instance attributes
        
        super().__init__(title, author)  # Call parent class constructor
    
        self.file_size = file_size

ebook = EBook("Python Programming", "John Doe", 2.5)
print(f"Title: {ebook.title}, Author: {ebook.author}, File Size: {ebook.file_size}MB")

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Instrument with a method play(). Create a derived class Guitar that overrides the play() method to print “Strum”.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 503
Create a base class Instrument with a method play(). Create a derived class Guitar that overrides the play() method to print “Strum”.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

class Instrument:  # Base class definition
    def play(self):  # Method: play
        return "Playing an instrument."  # Return the result

class Guitar(Instrument):  # Guitar inherits from Instrument
    def play(self):  # Method: play
        return "Strum"  # Return the result

generic_instrument = Instrument()
print(generic_instrument.play())

guitar = Guitar()
print(guitar.play())

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Game with a method start(). Create a derived class Chess that overrides the start() method to print “Start Chess”.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 504
Create a base class Game with a method start(). Create a derived class Chess that overrides the start() method to print “Start Chess”.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

class Game:  # Base class definition
    def start(self):  # Method: start
        return "Starting the game."  # Return the result

class Chess(Game):  # Chess inherits from Game

    def start(self):  # Method: start
        return "Start Chess"  # Return the result

generic_game = Game()
print(generic_game.start())

chess_game = Chess()
print(chess_game.start())

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Vehicle with a method drive(). Create a derived class Bicycle that overrides the drive() method to print “Pedal”.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 505
Create a base class Vehicle with a method drive(). Create a derived class Bicycle that overrides the drive() method to print “Pedal”.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

class Vehicle:  # Base class definition
    def drive(self):  # Method: drive
        return "Are you ready to drive?"  # Return the result

class Bicycle(Vehicle):  # Bicycle inherits from Vehicle

    def drive(self):  # Method: drive
        return "Pedal"  # Return the result

bicycle = Bicycle()
print(bicycle.drive())

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Computer with attributes brand and processor. Create a derived class Laptop that adds an attribute weight.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 506
Create a base class Computer with attributes brand and processor. Create a derived class Laptop that adds an attribute weight.
"""

# SOLUTION EXPLANATION:
# This solution uses inheritance to extend a base class. The derived class
# inherits attributes from the base class using super().__init__() and adds
# additional attributes. This allows code reuse and follows the DRY principle.

class Computer:  # Base class definition
    def __init__(self, brand, processor):  # Constructor: initializes instance attributes
        self.brand = brand
        self.processor = processor

class Laptop(Computer):  # Laptop inherits from Computer
    def __init__(self, brand, processor, weight):  # Constructor: initializes instance attributes
    
        super().__init__(brand, processor)  # Call parent class constructor
        
        self.weight = weight

laptop = Laptop("Dell", "Intel i7", 2.3)
print(f"Brand: {laptop.brand}, Processor: {laptop.processor}, Weight: {laptop.weight}kg")

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Device with a method turn_on(). Create a derived class Smartphone that adds an attribute apps.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 507
Create a base class Device with a method turn_on(). Create a derived class Smartphone that adds an attribute apps.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

class Device:  # Base class definition
    def turn_on(self):  # Method: turn_on
        return "Device is now on."  # Return the result

class Smartphone(Device):  # Smartphone inherits from Device
    def __init__(self, apps):  # Constructor: initializes instance attributes
        self.apps = apps


phone = Smartphone(["WhatsApp", "Instagram", "Spotify"])
print(phone.turn_on()) 
print(f"Installed apps: {', '.join(phone.apps)}")

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Parent with a method display(). Create a derived class Child that overrides the display() method to print “This is a child”.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 508
Create a base class Parent with a method display(). Create a derived class Child that overrides the display() method to print “This is a child”.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

class Parent:  # Base class definition
    def display(self):  # Method: display
        return "This is the parent."  # Return the result

class Child(Parent):  # Child inherits from Parent
    def display(self):  # Method: display
        return "This is a child"  # Return the result
        
parent = Parent()
print(parent.display()) 

child = Child()
print(child.display())

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Building with attributes floors and address. Create a derived class Skyscraper that adds an attribute height.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 509
Create a base class Building with attributes floors and address. Create a derived class Skyscraper that adds an attribute height.
"""

# SOLUTION EXPLANATION:
# This solution uses inheritance to extend a base class. The derived class
# inherits attributes from the base class using super().__init__() and adds
# additional attributes. This allows code reuse and follows the DRY principle.

class Building:  # Base class definition
    def __init__(self, floors, address):  # Constructor: initializes instance attributes
        self.floors = floors
        self.address = address

class Skyscraper(Building):  # Skyscraper inherits from Building
    def __init__(self, floors, address, height):  # Constructor: initializes instance attributes
        # Call the base class (Building) constructor to initialize floors and address
        super().__init__(floors, address)  # Call parent class constructor
        # Initialize the height attribute specific to Skyscraper
        self.height = height

skyscraper = Skyscraper(50, "123 High Street", 200)
print(f"Floors: {skyscraper.floors}, Address: {skyscraper.address}, Height: {skyscraper.height} meters")

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Plant with a method grow(). Create a derived class Flower that overrides the grow() method to print “Bloom”.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 510
Create a base class Plant with a method grow(). Create a derived class Flower that overrides the grow() method to print “Bloom”.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

class Plant:  # Base class definition
    def grow(self):  # Method: grow
        return "The plant is growing."  # Return the result

class Flower(Plant):  # Flower inherits from Plant
    
    def grow(self):  # Method: grow
        return "Bloom"  # Return the result

plant = Plant()
print(plant.grow())  # Output: The plant is growing.

flower = Flower()
print(flower.grow())  # Output: Bloom

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Teacher with attributes name and subject. Create a derived class MathTeacher that adds a method teach_math().
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 511
Create a base class Teacher with attributes name and subject. Create a derived class MathTeacher that adds a method teach_math().
"""

# SOLUTION EXPLANATION:
# This solution uses inheritance to extend a base class. The derived class
# inherits attributes from the base class using super().__init__() and adds
# additional attributes. This allows code reuse and follows the DRY principle.

class Teacher:  # Base class definition
    def __init__(self, name, subject):  # Constructor: initializes instance attributes
        self.name = name
        self.subject = subject

    def __str__(self):
        return f"Name: {self.name}, Subject: {self.subject}"  # Return the result


class MathTeacher(Teacher):  # MathTeacher inherits from Teacher
    def __init__(self, name):  # Constructor: initializes instance attributes
    
        super().__init__(name, "Math")  # Call parent class constructor

    def teach_math(self):  # Method: teach_math
        return "Teaching math concepts."  # Return the result

# Example usage
teacher = Teacher("John Doe", "Science")
print(teacher)  # Output: Name: John Doe, Subject: Science

math_teacher = MathTeacher("Alice Smith")
print(math_teacher)         # Output: Name: Alice Smith, Subject: Math
print(math_teacher.teach_math())  # Output: Teaching math concepts.

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Writer with attributes name and genre. Create a derived class Poet that overrides the genre attribute to “Poetry”.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 512
Create a base class Writer with attributes name and genre. Create a derived class Poet that overrides the genre attribute to “Poetry”.
"""

# SOLUTION EXPLANATION:
# This solution uses inheritance to extend a base class. The derived class
# inherits attributes from the base class using super().__init__() and adds
# additional attributes. This allows code reuse and follows the DRY principle.

class Writer:  # Base class definition
    def __init__(self, name, genre):  # Constructor: initializes instance attributes
        self.name = name
        self.genre = genre

    def __str__(self):
        return f"Name: {self.name}, Genre: {self.genre}"  # Return the result

class Poet(Writer):  # Poet inherits from Writer
    def __init__(self, name):  # Constructor: initializes instance attributes
        
        super().__init__(name, "Poetry")  # Call parent class constructor

# Example usage
writer = Writer("Jane Austen", "Fiction")
print(writer)  # Output: Name: Jane Austen, Genre: Fiction

poet = Poet("William Wordsworth")
print(poet)  # Output: Name: William Wordsworth, Genre: Poetry

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Appliance with a method use(). Create a derived class Oven that overrides the use() method to print “Bake”
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 513
Create a base class Appliance with a method use(). Create a derived class Oven that overrides the use() method to print “Bake”
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

class Appliance:  # Base class definition
    def use(self):  # Method: use
        return "Using the appliance."  # Return the result

# Derived class Oven that inherits from Appliance
class Oven(Appliance):  # Oven inherits from Appliance
    def use(self):  # Method: use
        return "Bake"  # Return the result

appliance = Appliance()
print(appliance.use())

oven = Oven()
print(oven.use())

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Artist with attributes name and medium. Create a derived class Painter that adds a method paint().
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 514
Create a base class Artist with attributes name and medium. Create a derived class Painter that adds a method paint().
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

# Base class Artist
class Artist:  # Base class definition
    def __init__(self, name, medium):  # Constructor: initializes instance attributes
        self.name = name
        self.medium = medium

    def __str__(self):
        return f"Name: {self.name}, Medium: {self.medium}"  # Return the result

# Derived class Painter that inherits from Artist
class Painter(Artist):  # Painter inherits from Artist
    def paint(self):  # Method: paint
        return "Painting with " + self.medium  # Return the result

# Example usage
artist = Artist("Claude Monet", "Watercolor")
print(artist)  # Output: Name: Claude Monet, Medium: Watercolor

painter = Painter("Vincent van Gogh", "Oil Paint")
print(painter)         # Output: Name: Vincent van Gogh, Medium: Oil Paint
print(painter.paint()) # Output: Painting with Oil Paint

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Worker with a method work(). Create a derived class Electrician that overrides the work() method to print “Fix wires”.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 515
Create a base class Worker with a method work(). Create a derived class Electrician that overrides the work() method to print “Fix wires”.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

# Base class Worker
class Worker:  # Base class definition
    def work(self):  # Method: work
        return "Working on general tasks."  # Return the result

# Derived class Electrician that inherits from Worker
class Electrician(Worker):  # Electrician inherits from Worker
    def work(self):  # Method: work
        return "Fix wires"  # Return the result

# Example usage
worker = Worker()
print(worker.work())  # Output: Working on general tasks.

electrician = Electrician()
print(electrician.work())  # Output: Fix wires

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Animal with a method eat(). Create a derived class Lion that overrides the eat() method to print “Eat meat”.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 516
Create a base class Animal with a method eat(). Create a derived class Lion that overrides the eat() method to print “Eat meat”.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

# Base class Animal
class Animal:  # Base class definition
    def eat(self):  # Method: eat
        return "Eating food."  # Return the result

# Derived class Lion that inherits from Animal
class Lion(Animal):  # Lion inherits from Animal
    def eat(self):  # Method: eat
        return "Eat meat"  # Return the result

# Example usage
animal = Animal()
print(animal.eat())  # Output: Eating food.

lion = Lion()
print(lion.eat())  # Output: Eat meat

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Appliance with a method run(). Create a derived class Fan that overrides the run() method to print “Spin blades”
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 517
Create a base class Appliance with a method run(). Create a derived class Fan that overrides the run() method to print “Spin blades”
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

# Base class Appliance
class Appliance:  # Base class definition
    def run(self):  # Method: run
        return "Running appliance."  # Return the result

# Derived class Fan that inherits from Appliance
class Fan(Appliance):  # Fan inherits from Appliance
    def run(self):  # Method: run
        return "Spin blades"  # Return the result

# Example usage
appliance = Appliance()
print(appliance.run())  # Output: Running appliance.

fan = Fan()
print(fan.run())  # Output: Spin blades

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Employee with a method get_salary(). Create a derived class Intern that overrides the get_salary() method to return a lower salary.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 518
Create a base class Employee with a method get_salary(). Create a derived class Intern that overrides the get_salary() method to return a lower salary.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

# Base class Employee
class Employee:  # Base class definition
    def get_salary(self):  # Method: get_salary
        return 5000  # Example salary for a general employee  # Return the result

# Derived class Intern that inherits from Employee
class Intern(Employee):  # Intern inherits from Employee
    def get_salary(self):  # Method: get_salary
        return 2000  # Example lower salary for an intern  # Return the result

# Example usage
employee = Employee()
print(f"Employee Salary: ${employee.get_salary()}")  # Output: Employee Salary: $5000

intern = Intern()
print(f"Intern Salary: ${intern.get_salary()}")  # Output: Intern Salary: $2000

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Vehicle with an attribute wheels. Create a derived class Motorcycle that overrides wheels to 2.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 519
Create a base class Vehicle with an attribute wheels. Create a derived class Motorcycle that overrides wheels to 2.
"""

# SOLUTION EXPLANATION:
# This solution uses inheritance to extend a base class. The derived class
# inherits attributes from the base class using super().__init__() and adds
# additional attributes. This allows code reuse and follows the DRY principle.

# Base class Vehicle
class Vehicle:  # Base class definition
    def __init__(self, wheels):  # Constructor: initializes instance attributes
        self.wheels = wheels

    def __str__(self):
        return f"Wheels: {self.wheels}"  # Return the result

# Derived class Motorcycle that inherits from Vehicle
class Motorcycle(Vehicle):  # Motorcycle inherits from Vehicle
    def __init__(self):  # Constructor: initializes instance attributes
        # Initialize the base class (Vehicle) with wheels set to 2
        super().__init__(2)  # Call parent class constructor

# Example usage
vehicle = Vehicle(4)  # Example with a generic vehicle
print(vehicle)  # Output: Wheels: 4

motorcycle = Motorcycle()
print(motorcycle)  # Output: Wheels: 2

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Tool with a method use(). Create a derived class Hammer that overrides the use() method to print “Hammer nails”.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 520
Create a base class Tool with a method use(). Create a derived class Hammer that overrides the use() method to print “Hammer nails”.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

# Base class Tool
class Tool:  # Base class definition
    def use(self):  # Method: use
        return "Using the tool."  # Return the result

# Derived class Hammer that inherits from Tool
class Hammer(Tool):  # Hammer inherits from Tool
    def use(self):  # Method: use
        return "Hammer nails"  # Return the result

# Example usage
tool = Tool()
print(tool.use())  # Output: Using the tool.

hammer = Hammer()
print(hammer.use())  # Output: Hammer nails

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class BankAccount with attributes balance and owner. Create a derived class SavingsAccount that adds an attribute interest_rate.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 521
Create a base class BankAccount with attributes balance and owner. Create a derived class SavingsAccount that adds an attribute interest_rate.
"""

# SOLUTION EXPLANATION:
# This solution uses inheritance to extend a base class. The derived class
# inherits attributes from the base class using super().__init__() and adds
# additional attributes. This allows code reuse and follows the DRY principle.

# Base class BankAccount
class BankAccount:  # Base class definition
    def __init__(self, balance, owner):  # Constructor: initializes instance attributes
        self.balance = balance
        self.owner = owner

    def __str__(self):
        return f"Owner: {self.owner}, Balance: ${self.balance}"  # Return the result

# Derived class SavingsAccount that inherits from BankAccount
class SavingsAccount(BankAccount):  # SavingsAccount inherits from BankAccount
    def __init__(self, balance, owner, interest_rate):  # Constructor: initializes instance attributes
        # Initialize base class (BankAccount) with balance and owner
        super().__init__(balance, owner)  # Call parent class constructor
        self.interest_rate = interest_rate

    def __str__(self):
        return f"Owner: {self.owner}, Balance: ${self.balance}, Interest Rate: {self.interest_rate}%"  # Return the result

# Example usage
account = BankAccount(1000, "Alice")
print(account)  # Output: Owner: Alice, Balance: $1000

savings = SavingsAccount(1500, "Bob", 2.5)
print(savings)  # Output: Owner: Bob, Balance: $1500, Interest Rate: 2.5%

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Weapon with a method attack(). Create a derived class Sword that overrides the attack() method to print “Slash”.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 522
Create a base class Weapon with a method attack(). Create a derived class Sword that overrides the attack() method to print “Slash”.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

# Base class Weapon
class Weapon:  # Base class definition
    def attack(self):  # Method: attack
        return "Weapon attack"  # Return the result

# Derived class Sword that inherits from Weapon
class Sword(Weapon):  # Sword inherits from Weapon
    def attack(self):  # Method: attack
        return "Slash"  # Return the result

# Example usage
weapon = Weapon()
print(weapon.attack())  # Output: Weapon attack

sword = Sword()
print(sword.attack())  # Output: Slash

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Appliance with an attribute power. Create a derived class Microwave that adds a method heat_food().
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 523
Create a base class Appliance with an attribute power. Create a derived class Microwave that adds a method heat_food().
"""

# SOLUTION EXPLANATION:
# This solution uses inheritance to extend a base class. The derived class
# inherits attributes from the base class using super().__init__() and adds
# additional attributes. This allows code reuse and follows the DRY principle.

# Base class Appliance
class Appliance:  # Base class definition
    def __init__(self, power):  # Constructor: initializes instance attributes
        self.power = power

    def __str__(self):
        return f"Power: {self.power} watts"  # Return the result

# Derived class Microwave that inherits from Appliance
class Microwave(Appliance):  # Microwave inherits from Appliance
    def __init__(self, power):  # Constructor: initializes instance attributes
        # Initialize the base class (Appliance) with power
        super().__init__(power)  # Call parent class constructor

    def heat_food(self):  # Method: heat_food
        return "Heating food"  # Return the result

# Example usage
appliance = Appliance(1500)  # Example with an appliance
print(appliance)  # Output: Power: 1500 watts

microwave = Microwave(1200)
print(microwave)  # Output: Power: 1200 watts
print(microwave.heat_food())  # Output: Heating food

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Vehicle with a method start(). Create a derived class ElectricCar that overrides the start() method to print “Silent start”.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 524
Create a base class Vehicle with a method start(). Create a derived class ElectricCar that overrides the start() method to print “Silent start”.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

# Base class Vehicle
class Vehicle:  # Base class definition
    def start(self):  # Method: start
        return "Starting vehicle"  # Return the result

# Derived class ElectricCar that inherits from Vehicle
class ElectricCar(Vehicle):  # ElectricCar inherits from Vehicle
    def start(self):  # Method: start
        return "Silent start"  # Return the result

# Example usage
vehicle = Vehicle()
print(vehicle.start())  # Output: Starting vehicle

electric_car = ElectricCar()
print(electric_car.start())  # Output: Silent start

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Pet with a method make_sound(). Create a derived class Cat that overrides the make_sound() method to print “Meow”.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 525
Create a base class Pet with a method make_sound(). Create a derived class Cat that overrides the make_sound() method to print “Meow”.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

# Base class Pet
class Pet:  # Base class definition
    def make_sound(self):  # Method: make_sound
        return "Some generic pet sound"  # Return the result

# Derived class Cat that inherits from Pet
class Cat(Pet):  # Cat inherits from Pet
    def make_sound(self):  # Method: make_sound
        return "Meow"  # Return the result

# Example usage
pet = Pet()
print(pet.make_sound())  # Output: Some generic pet sound

cat = Cat()
print(cat.make_sound())  # Output: Meow

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Chef with a method cook(). Create a derived class PastryChef that overrides the cook() method to print “Bake cake”.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 526
Create a base class Chef with a method cook(). Create a derived class PastryChef that overrides the cook() method to print “Bake cake”.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

# Base class Chef
class Chef:  # Base class definition
    def cook(self):  # Method: cook
        return "Cook food"  # Return the result

# Derived class PastryChef that inherits from Chef
class PastryChef(Chef):  # PastryChef inherits from Chef
    def cook(self):  # Method: cook
        return "Bake cake"  # Return the result

# Example usage
chef = Chef()
print(chef.cook())  # Output: Cook food

pastry_chef = PastryChef()
print(pastry_chef.cook())  # Output: Bake cake

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Furniture with attributes material and color. Create a derived class Chair that adds an attribute legs.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 527
Create a base class Furniture with attributes material and color. Create a derived class Chair that adds an attribute legs.
"""

# SOLUTION EXPLANATION:
# This solution uses inheritance to extend a base class. The derived class
# inherits attributes from the base class using super().__init__() and adds
# additional attributes. This allows code reuse and follows the DRY principle.

def create_chair(material, color, legs):  # Method: create_chair
    class Furniture:  # Base class definition
        def __init__(self, material, color):  # Constructor: initializes instance attributes
            self.material = material
            self.color = color

    class Chair(Furniture):  # Chair inherits from Furniture
        def __init__(self, material, color, legs):  # Constructor: initializes instance attributes
            super().__init__(material, color)  # Call parent class constructor
            self.legs = legs

    return Chair(material, color, legs)  # Return the result

my_chair = create_chair("wood", "brown", 4)

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Game with an attribute players. Create a derived class Soccer that overrides the players attribute to 22.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 528
Create a base class Game with an attribute players. Create a derived class Soccer that overrides the players attribute to 22.
"""

# SOLUTION EXPLANATION:
# This solution uses inheritance to extend a base class. The derived class
# inherits attributes from the base class using super().__init__() and adds
# additional attributes. This allows code reuse and follows the DRY principle.

# Base class Game
class Game:  # Base class definition
    def __init__(self, players):  # Constructor: initializes instance attributes
        self.players = players

    def __str__(self):
        return f"Players: {self.players}"  # Return the result

# Derived class Soccer that inherits from Game
class Soccer(Game):  # Soccer inherits from Game
    def __init__(self):  # Constructor: initializes instance attributes
        # Initialize the base class with the specific number of players for Soccer
        super().__init__(players=22)  # Call parent class constructor

# Example usage
game = Game(10)
print(game)  # Output: Players: 10

soccer = Soccer()
print(soccer)  # Output: Players: 22

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Musician with a method play_instrument(). Create a derived class Pianist that overrides the play_instrument() method to print “Play piano”.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 529
Create a base class Musician with a method play_instrument(). Create a derived class Pianist that overrides the play_instrument() method to print “Play piano”.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

# Base class Musician
class Musician:  # Base class definition
    def play_instrument(self):  # Method: play_instrument
        return "Play instrument"  # Return the result

# Derived class Pianist that inherits from Musician
class Pianist(Musician):  # Pianist inherits from Musician
    def play_instrument(self):  # Method: play_instrument
        return "Play piano"  # Return the result

# Example usage
musician = Musician()
print(musician.play_instrument())  # Output: Play instrument

pianist = Pianist()
print(pianist.play_instrument())  # Output: Play piano

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Company with attributes name and location. Create a derived class TechCompany that adds an attribute products.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 530
Create a base class Company with attributes name and location. Create a derived class TechCompany that adds an attribute products.
"""

# SOLUTION EXPLANATION:
# This solution uses inheritance to extend a base class. The derived class
# inherits attributes from the base class using super().__init__() and adds
# additional attributes. This allows code reuse and follows the DRY principle.

# Base class Company
class Company:  # Base class definition
    def __init__(self, name, location):  # Constructor: initializes instance attributes
        self.name = name
        self.location = location

    def __str__(self):
        return f"Name: {self.name}, Location: {self.location}"  # Return the result

# Derived class TechCompany that inherits from Company
class TechCompany(Company):  # TechCompany inherits from Company
    def __init__(self, name, location, products):  # Constructor: initializes instance attributes
        # Initialize the base class (Company) with name and location
        super().__init__(name, location)  # Call parent class constructor
        self.products = products

    def __str__(self):
        # Extend the base class string representation to include products
        return f"Name: {self.name}, Location: {self.location}, Products: {', '.join(self.products)}"  # Return the result

# Example usage
company = Company("Global Corp", "New York")
print(company)  # Output: Name: Global Corp, Location: New York

tech_company = TechCompany("Tech Innovators", "San Francisco", ["Smartphone", "Laptop", "Tablet"])
print(tech_company)  # Output: Name: Tech Innovators, Location: San Francisco, Products: Smartphone, Laptop, Tablet

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Gadget with a method operate(). Create a derived class Smartwatch that adds an attribute heart_rate_monitor.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 531
Create a base class Gadget with a method operate(). Create a derived class Smartwatch that adds an attribute heart_rate_monitor.
"""

# SOLUTION EXPLANATION:
# This solution uses inheritance to extend a base class. The derived class
# inherits attributes from the base class using super().__init__() and adds
# additional attributes. This allows code reuse and follows the DRY principle.

# Base class Gadget
class Gadget:  # Base class definition
    def operate(self):  # Method: operate
        return "Operate gadget"  # Return the result

# Derived class Smartwatch that inherits from Gadget
class Smartwatch(Gadget):  # Smartwatch inherits from Gadget
    def __init__(self, heart_rate_monitor):  # Constructor: initializes instance attributes
        # Initialize the base class (Gadget)
        super().__init__()  # Call parent class constructor
        self.heart_rate_monitor = heart_rate_monitor

    def __str__(self):
        # Provide a string representation of the Smartwatch
        return f"Heart Rate Monitor: {'Enabled' if self.heart_rate_monitor else 'Disabled'}"  # Return the result

# Example usage
gadget = Gadget()
print(gadget.operate())  # Output: Operate gadget

smartwatch = Smartwatch(heart_rate_monitor=True)
print(smartwatch.operate())  # Output: Operate gadget
print(smartwatch)           # Output: Heart Rate Monitor: Enabled

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Trainer with a method train(). Create a derived class FitnessTrainer that overrides the train() method to print “Train body”.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 532
Create a base class Trainer with a method train(). Create a derived class FitnessTrainer that overrides the train() method to print “Train body”.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

# Base class Trainer
class Trainer:  # Base class definition
    def train(self):  # Method: train
        return "Training session"  # Return the result

# Derived class FitnessTrainer that inherits from Trainer
class FitnessTrainer(Trainer):  # FitnessTrainer inherits from Trainer
    def train(self):  # Method: train
        print("Train body")

# Example usage
trainer = Trainer()
print(trainer.train())  # Output: Training session

fitness_trainer = FitnessTrainer()
fitness_trainer.train()  # Output: Train body

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Book with a method read(). Create a derived class ComicBook that overrides the read() method to print “Read with pictures”.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 533
Create a base class Book with a method read(). Create a derived class ComicBook that overrides the read() method to print “Read with pictures”.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

# Base class Book
class Book:  # Base class definition
    def read(self):  # Method: read
        return "Read the book"  # Return the result

# Derived class ComicBook that inherits from Book
class ComicBook(Book):  # ComicBook inherits from Book
    def read(self):  # Method: read
        print("Read with pictures")

# Example usage
book = Book()
print(book.read())  # Output: Read the book

comic_book = ComicBook()
comic_book.read()  # Output: Read with pictures

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a base class Software with attributes name and version. Create a derived class GameSoftware that adds an attribute genre.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 534
Create a base class Software with attributes name and version. Create a derived class GameSoftware that adds an attribute genre.
"""

# SOLUTION EXPLANATION:
# This solution uses inheritance to extend a base class. The derived class
# inherits attributes from the base class using super().__init__() and adds
# additional attributes. This allows code reuse and follows the DRY principle.

# Base class Software
class Software:  # Base class definition
    def __init__(self, name, version):  # Constructor: initializes instance attributes
        self.name = name
        self.version = version

    def __str__(self):
        return f"Name: {self.name}, Version: {self.version}"  # Return the result

# Derived class GameSoftware that inherits from Software
class GameSoftware(Software):  # GameSoftware inherits from Software
    def __init__(self, name, version, genre):  # Constructor: initializes instance attributes
        # Initialize the base class (Software) with name and version
        super().__init__(name, version)  # Call parent class constructor
        self.genre = genre

    def __str__(self):
        # Extend the base class string representation to include genre
        return f"Name: {self.name}, Version: {self.version}, Genre: {self.genre}"  # Return the result

# Example usage
software = Software("BasicApp", "1.0")
print(software)  # Output: Name: BasicApp, Version: 1.0

game_software = GameSoftware("EpicQuest", "2.5", "RPG")
print(game_software)  # Output: Name: EpicQuest, Version: 2.5, Genre: RPG

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count the number of times the letter ‘a’ appears in a string. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 535
Write a Python program to count the number of times the letter ‘a’ appears in a string. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_letter(s):  # Method: count_letter
    return s.count("a")  # Return the result
    
string = "what going on today"
print(count_letter(string))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function to count the occurrences of the number 5 in a list of integers. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 536
Write a Python function to count the occurrences of the number 5 in a list of integers. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_number(num):  # Method: count_number
    return num.count(5)  # Return the result

number = [3, 5, 5, 35, 78]
print(count_number(number))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count how many times the word “hello” appears in a sentence. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 537
Write a Python program to count how many times the word “hello” appears in a sentence. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_hello(string):  # Method: count_hello
    return string.count("hello")  # Return the result
    
string = "hello, you cunt"
print(count_hello(string))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that counts how many times the character # appears in a string.  Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 538
Write a function that counts how many times the character # appears in a string.  Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count(string):  # Method: count
    return string.count("#")  # Return the result
    
string = "hello, you cunt ###"
print(count(string))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count the occurrences of the substring “cat” in a given string. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 539
Write a Python program to count the occurrences of the substring “cat” in a given string. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_substring(s, substring="cat"):  # Method: count_substring
    return s.count(substring)  # Return the result

input_string = "The cat sat on the mat with another cat."
count = count_substring(input_string)
print(f"The substring 'cat' occurs {count} times.")

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function to count how many times the digit 0 appears in a list of numbers. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 540
Write a Python function to count how many times the digit 0 appears in a list of numbers. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_number(num):  # Method: count_number
    return num.count(0)  # Return the result
    
num = [3, 5, 0, 0, 6, 0]
print(count_number(num))

def main(lst):  # Method: main
    total = 0
    for num in lst:
        total += str(num).count('0')
    print(total)

lst = [56700, 40, 0, 0, 570]
main(lst)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program to count the number of spaces in a given string. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 541
Write a program to count the number of spaces in a given string. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_spaces(string):  # Method: count_spaces
    return string.count(" ")  # Return the result
    
num = "i'm going for a walk today"
print(count_spaces(num))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function to count the occurrences of a specific character in a string provided by the user. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 542
Write a Python function to count the occurrences of a specific character in a string provided by the user. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_occurrences():  # Method: count_occurrences
    user_input = input("Type a sentence: ")
    
    char_to_count = input("Enter the character to count: ")
    
    if len(char_to_count) != 1:
        print("Please enter exactly one character.")
        return
    
    count = user_input.count(char_to_count)
    
    print(f"The character '{char_to_count}' occurs {count} times.")

count_occurrences()

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count how many times a specific word appears in a text file. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 543
Write a Python program to count how many times a specific word appears in a text file. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_word_in_file(filename, word):  # Method: count_word_in_file
    try:  # Begin exception handling
        # Open the file and read its content
        with open(filename, 'r') as file:
            content = file.read()
        
        # Count the occurrences of the specified word
        word_count = content.count(word)
        
        return word_count  # Return the result
    except FileNotFoundError:  # Handle exception
        print(f"The file '{filename}' does not exist.")
        return 0  # Return the result

# Example usage
filename = 'example.txt'  # Replace with your actual file name
word_to_count = 'the'     # Replace with the word you want to count
count = count_word_in_file(filename, word_to_count)
print(f"The word '{word_to_count}' appears {count} times in the file.")

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function to count how many times the letter ‘e’ appears in a list of strings. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 544
Write a function to count how many times the letter ‘e’ appears in a list of strings. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_letters(lst):  # Method: count_letters
    total_count = 0
    
    for word in lst:
        total_count += word.count("e")
    return total_count  # Return the result

lst = ["Jonathen", "Nathan", "Netesha"]
print(count_letters(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count the number of times a certain element appears in a list of mixed types. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 545
Write a Python program to count the number of times a certain element appears in a list of mixed types. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_elements_in_lst(lst, element):  # Method: count_elements_in_lst
    return lst.count(element)  # Return the result

# Example usage
lst = ["tree", "sea", 42, "world", "sea", 42, 42]
element = 42  # Element to count
print(count_elements_in_lst(lst, element))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function to count the occurrences of the string “test” in a string where multiple “test” substrings might exist. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 546
Write a function to count the occurrences of the string “test” in a string where multiple “test” substrings might exist. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_test_occurrences(s):  # Method: count_test_occurrences
    return s.count("test")  # Return the result

s = "This is a test. Test the function with another test. Final test."
print(count_test_occurrences(s))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count how many times a specific number occurs in a list of floating-point numbers. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 547
Write a Python program to count how many times a specific number occurs in a list of floating-point numbers. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_floating_numbers(lst):  # Method: count_floating_numbers
    return float(lst.count())  # Return the result
    
lst = [2.3, 5, 6.3, 78, 0.6]
print(count_floating_numbers(lst))

def main(lst):  # Method: main
    result = []
    for num in lst:
        if isinstance(num, float):
            lst.count(num)
            result.append(num)
    return result  # Return the result
    
lst = [2.66, 67, 45556.67, 7888, 1]

main(lst)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function to count the number of vowels (a, e, i, o, u) in a given string. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 548
Write a function to count the number of vowels (a, e, i, o, u) in a given string. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_floating_numbers(lst, number):  # Method: count_floating_numbers
    return lst.count(number)  # Return the result

lst = [2.3, 5.0, 6.3, 78.0, 0.6, 5.0]
number = 5.0
print(count_floating_numbers(lst, number))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count the number of uppercase letters in a string. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 549
Write a Python program to count the number of uppercase letters in a string. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_uppercase(string):  # Method: count_uppercase
    total_uppercase = 0
    
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        total_uppercase += string.count(char)
    return total_uppercase  # Return the result

string = "AFHHJJ ghgghh"
print(count_uppercase(string))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that counts the occurrences of a specified digit in a number. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 550
Write a function that counts the occurrences of a specified digit in a number. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_digit(num):  # Method: count_digit
    num = str(num)
    return num.count("2")  # Return the result

num = 1223452
print(count_digit(num))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count how many times each letter appears in a given string. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 551
Write a Python program to count how many times each letter appears in a given string. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_letters(string):  # Method: count_letters
    letter_count = {}
    for letter in string.lower():
        letter_count[letter] = string.lower().count(letter)
    return letter_count  # Return the result

string = input("Enter a string: ")
print(count_letters(string))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function to count the number of times the word “Python” appears in a paragraph of text. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 552
Write a function to count the number of times the word “Python” appears in a paragraph of text. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_text(string):  # Method: count_text
    string = string.lower()
    
    return string.count("python")  # Return the result

string = "python is python in disguise"
print(count_text(string))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count the occurrences of a specific item in a list of dictionaries. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 553
Write a Python program to count the occurrences of a specific item in a list of dictionaries. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_item_in_dict_list(dict_list, item):  # Method: count_item_in_dict_list
    values = []
    
    for d in dict_list:
    
        for val in d.values():
            values.append(val)

    return values.count(item)  # Return the result

dict_list = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Charlie", "age": 35}
]

item = "Alice" 
print(count_item_in_dict_list(dict_list, item))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function to count how many times the letter ‘z’ appears in a list of strings. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 554
Write a function to count how many times the letter ‘z’ appears in a list of strings. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_letters(lst):  # Method: count_letters
    total_count = 0
    for string in lst:
        total_count += string.count("z")
    return total_count  # Return the result

lst = ["z", "h", "z", "gloat"]
print(count_letters(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count the occurrences of the character ‘*’ in a given string. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 555
Write a Python program to count the occurrences of the character ‘*’ in a given string. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_asterisks(s):  # Method: count_asterisks
    return s.count('*')  # Return the result

s = "Hello *world* and *everyone*"
print(count_asterisks(s))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function to count how many times the substring “123” appears in a string. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 556
Write a function to count how many times the substring “123” appears in a string. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_substring(s, substring):  # Method: count_substring
    return s.count(substring)  # Return the result

s = "123abc123def123"
substring = "123"
print(count_substring(s, substring))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count the number of lines in a text file that contain the word “error”. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 557
Write a Python program to count the number of lines in a text file that contain the word “error”. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_lines_with_word(filename, word):  # Method: count_lines_with_word
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if line.lower().count(word.lower()) > 0:
                count += 1
    return count  # Return the result

filename = 'example.txt'  # Replace with your actual file path
word = 'error'
print(count_lines_with_word(filename, word))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function to count the number of times a particular email domain appears in a list of email addresses. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 558
Write a function to count the number of times a particular email domain appears in a list of email addresses. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_email_domain(email_list, domain):  # Method: count_email_domain
    
    count = 0
    for email in email_list:
    
        email_domain = email.split('@')[-1]
        
        if email_domain == domain:
            count += 1
            
    return count  # Return the result

email_list = [
    "user1@example.com",
    "user2@example.com",
    "user3@sample.com",
    "user4@example.com"
]
domain = "example.com"
print(count_email_domain(email_list, domain))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count the occurrences of the word “happy” in a given list of sentences. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 559
Write a Python program to count the occurrences of the word “happy” in a given list of sentences. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_word(sentences):  # Method: count_word
    count = 0
    for sentence in sentences:
        count += sentence.count("happy")
    return count  # Return the result

sentences = ["I am happy today", "She looks very happy", "Happy times are here", "joy joy happy happy"]
print(count_word(sentences))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function to count the number of times the character ‘!’ appears in a list of strings. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 560
Write a function to count the number of times the character ‘!’ appears in a list of strings. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_exclamations(lst):  # Method: count_exclamations
    count = 0
    for string in lst:
        count += string.count('!')
    return count  # Return the result

lst = ["Hello!", "Wow! Amazing!", "No exclamation here", "Yes!"]
print(count_exclamations(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count the number of occurrences of a specific phrase in a block of text. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 561
Write a Python program to count the number of occurrences of a specific phrase in a block of text. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_phrase_occurrences(text, phrase):  # Method: count_phrase_occurrences
    return text.count(phrase)  # Return the result

text = """The quick brown fox jumps over the lazy dog. The fox is quick and clever.
Quick thinking by the fox saved the day. Foxes are known to be quick and agile."""
phrase = "quick"
print(count_phrase_occurrences(text, phrase))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function to count the number of occurrences of a word in a list of words. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 562
Write a function to count the number of occurrences of a word in a list of words. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_word_occurrences(lst, word):  # Method: count_word_occurrences
    return lst.count(word)  # Return the result

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_to_count = "apple"
print(count_word_occurrences(words, word_to_count))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count how many times the letter ‘x’ appears in a list of mixed data types. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 563
Write a Python program to count how many times the letter ‘x’ appears in a list of mixed data types. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_x_in_mixed_list(lst):  # Method: count_x_in_mixed_list
    count = 0
    for item in lst:

        if isinstance(item, str):
            count += item.count('x')
    return count  # Return the result

mixed_list = [1, "xylophone", 3.5, "example", "box", 7, "text", ["x", "x"], "extra"]
print(count_x_in_mixed_list(mixed_list))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function to count the occurrences of a specific letter in a string and return a formatted message with the result. Use count().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 564
Write a function to count the occurrences of a specific letter in a string and return a formatted message with the result. Use count().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_letter_occurrences(string, letter):  # Method: count_letter_occurrences
    count = string.count(letter)
    
    return f"The letter '{letter}' appears {count} times in the given string."  # Return the result

text = "This is an example sentence with several letters."
letter_to_count = "e"
print(count_letter_occurrences(text, letter_to_count))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Square List Elements: Write a function that takes a list of numbers and returns a list of their squares using map().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 565
Square List Elements: Write a function that takes a list of numbers and returns a list of their squares using map().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def square_lst(lst):  # Method: square_lst
    return list(map(square, lst))  # Return the result

def square(num):  # Method: square
    return num ** 2  # Return the result

lst = [2, 4, 6, 8]
print(square_lst(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Filter Odd Numbers: Write a function that takes a list of numbers and returns only the odd numbers using filter().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 566
Filter Odd Numbers: Write a function that takes a list of numbers and returns only the odd numbers using filter().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def filter_odd_numbers(lst):  # Method: filter_odd_numbers
    return list(filter(is_odd, lst))  # Return the result

def is_odd(x):  # Method: is_odd
    return x % 2 != 0  # Return the result

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(filter_odd_numbers(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Filter Even Numbers: Write a function that filters all even numbers from a list using filter().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 567
Filter Even Numbers: Write a function that filters all even numbers from a list using filter().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def filters_even_numbers(lst):  # Method: filters_even_numbers
    return list(filter(even_num, lst))  # Return the result

def even_num(num):  # Method: even_num
    if num % 2 != 0:
        return num  # Return the result

lst = [4, 67, 2, 78, 3, 1, 466, 7]
print(filters_even_numbers(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Convert to Uppercase: Write a function that takes a list of strings and returns the same list with each string converted to uppercase using map().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 568
Convert to Uppercase: Write a function that takes a list of strings and returns the same list with each string converted to uppercase using map().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def convert_to_uppercase(lst):  # Method: convert_to_uppercase
    return list(map(str.upper, lst))  # Return the result

lst = ["sleep", "walk", "eat"]    
print(convert_to_uppercase(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Remove Empty Strings: Write a function that filters out empty strings from a list using filter().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 569
Remove Empty Strings: Write a function that filters out empty strings from a list using filter().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def empty_strings(lst):  # Method: empty_strings
    return list(filter(call_filter, lst))  # Return the result
    
def call_filter(string):  # Method: call_filter
    return string.strip() != ""  # Return the result
    
lst = ["dog", "  ", "cat"]    
print(empty_strings(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Multiply List Elements: Write a function that takes a list of numbers and returns a list where each number is multiplied by 5 using map().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 570
Multiply List Elements: Write a function that takes a list of numbers and returns a list where each number is multiplied by 5 using map().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def multiply_lst(lst):  # Method: multiply_lst
    
    def multiply_by_five(x):  # Method: multiply_by_five
        return x * 5  # Return the result
    
    return list(map(multiply_by_five, lst))  # Return the result

lst = [2, 5, 20]
print(multiply_lst(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# String Lengths: Write a function that takes a list of strings and returns their lengths using map().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 571
String Lengths: Write a function that takes a list of strings and returns their lengths using map().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_of_string(lst):  # Method: lst_of_string
    
    def len_string(word):  # Method: len_string
        return len(word)  # Return the result
    return list(map(len_string, lst))  # Return the result
        
lst = ["hot", "cold", "giraffe"]
print(lst_of_string(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Filter Palindromes: Write a function that filters out palindromes (words that read the same backward) from a list using filter().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 572
Filter Palindromes: Write a function that filters out palindromes (words that read the same backward) from a list using filter().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def palindromes(lst):  # Method: palindromes
    
    def filter_palindrome(word):  # Method: filter_palindrome
        if word != word[::-1]:
            return word  # Return the result
            
    return list(filter(filter_palindrome, lst))  # Return the result
               
lst = ["radar", "red", "blue", "level", "noon"]
print(palindromes(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Sum of List: Write a function that calculates the sum of a list of numbers using reduce().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 573
Sum of List: Write a function that calculates the sum of a list of numbers using reduce().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

from functools import reduce

def sum_of_lst(lst):  # Method: sum_of_lst
    
    def add(x, y):  # Method: add
        return x + y  # Return the result
        
    return reduce(add, lst)  # Return the result

lst = [1, 2, 3, 4, 5]
print(sum_of_list(lst))

def add(x, y):  # Method: add
    return x + y  # Return the result

def sum_of_list(lst):  # Method: sum_of_list
    return reduce(add, lst)  # Return the result

lst = [1, 2, 3, 4, 5]
print(sum_of_list(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Product of List: Write a function that computes the product of a list of numbers using reduce().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 574
Product of List: Write a function that computes the product of a list of numbers using reduce().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

from functools import reduce

def sum_of_lst(lst):  # Method: sum_of_lst
    
    def add(x, y):  # Method: add
        return x * y  # Return the result
        
    return reduce(add, lst)  # Return the result

lst = [1, 2, 3, 4, 5]
print(sum_of_list(lst))

def multiply(x, y):  # Method: multiply
    return x * y  # Return the result

def product_of_list(lst):  # Method: product_of_list
    return reduce(multiply, lst)  # Return the result

lst = [1, 2, 3, 4, 5]
print(product_of_list(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Capitalize Strings: Write a function that takes a list of strings and returns the list with each string capitalized using map().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 575
Capitalize Strings: Write a function that takes a list of strings and returns the list with each string capitalized using map().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def capitalize_string(lst):  # Method: capitalize_string
    return list(map(str.capitalize, lst))  # Return the result
    
lst = ["sam","ion", "kon"]
capitalize_string(lst)

def lst_strings(lst):  # Method: lst_strings
    
    def capitalize_lst(word):  # Method: capitalize_lst
        word = word.capitalize()
        return word  # Return the result
        
    return list(map(capitalize_lst, lst))  # Return the result
    
    
lst = ["today", "hello", "sunshine"]
print(lst_strings(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Find Minimum: Write a function that finds the minimum number in a list using reduce().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 576
Find Minimum: Write a function that finds the minimum number in a list using reduce().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

from functools import reduce

def min_number(x, y):  # Method: min_number
    return x if x < y else y  # Return the result

def number_lst(lst):  # Method: number_lst
    return reduce(min_number, lst)  # Return the result

lst = [34, 67, 1, 778]    
print(number_lst(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Find Maximum: Write a function that finds the maximum number in a list using reduce(). (hint helper function)
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 577
Find Maximum: Write a function that finds the maximum number in a list using reduce(). (hint helper function)
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

from functools import reduce

def find_max(lst):  # Method: find_max
    def inner(x, y):  # Method: inner
        if x > y:
            return x  # Return the result
        else:
            return y  # Return the result
    
    return reduce(inner, lst)  # Return the result

# Test the function
lst = [567, 4, 1, 57]
print(find_max(lst))  # Output: 567

def main(lst):  # Method: main
    return reduce(max_num, lst)  # Return the result

def max_num(x, y):  # Method: max_num
    if x > y:
        return x  # Return the result
    return y  # Return the result
    
lst = [567, 4, 100000, 57]
main(lst)

from functools import reduce

def min_number(x, y):  # Method: min_number
    return x if x > y else y  # Return the result

def number_lst(lst):  # Method: number_lst
    return reduce(min_number, lst)  # Return the result

lst = [34, 67, 1, 778]    
print(number_lst(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Filter Short Words: Write a function that filters out words shorter than 4 characters from a list using filter().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 578
Filter Short Words: Write a function that filters out words shorter than 4 characters from a list using filter().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def list_words(lst):  # Method: list_words
    
    def filter_word(word):  # Method: filter_word
        if len(word) > 3:
            return word  # Return the result
            
    return list(filter(filter_word, lst))  # Return the result
    
    
lst = ["bot", "not", "boat", "chop"]    
print(list_words(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Concatenate Strings: Write a function that concatenates all strings in a list using reduce().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 579
Concatenate Strings: Write a function that concatenates all strings in a list using reduce().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

from functools import reduce

def lst_strings(lst):  # Method: lst_strings
    
    def concatenate_lst(x, y):  # Method: concatenate_lst
        return x + y  # Return the result
        
    return reduce(concatenate_lst, lst)  # Return the result
    

lst = ["to", "day", "is", "great"]    
print(lst_strings(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Filter Positive Numbers: Write a function that filters only positive numbers from a list using filter().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 580
Filter Positive Numbers: Write a function that filters only positive numbers from a list using filter().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def num_lst(lst):  # Method: num_lst
    
    def filter_num(num):  # Method: filter_num
        if num > 1:
            return num  # Return the result
    return list(filter(filter_num, lst))  # Return the result
    
lst = [-45, 4, 5, -56, 6]    
print(num_lst(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Cube List Elements: Write a function that returns a list where each element of the input list is cubed using map().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 581
Cube List Elements: Write a function that returns a list where each element of the input list is cubed using map().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def num_lst(lst):  # Method: num_lst
    
    def cubed_num(num):  # Method: cubed_num
        return num ** 3  # Return the result
            
    return list(map(cubed_num, lst))  # Return the result

lst = [-45, 4, 5, -56, 6]    
print(num_lst(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Sum of Squares: Write a function that returns the sum of squares of a list of numbers using map() and reduce().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 582
Sum of Squares: Write a function that returns the sum of squares of a list of numbers using map() and reduce().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

from functools import reduce

def lst_numbers(lst):  # Method: lst_numbers
    
    def square_number(num):  # Method: square_number
        return num ** 2  # Return the result

    def add(x, y):  # Method: add
        return x + y  # Return the result
    
    squared_lst = map(square_number, lst)
    return reduce(add, squared_lst)  # Return the result

lst = [2, 4, 6, 8]    
print(lst_numbers(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Combine Names: Write a function that takes two lists (first names, last names) and returns a list of full names using map().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 583
Combine Names: Write a function that takes two lists (first names, last names) and returns a list of full names using map().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_2(lst1, lst2):  # Method: lst_2
    
    def combine_names(first_last):  # Method: combine_names
        return f"{first_last[0]} {first_last[1]}"  # Return the result
        
    return list(map(combine_names, zip(lst1, lst2)))  # Return the result
    
lst1 = ["Tom", "Bob"]
lst2 = ["Dupond", "lesnake"]    
print(lst_2(lst1, lst2))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Filter Non-Alphabetic Strings: Write a function that filters out strings that contain non-alphabetic characters using filter().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 584
Filter Non-Alphabetic Strings: Write a function that filters out strings that contain non-alphabetic characters using filter().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def non_alphabetical_string(string):  # Method: non_alphabetical_string
    
    def non_alph(char):  # Method: non_alph
        return char.isalpha()  # Return the result
            
    return ''.join(filter(non_alph, string))  # Return the result
           
string = "whats up dog !?!@$"
print(non_alphabetical_string(string))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Count Words: Write a function that counts how many times each word appears in a list using reduce(). (hint, result dictionary)
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 585
Count Words: Write a function that counts how many times each word appears in a list using reduce(). (hint, result dictionary)
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

from functools import reduce

def lst_words(lst):  # Method: lst_words
    
    def count_word(counts, word):  # Method: count_word
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
        return counts  # Return the result
        
    return reduce(count_word, lst, {})  # Return the result

lst = ["Jon", "Chris", "Mike", "Chris", "Chris"]    
print(lst_words(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Unique Words: Write a function that filters out only unique words from a list using filter() and a helper function.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 586
Unique Words: Write a function that filters out only unique words from a list using filter() and a helper function.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def unique_words(lst):  # Method: unique_words
    
    def is_unique(word):  # Method: is_unique
        return lst.count(word) == 1  # Return the result
        
    return list(filter(is_unique, lst))  # Return the result

words = ["apple", "banana", "apple", "orange", "kiwi", "banana"]
print(unique_words(words))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Word Lengths Greater Than N: Write a function that filters words with a length greater than n using filter().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 587
Word Lengths Greater Than N: Write a function that filters words with a length greater than n using filter().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def word_lst(lst):  # Method: word_lst
    
    def filter_word(word):  # Method: filter_word
        if len(word) > n:
            return word  # Return the result
            
    return list(filter(filter_word, lst))  # Return the result
    
lst = ["not", "four", "September", "October"]
n = 4
print(word_lst(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Apply Multiple Functions: Write a function that applies two different functions to a list, one after another (e.g., first squares the numbers, then filters out even ones).
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 588
Apply Multiple Functions: Write a function that applies two different functions to a list, one after another (e.g., first squares the numbers, then filters out even ones).
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def apply_lsts(lst):  # Method: apply_lsts
    
    def square_num(num):  # Method: square_num
        return num * num  # Return the result
        
    def filter_num(num):  # Method: filter_num
        return num % 2 != 0  # Return the result
    
    squared_lst = list(map(square_num, lst))
    
    filtered_lst = list(filter(filter_num, squared_lst))
    
    
    return filtered_lst  # Return the result

lst = [2, 4, 2, 3, 5, 22, 3, 8]    
print(apply_lsts(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Sum of Nested Lists: Write a function that flattens and sums all elements of a nested list using map() and reduce().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 589
Sum of Nested Lists: Write a function that flattens and sums all elements of a nested list using map() and reduce().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

from functools import reduce

def sum_nested_list(nested_list):  # Method: sum_nested_list
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
    def flatten(lst):  # Method: flatten
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
    return total_sum  # Return the result

# Example usage:
nested_list = [1, 2, [3, 4, [5, 6]], 7, [8, 9]]
result = sum_nested_list(nested_list)
print(result)  # Output: 45

from functools import reduce

def sum_of_nested(lst):  # Method: sum_of_nested
    
    def flatten(nested_list):  # Method: flatten
        flat_list = []
        for item in nested_list:
            if isinstance(item, list):
                flat_list.extend(flatten(item))
            else:
                flat_list.append(item)
        return flat_list  # Return the result

    flattened_list = flatten(lst)
    
    return reduce(lambda x, y: x + y, flattened_list)  # Return the result

nested_list = [[1, 2], [3, [4, 5]], [6, [7, [8, 9]]]]
print(sum_of_nested(nested_list))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# First N Fibonacci Numbers: Write a function that generates the first N Fibonacci numbers using reduce().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 590
First N Fibonacci Numbers: Write a function that generates the first N Fibonacci numbers using reduce().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

from functools import reduce

def fibonacci_n_numbers(n):  # Method: fibonacci_n_numbers
    
    def fib(acc, _):  # Method: fib
        return acc + [acc[-1] + acc[-2]]  # Return the result
        
    return reduce(fib, range(n - 2), [0, 1])[:n]  # Return the result

print(fibonacci_n_numbers(10))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Count Vowels in Strings: Write a function that counts how many vowels are present in each string of a list using map() and a helper function.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 591
Count Vowels in Strings: Write a function that counts how many vowels are present in each string of a list using map() and a helper function.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_string(lst):  # Method: lst_string
    
    def count_vowels(word):  # Method: count_vowels
        vowels = "aeiou"
        count = 0
        for char in word:
            if char in vowels:
                count += 1
        return count  # Return the result
        
    return list(map(count_vowels, lst))  # Return the result
    
    
lst = ["Jonathan", "mountain", "lion"]    
print(lst_string(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Sum of Even Numbers: Write a function that computes the sum of all even numbers in a list using filter() and reduce().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 592
Sum of Even Numbers: Write a function that computes the sum of all even numbers in a list using filter() and reduce().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

from functools import reduce

def sum_even_numbers(lst):  # Method: sum_even_numbers
    def is_even(num):  # Method: is_even
        return num % 2 == 0  # Return the result

    def sum_numbers(x, y):  # Method: sum_numbers
        return x + y  # Return the result

    even_numbers = filter(is_even, lst)
    return reduce(sum_numbers, even_numbers)  # Return the result

lst = [1, 2, 3, 4, 5, 6]
print(sum_even_numbers(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Find Longest String: Write a function that finds the longest string in a list using reduce().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 593
Find Longest String: Write a function that finds the longest string in a list using reduce().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

from functools import reduce

def lst_string(lst):  # Method: lst_string
    
    def longest_string(x, y):  # Method: longest_string
        if len(x) > len(y):
            return x  # Return the result
        else:
            return y  # Return the result
        
    return reduce(longest_string, lst)  # Return the result
        
lst = ["shop", "mountain", "not"]
print(lst_string(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Cumulative Sum: Write a function that returns a list of cumulative sums of a given list using reduce().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 594
Cumulative Sum: Write a function that returns a list of cumulative sums of a given list using reduce().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

from functools import reduce

def lst_num(lst):  # Method: lst_num
    
    def cumulative(x, y):  # Method: cumulative
       return x + y  # Return the result
        
    return reduce(cumulative, lst)  # Return the result
        
lst = [2, 2, 2, 2, 2]
print(lst_num(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Flatten Nested Lists: Write a function that flattens a list of lists into a single list using reduce().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 595
Flatten Nested Lists: Write a function that flattens a list of lists into a single list using reduce().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

from functools import reduce

def flatten(lst):  # Method: flatten
    
    def concatenate(x, y):  # Method: concatenate
        return x + y  # Return the result
    return reduce(concatenate, lst)  # Return the result

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened_list = flatten(nested_list)
print(flattened_list)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Word Frequency Count: Write a function that counts the frequency of each word in a list using reduce().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 596
Word Frequency Count: Write a function that counts the frequency of each word in a list using reduce().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

from functools import reduce

def lst_words(lst):  # Method: lst_words
    
    def count_frequency(result, word):  # Method: count_frequency
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
        return result  # Return the result
    
    return reduce(count_frequency, lst, {})  # Return the result

lst = ["word", "sentence", "paragraph", "word", "word"]    
print(lst_words(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Anagram Filter: Write a function that filters out words that are anagrams of a given word using filter().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 597
Anagram Filter: Write a function that filters out words that are anagrams of a given word using filter().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_words(lst, target_word):  # Method: lst_words
    
    def anagram_filter(word):  # Method: anagram_filter
        return sorted(word) != sorted(target_word)  # Return the result

    return list(filter(anagram_filter, lst))  # Return the result

lst = ["listen", "sentence", "stop", "word", "rat", "trail"]
target_word = "listen"
filtered_words = lst_words(lst, target_word)
print(filtered_words)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Compose Functions: Write a function that takes two functions and composes them (i.e., applies one after another).
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 598
Compose Functions: Write a function that takes two functions and composes them (i.e., applies one after another).
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def compose(func1, func2):  # Method: compose
    
    def composed_function(x):  # Method: composed_function
        return func2(func1(x))  # Return the result
    return composed_function  # Return the result

def add_one(x):  # Method: add_one
    return x + 1  # Return the result

def multiply_by_two(x):  # Method: multiply_by_two
    return x * 2  # Return the result

composed_function = compose(add_one, multiply_by_two)

result = composed_function(5)  # (5 + 1) * 2
print(result)  # Output: 12

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Group By Length: Write a function that groups words by their lengths using reduce().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 599
Group By Length: Write a function that groups words by their lengths using reduce().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

from functools import reduce

def word_string(string):  # Method: word_string
    words = string.split()
    
    def sort_len_words(x, y):  # Method: sort_len_words
        if len(x) == 0:
            return [y]  # Return the result
        if len(y) >= len(x[-1]):
            x.append(y)
            return x  # Return the result
        else:
            x.insert(0, y)
            return x  # Return the result

    return reduce(sort_len_words, words, [])  # Return the result

string = "let's group words by the length"
print(word_string(string))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Filter Prime Numbers: Write a function that filters prime numbers from a list using filter() and a helper function to check for primality.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 600
Filter Prime Numbers: Write a function that filters prime numbers from a list using filter() and a helper function to check for primality.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def is_prime(n):  # Method: is_prime
    if n <= 1:
        return False  # Return the result
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Return the result
    return True  # Return the result

def filter_primes(lst):  # Method: filter_primes
    return list(filter(is_prime, lst))  # Return the result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
prime_numbers = filter_primes(numbers)
print(prime_numbers)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Map with Index: Write a function that uses map() but passes the index of each element to the mapping function as well.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 601
Map with Index: Write a function that uses map() but passes the index of each element to the mapping function as well.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def map_with_index(lst, func):  # Method: map_with_index
    
    def indexed_func(indexed_item):  # Method: indexed_func
        index, item = indexed_item
        return func(index, item)  # Return the result

    return list(map(indexed_func, enumerate(lst)))  # Return the result


def example_func(index, value):  # Method: example_func
    return index * value  # Return the result

numbers = [10, 20, 30, 40]
result = map_with_index(numbers, example_func)
print(result)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Intersection of Two Lists: Write a function that finds the intersection of two lists using filter().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 602
Intersection of Two Lists: Write a function that finds the intersection of two lists using filter().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def is_in_list(x, list2):  # Method: is_in_list
    return x in list2  # Return the result

def intersection(list1, list2):  # Method: intersection
    
    def check_in_list(x):  # Method: check_in_list
        return is_in_list(x, list2)  # Return the result
    
    return list(filter(check_in_list, list1))  # Return the result

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = intersection(list1, list2)
print(result)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Average of List: Write a function that calculates the average of a list of numbers using reduce().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 603
Average of List: Write a function that calculates the average of a list of numbers using reduce().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

from functools import reduce

def add(x, y):  # Method: add
    return x + y  # Return the result

def average(lst):  # Method: average
    if not lst:
        return 0  # Return the result
    total = reduce(add, lst)
    return total / len(lst)  # Return the result

numbers = [10, 20, 30, 40, 50]
result = average(numbers)
print(result)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Compose Multiple Functions: Write a function that takes a list of functions and an initial value, and applies the functions sequentially to the value using reduce().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 604
Compose Multiple Functions: Write a function that takes a list of functions and an initial value, and applies the functions sequentially to the value using reduce().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

from functools import reduce

def compose_functions(functions, initial_value):  # Method: compose_functions
    def apply_functions(x, func):  # Method: apply_functions
        return func(x)  # Return the result
    
    return reduce(apply_functions, functions, initial_value)  # Return the result

# Example usage
def add_one(x):  # Method: add_one
    return x + 1  # Return the result

def multiply_by_two(x):  # Method: multiply_by_two
    return x * 2  # Return the result

functions = [add_one, multiply_by_two, add_one]
initial_value = 5
result = compose_functions(functions, initial_value)
print(result)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program to create a dictionary and retrieve a list of its keys. Use key().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 605
Write a program to create a dictionary and retrieve a list of its keys. Use key().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def get_keys(dic):  # Method: get_keys
    return list(dic.keys())  # Return the result

dic = {"Sam": 56, "Chris": 34, "Simon": 12}
print(get_keys(dic)) 

def get_dict_keys():  # Method: get_dict_keys
    my_dict = {
        'apple': 3,
        'banana': 5,
        'cherry': 2,
        'date': 7
    }

    return list(my_dict.keys())  # Return the result

keys_list = get_dict_keys()
print(keys_list)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that sorts a list of strings by their length using the key parameter. Use key().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 606
Write a function that sorts a list of strings by their length using the key parameter. Use key().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sort_string_len(lst):  # Method: sort_string_len
    
    return sorted(lst, key=len)  # Return the result


lst = ["length", "lenny", "len"]    
print(sort_string_len(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a list of tuples based on the second element of each tuple using key().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 607
Write a Python program to sort a list of tuples based on the second element of each tuple using key().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_tuples_second(lst):  # Method: lst_tuples_second
    
    def sort_tuples(x):  # Method: sort_tuples
        return x[1]  # Return the result
        
    return sorted(lst, key=sort_tuples)  # Return the result

lst = [("ton", 54), ("tron", 4), ("zicn", 1)]    
print(lst_tuples_second(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function to sort a list of dictionaries by a specific key in each dictionary using key().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 608
Write a function to sort a list of dictionaries by a specific key in each dictionary using key().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sort_dicts_by_key(lst, target_key):  # Method: sort_dicts_by_key
    
    def get_key_value(d):  # Method: get_key_value
        return d[target_key]  # Return the result
    
    return sorted(lst, key=get_key_value)  # Return the result

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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a list of names by their last name using the key().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 609
Write a Python program to sort a list of names by their last name using the key().
""" 

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sort_last_names(names):  # Method: sort_last_names
    
    def get_last_name(name):  # Method: get_last_name
        return name.split()[-1]  # Return the result
    
    return sorted(names, key=get_last_name)  # Return the result

names = ["Tom Simons", "Lisa Johnson", "Mark Twain", "Sarah Connor", "Peter Parker"]
print(sort_last_names(names))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that sorts a list of mixed case strings, ignoring case. use key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 610
Write a function that sorts a list of mixed case strings, ignoring case. use key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sort_ignore_case(strings):  # Method: sort_ignore_case
    
    def case_insensitive_key(s):  # Method: case_insensitive_key
        return s.lower()  # Return the result
    
    return sorted(strings, key=case_insensitive_key)  # Return the result

mixed_case_strings = ["banana", "Apple", "orange", "mango", "grape"]
sorted_strings = sort_ignore_case(mixed_case_strings)
print(sorted_strings)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a list of floats in descending order. Use key().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 611
Write a Python program to sort a list of floats in descending order. Use key().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def list_floats(lst):  # Method: list_floats
    
    def sort(x):  # Method: sort
        return x  # Return the result
        
    return sorted(lst, key=sort, reverse=True)  # Return the result


lst = [3.6, 56.5, 78.3, 1.5, 0.006]
print(list_floats(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that sorts a list of words by the number of vowels they contain using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 612
Write a function that sorts a list of words by the number of vowels they contain using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_words(lst):  # Method: lst_words
    
    def sort(x):  # Method: sort
        vowels = "aeiou"
        
        count = 0
        for char in x.lower():
            if char in vowels:
                count += 1
        return count  # Return the result
        
    return sorted(lst, key=sort)  # Return the result
    
lst = ["jobaeiou", "Jo", "aei"]    
print(lst_words(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a list of people by their age from a list of dictionaries.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 613
Write a Python program to sort a list of people by their age from a list of dictionaries.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sort_people_by_age(people):  # Method: sort_people_by_age
    
    def get_age(person):  # Method: get_age
        return person['age']  # Return the result
    
    return sorted(people, key=get_age)  # Return the result

people = [
    {"name": "Jon", "age": 34},
    {"name": "Sam", "age": 23},
    {"name": "Bob", "age": 45}
]
sorted_people = sort_people_by_age(people)
print(sorted_people)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that sorts a list of integers based on the sum of their digits using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 614
Write a function that sorts a list of integers based on the sum of their digits using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_integers(lst):  # Method: lst_integers
    
    def sort_sum(x):  # Method: sort_sum
        total = 0
        for digit in str(x):
            total += int(digit) 
        return total  # Return the result
    
    return sorted(lst, key=sort_sum)  # Return the result

lst = [5666, 566, 56, 6]
sorted_list = lst_integers(lst)
print(sorted_list)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a list of products by price using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 615
Write a Python program to sort a list of products by price using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_products(lst):  # Method: lst_products
    
    def sort(product):  # Method: sort
        return product['price']  # Return the result

    return sorted(lst, key=sort)  # Return the result

products = [
    {"name": "chocolate", "price": 2.50},
    {"name": "bread", "price": 1.20},
    {"name": "milk", "price": 1.50},
    {"name": "cheese", "price": 3.00}
]
sorted_products = lst_products(products)
print(sorted_products)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that sorts a list of dates in string format (e.g., “YYYY-MM-DD”) using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 616
Write a function that sorts a list of dates in string format (e.g., “YYYY-MM-DD”) using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sort_dates(dates):  # Method: sort_dates
    
    def date_key(date_str):  # Method: date_key
        year, month, day = map(int, date_str.split('-'))
        return (year, month, day)  # Return the result

    return sorted(dates, key=date_key)  # Return the result

date_list = [
    "2022-01-15",
    "2021-12-25",
    "2023-05-05",
    "2020-11-30"
]

sorted_dates = sort_dates(date_list)
print(sorted_dates)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a list of tuples by the first element, then by the second if the first elements are equal using key.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 617
Write a Python program to sort a list of tuples by the first element, then by the second if the first elements are equal using key.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_tuples(lst):  # Method: lst_tuples
    def sort(tup):  # Method: sort
        return (tup[0], tup[1])  # Return the result
    
    return sorted(lst, key=sort)  # Return the result

lst = [("nice", "good"), ("evil", "bad"), ("nice", "better"), ("evil", "worse")]
sorted_tuples = lst_tuples(lst)
print(sorted_tuples)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that sorts a list of names based on the number of characters in each name using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 618
Write a function that sorts a list of names based on the number of characters in each name using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_names(lst):  # Method: lst_names
    
    def sort_len_of_name(name):  # Method: sort_len_of_name
        return len(name)  # Return the result
        
    return sorted(lst, key=sort_len_of_name)  # Return the result
        

lst = ["Jonathan", "Christopher", "Chantelle", "Bob", "Mimi"]
print(lst_names(lst))

def lst_names(lst):  # Method: lst_names
    
    def sort_len_of_name(name):  # Method: sort_len_of_name
        count = 0
        for char in name:
            count += 1
        return count  # Return the result
        
    return sorted(lst, key=sort_len_of_name)  # Return the result
        
lst = ["Jonathan", "Christopher", "Chantelle", "Bob", "Mimi"]
print(lst_names(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a list of employees by their hire date using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 619
Write a Python program to sort a list of employees by their hire date using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sort_by_hire_date(employees):  # Method: sort_by_hire_date
    
    def get_hire_date(employee):  # Method: get_hire_date
        return employee[1]  # Return the result

    return sorted(employees, key=get_hire_date)  # Return the result

employees = [
    ("Alice", "2020-05-15"),
    ("Bob", "2019-03-22"),
    ("Charlie", "2021-07-30"),
    ("David", "2018-12-01")
]

sorted_employees = sort_by_hire_date(employees)
print(sorted_employees)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that sorts a list of sentences based on their length using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 620
Write a function that sorts a list of sentences based on their length using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_of_sentences(sentences):  # Method: lst_of_sentences
    
    def sort(sentence):  # Method: sort
        return len(sentence)  # Return the result

    return sorted(sentences, key=sort)  # Return the result


sentences = ["hey what's happening today?", "what is", "what about me"]
print(lst_of_sentences(sentences))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a list of words based on the frequency of their first letter using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 621
Write a Python program to sort a list of words based on the frequency of their first letter using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def frequency_first_letter(words):  # Method: frequency_first_letter
    letter_count = {}
    for word in words:
        first_letter = word[0]
        if first_letter in letter_count:
            letter_count[first_letter] += 1
        else:
            letter_count[first_letter] = 1
    
    def sort(word):  # Method: sort
        return letter_count[word[0]]  # Return the result
        
    return sorted(words, key=sort)  # Return the result

words = ["apple", "apricot", "banana", "berry", "blueberry", "cherry", "carrot"]
print(frequency_first_letter(words))


from collections import Counter

def frequency_first_letter(words):  # Method: frequency_first_letter
    
    letter_count = Counter()
    
    for word in words:
        first_letter = word[0] 
        letter_count[first_letter] += 1

    def sort(word):  # Method: sort
        return letter_count[word[0]]  # Return the result
        
    return sorted(words, key=sort)  # Return the result

words = ["apple", "apricot", "banana", "berry", "blueberry", "cherry", "carrot"]
print(frequency_first_letter(words))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that sorts a list of tuples by the absolute value of the first element using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 622
Write a function that sorts a list of tuples by the absolute value of the first element using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_of_tuples(lst):  # Method: lst_of_tuples
    
    def sort(x):  # Method: sort
        return abs((x)[0])  # Return the result
        
    return sorted(lst, key=sort)  # Return the result


lst = [(2.3, 4.2), (5.3, 7.3), (3.1, 2.4), (5.2, 6.2)]
print(lst_of_tuples(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a list of strings by their reverse order using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 623
Write a Python program to sort a list of strings by their reverse order using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def reverse_order(lst):  # Method: reverse_order
    
    def sort(word):  # Method: sort
        return word  # Return the result
        
    return sorted(lst, key=sort, reverse= True)  # Return the result
        
lst = ["butt", "shoulders", "legs"]    
print(reverse_order(lst))


def reverse_order(lst):  # Method: reverse_order
    
    def sort(word):  # Method: sort
        return word[::-1]  # Return the result
        
    return sorted(lst, key=sort)  # Return the result
        
lst = ["butt", "shoulders", "legs"]    
print(reverse_order(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that sorts a list of temperatures in Celsius, converting them to Fahrenheit for sorting using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 624
Write a function that sorts a list of temperatures in Celsius, converting them to Fahrenheit for sorting using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def temperture(lst):  # Method: temperture
    
    def sort(celsius):  # Method: sort
        
        fahrenheit = (9/5) * celsius + 32
        return fahrenheit  # Return the result
        
    return sorted(lst, key=sort)  # Return the result
            
lst = [23, 33, 12, 45]    
print(temperture(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a list of scores from a game, taking into account that some scores may be negative using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 625
Write a Python program to sort a list of scores from a game, taking into account that some scores may be negative using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sort_scores(scores):  # Method: sort_scores
    
    def key_function(x):  # Method: key_function
        return x  # Return the result
    
    return sorted(scores, key=key_function)  # Return the result

scores = [10, -5, 20, 0, -15, 5]
sorted_scores = sort_scores(scores)
print(sorted_scores)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that sorts a list of email addresses by the domain part using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 626
Write a function that sorts a list of email addresses by the domain part using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sort_emails(emails):  # Method: sort_emails
    
    def get_domain(email):  # Method: get_domain
        return email.split('@')[1]  # Return the result
    
    return sorted(emails, key=get_domain)  # Return the result

emails = ["alice@example.com", "bob@test.com", "charlie@example.com", "dave@sample.com"]
sorted_emails = sort_emails(emails)
print(sorted_emails)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a list of cities by their population using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 627
Write a Python program to sort a list of cities by their population using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sort_cities_by_population(cities):  # Method: sort_cities_by_population
    
    def get_population(city):  # Method: get_population
        return city[1]  # Return the result
    
    return sorted(cities, key=get_population)  # Return the result

# List of cities with their population
cities = [("New York", 8419600), ("Los Angeles", 3980400), ("Chicago", 2716000), ("Houston", 2328000), ("Phoenix", 1690000)]

sorted_cities = sort_cities_by_population(cities)
print(sorted_cities)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that sorts a list of words by the last letter of each word using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 628
Write a function that sorts a list of words by the last letter of each word using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def last_letter(lst):  # Method: last_letter
    
    def sort(word):  # Method: sort
        return word[-1]  # Return the result
        
    return sorted(lst, key=sort)  # Return the result
    
lst = ["house", "garden", "boat", "building"]
print(last_letter(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a list of numbers by the number of times they appear in another list using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 629
Write a Python program to sort a list of numbers by the number of times they appear in another list using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_of_numbers(lst):  # Method: lst_of_numbers
    frequency = {}
    for number in lst:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    
    def sort(number):  # Method: sort
        return frequency[number]  # Return the result
    
    return sorted(lst, key=sort)  # Return the result

lst = [3, 677, 4, 3, 67, 4]
print(lst_of_numbers(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that sorts a list of students by their grades using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 630
Write a function that sorts a list of students by their grades using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sort_students_by_grades(students):  # Method: sort_students_by_grades
    
    def get_grade(student):  # Method: get_grade
        return student[1]  # Return the result
        
    return sorted(students, key=get_grade)  # Return the result

students = [("Alice", 85), ("Bob", 70), ("Charlie", 95), ("David", 65)]
print(sort_students_by_grades(students))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a list of book titles by the year they were published using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 631
Write a Python program to sort a list of book titles by the year they were published using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sort_books_by_year(books):  # Method: sort_books_by_year
    
    def get_year(book):  # Method: get_year
        return book[1]  # Return the result
        
    return sorted(books, key=get_year)  # Return the result

books = [("Book A", 2005), ("Book B", 1999), ("Book C", 2010), ("Book D", 1985)]
print(sort_books_by_year(books))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that sorts a list of files based on their file extension using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 632
Write a function that sorts a list of files based on their file extension using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sort_files_by_extension(files):  # Method: sort_files_by_extension

    def get_extension(file):  # Method: get_extension
        return file.split('.')[-1]  # Return the result
        
    return sorted(files, key=get_extension)  # Return the result

files = ["document.pdf", "image.png", "archive.zip", "presentation.pptx", "notes.txt"]
print(sort_files_by_extension(files))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a list of movies by their release date using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

""" 
Problem: 633
Write a Python program to sort a list of movies by their release date using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sort_movies_by_release_date(movies):  # Method: sort_movies_by_release_date
    
    def get_release_date(movie):  # Method: get_release_date
        return movie['release_date']  # Return the result
        
    return sorted(movies, key=get_release_date)  # Return the result

movies = [
    {"title": "Inception", "release_date": "2010-07-16"},
    {"title": "The Matrix", "release_date": "1999-03-31"},
    {"title": "Interstellar", "release_date": "2014-11-07"},
    {"title": "The Godfather", "release_date": "1972-03-24"}
]
sorted_movies = sort_movies_by_release_date(movies)
for movie in sorted_movies:
    print(f"{movie['title']} - {movie['release_date']}")

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that sorts a list of sentences based on the number of unique words in each sentence using the key parameter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 634
Write a function that sorts a list of sentences based on the number of unique words in each sentence using the key parameter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sort_sentences_by_unique_words(sentences):  # Method: sort_sentences_by_unique_words

    def count_unique_words(sentence):  # Method: count_unique_words
        words = sentence.split() 
        unique_words = set(words)
        
        return len(unique_words)  # Return the result
        
    return sorted(sentences, key=count_unique_words)  # Return the result

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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program to create a dictionary and retrieve a list of its keys.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 635
Write a program to create a dictionary and retrieve a list of its keys.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def get_keys_from_dictionary(dic):  # Method: get_keys_from_dictionary

    return list(dic.keys())  # Return the result

example_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

keys = get_keys_from_dictionary(example_dict)
print(keys)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that takes a dictionary and returns a list of keys that have values greater than 10.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 636
Write a function that takes a dictionary and returns a list of keys that have values greater than 10.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def dic_keys(dic):  # Method: dic_keys
    result = []
    for key, value in dic.items():
        if value > 10:
            result.append(key)
    return result  # Return the result

dic = {"a": 5, "b": 34, "c": 67, "d": 9}
print(dic_keys(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of fruits with their prices, and print all the keys.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 637
Create a dictionary of fruits with their prices, and print all the keys.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def print_fruit_keys(fruit_prices):  # Method: print_fruit_keys
    return list(fruit_prices.keys())  # Return the result
    
fruit_prices = {
    "apple": 1.2,
    "banana": 0.5,
    "orange": 0.75,
    "grape": 2.0
}
print(print_fruit_keys(fruit_prices))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program to find the maximum key in a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 638
Write a program to find the maximum key in a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def max_key(dic):  # Method: max_key
    return max(dic.keys())  # Return the result

example_dict = {
    1: "apple",
    3: "banana",
    5: "cherry",
    2: "date"
}
print(max_key(example_dict))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of names and ages, and return the keys sorted by age.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 639
Create a dictionary of names and ages, and return the keys sorted by age.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def name_age(dic):  # Method: name_age
    
    def sort_key(name):  # Method: sort_key
        return dic[name]  # Return the result
    
    sorted_keys = sorted(dic.keys(), key=sort_key)
    
    return sorted_keys  # Return the result

dic = {"Natty": 78, "Bob": 45}
print(name_age(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that accepts a dictionary and returns the keys as a single concatenated string.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 640
Write a function that accepts a dictionary and returns the keys as a single concatenated string.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def concatenate_keys(dic):  # Method: concatenate_keys
    result = ""
    for key in dic.keys():
        result += str(key)
    return result  # Return the result
    
dic = {1: 456, 2: 5566, 3: 566}    
print(concatenate_keys(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of countries and their capitals, and print each key with its corresponding value.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 641
Create a dictionary of countries and their capitals, and print each key with its corresponding value.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def print_countries_and_capitals(dic):  # Method: print_countries_and_capitals
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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program to create a dictionary and count how many keys it has.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 642
Write a program to create a dictionary and count how many keys it has.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_key(dic):  # Method: count_key
    count = 0
    for key in dic.keys():
        count += 1
    return count  # Return the result

dic = {"a":1, "b": 2, "c": 3}
print(count_key(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that takes a dictionary and returns only the keys that start with a specific letter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 643
Write a function that takes a dictionary and returns only the keys that start with a specific letter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_key(dic, letter):  # Method: count_key
    result = []
    for key in dic.keys():
        if key.startswith(letter):
            result.append(key)
    return result  # Return the result

dic = {"apple": 1, "banana": 2, "apricot": 3, "berry": 4}
print(count_key(dic, 'a'))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of students and their grades, and print the keys sorted alphabetically.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 644
Create a dictionary of students and their grades, and print the keys sorted alphabetically.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sorted_students_grades(dic):  # Method: sorted_students_grades
    return sorted(dic.keys())  # Return the result

students_grades = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 95,
    "David": 88
}
print(sorted_students_grades(students_grades))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program to create a dictionary from two lists: one for keys and one for values.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 645
Write a program to create a dictionary from two lists: one for keys and one for values.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def list_dictionary(lst1, lst2):  # Method: list_dictionary
    dic = {}
    
    for key, value in zip(lst1, lst2):
        dic[key] = value 
    
    return dic  # Return the result

lst1 = [1, 2, 3]    
lst2 = ["goat", "boat", "soap"]    
print(list_dictionary(lst1, lst2))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of colors and their hexadecimal values, and print the keys in reverse order.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 646
Create a dictionary of colors and their hexadecimal values, and print the keys in reverse order.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def reverse_keys(dic):  # Method: reverse_keys
    return list(dic.keys())[::-1]  # Return the result

colors = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF",
    "yellow": "#FFFF00"
}
print(reverse_keys(colors))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that returns the first key in a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 647
Write a function that returns the first key in a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def first_key(dic):  # Method: first_key
    return next(iter(dic))  # Return the result

example_dict = {"Nat": 90, "Xav": 70, "Zac": 60}
print(first_key(example_dict))

def first_key(dic):  # Method: first_key
    for key in dic:
        return key  # Return the result
dic = {"apple": 1, "orange": 33, "mango": 5}
first_key(dic)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary representing a shopping cart, and print the keys of the items in the cart.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 648
Create a dictionary representing a shopping cart, and print the keys of the items in the cart.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def shopping_cart_items(cart):  # Method: shopping_cart_items
    for item in cart.keys():
        
        print(item)

cart = {
    "apple": 3,
    "banana": 6,
    "orange": 4,
    "milk": 1
}
shopping_cart_items(cart)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that checks if a specific key exists in a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 649
Write a program that checks if a specific key exists in a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def check_key_exists(dic, key):  # Method: check_key_exists
    if key in dic:
        return True  # Return the result
    else:
        return False  # Return the result

example_dict = {"apple": 3, "banana": 6, "orange": 4, "milk": 1}

key_to_check = "banana"
print(check_key_exists(example_dict, key_to_check))  # Output: True

key_to_check = "bread"
print(check_key_exists(example_dict, key_to_check))  # Output: False

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of items and their quantities, and print keys with quantities greater than 5.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 650
Create a dictionary of items and their quantities, and print keys with quantities greater than 5.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def print_keys_greater_than_five(dic):  # Method: print_keys_greater_than_five
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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that accepts a dictionary and returns a list of keys that are strings.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 651
Write a function that accepts a dictionary and returns a list of keys that are strings.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def returns_strings(dic):  # Method: returns_strings
    result = []
    for key in dic.keys():
        if isinstance(key, str):
            result.append(key)
    return result  # Return the result

example_dict = {"Nat": 90, 56: 70, "Zac": 60, 56: 56}
print(returns_strings(example_dict))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of sports and their popularity rankings, and return the keys sorted by ranking.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 652
Create a dictionary of sports and their popularity rankings, and return the keys sorted by ranking.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sports_by_popularity(sports_dict):  # Method: sports_by_popularity

    def get_ranking(sport):  # Method: get_ranking
        return sports_dict[sport]  # Return the result

    return sorted(sports_dict, key=get_ranking)  # Return the result

sports_dict = {
    "Soccer": 1,
    "Basketball": 3,
    "Cricket": 2,
    "Tennis": 4
}
print(sports_by_popularity(sports_dict))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that retrieves keys from a dictionary that are of type integer.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 653
Write a program that retrieves keys from a dictionary that are of type integer.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(dic):  # Method: main
    result = {}
    for key, value in dic.items():
        if isinstance(value, int):
            result[key] = value
    return result  # Return the result

dic = {2: 1, "orange": 33, "mango": 5}
main(dic)

# Define a dictionary with integer keys
data = {1: 'one', 2: 'two', 3: 'three', 'a': 4, 'b': 5}

# Retrieve keys that are of type integer
integer_keys = [key for key in data if isinstance(key, int)]

# Print the retrieved keys
print(integer_keys)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of books and their authors, and print the keys formatted as a numbered list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 654
Create a dictionary of books and their authors, and print the keys formatted as a numbered list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def books_authors(dic):  # Method: books_authors
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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that takes a dictionary and returns a list of keys that are palindromes.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 655
Write a function that takes a dictionary and returns a list of keys that are palindromes.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def palindromic_keys(dic):  # Method: palindromic_keys
    result = []
    for key in dic.keys():
        if key == key[::-1]: 
            result.append(key)
    return result  # Return the result

example_dict = {
    "madam": 1,
    "racecar": 2,
    "hello": 3,
    "world": 4,
    "level": 5
}
print(palindromic_keys(example_dict))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of pets and their owners, and print all the keys that contain the letter “o”.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 656
Create a dictionary of pets and their owners, and print all the keys that contain the letter “o”.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def pet_owners(dic):  # Method: pet_owners
    result = []
    for key in dic.keys():
        if "o" in key: 
            result.append(key)
    return result  # Return the result

dic = {
    "Boudy": "Alice",
    "Mittens": "Bob",
    "Charlie": "Catherine",
    "Monty": "David",
    "Bella": "Eva"
}
print(pet_owners(dic))

def pet_owners(dic):  # Method: pet_owners
    result = []
    for key in dic.keys():
        for char in key:
            if char == "o":
                result.append(key)
    return result  # Return the result
    
dic = {
    "Boudy": "Alice",
    "Mittens": "Bob",
    "Charlie": "Catherine",
    "Monty": "David",
    "Bella": "Eva"
}
print(pet_owners(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that counts how many keys in a dictionary are of type tuples.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 657
Write a program that counts how many keys in a dictionary are of type tuples.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_tuple_keys(dic):  # Method: count_tuple_keys
    count = 0
    for key in dic.keys():
        if isinstance(key, tuple):
            count += 1
    return count  # Return the result

dic = {
    (1, 2): "tuple_key_1",
    "string_key": "value1",
    (3, 4): "tuple_key_2",
    3: "integer_key"
}
print(count_tuple_keys(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of movies and their release years, and return the keys as a sorted list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 658
Create a dictionary of movies and their release years, and return the keys as a sorted list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def movies(dic):  # Method: movies
    return sorted(dic.keys())  # Return the result

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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that returns the keys of a dictionary whose values are lists.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 659
Write a function that returns the keys of a dictionary whose values are lists.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(dic):  # Method: main
    for key, value in dic.items():
        if isinstance(value, list):
            return key  # Return the result

dic = {"apple": 1, "orange": [45, 74], "mango": 5}
main(dic)

def keys_with_list_values(dic):  # Method: keys_with_list_values
    result = []
    for key, value in dic.items():
        if isinstance(value, list):
            result.append(key)
    return result  # Return the result

dic = {
    "fruits": ["apple", "banana", "cherry"],
    "vegetable": "carrot",
    "numbers": [1, 2, 3],
    "color": "blue"
}
print(keys_with_list_values(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of car brands and their models, and print the keys in a formatted manner.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 660
Create a dictionary of car brands and their models, and print the keys in a formatted manner.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def print_car_brands(dic):  # Method: print_car_brands
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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that retrieves the second key from a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 661
Write a program that retrieves the second key from a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def second_key(dic):  # Method: second_key
    keys_list = list(dic.keys())
    return keys_list[1] if len(keys_list) > 1 else None  # Return the result

dic = {"hope": 12, "dispel": 23, "faith": 34}
print(second_key(dic))

def second_key(dic):  # Method: second_key
    return list(dic.keys())[1]  # Return the result
  

dic = {"hope": 12, "dispel": 23, "faith": 34}
print(second_key(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of temperatures and their units, and return the keys as uppercase strings.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 662
Create a dictionary of temperatures and their units, and return the keys as uppercase strings.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def temperature(dic):  # Method: temperature
    upper_keys = []
    for key in dic.keys():
        upper_keys.append(key.upper())
    return upper_keys  # Return the result

dic = {
    "Celsius": [0, 20, 37, 100],
    "Fahrenheit": [32, 68, 98.6, 212],
    "Kelvin": [273.15, 293.15, 310.15, 373.15]
}
print(temperature(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that takes a dictionary and returns keys that are found in a given list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 663
Write a function that takes a dictionary and returns keys that are found in a given list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def keys_in_list(dic, given_list):  # Method: keys_in_list
    result = []
    for key in dic.keys():
        if key in given_list:
            result.append(key)
    return result  # Return the result

dic = {
    "apple": 1,
    "banana": 2,
    "cherry": 3,
    "date": 4
}

given_list = ["banana", "date", "grape"]
print(keys_in_list(dic, given_list))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of electronic devices and their prices, and print all keys with a price less than $100.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 664
Create a dictionary of electronic devices and their prices, and print all keys with a price less than $100.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that takes a dictionary and returns a list of keys that have values greater than 10.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 665
Write a function that takes a dictionary and returns a list of keys that have values greater than 10.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def keys_with_values_greater_than_10(dic):  # Method: keys_with_values_greater_than_10
    result = []
    for key in dic.keys(): 
        if dic[key] > 10: 
            result.append(key)
    return result  # Return the result

dic = {"Sam": 5, "Chris": 34, "Simon": 12, "Anna": 9}
print(keys_with_values_greater_than_10(dic)) 

def get_dict_keys(dic):  # Method: get_dict_keys
    result = []
    for key, value in dic.items():
        if value > 10:
            result.append(key)
    return result  # Return the result

my_dict = {'apple': 30, 'banana': 50, 'cherry': 2, 'date': 7}
print(get_dict_keys(my_dict))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of fruits with their prices, and print all the keys. Use key().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 666
Create a dictionary of fruits with their prices, and print all the keys. Use key().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def print_fruit_keys(fruits):  # Method: print_fruit_keys
    
    for key in fruits.keys():
        print(key)

fruits = {
    "Apple": 3,
    "Banana": 1,
    "Mango": 2,
    "Orange": 4
}
print_fruit_keys(fruits)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of names and ages, and return the keys sorted by age.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 667
Create a dictionary of names and ages, and return the keys sorted by age.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def name_age(dic):  # Method: name_age
    
    def sort_age(x):  # Method: sort_age
        for keys, values in x:
            return values  # Return the result
    return sorted(dic, key=sort_age)  # Return the result
    

dic = {"Tom": 15, "Lucka": 66, "Bob": 8}    
print(name_age(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that accepts a dictionary and returns the keys as a single concatenated string.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 668
Write a function that accepts a dictionary and returns the keys as a single concatenated string.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def concatenate(dic):  # Method: concatenate
    result = ""
    for key in dic.keys():
        result += str(key)
    return result  # Return the result
        
dic = {1: "one", 2: "two", 3: "three", 4: "four"}    
print(concatenate(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of countries and their capitals, and print each key with its corresponding value.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 669
Create a dictionary of countries and their capitals, and print each key with its corresponding value.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def countries_capitals(dic):  # Method: countries_capitals
    result = ""
    for key, value in dic.items():
        result += f"{key}: {value}\n" 
    return result  # Return the result
    
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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program to create a dictionary and count how many keys it has.
dic = {
    "United States": "Washington, D.C.",
    "Canada": "Ottawa",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin"
}
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

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

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_keys(dic):  # Method: count_keys
    return len(dic)  # Return the result

dic = {
    "United States": "Washington, D.C.",
    "Canada": "Ottawa",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin"
}
print(count_keys(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that takes a dictionary and returns only the keys that start with a specific letter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 671
Write a function that takes a dictionary and returns only the keys that start with a specific letter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def keys_starting_with(dic, letter):  # Method: keys_starting_with
    result = []
    for key in dic.keys():
        if key.startswith(letter):
            result.append(key)
    return result  # Return the result

dic = {
    "apple": 1,
    "banana": 2,
    "apricot": 3,
    "berry": 4,
    "carrot": 5
}
print(keys_starting_with(dic, "a"))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of students and their grades, and print the keys sorted alphabetically.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 672
Create a dictionary of students and their grades, and print the keys sorted alphabetically.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def students_grades(dic):  # Method: students_grades
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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program to create a dictionary from two lists: one for keys and one for values.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 673
Write a program to create a dictionary from two lists: one for keys and one for values.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def two_lst(lst1, lst2):  # Method: two_lst
    result = {}
    for key, value in zip(lst1, lst2):
        result[key] = value
        
    return result  # Return the result
    
lst1 = [1, 2, 3, 4]
lst2 = ["sand", "rock", "wood", "stone"]
print(two_lst(lst1, lst2))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of colors and their hexadecimal values, and print the keys in reverse order.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 674
Create a dictionary of colors and their hexadecimal values, and print the keys in reverse order.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def colors_hex(dic):  # Method: colors_hex
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

def colors_hex(dic):  # Method: colors_hex
    return list(dic.keys())[::-1]  # Return the result
colors_dict = {
    "Red": "#FF0000",
    "Green": "#00FF00",
    "Blue": "#0000FF",
    "Yellow": "#FFFF00",
    "Black": "#000000",
    "White": "#FFFFFF"
}
colors_hex(colors_dict)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that returns the first key in a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 675
Write a function that returns the first key in a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def first_key(dic):  # Method: first_key
    return next(iter(dic))  # Return the result
    
example_dict = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
}
print(first_key(example_dict))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary representing a shopping cart, and print the keys of the items in the cart.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 676
Create a dictionary representing a shopping cart, and print the keys of the items in the cart.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def print_cart_items(cart):  # Method: print_cart_items
    for item in cart.keys():
        print(item)

shopping_cart = {
    "apple": 3,
    "banana": 2,
    "bread": 1,
    "milk": 2
}
print_cart_items(shopping_cart)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that checks if a specific key exists in a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 677
Write a program that checks if a specific key exists in a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def check_key_exists(dic, key):  # Method: check_key_exists
    if key in dic:
        return True  # Return the result
    else:
        return False  # Return the result

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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of items and their quantities, and print keys with quantities greater than 5.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 678
Create a dictionary of items and their quantities, and print keys with quantities greater than 5.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def items_with_high_quantity(dic):  # Method: items_with_high_quantity
    result = []
    for item, quantity in dic.items():
        if quantity > 5:
            result.append(item)
    return result  # Return the result

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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that accepts a dictionary and returns a list of keys that are strings.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 679
Write a function that accepts a dictionary and returns a list of keys that are strings.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def string_keys(dic):  # Method: string_keys
    result = []
    for key in dic.keys():
        if isinstance(key, str): 
            result.append(key)
    return result  # Return the result

example_dict = {
    "name": "Alice",
    42: "answer",
    "city": "Wonderland",
    (1, 2): "tuple_key",
    "age": 30
}
string_keys_list = string_keys(example_dict)
print("Keys that are strings:", string_keys_list)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of sports and their popularity rankings, and return the keys sorted by ranking.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 680
Create a dictionary of sports and their popularity rankings, and return the keys sorted by ranking.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sports_by_popularity(sports_dict):  # Method: sports_by_popularity
    def get_ranking(sport):  # Method: get_ranking
        return sports_dict[sport]  # Return the result

    return sorted(sports_dict.keys(), key=get_ranking)  # Return the result

sports_dict = {
    "Soccer": 1,
    "Basketball": 3,
    "Cricket": 2,
    "Tennis": 4
}
print(sports_by_popularity(sports_dict))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that retrieves keys from a dictionary that are of type integer.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 681
Write a program that retrieves keys from a dictionary that are of type integer.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def retrieve_integer_keys(dic):  # Method: retrieve_integer_keys
    result = []
    for key in dic.keys():
        if isinstance(key, int):
            result.append(key)
    return result  # Return the result

example_dict = {
    1: "one",
    "two": 2,
    3: "three",
    "four": 4
}
print(retrieve_integer_keys(example_dict))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of books and their authors, and print the keys formatted as a numbered list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 682
Create a dictionary of books and their authors, and print the keys formatted as a numbered list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def print_numbered_books(dic):  # Method: print_numbered_books
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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that takes a dictionary and returns a list of keys that are palindromes.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 683
Write a function that takes a dictionary and returns a list of keys that are palindromes.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def palindrome_keys(dic):  # Method: palindrome_keys
    result = []
    for key in dic.keys():
        if str(key) == str(key)[::-1]:
            result.append(key)
    return result  # Return the result

example_dict = {
    "racecar": 1,
    "level": 2,
    "hello": 3,
    "madam": 4,
    "world": 5
}
print(palindrome_keys(example_dict))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of pets and their owners, and print all the keys that contain the letter “o”.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 684
Create a dictionary of pets and their owners, and print all the keys that contain the letter “o”.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def pets_with_o(dic):  # Method: pets_with_o
    result = []
    for key in dic.keys():
        if 'o' in key:
            result.append(key)
    return result  # Return the result

pets_dict = {
    "Boudy": "Alice",
    "Mittens": "Bob",
    "Charlie": "Catherine",
    "Monty": "David",
    "Bella": "Eva"
}
print(pets_with_o(pets_dict))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that counts how many keys in a dictionary are of type list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 685
Write a program that counts how many keys in a dictionary are of type list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_list_keys(dic):  # Method: count_list_keys
    count = 0
    for key in dic.keys():
        if isinstance(key, list):
            count += 1
    return count  # Return the result

example_dict = {
    (1, 2): "tuple_key",
    "string_key": "value1",
    3: "integer_key",
}
print(count_list_keys(example_dict))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of movies and their release years, and return the keys as a sorted list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 686
Create a dictionary of movies and their release years, and return the keys as a sorted list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sorted_movie_titles(movies):  # Method: sorted_movie_titles
    return sorted(movies.keys())  # Return the result

movies_dict = {
    "The Shawshank Redemption": 1994,
    "The Godfather": 1972,
    "The Dark Knight": 2008,
    "Pulp Fiction": 1994,
    "Forrest Gump": 1994,
}
print(sorted_movie_titles(movies_dict))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that returns the keys of a dictionary whose values are lists.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 687
Write a function that returns the keys of a dictionary whose values are lists.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def keys_with_list_values(dic):  # Method: keys_with_list_values
    result = []
    for key, value in dic.items():
        if isinstance(value, list):
            result.append(key)
    return result  # Return the result

example_dict = {
    "fruits": ["apple", "banana"],
    "vegetable": "carrot",
    "grains": ["rice", "wheat"]
}
print(keys_with_list_values(example_dict))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of car brands and their models, and print the keys in a formatted manner.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 688
Create a dictionary of car brands and their models, and print the keys in a formatted manner.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def print_car_brands(dic):  # Method: print_car_brands
    for brand in dic.keys():
        print(f"Brand: {brand}")

car_brands = {
    "Toyota": ["Camry", "Corolla", "RAV4"],
    "Honda": ["Civic", "Accord", "CR-V"],
    "Ford": ["F-150", "Mustang", "Explorer"]
}
print_car_brands(car_brands)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that retrieves the second key from a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 689
Write a program that retrieves the second key from a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def second_key(dic):  # Method: second_key
    return list(dic.keys())[1]  # Return the result

example_dict = {"apple": 1, "banana": 2, "cherry": 3}
print(second_key(example_dict))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a dictionary of temperatures and their units, and return the keys as uppercase strings. keys only ("Celsius": [0, 20, 37, 100]).
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 690
Create a dictionary of temperatures and their units, and return the keys as uppercase strings. keys only ("Celsius": [0, 20, 37, 100]).
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def uppercase_keys(dic):  # Method: uppercase_keys
    result = []
    for key in dic.keys():
        result.append(key.upper())
    return result  # Return the result

dic = {
    "Celsius": [0, 20, 37, 100],
    "Fahrenheit": [32, 68, 98.6, 212],
    "Kelvin": [273.15, 293.15, 310.15, 373.15]
}
print(uppercase_keys(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program to find the maximum key in a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 691
Write a program to find the maximum key in a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def key_max(dic):  # Method: key_max
    
    return max(dic)  # Return the result
    
dic = {"banana": 1.50, "Apple": 2, "apricot": 3.5}    
print(key_max(dic))

def key_max(dic):  # Method: key_max
    max_key = None
    max_key_lower = None
    
    for key in dic:

        key_lower = key.lower()
        
        if max_key_lower is None or key_lower > max_key_lower:
            max_key = key
            max_key_lower = key_lower
    
    return max_key  # Return the result

dic = {"banana": 1.50, "Apple": 2, "apricot": 3.5}

print(key_max(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that takes a list of numbers and returns a new list with each number squared using map().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 692
Write a program that takes a list of numbers and returns a new list with each number squared using map().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def square_numbers(lst):  # Method: square_numbers
    
    def square(num):  # Method: square
        return num ** 2  # Return the result
    
    return list(map(square, lst))  # Return the result

numbers = [1, 2, 3, 4, 5]
print(square_numbers(numbers))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a program that takes a list of strings and returns a list of their lengths using map().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 693
Create a program that takes a list of strings and returns a list of their lengths using map().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def string_lengths(lst):  # Method: string_lengths
    
    def length(string):  # Method: length
        return len(string)  # Return the result
    
    return list(map(length, lst))  # Return the result

strings = ["hello", "world", "python", "programming"]
print(string_lengths(strings))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that takes a list of strings and converts all of them to uppercase using `map()`.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 694
Write a function that takes a list of strings and converts all of them to uppercase using `map()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_words(lst):  # Method: lst_words
    
    def word_len(word):  # Method: word_len
        return word.upper()  # Return the result
        
    return list(map(word_len, lst))  # Return the result

lst = ["monkey", "lizard", "hippopotamus"]
print(lst_words(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Given a list of floats, use `map()` to round all the numbers to two decimal places.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 695
Given a list of floats, use `map()` to round all the numbers to two decimal places.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_numbers(lst):  # Method: lst_numbers
    
    def round_two_decimals(x):  # Method: round_two_decimals
        return round(x, 2)  # Return the result
        
    return list(map(round_two_decimals, lst))  # Return the result

lst = [2.6666, 4.77, 7.566, 9.55]
print(lst_numbers(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that converts a list of temperatures in Celsius to Fahrenheit using `map()`.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 696
Write a program that converts a list of temperatures in Celsius to Fahrenheit using `map()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def celsius_to_fahrenheit(lst):  # Method: celsius_to_fahrenheit
    
    def convert(celsius):  # Method: convert
        return (celsius * 9/5) + 32  # Return the result
        
    return list(map(convert, lst))  # Return the result

celsius_temps = [0, 20, 37, 100]
fahrenheit_temps = celsius_to_fahrenheit(celsius_temps)
print(fahrenheit_temps)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `map()` to convert a list of numbers into their corresponding ASCII characters.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 697
Use `map()` to convert a list of numbers into their corresponding ASCII characters.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def numbers_to_ascii(lst):  # Method: numbers_to_ascii
    
    def to_ascii(number):  # Method: to_ascii
        return chr(number)  # Return the result
        
    return list(map(to_ascii, lst))  # Return the result

numbers = [0, 65, 66, 67, 68, 69, 91, 120]
ascii_characters = numbers_to_ascii(numbers)
print(ascii_characters)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that takes a list of words and returns the reversed version of each word using `map()`.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 698
Write a function that takes a list of words and returns the reversed version of each word using `map()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_words(lst):  # Method: lst_words
    
    def reverse_word(word):  # Method: reverse_word
        return word[::-1]  # Return the result
        
    return list(map(reverse_word, lst))  # Return the result

lst = ["monkey", "lizard", "hippopotamus"]
print(lst_words(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a program that takes a list of integers and returns a list where each number is doubled using `map()`.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 700
Create a program that takes a list of integers and returns a list where each number is doubled using `map()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_integers(lst):  # Method: lst_integers
    
    def double_num(number):  # Method: double_num
        return number * 2  # Return the result
        
    return list(map(double_num, lst))  # Return the result

lst = [0, 65, 66, 67, 68, 69, 91, 120]
print(lst_integers(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program to take a list of strings and return a list of their first characters using `map()`.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 701
Write a program to take a list of strings and return a list of their first characters using `map()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_words(lst):  # Method: lst_words
    
    def first_char(word):  # Method: first_char
        return word[0]  # Return the result
        
    return list(map(first_char, lst))  # Return the result

lst = ["monkey", "lizard", "hippopotamus"]
print(lst_words(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `map()` to convert a list of binary strings to their decimal equivalents.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 702
Use `map()` to convert a list of binary strings to their decimal equivalents.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_words(lst):  # Method: lst_words
    
    def binary(word):  # Method: binary
        return int(word, 2)  # Return the result
        
    return list(map(binary, lst))  # Return the result

lst = ["101", "110", "1001"]
print(lst_words(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that takes a list of mixed-case strings and returns all strings in lowercase using `map()`.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 703
Write a program that takes a list of mixed-case strings and returns all strings in lowercase using `map()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_mixed_case(lst):  # Method: lst_mixed_case
    
    def lowercase(string):  # Method: lowercase
        return string.lower()  # Return the result
        
    return list(map(lowercase, lst))  # Return the result

lst = ["LIZARD", "hiPpopotamus", "FroG"]
print(lst_mixed_case(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Given two lists of numbers, use `map()` to multiply each pair of numbers from the two lists together.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 704
Given two lists of numbers, use `map()` to multiply each pair of numbers from the two lists together.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_integers(lst1, lst2):  # Method: lst_integers
    
    def multiply(num1, num2):  # Method: multiply
        return num1 * num2  # Return the result
        
    return list(map(multiply, lst1, lst2))  # Return the result

lst1 = [6, 12, 23, 68]
lst2 = [1, 2, 3, 4]
print(lst_integers(lst1, lst2))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `map()` to convert a list of tuples (representing x, y points) into a list of their Euclidean distances from the origin.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 705
Use `map()` to convert a list of tuples (representing x, y points) into a list of their Euclidean distances from the origin.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

import math  # Import module

def euclidean_distances(points):  # Method: euclidean_distances
    
    def distance(point):  # Method: distance
        return math.sqrt(point[0]**2 + point[1]**2)  # Return the result
        
    return list(map(distance, points))  # Return the result

points = [(3, 4), (1, 1), (0, 0), (6, 8)]
print(euclidean_distances(points))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that takes a list of email addresses and extracts the domain names using `map()`.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 706
Write a function that takes a list of email addresses and extracts the domain names using `map()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_emails(lst):  # Method: lst_emails
    
    def domain(string):  # Method: domain
        return string.split('@')[1]  # Return the result
        
    return list(map(domain, lst))  # Return the result

lst = ["user@example.com", "admin@domain.org", "info@website.net"]
print(lst_emails(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `map()` to take a list of numbers and return a list indicating whether each number is even or odd.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 707
Use `map()` to take a list of numbers and return a list indicating whether each number is even or odd.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_integers(lst):  # Method: lst_integers
    
    def even_odd(number):  # Method: even_odd
        if number % 2 == 0:
            return "Even"  # Return the result
        else:
            return "Odd"  # Return the result
        
    return list(map(even_odd, lst))  # Return the result

lst = [65, 66, 67, 68, 69, 91, 120]
print(lst_integers(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that uses `map()` to convert a list of string representations of numbers to a list of integers.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 708
Write a program that uses `map()` to convert a list of string representations of numbers to a list of integers.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def negate_bool(value):  # Method: negate_bool
    return not value  # Return the result

bool_list = [True, False, True, False]
negated_list = list(map(negate_bool, bool_list))
print(negated_list)  # Output: [False, True, False, True]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a program that takes a list of Boolean values and negates each value using `map()`.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 709
Create a program that takes a list of Boolean values and negates each value using `map()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def negate_bool(bool_list):  # Method: negate_bool
    def inner(value):  # Method: inner
        return not value  # Return the result
    return list(map(inner, bool_list))  # Return the result

bool_list = [True, False, True, False]
negate_bool(bool_list)

def negate_bool(value):  # Method: negate_bool
    return not value  # Return the result

bool_list = [True, False, True, False]
negated_list = list(map(negate_bool, bool_list))
print(negated_list)  # Output: [False, True, False, True]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that takes a list of strings and returns a list of booleans indicating whether each string is a palindrome using `map()`.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 710
Write a function that takes a list of strings and returns a list of booleans indicating whether each string is a palindrome using `map()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def negate_booleans(lst):  # Method: negate_booleans
    
    def negate(value):  # Method: negate
        return not value  # Return the result
        
    return list(map(negate, lst))  # Return the result

lst = [True, False, True, False]
print(negate_booleans(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Given a list of sentences, use `map()` to return a list of the number of words in each sentence.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 711
Given a list of sentences, use `map()` to return a list of the number of words in each sentence.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_sentence(lst):  # Method: lst_sentence
    
    def num_of_words(string):  # Method: num_of_words
        words = string.split()
        return len(words)  # Return the result
        
    return list(map(num_of_words, lst))  # Return the result
    
lst = ["how hot is it", "what's up dog", "today is the best day of my life"]    
print(lst_sentence(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `map()` to take a list of strings and return a list of strings where each word has its first letter capitalized.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 712
Use `map()` to take a list of strings and return a list of strings where each word has its first letter capitalized.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_sentence(lst):  # Method: lst_sentence
    
    def cap(word):  # Method: cap
        word = word.capitalize()
        return word  # Return the result
           
    return list(map(cap, lst))  # Return the result
    
lst = ["mop", "sop", "dop"]    
print(lst_sentence(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that takes a list of strings and removes all spaces from each string using `map()`.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 713
Write a program that takes a list of strings and removes all spaces from each string using `map()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_sentence(lst):  # Method: lst_sentence
    
    def remove_spaces(word):  # Method: remove_spaces
        return word.replace(" ", "")  # Return the result
           
    return list(map(remove_spaces, lst))  # Return the result
    
lst = ["mop in tate", "sop in tate", "dop in tate"]    
print(lst_sentence(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a program that takes a list of tuples representing (width, height) and returns a list of their areas using `map()`.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 714
Create a program that takes a list of tuples representing (width, height) and returns a list of their areas using `map()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_of_tuples(lst):  # Method: lst_of_tuples
    
    def area_lst(dimensions):  # Method: area_lst
        width, height = dimensions
        area = width * height
        return area  # Return the result
        
    return list(map(area_lst, lst))  # Return the result
            
lst = [(3, 5), (4, 9), (3, 9)]    
print(lst_of_tuples(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `map()` to take a list of URLs and extract the domain name from each one.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 715
Use `map()` to take a list of URLs and extract the domain name from each one.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def extract_domain(lst):  # Method: extract_domain
    
    def domain(url):  # Method: domain
        return url.split("//")[-1].split("/")[0]  # Return the result
        
    return list(map(domain, lst))  # Return the result

urls = [
    "https://www.example.com/page",
    "http://another-domain.org",
    "https://sub.domain.com/path/to/resource"
]

print(extract_domain(urls))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that takes two lists: one of numbers and one of strings, and returns a list of tuples pairing the elements using `map()`.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 716
Write a function that takes two lists: one of numbers and one of strings, and returns a list of tuples pairing the elements using `map()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def pair_elements(numbers, strings):  # Method: pair_elements
    
    def pair(num, string):  # Method: pair
        return (num, string)  # Return the result
    
    return list(map(pair, numbers, strings))  # Return the result

numbers = [1, 2, 3]
strings = ["apple", "banana", "cherry"]
print(pair_elements(numbers, strings))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a program that converts a list of lowercase letters to uppercase using `map()`.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 717
Create a program that converts a list of lowercase letters to uppercase using `map()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lowercase_to_uppercase(lst):  # Method: lowercase_to_uppercase
    
    def to_uppercase(letter):  # Method: to_uppercase
        return letter.upper()  # Return the result
    
    return list(map(to_uppercase, lst))  # Return the result

lst = ['a', 'b', 'c', 'd']
print(lowercase_to_uppercase(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `map()` to calculate the factorial of each number in a list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 718
Use `map()` to calculate the factorial of each number in a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def factorial_lst(lst):  # Method: factorial_lst
    
    def factorial(num):  # Method: factorial
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result  # Return the result
    
    return list(map(factorial, lst))  # Return the result

lst = [3, 4, 5, 6]
print(factorial_lst(lst))

import math  # Import module

def factorial_lst(lst):  # Method: factorial_lst
    
    def factorial(num):  # Method: factorial
        return math.factorial(num)  # Return the result
    
    return list(map(factorial, lst))  # Return the result

lst = [3, 4, 5, 6]
print(factorial_lst(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that takes a list of sentences and returns a list of sentences in which each word is reversed using `map()`.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 719
Write a program that takes a list of sentences and returns a list of sentences in which each word is reversed using `map()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def reverse_words_in_sentences(lst):  # Method: reverse_words_in_sentences
    
    def reverse_sentence(sentence):  # Method: reverse_sentence
        words = sentence.split()
        reversed_words = []
        for word in words:
            reversed_words.append(word[::-1])
        return ' '.join(reversed_words)  # Return the result
        
    return list(map(reverse_sentence, lst))  # Return the result

lst = ["The cat is fast", "Hello world", "Python is fun"]
print(reverse_words_in_sentences(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `map()` to check whether the elements of a list of strings contain only alphabetic characters.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 720
Use `map()` to check whether the elements of a list of strings contain only alphabetic characters.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_strings(lst):  # Method: lst_strings
    
    def alpha_only(word):  # Method: alpha_only
        if word.isalpha():
            return True  # Return the result
        else:
            return False  # Return the result
            
    return list(map(alpha_only, lst))  # Return the result
                

lst = ["monkey", "tomy&", "magic"]
print(lst_strings(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that takes a list of floats and returns a list where each float is squared using `map()`.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 721
Write a function that takes a list of floats and returns a list where each float is squared using `map()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def square_floats(lst):  # Method: square_floats
    
    def square(num):  # Method: square
        return num * num  # Return the result
        
    return list(map(square, lst))  # Return the result

lst = [2.5, 3.1, 4.8, 6.7]
print(square_floats(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Given a list of phone numbers, use `map()` to format them as international phone numbers.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 722
Given a list of phone numbers, use `map()` to format them as international phone numbers.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def format_phone_numbers(lst):  # Method: format_phone_numbers
    
    def format_number(number):  # Method: format_number
        return f"+1-{number}"  # Return the result
        
    return list(map(format_number, lst))  # Return the result

lst = ["5551234567", "5559876543", "5556789123"]
print(format_phone_numbers(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `map()` to find the absolute value of each number in a list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 723
Use `map()` to find the absolute value of each number in a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def absolute_values(lst):  # Method: absolute_values
    
    def absolute(num):  # Method: absolute
        return abs(num)  # Return the result
        
    return list(map(absolute, lst))  # Return the result

lst = [-10, 5, -3.2, 8]
print(absolute_values(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that takes two lists of integers and returns a list of tuples pairing corresponding numbers from each list using `map()`.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 724
Write a program that takes two lists of integers and returns a list of tuples pairing corresponding numbers from each list using `map()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def pair_lists(lst1, lst2):  # Method: pair_lists
    
    def pair_numbers(num1, num2):  # Method: pair_numbers
        return (num1, num2)  # Return the result

    return list(map(pair_numbers, lst1, lst2))  # Return the result

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
print(pair_lists(lst1, lst2))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `map()` to convert a list of tuples representing (x, y) coordinates into polar coordinates.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 725
Use `map()` to convert a list of tuples representing (x, y) coordinates into polar coordinates.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

import math  # Import module

def cartesian_to_polar(lst):  # Method: cartesian_to_polar
    
    def to_polar(coords):  # Method: to_polar
        x, y = coords
        r = math.sqrt(x**2 + y**2)
        theta = math.atan2(y, x)
        return (r, theta)  # Return the result

    return list(map(to_polar, lst))  # Return the result

coordinates = [(1, 1), (0, 0), (3, 4)]
print(cartesian_to_polar(coordinates))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that uses `map()` to find the cube of each number in a list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 726
Write a program that uses `map()` to find the cube of each number in a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_cubes(lst):  # Method: lst_cubes
    
    def cube(num):  # Method: cube
        return num ** 3  # Return the result
        
    return list(map(cube, lst))  # Return the result

numbers = [1, 2, 3, 4, 5]
print(lst_cubes(numbers))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `map()` to create a program that takes a list of integers and returns a list of their squares and cubes as tuples.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 727
Use `map()` to create a program that takes a list of integers and returns a list of their squares and cubes as tuples.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_squares_and_cubes(lst):  # Method: lst_squares_and_cubes
    
    def square_and_cube(num):  # Method: square_and_cube
        return (num ** 2, num ** 3)  # Return the result
        
    return list(map(square_and_cube, lst))  # Return the result

lst = [1, 2, 3, 4, 5]
print(lst_squares_and_cubes(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that uses `map()` to convert a list of RGB tuples into hexadecimal color codes.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 728
Write a program that uses `map()` to convert a list of RGB tuples into hexadecimal color codes.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def rgb_to_hex(lst):  # Method: rgb_to_hex
    
    def to_hex(rgb):  # Method: to_hex
        return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])  # Return the result
        
    return list(map(to_hex, lst))  # Return the result

lst = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
print(rgb_to_hex(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Given a list of mixed-case strings, use `map()` to return a list of strings where every second string is converted to uppercase.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 729
Given a list of mixed-case strings, use `map()` to return a list of strings where every second string is converted to uppercase.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def mixed_case_string(lst):  # Method: mixed_case_string
    
    def second_uppercase(word):  # Method: second_uppercase
        return word[0] + word[1].upper() + word[2:]  # Return the result

    return list(map(second_uppercase, lst))  # Return the result

lst = ["first", "second", "third", "fourth"]
print(mixed_case_string(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a function that uses `map()` to convert a list of dates (in string format) into Python `datetime` objects.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 730
Write a function that uses `map()` to convert a list of dates (in string format) into Python `datetime` objects.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

from datetime import datetime

def convert_dates(date_list):  # Method: convert_dates
    
    def parse_date(date_string):  # Method: parse_date
        return datetime.strptime(date_string, "%Y-%m-%d")  # Return the result
    
    return list(map(parse_date, date_list))  # Return the result

date_list = ["2024-01-01", "2023-12-25", "2022-07-04"]
print(convert_dates(date_list))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `map()` to calculate the square roots of each number in a list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 731
Use `map()` to calculate the square roots of each number in a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

import math  # Import module

def calculate_square_roots(numbers):  # Method: calculate_square_roots
    def square_root(x):  # Method: square_root
        return math.sqrt(x)  # Return the result
    
    return list(map(square_root, numbers))  # Return the result

numbers = [1, 4, 9, 16, 25]
print(calculate_square_roots(numbers))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a program that uses `map()` to calculate the percentage of each score in a list of scores based on the maximum score.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 732
Create a program that uses `map()` to calculate the percentage of each score in a list of scores based on the maximum score.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def calculate_percentage(scores, max_score):  # Method: calculate_percentage
    def percentage(score):  # Method: percentage
        return (score / max_score) * 100  # Return the result
    
    return list(map(percentage, scores))  # Return the result

scores = [50, 75, 100, 80]
max_score = 100
print(calculate_percentage(scores, max_score))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that defines a helper function `add(a, b)` to return the sum of two numbers, and uses it to sum a list of numbers.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 733
Write a Python program that defines a helper function `add(a, b)` to return the sum of two numbers, and uses it to sum a list of numbers.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def add(a, b):  # Method: add
    return a + b  # Return the result

def sum_list(numbers):  # Method: sum_list
    total = 0
    for number in numbers:
        total = add(total, number)
    return total  # Return the result

numbers = [1, 2, 3, 4, 5]
result = sum_list(numbers)
print(result)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a program with a helper function `is_even(n)` that returns `True` if a number is even and `False` otherwise, and use it to filter a list of numbers.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 734
Create a program with a helper function `is_even(n)` that returns `True` if a number is even and `False` otherwise, and use it to filter a list of numbers.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def is_even(n):  # Method: is_even
    return n % 2 == 0  # Return the result

def filter_even_numbers(numbers):  # Method: filter_even_numbers
    return list(filter(is_even, numbers))  # Return the result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(numbers)
print(even_numbers)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that uses a helper function `capitalize_first_letter(word)` to capitalize the first letter of each word in a list of strings.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 735
Write a program that uses a helper function `capitalize_first_letter(word)` to capitalize the first letter of each word in a list of strings.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def capitalize_first_letter(word):  # Method: capitalize_first_letter
    return word.capitalize()  # Return the result

def word_list(lst):  # Method: word_list
    return list(map(capitalize_first_letter, lst))  # Return the result

lst = ["first", "letter", "word"]
print(word_list(lst))


def word_list(lst):  # Method: word_list
    return list(map(capitalize_first_letter, lst))  # Return the result

def capitalize_first_letter(word):  # Method: capitalize_first_letter
    return word.capitalize()  # Return the result

lst = ["first", "letter", "word"]
print(word_list(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Define a helper function `find_max(numbers)` that returns the maximum number from a list, and use it in a program to find the largest number.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 736
Define a helper function `find_max(numbers)` that returns the maximum number from a list, and use it in a program to find the largest number.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_numbers(lst):  # Method: lst_numbers
    return find_max(lst)  # Return the result
    
def find_max(numbers):  # Method: find_max
    return max(numbers)  # Return the result
    
lst = [2, 4, 6]
print(lst_numbers(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a helper function `convert_to_celsius(fahrenheit)` that converts a temperature from Fahrenheit to Celsius, and use it to convert a list of temperatures.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 737
Create a helper function `convert_to_celsius(fahrenheit)` that converts a temperature from Fahrenheit to Celsius, and use it to convert a list of temperatures.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_tempertures(lst):  # Method: lst_tempertures
    return list(map(convert_to_celsius, lst))  # Return the result
    
def convert_to_celsius(fahrenheit):  # Method: convert_to_celsius
    return (fahrenheit - 32) / 1.8  # Return the result
       
lst = [1, 16, 20, 27]    
print(lst_tempertures(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that defines a helper function `reverse_string(s)` that returns the reversed version of a string, and uses it to reverse all strings in a list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 738
Write a program that defines a helper function `reverse_string(s)` that returns the reversed version of a string, and uses it to reverse all strings in a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def string_lst(lst):  # Method: string_lst
    return list(map(reverse_string, lst))  # Return the result

def reverse_string(word):  # Method: reverse_string
    return word[::-1]  # Return the result

lst = ["hello", "twice"]    
print(string_lst(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Define a helper function `count_vowels(word)` that counts the number of vowels in a word, and use it to find the word with the most vowels in a list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 739
Define a helper function `count_vowels(word)` that counts the number of vowels in a word, and use it to find the word with the most vowels in a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_words(lst):  # Method: lst_words
    return max(lst, key=count_vowels)  # Return the result

def count_vowels(word):  # Method: count_vowels
    vowels = "aeiou"
    count = 0
    for char in word:
        if char.lower() in vowels:
            count += 1
    return count  # Return the result

lst = ["word", "eerie"]    
print(lst_words(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a program with a helper function `is_palindrome(word)` that checks if a word is a palindrome and uses it to filter a list of words.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 740
Create a program with a helper function `is_palindrome(word)` that checks if a word is a palindrome and uses it to filter a list of words.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_of_word(lst):  # Method: lst_of_word
    return list(filter(is_palindrome, lst))  # Return the result
    
def is_palindrome(word):  # Method: is_palindrome
    return word == word[::-1]  # Return the result

lst = ["radar", "words", "level", "deed"]
print(lst_of_word(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that defines a helper function `calculate_area(radius)` to calculate the area of a circle given its radius, and uses it for a list of radii.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 741
Write a program that defines a helper function `calculate_area(radius)` to calculate the area of a circle given its radius, and uses it for a list of radii.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_of_radii(lst):  # Method: lst_of_radii
    return list(map(calculate_area, lst))  # Return the result

def calculate_area(radius):  # Method: calculate_area
    return 3.14159 * radius ** 2  # Return the result

lst = [1, 2, 3, 4, 5]
print(lst_of_radii(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Define a helper function `square(n)` that returns the square of a number, and use it to square each element in a list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 742
Define a helper function `square(n)` that returns the square of a number, and use it to square each element in a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_numbers(lst):  # Method: lst_numbers
    return list(map(sqaure_number, lst))  # Return the result

def sqaure_number(num):  # Method: sqaure_number
    return num * num  # Return the result
    
lst = [2, 5, 7]
print(lst_numbers(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a program with a helper function `get_first_n_elements(lst, n)` that returns the first `n` elements of a list, and use it on a sample list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 743
Create a program with a helper function `get_first_n_elements(lst, n)` that returns the first `n` elements of a list, and use it on a sample list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def get_first_n_elements(lst, num):  # Method: get_first_n_elements
    return lst[:num]  # Return the result

def main():  # Method: main
    lst = [1, 2, 3, 4, 5, 6]
    num = 3
    return get_first_n_elements(lst, num)  # Return the result

print(main())

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that defines a helper function `merge_dicts(dict1, dict2)` that merges two dictionaries, and uses it to combine multiple dictionaries.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 744
Write a program that defines a helper function `merge_dicts(dict1, dict2)` that merges two dictionaries, and uses it to combine multiple dictionaries.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def merge_dicts(dict1, dict2):  # Method: merge_dicts
    return {**dict1, **dict2}  # Return the result

def combine_dicts(dicts):  # Method: combine_dicts
    result = {}
    for d in dicts:
        result = merge_dicts(result, d) 
    return result  # Return the result
    
dicts = [
    {'a': 1, 'b': 2},
    {'b': 3, 'c': 4},
    {'d': 5}
]

print(combine_dicts(dicts))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Define a helper function `format_name(first_name, last_name)` that returns a formatted full name, and use it to format a list of names.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 745
Define a helper function `format_name(first_name, last_name)` that returns a formatted full name, and use it to format a list of names.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def format_name(first_name, last_name):  # Method: format_name
    return f"{first_name} {last_name}"  # Return the result

def format_names(lst):  # Method: format_names
    
    def format_pair(name_pair):  # Method: format_pair
        return format_name(name_pair[0], name_pair[1])  # Return the result
    
    return list(map(format_pair, lst))  # Return the result

names = [("John", "Doe"), ("Jane", "Smith"), ("Alice", "Johnson")]
formatted_names = format_names(names)
print(formatted_names)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a program with a helper function `find_gcd(a, b)` that finds the greatest common divisor of two numbers, and use it to find the GCD of a list of pairs.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 746
Create a program with a helper function `find_gcd(a, b)` that finds the greatest common divisor of two numbers, and use it to find the GCD of a list of pairs.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def find_gcd(a, b):  # Method: find_gcd
    while b:
        a, b = b, a % b
    return a  # Return the result

def gcd_of_pairs(lst):  # Method: gcd_of_pairs
    def gcd_pair(pair):  # Method: gcd_pair
        return find_gcd(pair[0], pair[1])  # Return the result
    
    return list(map(gcd_pair, lst))  # Return the result

pairs = [(48, 18), (56, 98), (100, 10)]
gcd_results = gcd_of_pairs(pairs)
print(gcd_results)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that defines a helper function `count_occurrences(lst, element)` that counts occurrences of an element in a list, and uses it for a given list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 747
Write a program that defines a helper function `count_occurrences(lst, element)` that counts occurrences of an element in a list, and uses it for a given list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_elements(lst):  # Method: lst_elements
    element = "tree" 
    return count_occurrences(lst, element)  # Return the result
    
def count_occurrences(lst, element):  # Method: count_occurrences
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count  # Return the result
    
lst = ["tree", "tree", "tree", "sand"]
print(lst_elements(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Define a helper function `sort_list(lst)` that sorts a list and returns the sorted list, and use it to sort several lists.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 748
Define a helper function `sort_list(lst)` that sorts a list and returns the sorted list, and use it to sort several lists.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_words(lst1, lst2):  # Method: lst_words
    return sort_lst(lst1), sort_lst(lst2)  # Return the result


def sort_lst(lst):  # Method: sort_lst
    return sorted(lst)  # Return the result


lst1 = ["zebra", "frog", "toad", "anaconda", "baboon"]
lst2 = ["ktm", "Honda", "Suzuki"]
sorted_lists = lst_words(lst1, lst2)
print(sorted_lists)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a program with a helper function `extract_domain(url)` that extracts the domain from a URL, and use it on a list of URLs.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 749
Create a program with a helper function `extract_domain(url)` that extracts the domain from a URL, and use it on a list of URLs.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def domain_names(lst):  # Method: domain_names
    return list(map(extract_URL, lst))  # Return the result
        
def extract_URL(url):  # Method: extract_URL
    site_name = url.split("//")[1]
    return site_name  # Return the result

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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that defines a helper function `remove_duplicates(lst)` that removes duplicate elements from a list, and uses it on a sample list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 750
Write a program that defines a helper function `remove_duplicates(lst)` that removes duplicate elements from a list, and uses it on a sample list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_sites(lst):  # Method: lst_sites
    return remove_duplicates(lst)  # Return the result

    
def remove_duplicates(lst):  # Method: remove_duplicates
    return list(set(lst))  # Return the result
    

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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Define a helper function `flatten_list(nested_list)` that flattens a nested list, and use it to flatten a list of lists.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 751
Define a helper function `flatten_list(nested_list)` that flattens a nested list, and use it to flatten a list of lists.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(lst):  # Method: main
    result = []
    for i in lst:
        for j in i:
            result.append(j)       
    return result  # Return the result

lst  = [["list1", "list2"], ["list3", "list4"]]
print(main(lst))

def lst_of_lists(nested_list):  # Method: lst_of_lists
    return flatten_list(nested_list)  # Return the result

def flatten_list(nested_list):  # Method: flatten_list
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list  # Return the result

nested_list = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9],
    [10]
]

print(lst_of_lists(nested_list))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a program with a helper function `is_prime(n)` that checks if a number is prime, and uses it to filter a list of numbers.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 752
Create a program with a helper function `is_prime(n)` that checks if a number is prime, and uses it to filter a list of numbers.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def filter_primes(lst):  # Method: filter_primes
    return list(filter(is_prime, lst))  # Return the result
    
def is_prime(n):  # Method: is_prime
    if n <= 1:
        return False  # Return the result
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Return the result
    return True  # Return the result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(filter_primes(numbers))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that defines a helper function `calculate_factorial(n)` that calculates the factorial of a number, and uses it for a range of numbers.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 753
Write a program that defines a helper function `calculate_factorial(n)` that calculates the factorial of a number, and uses it for a range of numbers.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(lst):  # Method: main
    def inner(n):  # Method: inner
        factorial = 1
        for num in range(1, n + 1):
            factorial *= num
        return factorial  # Return the result
    return list(map(inner, lst))  # Return the result
            
lst = [4,5,6,7]
main(lst)

def lst_of_numbers(lst):  # Method: lst_of_numbers
    return list(map(calculate_factorial, lst))  # Return the result

def calculate_factorial(num):  # Method: calculate_factorial
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial  # Return the result

lst = [2, 4, 7, 8]
print(lst_of_numbers(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Define a helper function `sort_dict_by_value(d)` that sorts a dictionary by its values, and use it to sort a given dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 754
Define a helper function `sort_dict_by_value(d)` that sorts a dictionary by its values, and use it to sort a given dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(dic):  # Method: main
    return sort_dict_by_value(dic)  # Return the result

def sort_dict_by_value(d):  # Method: sort_dict_by_value
    return dict(sorted(d.items(), key=get_value))  # Return the result

def get_value(item):  # Method: get_value
    return item[1]  # Return the result

dic = {
    "name": 2,
    "age": 5,
    "city": 1,
    "job": 3
}    
print(main(dic))

def main(dic):  # Method: main
    return sort_dict_by_value(dic)  # Return the result

def sort_dict_by_value(d):  # Method: sort_dict_by_value
    sorted_items = sorted(d.items(), key=get_value)

    result = {}
    for key, value in sorted_items:
        result[key] = value
    return result  # Return the result

dic = {
    "name": 2,
    "age": 5,
    "city": 1,
    "job": 3
}    
print(main(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a program with a helper function `get_unique_elements(lst)` that returns the unique elements of a list, and uses it on a sample list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 755
Create a program with a helper function `get_unique_elements(lst)` that returns the unique elements of a list, and uses it on a sample list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(lst):  # Method: main
    return get_unique_elements(lst)  # Return the result
    
def get_unique_elements(word):  # Method: get_unique_elements
    return list(set(word))  # Return the result


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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that defines a helper function `check_anagram(str1, str2)` that checks if two strings are anagrams, and uses it on a list of string pairs.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 756
Write a program that defines a helper function `check_anagram(str1, str2)` that checks if two strings are anagrams, and uses it on a list of string pairs.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(str1, str2):  # Method: main
    return check_anagram(str1, str2)  # Return the result

def check_anagram(x, y):  # Method: check_anagram
    return sorted(x) == sorted(y)  # Return the result

str1 = "evil"
str2 = "vile"
print(main(str1, str2))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Define a helper function `find_index(lst, element)` that returns the index of an element in a list, and uses it for a given list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 757
Define a helper function `find_index(lst, element)` that returns the index of an element in a list, and uses it for a given list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(lst1, target1):  # Method: main
    return find_index(lst, target1)  # Return the result
    
    
def find_index(lst, target):  # Method: find_index
    for index, word in enumerate(lst):
        if word == target:
            return index  # Return the result
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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a program with a helper function `generate_fibonacci(n)` that generates the first `n` Fibonacci numbers, and uses it to print Fibonacci sequences.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 758
Create a program with a helper function `generate_fibonacci(n)` that generates the first `n` Fibonacci numbers, and uses it to print Fibonacci sequences.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(n):  # Method: main
    return generate_fibonacci(n)  # Return the result


def generate_fibonacci(n):  # Method: generate_fibonacci
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence  # Return the result

n = 10 
print(main(n))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that defines a helper function `calculate_average(lst)` that calculates the average of a list, and uses it on multiple lists.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 759
Write a program that defines a helper function `calculate_average(lst)` that calculates the average of a list, and uses it on multiple lists.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(lst1, lst2):  # Method: main
    avg1 = calculate_average(lst1)
    avg2 = calculate_average(lst2)
    return avg1, avg2  # Return the result

def calculate_average(lst):  # Method: calculate_average
    length_lst = len(lst)
    total = sum(lst)
    average = total / length_lst
    return average  # Return the result

list1 = [3, 7, 2, 9, 12, 5]
list2 = [14, 6, 8, 11, 3, 10]
print(main(list1, list2))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Define a helper function `convert_to_kilometers(miles)` that converts miles to kilometers, and uses it to convert a list of distances.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 760
Define a helper function `convert_to_kilometers(miles)` that converts miles to kilometers, and uses it to convert a list of distances.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(lst):  # Method: main
    return list(map(convert_to_kilometers, lst))  # Return the result

def convert_to_kilometers(miles):  # Method: convert_to_kilometers
    miles_to_km = 1.60934 
    kilometers = miles * miles_to_km
    return kilometers  # Return the result

lst = [34, 67, 157]
print(main(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a program with a helper function `get_last_n_elements(lst, n)` that returns the last `n` elements of a list, and uses it on a sample list. For example 
lst = [1, 2, 3, 4, 5, 6]
n = 3
result = [1, 2, 3]
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 761
Create a program with a helper function `get_last_n_elements(lst, n)` that returns the last `n` elements of a list, and uses it on a sample list. For example 
lst = [1, 2, 3, 4, 5, 6]
n = 3
result = [1, 2, 3]
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(lst, n):  # Method: main
    return get_last_n_elements(lst, n)  # Return the result
    
def get_last_n_elements(lst, n):  # Method: get_last_n_elements
    return lst[:n]  # Return the result
       
lst = [1, 2, 3, 4, 5, 6]
n = 3    
print(main(lst, n))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that defines a helper function `remove_whitespace(s)` that removes whitespace from a string, and uses it on a list of strings.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 762
Write a program that defines a helper function `remove_whitespace(s)` that removes whitespace from a string, and uses it on a list of strings.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(string):  # Method: main
    return remove_whitespace(string)  # Return the result

def remove_whitespace(s):  # Method: remove_whitespace
    return s.replace(" ", "")  # Return the result

string = "today I'm going to the shopping centre"
print(main(string))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Define a helper function `get_positive_numbers(lst)` that returns only the positive numbers from a list, and uses it on a sample list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 763
Define a helper function `get_positive_numbers(lst)` that returns only the positive numbers from a list, and uses it on a sample list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(lst):  # Method: main
    return list(filter(get_positive_numbers, lst))  # Return the result

def get_positive_numbers(number):  # Method: get_positive_numbers
    return number > 0  # Return the result

lst = [1, -2, 2, -3, 3, 4, -4]    
print(main(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a program with a helper function `get_common_elements(lst1, lst2)` that returns common elements between two lists, and uses it on two sample lists.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 764
Create a program with a helper function `get_common_elements(lst1, lst2)` that returns common elements between two lists, and uses it on two sample lists.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def get_common_elements(lst1, lst2):  # Method: get_common_elements
    common_word = []
    for word in lst1:
        if word in lst2:
            common_word.append(word)
    return common_word  # Return the result
  
lst1 = ["tree", "boat", "sea", "dog"]
lst2 = ["boat", "cat", "sea"]
print(get_common_elements(lst1, lst2))

def main(lst1, lst2):  # Method: main
    return get_common_elements(lst1, lst2)  # Return the result

def get_common_elements(x, y):  # Method: get_common_elements
    duplicates = []
    for item in x:
        if item in y and item not in duplicates:
            duplicates.append(item)
    return duplicates  # Return the result

lst1 = ["tree", "boat", "sea", "dog"]
lst2 = ["boat", "cat", "sea"]
print(main(lst1, lst2))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that defines a helper function `check_even_odd(n)` that returns "Even" or "Odd" for a number, and uses it for a list of numbers.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 765
Write a program that defines a helper function `check_even_odd(n)` that returns "Even" or "Odd" for a number, and uses it for a list of numbers.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(lst):  # Method: main
    return list(map(check_even_odd, lst))  # Return the result

def check_even_odd(n):  # Method: check_even_odd
    if n % 2 == 0:
        return "Even"  # Return the result
    else:
        return "Odd"  # Return the result

lst = [45, 7, 2, 3, 68, 36]
print(main(lst))

def main(lst):  # Method: main
    results = []
    for number in lst:
        results.append(check_even_odd(number))
    return results  # Return the result

def check_even_odd(n):  # Method: check_even_odd
    if n % 2 == 0:
        return "Even"  # Return the result
    else:
        return "Odd"  # Return the result

lst = [45, 7, 2, 3, 68, 36]
print(main(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Define a helper function `convert_to_uppercase(word)` that converts a word to uppercase, and uses it on a list of words.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 766
Define a helper function `convert_to_uppercase(word)` that converts a word to uppercase, and uses it on a list of words.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(lst):  # Method: main
    return list(map(convert_to_uppercase, lst))  # Return the result

def convert_to_uppercase(word):  # Method: convert_to_uppercase
    return word.upper()  # Return the result

lst = ["eorl", "sitting", "kong"]
print(main(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a program with a helper function `count_characters(s)` that counts the characters in a string, and uses it on a list of strings.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 767
Create a program with a helper function `count_characters(s)` that counts the characters in a string, and uses it on a list of strings.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(lst_str):  # Method: main
    return list(map(count_characters, lst_str))  # Return the result

def count_characters(s):  # Method: count_characters
    return len(s)  # Return the result

lst_str = ["eorl", "sitting", "mountain"]
print(count_characters(lst_str))


def main(lst_str):  # Method: main
    return list(map(count_characters, lst_str))  # Apply count_characters to each string in the list  # Return the result

def count_characters(s):  # Method: count_characters
    return len(s)  # Return the result

lst_str = ["eorl", "sitting", "mountain"]
print(main(lst_str))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that defines a helper function `remove_special_characters(s)` that removes special characters from a string, and uses it on a sample list of strings.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 768
Write a program that defines a helper function `remove_special_characters(s)` that removes special characters from a string, and uses it on a sample list of strings.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(lst):  # Method: main
    return list(map(remove_special_characters, lst))  # Return the result

def remove_special_characters(s):  # Method: remove_special_characters
    s = s.replace('@', '').replace('?', '')
    return s  # Return the result

lst = ["eor?@l", "s@itting?", "@mountain?"] 
print(main(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Define a helper function `is_substring(s1, s2)` that checks if `s1` is a substring of `s2`, and uses it on a list of string pairs.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 769
Define a helper function `is_substring(s1, s2)` that checks if `s1` is a substring of `s2`, and uses it on a list of string pairs.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(lst):  # Method: main
    results = []
    for pair in lst:
        results.append(is_substring(pair[0], pair[1]))
    return results  # Return the result

def is_substring(s1, s2):  # Method: is_substring
    return s1 in s2  # Return the result

lst = [("apple", "pineapple"), ("dog", "doghouse"), ("cat", "concatenate")]
print(main(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Create a program with a helper function `sum_of_list(lst)` that returns the sum of all numbers in a list, and uses it on a sample list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 770
Create a program with a helper function `sum_of_list(lst)` that returns the sum of all numbers in a list, and uses it on a sample list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(lst):  # Method: main
    return sum_of_list(lst)  # Return the result
    
def sum_of_list(n):  # Method: sum_of_list
    count = 0
    for n in lst:
        count += n
    return count  # Return the result

lst = [2, 2, 2, 2, 2]
print(main(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a program that defines a helper function `get_even_numbers(lst)` that filters and returns even numbers from a list, and uses it on a sample list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 771
Write a program that defines a helper function `get_even_numbers(lst)` that filters and returns even numbers from a list, and uses it on a sample list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(lst):  # Method: main
    return list(filter(get_even_numbers, lst))  # Return the result

def get_even_numbers(n):  # Method: get_even_numbers
    return n % 2 == 0  #  # Return the result

lst = [46, 22, 7, 4, 8, 13]
print(main(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Define a helper function `merge_sorted_lists(lst1, lst2)` that merges and sorts two lists, and uses it to combine multiple sorted lists.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 772
Define a helper function `merge_sorted_lists(lst1, lst2)` that merges and sorts two lists, and uses it to combine multiple sorted lists.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(lst1, lst2):  # Method: main
    return merge_sorted_lists(lst1, lst2)  # Return the result

def merge_sorted_lists(x, y):  # Method: merge_sorted_lists
    return sorted(x + y)  # Return the result

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]   
print(main(lst1, lst2))

def main(lst1, lst2):  # Method: main
    sort1 = sorted(lst1)
    sort2 = sorted(lst2)
    merge_lst = {*sort1, *sort2}
    return merge_lst  # Return the result
    
lst1 = [1, 33, 8]
lst2 = [9, 2, 7]
main(lst1, lst2)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a dictionary from two lists, one containing keys and the other containing values.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 773
Write a Python program to create a dictionary from two lists, one containing keys and the other containing values.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_to_dic(lst1, lst2):  # Method: lst_to_dic
    result = {}
    
    for x, y in zip(lst1, lst2):
        result[x] = y
    return result  # Return the result

lst1 = [1, 2, 3]
lst2 = ["start", "middle", "end"]
print(lst_to_dic(lst1, lst2))

def lst_to_dic(lst1, lst2):  # Method: lst_to_dic
    result = {}
    
    for i in range(len(lst1)):
        result[lst1[i]] = lst2[i]
    return result  # Return the result

lst1 = [1, 2, 3]
lst2 = ["start", "middle", "end"]
print(lst_to_dic(lst1, lst2))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get the value of a specific key from a dictionary, or return a default value if the key is not found.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 774
Write a Python program to get the value of a specific key from a dictionary, or return a default value if the key is not found.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(dic, key_to_find):  # Method: main
    return dic.get(key_to_find, None)  # Return the result

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

def value_of_specific_key(dic, target):  # Method: value_of_specific_key
    return dic.get(target, "Default value")  # Return the result
    
dic = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "job": "Engineer"
}
target = "age"
print(value_of_specific_key(dic, target))

def value_of_specific_key(dic, target):  # Method: value_of_specific_key
    for key, value in dic.items():
        if key == target:
            return value  # Return the result
    return None  # Return the result
    
dic = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "job": "Engineer"
}
target = "age"
print(value_of_specific_key(dic, target))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to merge two dictionaries into one.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 775
Write a Python program to merge two dictionaries into one.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(dic1, dic2):  # Method: main
    merge_dic = dic1.copy()  
    for key, value in dic2.items():
        if key in merge_dic:
            merge_dic[key] = [merge_dic[key], value]
        else:
            merge_dic[key] = value
    return merge_dic  # Return the result

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

def merge_dicts(dic1, dic2):  # Method: merge_dicts
    merged_dict = {**dic1, **dic2}
    return merged_dict  # Return the result

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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove a key from a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 776
Write a Python program to remove a key from a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def remove_key(dic, key_to_remove):  # Method: remove_key
    if key_to_remove in dic:
        del dic[key_to_remove]
    return dic  # Return the result

dic = {
    "name": "Steven",
    "age": 56,
    "city": "New York",
    "job": "Engineer"
}
key_to_remove = "age"
print(remove_key(dic, key_to_remove))

def main(dic, target):  # Method: main
    result = {}
    for key, value in dic.items():
        if key != target:
            result[key] = value
    return result  # Return the result
    
dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
target = "job"
print(main(dic, target))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to iterate over the keys and values of a dictionary and print them in the format `key: value`.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 777
Write a Python program to iterate over the keys and values of a dictionary and print them in the format `key: value`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def print_dict_items(dic):  # Method: print_dict_items
    for key, value in dic.items():
        print(f"{key}: {value}")

dic = {
    "name": "Steven",
    "age": 56,
    "city": "New York",
    "job": "Engineer"
}
print_dict_items(dic)

def main(dic):  # Method: main
    result = ""
    for key, value in dic.items():
        result += f"{key}: {value}, \n"
    print(result)
        
dic = {"apple": 1, "orange": 33, "mango": 5}
main(dic)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a given key exists in a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 778
Write a Python program to check if a given key exists in a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(dic1):  # Method: main
    if target in dic1.keys():
        return True  # Return the result
    return False  # Return the result
           
dic1 = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
target = "names"
print(main(dic1))

def does_key_exist(dic, target):  # Method: does_key_exist
    for key in dic.keys():
        if key == target:
            return "key exists"  # Return the result
    return "key does not exist"  # Return the result

print(does_key_exist({"name": "Steven", "age": 56}, "job"))
print(does_key_exist({"name": "Steven", "age": 56}, "name"))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a dictionary by its keys.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 779
Write a Python program to sort a dictionary by its keys.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sort_dic(dic):  # Method: sort_dic
    return dict(sorted(dic.items()))  # Return the result

dic = {
    "name": "Steven",
    "age": 56,
    "city": "New York",
    "job": "Engineer"
}
print(sort_dic(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a dictionary by its values.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 780
Write a Python program to sort a dictionary by its values.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(dic):  # Method: main
    dic = dic.items()

    def sort_value(item):  # Method: sort_value
        return item[1]  # Return the result
        
    return dict(sorted(dic, key=sort_value))  # Return the result
    
         
dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
print(main(dic))

def sort_values(dic):  # Method: sort_values
    sorted_items = sorted(dic.items(), key=sort_key)
    return dict(sorted_items)  # Return the result

def sort_key(item):  # Method: sort_key
    return item[1]  # Return the result

dic = {
    "cat": 34,
    "dog": 56,
    "rabbit": 566,
    "fish": 4
}
print(sort_values(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count the frequency of elements in a list and store the result in a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 781
Write a Python program to count the frequency of elements in a list and store the result in a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def frequency_elements(lst):  # Method: frequency_elements
    result = {}
    for word in lst:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1   
    return result  # Return the result
    
lst = ["tree", "tree", "flower", "flower"]
print(frequency_elements(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a dictionary where the keys are numbers from 1 to 5, and the values are the squares of the keys.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 782
Write a Python program to create a dictionary where the keys are numbers from 1 to 5, and the values are the squares of the keys.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def square_dic():  # Method: square_dic
    result = {}
    for key in range(1, 6):
        result[key] = key ** 2
    return result  # Return the result
        
print(square_dic())

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to update the value of an existing key in a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 783
Write a Python program to update the value of an existing key in a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(dic, target):  # Method: main
    key_to_update, new_value = target
    if key_to_update in dic:
        dic[key_to_update] = new_value
    return dic  # Return the result

dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
target = ("city", 78)
print(main(dic, target))


def update_value(dic, key, new_value):  # Method: update_value
    if key in dic:
        dic[key] = new_value
    return dic  # Return the result

dic = {
    "name": "Steven",
    "age": 56,
    "city": "New York",
    "job": "Engineer"
}

update_value(dic, "age", 60)
print(dic)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get all the keys from a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 784
Write a Python program to get all the keys from a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def get_keys(dic):  # Method: get_keys
    return dic.keys()  # Return the result

dic = {
    "name": "Steven",
    "age": 56,
    "city": "New York",
    "job": "Engineer"
}
print(get_keys(dic))

def main(dic):  # Method: main
    for key in dic:
        print(key)
        
dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
print(main(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get all the values from a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 785
Write a Python program to get all the values from a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def get_keys(dic):  # Method: get_keys
    return dic.values()  # Return the result

dic = {
    "name": "Steven",
    "age": 56,
    "city": "New York",
    "job": "Engineer"
}
print(get_keys(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get all the values from a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 786
Write a Python program to get all the values from a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def get_keys(dic):  # Method: get_keys
    return dic.values()  # Return the result

dic = {
    "name": "Steven",
    "age": 56,
    "city": "New York",
    "job": "Engineer"
}
print(get_keys(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the key with the largest value in a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 787
Write a Python program to find the key with the largest value in a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def largest_value(dic):  # Method: largest_value
    return max(dic.values())  # Return the result

dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
print(largest_value(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the key with the smallest value in a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 788
Write a Python program to find the key with the smallest value in a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def largest_value(dic):  # Method: largest_value
    return min(dic.values())  # Return the result

dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
print(largest_value(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to convert two lists into a dictionary, where one list contains keys and the other contains values, but skip values if the lists are of unequal length.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 789
Write a Python program to convert two lists into a dictionary, where one list contains keys and the other contains values, but skip values if the lists are of unequal length.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_dic(lst1, lst2):  # Method: lst_dic
    result = {}
    min_length = min(len(lst1), len(lst2))
    
    for i in range(min_length):
        result[lst1[i]] = lst2[i]
    
    return result  # Return the result

lst1 = [1, 2, 3]
lst2 = ["sand", "rock", "beach", "sea"]
print(lst_dic(lst1, lst2))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to combine two dictionaries by adding values of common keys.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 790
Write a Python program to combine two dictionaries by adding values of common keys.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def combine_dictionaries(dic1, dic2):  # Method: combine_dictionaries
    result = {}
    for key in dic1:
        result[key] = dic1[key]
    for key, value in dic2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result  # Return the result

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

def combine_dictionaries(dic1, dic2):  # Method: combine_dictionaries
    result = dic1.copy()
    for key, value in dic2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result  # Return the result

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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to invert the keys and values of a dictionary (i.e., make the keys the values and the values the keys).
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 791
Write a Python program to invert the keys and values of a dictionary (i.e., make the keys the values and the values the keys).
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def invert_dictionary(dic):  # Method: invert_dictionary
    inverted = {}
    for key, value in dic.items():
        inverted[value] = key
    return inverted  # Return the result

dic = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(invert_dictionary(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove duplicate values from a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 792
Write a Python program to remove duplicate values from a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def remove_duplicates_values(dic):  # Method: remove_duplicates_values
    unique_values = {}
    for key, value in dic.items():
        if value not in unique_values.values():
            unique_values[key] = value
    return unique_values  # Return the result

dic = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "job": "Engineer",
    "nickname": "Alice" 
}
print(remove_duplicates_values(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if two dictionaries have the same keys.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 793
Write a Python program to check if two dictionaries have the same keys.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def same_keys(dic1, dic2):  # Method: same_keys
    return dic1.keys() == dic2.keys()  # Return the result

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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to multiply all the values in a dictionary by 2.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 794
Write a Python program to multiply all the values in a dictionary by 2.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def multiply_by2(dic):  # Method: multiply_by2
    result = {}
    for key, value in dic.items():
        result[key] = value * 2 
    return result  # Return the result
    
dic = {"a": 2, "b": 8}    
print(multiply_by2(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the length (i.e., number of key-value pairs) of a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 795
Write a Python program to find the length (i.e., number of key-value pairs) of a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def len_key_value_pair(dic):  # Method: len_key_value_pair
    return len(dic)  # Return the result

dic = {
    "name": "Alice",
    "ages": "stop",
    "cities": "New York",
    "job": "Engineer",
    "nickname": "Alice" 
}
print(len_key_value_pair(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to map a list of strings to their lengths using a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 796
Write a Python program to map a list of strings to their lengths using a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def map_lst_string_dic(lst):  # Method: map_lst_string_dic
    result = {}
    for word in lst:
        result[word] = len(word)
    return result  # Return the result

lst = ["it", "shop", "jonny"]
print(map_lst_string_dic(lst))

def len_dic(lst):  # Method: len_dic
    result = {}
    for word in lst:
        count = 0
        for char in word:
            count += 1
        result[word] = count
    return result  # Return the result
    

lst = ["not", "house", "Jonathan"]
print(len_dic(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to add a new key-value pair to an existing dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 797
Write a Python program to add a new key-value pair to an existing dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def add_key_value_pair(dic):  # Method: add_key_value_pair
    dic["new_key"] = "new_value"
    return dic  # Return the result
    
dic = {
    "name": "Alice",
    "ages": "stop",
    "cities": "New York",
    "job": "Engineer",
    "nickname": "Alice" 
}
print(add_key_value_pair(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a dictionary with keys as numbers from 1 to 10 and values as their cubes.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 798
Write a Python program to create a dictionary with keys as numbers from 1 to 10 and values as their cubes.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def value_cubes():  # Method: value_cubes
    result = {}
    for num in range(1, 6):
        result[num] = num ** 3
    return result  # Return the result
    
print(value_cubes())

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a dictionary is empty.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 799
Write a Python program to check if a dictionary is empty.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def check_if_empty(dic):  # Method: check_if_empty
    if not dic: 
        return "Dictionary is empty"  # Return the result
    return "Dictionary is not empty"  # Return the result

dic = {
    "name": "Alice",
    "ages": "stop",
    "cities": "New York",
    "job": "Engineer",
    "nickname": "Alice" 
}
print(check_if_empty(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove a set of keys from a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 800
Write a Python program to remove a set of keys from a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def remove_set_keys(dic, keys_to_remove):  # Method: remove_set_keys
    result = {}
    for key, value in dic.items():
        if key not in keys_to_remove:
            result[key] = value
    return result  # Return the result

dic = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "job": "Engineer",
    "nickname": "Alice"
}
keys_to_remove = {"age", "city"}
print(remove_set_keys(dic, keys_to_remove))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to convert a dictionary into a list of tuples, where each tuple contains a key-value pair.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 801
Write a Python program to convert a dictionary into a list of tuples, where each tuple contains a key-value pair.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def dic_lst_tuples(dic):  # Method: dic_lst_tuples
    return list(dic.items())  # Return the result
    
dic = {
    "name": "Alice",
    "ages": "stop",
    "cities": "New York",
    "job": "Engineer",
    "nickname": "Alice" 
}
print(dic_lst_tuples(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find all keys in a dictionary that map to a given value.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 802
Write a Python program to find all keys in a dictionary that map to a given value.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(dic):  # Method: main
    result = {}
    
    for key, value in dic.items():
        if value == 1:
            result[key] = value
    return tuple(result.keys())  # Return the result
    
dic = {
    "name": 1,
    "age": 56,
    "city": 34,
    "job": 1
}
print(main(dic))

def map_value(dic, target_value):  # Method: map_value
    result = {}
    for key, value in dic.items():
        if value == target_value:
            result[key] = value
    return result  # Return the result

dic = {
    "name": "Alice",
    "ages": "Alice",
    "cities": "New York",
    "job": "Engineer",
    "nickname": "Alice" 
}
target_value = "Alice"
print(map_value(dic, target_value))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to replace the value of a key in a dictionary with a list of values if the value is not already a list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 803
Write a Python program to replace the value of a key in a dictionary with a list of values if the value is not already a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def replace_value(dic, list_values):  # Method: replace_value
    for key in dic:
        if not isinstance(dic[key], list):
            dic[key] = list_values
    return dic  # Return the result

dic = {
    "name": "Alice",
    "ages": "Alice",
    "cities": "New York",
    "job": "Engineer",
    "nickname": "Alice" 
}
list_values = ["one", "two", "three", "four", "five"]
print(replace_value(dic, list_values))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a nested dictionary where keys are numbers and values are dictionaries containing the squares and cubes of the keys.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 804
Write a Python program to create a nested dictionary where keys are numbers and values are dictionaries containing the squares and cubes of the keys.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def nested_dic():  # Method: nested_dic
    result = {}
    for key in range(1, 6):
        result[key] = {'square': key ** 2, 'cube': key ** 3}
    return result  # Return the result

print(nested_dic())

def nested_dic():  # Method: nested_dic
    result = {}
    for key in range(1, 6):
        result[key] = {'square': key ** 2, 'cube': key ** 3}
    return result  # Return the result

result = nested_dic()
for key, value in result.items():
    print(f"{key}: {value}")

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a dictionary from a string where the keys are characters and the values are the number of occurrences of each character.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 805
Write a Python program to create a dictionary from a string where the keys are characters and the values are the number of occurrences of each character.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def string_dic(string):  # Method: string_dic
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result  # Return the result

string = "what's happening today?"
print(string_dic(string))

#new line
def string_dic(string):  # Method: string_dic
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result  # Return the result

string = "what's happening today?"
result = string_dic(string)

for key, value in result.items():
    print(f"{key}: {value}")

#sort keys    
def string_dic(string):  # Method: string_dic
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result  # Return the result

string = "what's happening today?"
result = string_dic(string)

for key in sorted(result):
    print(f"{key}: {result[key]}")

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a dictionary by its values in descending order.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 806
Write a Python program to sort a dictionary by its values in descending order.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def sort_dic(dic):  # Method: sort_dic
    
    def value_sort(item):  # Method: value_sort
        return item[1]  # Return the result
    
    return dict(sorted(dic.items(), key=value_sort, reverse=True))  # Return the result

dic = {
    "name": "Alice",
    "ages": "Alice",
    "cities": "New York",
    "job": "Engineer",
    "nickname": "Alice"
}
print(sort_dic(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a dictionary from a list of tuples.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 807
Write a Python program to create a dictionary from a list of tuples.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def lst_tuples(lst):  # Method: lst_tuples
    return dict(lst)  # Return the result

lst = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]
print(lst_tuples(lst))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to filter out keys from a dictionary that have a value less than 10.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 808
Write a Python program to filter out keys from a dictionary that have a value less than 10.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def less_then_10(dic):  # Method: less_then_10
    result = {}
    for key, value in dic.items():
        if value >= 10:
            result[key] = value
    return result  # Return the result
    
dic = {
    "name": 3,
    "ages": 6,
    "cities": 46,
    "job": 12,
    "nickname": 7 
}
print(less_then_10(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to print the dictionary in a readable, formatted way (pretty printing).
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 809
Write a Python program to print the dictionary in a readable, formatted way (pretty printing).
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def print_readable(dic):  # Method: print_readable
    result = ""
    for key, value in dic.items():
        result += f"{key}: {value}\n"
    return result  # Return the result

dic = {
    "name": 3,
    "ages": 6,
    "cities": 46,
    "job": 12,
    "nickname": 7 
}
print(print_readable(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a dictionary of students and their grades, and print all students who scored more than 75.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 810
Write a Python program to create a dictionary of students and their grades, and print all students who scored more than 75.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def students_grades(dic):  # Method: students_grades
    result = {}
    for key, value in dic.items():
        if value >= 70:
            result[key] = value
    return list(result)  # Return the result
    
dic = {
    "Bob": 50,
    "Alex": 72,
    "Fred": 87,
    "Mike": 60,
    "Liz": 90 
}
print(students_grades(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a dictionary of words and their lengths from a given sentence.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 811
Write a Python program to create a dictionary of words and their lengths from a given sentence.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def word_len(string):  # Method: word_len
    words = string.split()
    result = {}
    for word in words:
        result[word] = len(word)
    return result  # Return the result

string = "today we are going to the beach"
print(word_len(string))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a dictionary of words and their lengths from a given sentence.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 812
Write a Python program to create a dictionary of words and their lengths from a given sentence.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def word_len(string):  # Method: word_len
    words = string.split()
    result = {}
    for word in words:
        result[word] = len(word)
    return result  # Return the result

string = "today we are going to the beach"
print(word_len(string))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to group words in a dictionary based on their starting letter.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 813
Write a Python program to group words in a dictionary based on their starting letter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def starting_letter(dic):  # Method: starting_letter
    result = {}
    for key in dic.keys():
        first_letter = key[0]
        if first_letter not in result:
            result[first_letter] = []
        result[first_letter].append(key)
    return result  # Return the result

dic = {
    "Bob": 50,
    "Alex": 72,
    "Fred": 87,
    "Mike": 60,
    "Liz": 90 
}
print(starting_letter(dic))

def main(dic):  # Method: main
    result = {}
    for key, value in dic.items():
        first_letter = key[0]
        result[first_letter] = key
    return result  # Return the result
    

dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
print(main(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to iterate through a dictionary and change the case of all keys (upper or lower).
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 814
Write a Python program to iterate through a dictionary and change the case of all keys (upper or lower).
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def upper_keys(dic):  # Method: upper_keys
    result = {}
    for key, value in dic.items():
        result[key.upper()] = value
    return result  # Return the result
    
dic = {
    "Bob": 50,
    "Alex": 72,
    "Fred": 87,
    "Mike": 60,
    "Liz": 90 
}
print(upper_keys(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the intersection of two dictionaries (i.e., keys that are common in both dictionaries).
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 815
Write a Python program to find the intersection of two dictionaries (i.e., keys that are common in both dictionaries).
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def intersection(dic1, dic2):  # Method: intersection
    result = {}
    for key in dic1:
        if key in dic2:
            result[key] = dic1[key]
    return result  # Return the result

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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count how many times each vowel occurs in a given sentence using a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 816
Write a Python program to count how many times each vowel occurs in a given sentence using a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def count_vowels(string):  # Method: count_vowels
    vowels = "aeiou"
    result = {}
    
    for vowel in vowels:
        result[vowel] = 0
    
    for char in string.lower():
        if char in vowels:
            result[char] += 1
    
    return result  # Return the result

string = "word how many times vowels? How many times many times many"
print(count_vowels(string))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove all key-value pairs from a dictionary where the value is None.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 817
Write a Python program to remove all key-value pairs from a dictionary where the value is None.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def remove_value_is_none(dic):  # Method: remove_value_is_none
    result = {}
    for key, value in dic.items():
        if value is not None:
            result[key] = value
    return result  # Return the result

dic1 = {
    "Bob": None,
    "Alex": None,
    "Fred": 89,
    "Mike": 61,
    "Liz": 90 
}
print(remove_value_is_none(dic1))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a dictionary contains a specific key and value pair.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 818
Write a Python program to check if a dictionary contains a specific key and value pair.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def check_key_value(dic, target):  # Method: check_key_value
    for key, value in dic.items():
        if key in target and dic[key] == target[key]:
            return True  # Return the result
    return False  # Return the result

dic1 = {
    "Bob": 500,
    "Alex": 72,
    "Fred": 89,
    "Mike": 61,
    "Liz": 90 
}
target = {"Liz": 90}
print(check_key_value(dic1, target))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to convert a dictionary to JSON format using `json.dumps()`.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 819
Write a Python program to convert a dictionary to JSON format using `json.dumps()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

import json  # Import module

def dict_to_json(dic):  # Method: dict_to_json
    return json.dumps(dic)  # Return the result

dic1 = {
    "Bob": 500,
    "Alex": 72,
    "Fred": 89,
    "Mike": 61,
    "Liz": 90
}
print(dict_to_json(dic1))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to merge multiple dictionaries into one.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 820
Write a Python program to merge multiple dictionaries into one.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def merge_dicts(dic1, dic2):  # Method: merge_dicts
    merged_dict = {**dic1, **dic2}
    return merged_dict  # Return the result

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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to iterate through a dictionary and calculate the product of all its values.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 821
Write a Python program to iterate through a dictionary and calculate the product of all its values.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def product_values(dic):  # Method: product_values
    product = 1
    for value in dic.values():
        product *= value
    return product  # Return the result

dic = {
    "named": 2,
    "aged": 2,
    "cities": 2,
    "jobless": 2
}
print(product_values(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to calculate the average of all values in a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 822
Write a Python program to calculate the average of all values in a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def average_values(dic):  # Method: average_values
    sum_values = sum(dic.values())
    len_values = len(dic)
    average = sum_values / len_values
    return average  # Return the result

dic = {
    "named": 200,
    "aged": 257,
    "cities": 230,
    "jobless": 280
}
print(average_values(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to swap the values of two keys in a dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 823
Write a Python program to swap the values of two keys in a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(dic):  # Method: main
    dic["city"] = 1
    dic["job"] = 34
    return dic  # Return the result
        
dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
target = ("city", "job")
print(main(dic))

def main(dic, x, y):  # Method: main
    result = {}
    reverse_values = dic[x], dic[y] = dic[y], dic[x]

    for key, value in dic.items():
        if reverse_values not in result:
            result[key] = value
    return result  # Return the result
        
dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
print(main(dic, "name", "job"))

def main(dic, change_keys):  # Method: main
    result = {}
    change_keys = dic["name"], dic["job"] = dic["job"], dic["name"]

    for key, value in dic.items():
        if change_keys not in result:
            result[key] = value
    return result  # Return the result
        
dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
change_keys = {"name", "job"}
print(main(dic, change_keys))

def swap_values(dic, key1, key2):  # Method: swap_values
    dic[key1], dic[key2] = dic[key2], dic[key1]
    return dic  # Return the result

dic = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(swap_values(dic, "a", "c"))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the key with the largest value in a dictionary. Do not use max().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 824
Write a Python program to find the key with the largest value in a dictionary. Do not use max().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def largest_value(dic):  # Method: largest_value
    largest_key = None
    largest_val = float('-inf')
    
    for key, value in dic.items():
        if value > largest_val:
            largest_val = value
            largest_key = key
    
    return largest_key  # Return the result

dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
print(largest_value(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the key with the largest value in a dictionary. Do not use min().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 825
Write a Python program to find the key with the largest value in a dictionary. Do not use min().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def smallest_value(dic):  # Method: smallest_value
    smallest_key = None
    smallest_val = float('inf')
    
    for key, value in dic.items():
        if value < smallest_val:
            smallest_val = value
            smallest_key = key
    
    return smallest_key  # Return the result

dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
print(smallest_value(dic))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to add multiple new key-value pair to an existing dictionary.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 826
Write a Python program to add multiple new key-value pair to an existing dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(dic):  # Method: main
    dic["first"] = 1
    dic["second"] = 2
    return dic  # Return the result
    

dic = {
    "name": 777,
    "age": 56,
    "city": 34,
    "job": 1
}
print(main(dic))


def add_multiple_pairs(dic, new_pairs):  # Method: add_multiple_pairs
    dic.update(new_pairs)
    return dic  # Return the result

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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that prints numbers from 1 to 10 using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 827
Write a Python program that prints numbers from 1 to 10 using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

i = 1
while i <= 10:
    print(i)
    i += 1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that prints even numbers between 1 and 20 using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 828
Write a Python program that prints even numbers between 1 and 20 using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

i = 2
while i <= 20:
    print(i)
    i += 2

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to print all the numbers from 10 to 1 (in reverse order) using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 829
Write a Python program to print all the numbers from 10 to 1 (in reverse order) using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

i = 10
while i >= 1:
    print(i)
    i -= 1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that asks the user for a number and keeps printing “Hello” that many times using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 830
Write a Python program that asks the user for a number and keeps printing “Hello” that many times using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

count = int(input("Enter a number: "))
i = 0
while i < count:
    print("Hello")
    i += 1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that keeps asking the user for input until they type “exit”.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 831
Write a Python program that keeps asking the user for input until they type “exit”.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

user_input = ""
while user_input != "exit":
    user_input = input("Enter something (type 'exit' to stop): ")

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sum all numbers from 1 to 100 using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 831
Write a Python program to sum all numbers from 1 to 100 using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print(total)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that keeps doubling a number (starting from 1) until it exceeds 1000 using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 832
Write a Python program that keeps doubling a number (starting from 1) until it exceeds 1000 using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

number = 1
while number <= 1000:
    print(number)
    number *= 2

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that prints the multiplication table of 5 using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 833
Write a Python program that prints the multiplication table of 5 using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

i = 1
while i <= 10:
    print(5 * i)
    i += 1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that asks the user for numbers and stops when the sum exceeds 50 using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 834
Write a Python program that asks the user for numbers and stops when the sum exceeds 50 using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

total = 0
while total <= 50:
    number = int(input("Enter a number: "))
    total += number
print(total)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that keeps asking the user for input until they enter an even number using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 835
Write a Python program that keeps asking the user for input until they enter an even number using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

number = 1
while number % 2 != 0:
    number = int(input("Enter an even number: "))

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that asks the user to input numbers, and prints the sum when they input the number 0 using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 836
Write a Python program that asks the user to input numbers, and prints the sum when they input the number 0 using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

total = 0
number = None
while number != 0:
    number = int(input("Enter a number (0 to stop): "))
    total += number
print(total)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that prints the Fibonacci sequence up to the 10th number using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 837
Write a Python program that prints the Fibonacci sequence up to the 10th number using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

a, b = 0, 1
i = 0
while i < 10:
    print(a)
    a, b = b, a + b
    i += 1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that keeps asking the user to guess a secret number between 1 and 10 until they guess it correctly using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 838
Write a Python program that keeps asking the user to guess a secret number between 1 and 10 until they guess it correctly using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

secret_number = 7
guess = 0
while guess != secret_number:
    guess = int(input("Guess the secret number (between 1 and 10): "))

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that counts the number of vowels in a user-provided string using a while loop.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 839
Write a Python program that counts the number of vowels in a user-provided string using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
i = 0
count = 0
while i < len(string):
    if string[i] in vowels:
        count += 1
    i += 1
print(count)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that asks the user to input a string and keeps removing the last character of the string until it’s empty using a while loop.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 840
Write a Python program that asks the user to input a string and keeps removing the last character of the string until it’s empty using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

string = input("Enter a string: ")
while string:
    print(string)
    string = string[:-1]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count down from a user-provided number to 0 using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 841
Write a Python program to count down from a user-provided number to 0 using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

number = int(input("Enter a number: "))
while number >= 0:
    print(number)
    number -= 1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to keep asking the user for positive numbers and print the sum when a negative number is entered using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 842
Write a Python program to keep asking the user for positive numbers and print the sum when a negative number is entered using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

total = 0
num = int(input("Enter a positive number: "))
while num >= 0:
    total += num
    num = int(input("Enter another number: "))
print(total)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that asks the user to input numbers and finds the largest number entered using a while loop. Stop when the user types “stop”
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 843
Write a Python program that asks the user to input numbers and finds the largest number entered using a while loop. Stop when the user types “stop”
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

largest = float('-inf')
while True:
    user_input = input("Enter a number (type 'stop' to end): ")
    if user_input == "stop":
        break
    num = int(user_input)
    if num > largest:
        largest = num
print(largest)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that asks the user for a password and keeps asking until the correct password (“python”) is entered using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 844
Write a Python program that asks the user for a password and keeps asking until the correct password (“python”) is entered using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

password = ""
while password != "python":
    password = input("Enter the password: ")

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that multiplies a number by itself until it exceeds 10,000 using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 845
Write a Python program that multiplies a number by itself until it exceeds 10,000 using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

num = 2
while num <= 10000:
    print(num)
    num *= num

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to reverse the digits of a number using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 846
Write a Python program to reverse the digits of a number using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that asks the user to input numbers and prints the average when they type “done” using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 847
Write a Python program that asks the user to input numbers and prints the average when they type “done” using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that asks the user to input a positive number and keeps subtracting 1 until it reaches zero using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 848
Write a Python program that asks the user to input a positive number and keeps subtracting 1 until it reaches zero using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

num = int(input("Enter a positive number: "))
while num > 0:
    print(num)
    num -= 1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that generates random numbers between 1 and 100 and stops when it generates a number divisible by 7 using a while loop.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 849
Write a Python program that generates random numbers between 1 and 100 and stops when it generates a number divisible by 7 using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module
num = random.randint(1, 100)
while num % 7 != 0:
    print(num)
    num = random.randint(1, 100)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to keep asking the user for a number and print whether it is prime or not. Stop when the user types “exit”.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 850
Write a Python program to keep asking the user for a number and print whether it is prime or not. Stop when the user types “exit”.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def is_prime(n):  # Method: is_prime
    if n < 2:
        return False  # Return the result
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Return the result
    return True  # Return the result

while True:
    user_input = input("Enter a number (type 'exit' to stop): ")
    if user_input == "exit":
        break
    num = int(user_input)
    if is_prime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that prints all the letters of a string except the vowels using a while loop.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 851
Write a Python program that prints all the letters of a string except the vowels using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
i = 0
while i < len(string):
    if string[i] not in vowels:
        print(string[i], end="")
    i += 1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count the number of digits in a number using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 852
Write a Python program to count the number of digits in a number using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print(count)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to keep adding numbers to a list until the list contains 10 elements using a while loop.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 853
Write a Python program to keep adding numbers to a list until the list contains 10 elements using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

lst = []
while len(lst) < 10:
    lst.append(int(input("Enter a number: ")))
print(lst)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that keeps dividing a number by 2 until it is smaller than 1 using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 854
Write a Python program that keeps dividing a number by 2 until it is smaller than 1 using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

num = int(input("Enter a number: "))
while num >= 1:
    print(num)
    num /= 2

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that keeps asking the user for input and adds it to a list until the user types “stop”. Then print the list using a while loop.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 855
Write a Python program that keeps asking the user for input and adds it to a list until the user types “stop”. Then print the list using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

lst = []
while True:
    user_input = input("Enter something (type 'stop' to end): ")
    if user_input == "stop":
        break
    lst.append(user_input)
print(lst)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that asks the user for a number and keeps printing its square until the square exceeds 1000 using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 856
Write a Python program that asks the user for a number and keeps printing its square until the square exceeds 1000 using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

num = int(input("Enter a number: "))
while num ** 2 <= 1000:
    print(num ** 2)
    num += 1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that prints all the numbers from 1 to 50, skipping multiples of 3, using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 857
Write a Python program that prints all the numbers from 1 to 50, skipping multiples of 3, using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

num = 1
while num <= 50:
    if num % 3 != 0:
        print(num)
    num += 1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that keeps adding 5 to a number starting from 0 until the number is greater than 100 using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 858
Write a Python program that keeps adding 5 to a number starting from 0 until the number is greater than 100 using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

num = 0
while num <= 100:
    print(num)
    num += 5

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that prints all the elements of a list using a while loop.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 859
Write a Python program that prints all the elements of a list using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

lst = [1, 2, 3, 4, 5]
i = 0
while i < len(lst):
    print(lst[i])
    i += 1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sum all the odd numbers from 1 to 100 using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 860
Write a Python program to sum all the odd numbers from 1 to 100 using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

num = 1
total = 0
while num <= 100:
    if num % 2 != 0:
        total += num
    num += 1
print(total)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that keeps doubling a number (starting from 2) and prints how many times it doubled before exceeding 1000 using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 861
Write a Python program that keeps doubling a number (starting from 2) and prints how many times it doubled before exceeding 1000 using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

num = 2
count = 0
while num <= 1000:
    num *= 2
    count += 1
print(count)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that keeps asking the user for a number and prints whether it is a palindrome. Stop when the user types “quit”.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 862
Write a Python program that keeps asking the user for a number and prints whether it is a palindrome. Stop when the user types “quit”.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

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

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that simulates a countdown timer by printing the numbers from 10 to 1, and then “Lift off!” using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 863
Write a Python program that simulates a countdown timer by printing the numbers from 10 to 1, and then “Lift off!” using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

num = 10
while num > 0:
    print(num)
    num -= 1
print("Lift off!")

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that keeps asking the user for a string and prints its length until the user types “exit”.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 864
Write a Python program that keeps asking the user for a string and prints its length until the user types “exit”.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

while True:
    user_input = input("Enter a string (type 'exit' to stop): ")
    if user_input == "exit":
        break
    print(len(user_input))

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that asks the user to input 5 numbers and calculates their product using a while loop.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 865
Write a Python program that asks the user to input 5 numbers and calculates their product using a while loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

i = 0
product = 1
while i < 5:
    num = int(input("Enter a number: "))
    product *= num
    i += 1
print(product)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a dictionary from two lists, one containing keys and the other containing values. Use zip()
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 866
Write a Python program to create a dictionary from two lists, one containing keys and the other containing values. Use zip()
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(lst1, lst2):  # Method: main
    result = {}
    for x, y in zip(lst1, lst2):
        result[x] = y
    return result  # Return the result
    
lst1 = [1, 3, 8]
lst2 = ["9", "2", "7"]
main(lst1, lst2)

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a dictionary from two lists, one containing keys and the other containing values. Do not use zip().
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 867
Write a Python program to create a dictionary from two lists, one containing keys and the other containing values. Do not use zip().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def create_dictionary(keys, values):  # Method: create_dictionary

    dictionary = {}
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]
    return dictionary  # Return the result

keys = ["apple", "banana", "cherry"]
values = [1, 2, 3]

result = create_dictionary(keys, values)
print(result)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that defines a function `capitalize_words()` which contains a nested function `capitalize()` that capitalizes a word. The `capitalize_words()` function should return a list with each word capitalized.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 868
Write a Python program that defines a function `capitalize_words()` which contains a nested function `capitalize()` that capitalizes a word. The `capitalize_words()` function should return a list with each word capitalized.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def capitalize_words(lst):  # Method: capitalize_words
    def capitalize(name):  # Method: capitalize
        return name.capitalize()  # Return the result
    return list(map(capitalize, lst))  # Return the result

lst = ["jonathan", "sam", "mimi"]
capitalize_words(lst)

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack a list of three elements into three variables.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 869
Write a Python program to unpack a list of three elements into three variables.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

numbers = [1, 2, 3]
a, b, c = numbers
print(a, b, c)  # Expected output: 1 2 3

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack the first and last elements of a list while collecting the middle elements in another variable.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 870
Write a Python program to unpack the first and last elements of a list while collecting the middle elements in another variable.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

numbers = [10, 20, 30, 40, 50]
first, *middle, last = numbers
print(first, middle, last)  # Expected output: 10 [20, 30, 40] 50

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to swap two variables using unpacking.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 871
Write a Python program to swap two variables using unpacking.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

x, y = 5, 10
x, y = y, x
print(x, y)  # Expected output: 10 5

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack the keys and values of a dictionary.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 872
Write a Python program to unpack the keys and values of a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

data = {"name": "Alice", "age": 25, "city": "New York"}
keys, values = zip(*data.items())
print(keys, values)  # Expected output: ('name', 'age', 'city') ('Alice', 25, 'New York')

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to assign multiple return values from a function to separate variables using unpacking.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 873
Write a Python program to assign multiple return values from a function to separate variables using unpacking.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def get_coordinates():  # Method: get_coordinates
    return (5, 10)  # Return the result

x, y = get_coordinates()
print(x, y)  # Expected output: 5 10

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract the first two characters and the rest of a string using unpacking.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 874
Write a Python program to extract the first two characters and the rest of a string using unpacking.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

word = "Python"
first, second, *rest = word
print(first, second, "".join(rest))  # Expected output: P y thon

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract the first and last elements of a tuple using unpacking.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 875
Write a Python program to extract the first and last elements of a tuple using unpacking.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

values = (100, 200, 300, 400, 500)
first, *_, last = values
print(first, last)  # Expected output: 100 500

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack a nested list into separate variables.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 876
Write a Python program to unpack a nested list into separate variables.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

nested_list = [[1, 2], [3, 4]]
(a, b), (c, d) = nested_list
print(a, b, c, d)  # Expected output: 1 2 3 4

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack a range into separate variables.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 877
Write a Python program to unpack a range into separate variables.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

a, b, c = range(3)
print(a, b, c)  # Expected output: 0 1 2

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to split a full name into first and last name using unpacking.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 878
Write a Python program to split a full name into first and last name using unpacking.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

full_name = "John Doe"
first_name, last_name = full_name.split()
print(first_name, last_name)  # Expected output: John Doe

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to assign function arguments using unpacking.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 879
Write a Python program to assign function arguments using unpacking.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def greet(name, age):  # Method: greet
    print(f"Hello, {name}. You are {age} years old.")

person = ("Alice", 30)
greet(*person)  # Expected output: Hello, Alice. You are 30 years old.

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to merge two lists using unpacking.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 880
Write a Python program to merge two lists using unpacking.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = [*list1, *list2]
print(merged)  # Expected output: [1, 2, 3, 4, 5, 6]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to merge two dictionaries using unpacking.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 881
Write a Python program to merge two dictionaries using unpacking.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Expected output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack and ignore certain values using `_`.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 882
Write a Python program to unpack and ignore certain values using `_`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

values = (1, 2, 3, 4, 5)
first, _, third, _, last = values
print(first, third, last)  # Expected output: 1 3 5

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack a list into positional function arguments.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 883
Write a Python program to unpack a list into positional function arguments.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def add(a, b, c):  # Method: add
    return a + b + c  # Return the result

numbers = [2, 4, 6]
result = add(*numbers)
print(result)  # Expected output: 12

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack a dictionary into keyword function arguments.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 884
Write a Python program to unpack a dictionary into keyword function arguments.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def describe(name, age, city):  # Method: describe
    return f"{name} is {age} years old and lives in {city}."  # Return the result

person = {"name": "Emma", "age": 28, "city": "London"}
print(describe(**person))  # Expected output: Emma is 28 years old and lives in London.

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract individual characters from a string using unpacking.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 885
Write a Python program to extract individual characters from a string using unpacking.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

word = "ABC"
a, b, c = word
print(a, b, c)  # Expected output: A B C

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack a list with unknown length using the starred expression.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 886
Write a Python program to unpack a list with unknown length using the starred expression.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, *middle, last = numbers
print(first, middle, last)  # Expected output: 1 [2, 3, 4, 5, 6, 7, 8] 9

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use unpacking inside a loop to iterate through a list of tuples.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 887
Write a Python program to use unpacking inside a loop to iterate through a list of tuples.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
for number, letter in pairs:
    print(number, letter)

# Expected output:
# 1 a
# 2 b
# 3 c

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack a tuple returned from a function.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 888
Write a Python program to unpack a tuple returned from a function.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def get_user():  # Method: get_user
    return "Alice", 25  # Return the result

name, age = get_user()
print(name, age)  # Expected output: Alice 25

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack a list of lists and sum corresponding elements using the `zip()` function.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 888
Write a Python program to unpack a list of lists and sum corresponding elements using the `zip()` function.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
summed = [sum(x) for x in zip(*lists)]
print(summed)  # Expected output: [12, 15, 18]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack a list of lists and sum corresponding elements using the `zip()` function. Use list comprehension.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 889
Write a Python program to unpack a list of lists and sum corresponding elements using the `zip()` function. Use list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
summed = [sum(x) for x in zip(*lists)]
print(summed)  # Expected output: [12, 15, 18]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack a dictionary’s items and reformat them as key-value pairs.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 890
Write a Python program to unpack a dictionary’s items and reformat them as key-value pairs.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

data = {"name": "Alice", "age": 25, "city": "New York"}
formatted = [f"{key}: {value}" for key, value in data.items()]
print(formatted)  # Expected output: ['name: Alice', 'age: 25', 'city: New York']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use unpacking to split a sentence into words and capture the first and last words separately.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 891
Write a Python program to use unpacking to split a sentence into words and capture the first and last words separately.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

sentence = "Python is a powerful programming language"
first, *middle, last = sentence.split()
print(first, middle, last)  # Expected output: Python ['is', 'a', 'powerful', 'programming'] language

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack only the vowels from a given word using list comprehension.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 892
Write a Python program to unpack only the vowels from a given word using list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

word = "unpacking"
vowels = [c for c in word if c in "aeiou"]
print(vowels)  # Expected output: ['u', 'a', 'i']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack a tuple containing mixed data types.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 893
Write a Python program to unpack a tuple containing mixed data types.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

data = ("Alice", 30, 5.8, True)
name, age, height, is_student = data
print(name, age, height, is_student)  # Expected output: Alice 30 5.8 True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack and sort a list of tuples by the second element.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 894
Write a Python program to unpack and sort a list of tuples by the second element.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

tuples = [(1, 3), (4, 1), (2, 2)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)  # Expected output: [(4, 1), (2, 2), (1, 3)]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract only even numbers from a list using unpacking inside list comprehension.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 895
Write a Python program to extract only even numbers from a list using unpacking inside list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # Expected output: [2, 4, 6]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to swap three variables using unpacking.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 896
Write a Python program to swap three variables using unpacking.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

a, b, c = 1, 2, 3
a, b, c = c, a, b
print(a, b, c)  # Expected output: 3 1 2

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack a range of numbers into three variables and collect the remaining in another variable.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 897
Write a Python program to unpack a range of numbers into three variables and collect the remaining in another variable.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

first, second, *remaining = range(10)
print(first, second, remaining)  # Expected output: 0 1 [2, 3, 4, 5, 6, 7, 8, 9]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use unpacking inside a lambda function to add three numbers.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 898
Write a Python program to use unpacking inside a lambda function to add three numbers.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

add_three = lambda x, y, z: x + y + z
numbers = (4, 5, 6)
print(add_three(*numbers))  # Expected output: 15

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract and reverse the digits of a number using unpacking.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 899
Write a Python program to extract and reverse the digits of a number using unpacking.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

num = 12345
digits = list(str(num))
reversed_digits = digits[::-1]
print(reversed_digits)  # Expected output: ['5', '4', '3', '2', '1']

num = 123456
str_num = str(num)[::-1]
lst_num = list(str_num)
print(lst_num)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use unpacking in a function that returns the minimum and maximum of a list.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 900
Write a Python program to use unpacking in a function that returns the minimum and maximum of a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def min_max(lst):  # Method: min_max
    return min(lst), max(lst)  # Return the result

numbers = [4, 1, 7, 9, 2]
minimum, maximum = min_max(numbers)
print(minimum, maximum)  # Expected output: 1 9

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack a list of tuples and extract the first elements using list comprehension.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 901
Write a Python program to unpack a list of tuples and extract the first elements using list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

tuples = [(10, "a"), (20, "b"), (30, "c")]
first_elements = [x for x, _ in tuples]
print(first_elements)  # Expected output: [10, 20, 30]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack a list of dictionaries and extract all the values under a specific key.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 902
Write a Python program to unpack a list of dictionaries and extract all the values under a specific key.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def main(lst_dic):  # Method: main
    ages = [value["age"] for value in lst_dic]
    return ages  # Return the result
    
lst_dic = [{"name": "jon", "age": 55}, {"name": "sam", "age": 8}]
main(lst_dic)

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
]

ages = [person["age"] for person in people]
print(ages)  # Expected output: [25, 30, 35]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use unpacking to separate numbers in a mathematical expression.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 903
Write a Python program to use unpacking to separate numbers in a mathematical expression.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

expression = "3 + 5 - 2 * 4"
a, op1, b, op2, c, op3, d = expression.split()
print(a, op1, b, op2, c, op3, d)  # Expected output: 3 + 5 - 2 * 4

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack and reassign dictionary values dynamically.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 904
Write a Python program to unpack and reassign dictionary values dynamically.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

data = {"x": 10, "y": 20, "z": 30}
x, y, z = data.values()
x, y, z = z, x, y
print(x, y, z)  # Expected output: 30 10 20

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use unpacking to extract domain and subdomain from an email address.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 905
Write a Python program to use unpacking to extract domain and subdomain from an email address.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

email = "john.doe@example.com"
user, domain = email.split("@")
print(user, domain)  # Expected output: john.doe example.com

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack nested tuples inside a list.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 906
Write a Python program to unpack nested tuples inside a list.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

nested_tuples = [(1, (2, 3)), (4, (5, 6))]
for a, (b, c) in nested_tuples:
    print(a, b, c)

# Expected output:
# 1 2 3
# 4 5 6

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to unpack values returned from `divmod()`.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 907
Write a Python program to unpack values returned from `divmod()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

quotient, remainder = divmod(17, 5)
print(quotient, remainder)  # Expected output: 3 2

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to generate a random integer between 1 and 100.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 908
Write a Python program to generate a random integer between 1 and 100.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module

num = random.randint(1, 100)
print(num)  # Expected output: A random number between 1 and 100

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to generate a random floating-point number between 0 and 1.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 909
Write a Python program to generate a random floating-point number between 0 and 1.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module

num = random.random()
print(num)  # Expected output: A random float between 0 and 1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to generate a random even integer between 10 and 50.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 910
Write a Python program to generate a random even integer between 10 and 50.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module

num = random.randrange(10, 51, 2)
print(num)  # Expected output: A random even number between 10 and 50

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to randomly select an element from a given list.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 911
Write a Python program to randomly select an element from a given list.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

import random  # Import module

colors = ["red", "blue", "green", "yellow", "purple"]
selected = random.choice(colors)
print(selected)  # Expected output: A random color from the list

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to shuffle a list randomly.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 912
Write a Python program to shuffle a list randomly.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

import random  # Import module

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # Expected output: A shuffled version of the list

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to select 3 unique random numbers from a list.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 913
Write a Python program to select 3 unique random numbers from a list.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module

numbers = list(range(1, 21))
selected = random.sample(numbers, 3)
print(selected)  # Expected output: 3 unique numbers from 1 to 20

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to generate a random floating-point number between 5 and 10.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 914
Write a Python program to generate a random floating-point number between 5 and 10.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module

num = random.uniform(5, 10)
print(num)  # Expected output: A random float between 5 and 10

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to generate a random letter from the English alphabet.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 915
Write a Python program to generate a random letter from the English alphabet.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module
import string  # Import module

letter = random.choice(string.ascii_letters)
print(letter)  # Expected output: A random letter from a-z or A-Z

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to simulate the rolling of a six-sided die.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 916
Write a Python program to simulate the rolling of a six-sided die.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module

roll = random.randint(1, 6)
print(roll)  # Expected output: A number between 1 and 6

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to simulate flipping a coin.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 917
Write a Python program to simulate flipping a coin.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

import random  # Import module

flip = random.choice(["Heads", "Tails"])
print(flip)  # Expected output: Heads or Tails

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to randomly select a first name and last name from separate lists and combine them.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 918
Write a Python program to randomly select a first name and last name from separate lists and combine them.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

import random  # Import module

first_names = ["Alice", "Bob", "Charlie", "David"]
last_names = ["Smith", "Johnson", "Brown", "Williams"]

full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
print(full_name)  # Expected output: A random full name

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to generate a random password with 8 characters including letters, digits, and special characters.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 919
Write a Python program to generate a random password with 8 characters including letters, digits, and special characters.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module
import string  # Import module

characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.sample(characters, 8))
print(password)  # Expected output: A random 8-character password

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to generate a random boolean value (True or False).
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 920
Write a Python program to generate a random boolean value (True or False).
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

import random  # Import module

boolean_value = random.choice([True, False])
print(boolean_value)  # Expected output: True or False

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to generate 5 random numbers between 1 and 100 and store them in a list.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 921
Write a Python program to generate 5 random numbers between 1 and 100 and store them in a list.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

import random  # Import module

numbers = [random.randint(1, 100) for _ in range(5)]
print(numbers)  # Expected output: A list of 5 random numbers between 1 and 100

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to select a random subset of 4 elements from a list.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 922
Write a Python program to select a random subset of 4 elements from a list.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module

items = list(range(1, 11))
subset = random.sample(items, 4)
print(subset)  # Expected output: A random selection of 4 numbers from 1 to 10

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to generate a random date within the year 2023.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 923
Write a Python program to generate a random date within the year 2023.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module
import datetime  # Import module

start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 12, 31)
random_days = random.randint(0, (end_date - start_date).days)
random_date = start_date + datetime.timedelta(days=random_days)
print(random_date)  # Expected output: A random date in 2023

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to randomly pick an element from a set.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 924
Write a Python program to randomly pick an element from a set.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module

fruits = {"apple", "banana", "cherry", "date"}
random_fruit = random.choice(list(fruits))
print(random_fruit)  # Expected output: A random fruit from the set

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to randomly generate a 6-digit verification code.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 925
Write a Python program to randomly generate a 6-digit verification code.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module

code = random.randint(100000, 999999)
print(code)  # Expected output: A 6-digit random number

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to generate a random hexadecimal color code.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 926
Write a Python program to generate a random hexadecimal color code.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module

hex_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
print(hex_color)  # Expected output: A random hex color

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to generate a random phone number in the format (XXX) XXX-XXXX.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 927
Write a Python program to generate a random phone number in the format (XXX) XXX-XXXX.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module

phone_number = f"({random.randint(100, 999)}) {random.randint(100, 999)}-{random.randint(1000, 9999)}"
print(phone_number)  # Expected output: A random phone number

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to generate a random 4-digit PIN code.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 928
Write a Python program to generate a random 4-digit PIN code.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module

pin = f"{random.randint(1000, 9999)}"
print(pin)  # Expected output: A 4-digit random PIN

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to simulate a random dice roll with two six-sided dice.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 929
Write a Python program to simulate a random dice roll with two six-sided dice.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
print(dice1, dice2)  # Expected output: Two random numbers between 1 and 6

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to generate a random IP address.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 930
Write a Python program to generate a random IP address.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module

ip_address = ".".join(str(random.randint(0, 255)) for _ in range(4))
print(ip_address)  # Expected output: A random IP address

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to generate a random strong password of 12 characters.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 931
Write a Python program to generate a random strong password of 12 characters.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module
import string  # Import module

characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choices(characters, k=12))
print(password)  # Expected output: A random 12-character password

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to randomly pick an item from a tuple.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 932
Write a Python program to randomly pick an item from a tuple.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import random  # Import module

animals = ("dog", "cat", "elephant", "lion")
random_animal = random.choice(animals)
print(random_animal)  # Expected output: A random animal from the tuple

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to handle division by zero exception when dividing two numbers.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 933
Write a Python program to handle division by zero exception when dividing two numbers.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

try:  # Begin exception handling
    a, b = 10, 0
    result = a / b
except ZeroDivisionError:  # Handle exception
    result = "Cannot divide by zero"
    
print(result)  # Expected output: Cannot divide by zero

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to handle an IndexError when accessing an out-of-range list index.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 934
Write a Python program to handle an IndexError when accessing an out-of-range list index.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

try:  # Begin exception handling
    lst = [1, 2, 3]
    value = lst[5]
except IndexError:  # Handle exception
    value = "Index out of range"

print(value)  # Expected output: Index out of range

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to handle a KeyError when accessing a non-existent key in a dictionary.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 935
Write a Python program to handle a KeyError when accessing a non-existent key in a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

try:  # Begin exception handling
    d = {"name": "Alice"}
    value = d["age"]
except KeyError:  # Handle exception
    value = "Key not found"

print(value)  # Expected output: Key not found

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to handle a ValueError when converting an invalid string to an integer.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 936
Write a Python program to handle a ValueError when converting an invalid string to an integer.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

try:  # Begin exception handling
    num = int("abc")
except ValueError:  # Handle exception
    num = "Invalid integer conversion"

print(num)  # Expected output: Invalid integer conversion

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to handle a TypeError when trying to concatenate a string with an integer.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 937
Write a Python program to handle a TypeError when trying to concatenate a string with an integer.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

try:  # Begin exception handling
    result = "Age: " + 25
except TypeError:  # Handle exception
    result = "Type mismatch error"

print(result)  # Expected output: Type mismatch error

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to handle a FileNotFoundError when trying to open a non-existent file.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 938
Write a Python program to handle a FileNotFoundError when trying to open a non-existent file.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

try:  # Begin exception handling
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:  # Handle exception
    content = "File not found"

print(content)  # Expected output: File not found

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to catch an AttributeError when accessing a non-existent attribute of an object.
# 
# This problem involves creating classes to organize code and data.
# Classes provide a way to encapsulate related attributes and methods together.
# 
# Key Requirements:
# - Define a class with the required attributes and methods
# - Implement proper initialization if needed
# - Ensure methods return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 939
Write a Python program to catch an AttributeError when accessing a non-existent attribute of an object.
"""

# SOLUTION EXPLANATION:
# This solution uses classes to organize code and data. Classes provide
# encapsulation, allowing us to group related attributes and methods together.

class Person:  # Base class definition
    def __init__(self, name):  # Constructor: initializes instance attributes
        self.name = name

try:  # Begin exception handling
    p = Person("Alice")
    age = p.age
except AttributeError:  # Handle exception
    age = "Attribute not found"

print(age)  # Expected output: Attribute not found

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to catch a NameError when accessing an undefined variable.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 940
Write a Python program to catch a NameError when accessing an undefined variable.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

try:  # Begin exception handling
    result = x + 10
except NameError:  # Handle exception
    result = "Variable not defined"

print(result)  # Expected output: Variable not defined

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to handle a PermissionError when trying to write to a read-only file.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 941
Write a Python program to handle a PermissionError when trying to write to a read-only file.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

try:  # Begin exception handling
    with open("/root/protected.txt", "w") as file:
        file.write("Test")
except PermissionError:  # Handle exception
    result = "Permission denied"

print(result)  # Expected output: Permission denied

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use a try-except-else block to catch errors in division.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 942
Write a Python program to use a try-except-else block to catch errors in division.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

try:  # Begin exception handling
    a, b = 10, 2
    result = a / b
except ZeroDivisionError:  # Handle exception
    result = "Cannot divide by zero"
else:
    result = f"Division successful: {result}"

print(result)  # Expected output: Division successful: 5.0

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use a finally block to always print a message after exception handling.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 943
Write a Python program to use a finally block to always print a message after exception handling.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

try:  # Begin exception handling
    result = 10 / 0
except ZeroDivisionError:  # Handle exception
    result = "Cannot divide by zero"
finally:
    print("Execution completed")

print(result)  # Expected output: Cannot divide by zero
               # Execution completed

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to raise a custom exception if a number is negative.
# 
# This problem demonstrates object-oriented programming concepts, specifically
# class inheritance. Inheritance allows a derived class (child class) to inherit
# attributes and methods from a base class (parent class), and optionally override
# or extend them to provide specialized behavior.
# 
# Key Requirements:
# - Create a base class with the specified attributes or methods
# - Create a derived class that inherits from the base class
# - Implement method overriding or attribute extension as required
# - Ensure proper initialization using super() when needed
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The derived class should demonstrate inheritance and polymorphism
# ============================================================================

"""
Problem: 944
Write a Python program to raise a custom exception if a number is negative.
"""

# SOLUTION EXPLANATION:
# This solution demonstrates class inheritance and method overriding. The base
# class defines a general method, and the derived class overrides it to provide
# specialized behavior. This is a key concept in object-oriented programming
# called polymorphism.

class NegativeNumberError(Exception):  # NegativeNumberError inherits from Exception
    pass

def check_number(n):  # Method: check_number
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed")

try:  # Begin exception handling
    check_number(-5)
except NegativeNumberError as e:  # Handle exception
    print(e)  # Expected output: Negative numbers are not allowed

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to handle a multiple exception scenario (ZeroDivisionError and TypeError).
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 945
Write a Python program to handle a multiple exception scenario (ZeroDivisionError and TypeError).
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

try:  # Begin exception handling
    num = "10" / 2
except (ZeroDivisionError, TypeError):  # Handle exception
    result = "An error occurred"

print(result)  # Expected output: An error occurred

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `assert` statement to raise an AssertionError if a condition is false.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 946
Write a Python program to use the `assert` statement to raise an AssertionError if a condition is false.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

try:  # Begin exception handling
    x = -1
    assert x >= 0, "Negative number not allowed"
except AssertionError as e:  # Handle exception
    print(e)  # Expected output: Negative number not allowed

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to handle a MemoryError by attempting to allocate excessive memory.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 947
Write a Python program to handle a MemoryError by attempting to allocate excessive memory.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

try:  # Begin exception handling
    lst = [0] * (10**9)
except MemoryError:  # Handle exception
    print("Memory limit exceeded")  # Expected output: Memory limit exceeded

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to catch a RecursionError when a function calls itself infinitely.
# 
# This problem requires implementing a function to perform a specific task.
# Functions allow us to organize code into reusable blocks.
# 
# Key Requirements:
# - Create a function with the specified name and parameters
# - Implement the required logic
# - Return or print the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 948
Write a Python program to catch a RecursionError when a function calls itself infinitely.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using functions. Functions
# allow code reuse and make programs more modular and easier to maintain.

def infinite_recursion():  # Method: infinite_recursion
    return infinite_recursion()  # Return the result

try:  # Begin exception handling
    infinite_recursion()
except RecursionError:  # Handle exception
    print("Recursion limit exceeded")  # Expected output: Recursion limit exceeded

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to catch a ModuleNotFoundError when trying to import a non-existent module.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 949
Write a Python program to catch a ModuleNotFoundError when trying to import a non-existent module.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

try:  # Begin exception handling
    import nonexistent_module  # Import module
except ModuleNotFoundError:  # Handle exception
    print("Module not found")  # Expected output: Module not found

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to catch an IOError when trying to read a file that does not exist.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 950
Write a Python program to catch an IOError when trying to read a file that does not exist.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

try:  # Begin exception handling
    with open("missingfile.txt", "r") as f:
        data = f.read()
except IOError:  # Handle exception
    print("Error reading file")  # Expected output: Error reading file

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to catch a KeyboardInterrupt exception when the user manually stops the script.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 951
Write a Python program to catch a KeyboardInterrupt exception when the user manually stops the script.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

try:  # Begin exception handling
    while True:
        pass  # Infinite loop to simulate long-running process
except KeyboardInterrupt:  # Handle exception
    print("Process interrupted by user")  # Expected output: Process interrupted by user

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to convert a string to uppercase using a built-in method.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 952
Write a Python program to convert a string to uppercase using a built-in method.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

text = "hello world"
upper_text = text.upper()
print(upper_text)  # Expected output: HELLO WORLD

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count the occurrences of a specific character in a string using a method.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 953
Write a Python program to count the occurrences of a specific character in a string using a method.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

text = "banana"
count_a = text.count("a")
print(count_a)  # Expected output: 3

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string starts with a specific prefix using a method.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 954
Write a Python program to check if a string starts with a specific prefix using a method.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

text = "hello world"
result = text.startswith("hello")
print(result)  # Expected output: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to replace all occurrences of a word in a string using a method.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 955
Write a Python program to replace all occurrences of a word in a string using a method.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

text = "I love apples. Apples are delicious."
new_text = text.replace("Apples", "Bananas")
print(new_text)  # Expected output: I love apples. Bananas are delicious.

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to split a sentence into words using a method.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 956
Write a Python program to split a sentence into words using a method.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

sentence = "Python is amazing"
words = sentence.split()
print(words)  # Expected output: ['Python', 'is', 'amazing']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to join a list of words into a sentence using a method.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 957
Write a Python program to join a list of words into a sentence using a method.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)  # Expected output: Python is fun

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove leading and trailing spaces from a string using a method.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 958
Write a Python program to remove leading and trailing spaces from a string using a method.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

text = "   hello world   "
trimmed_text = text.strip()
print(trimmed_text)  # Expected output: hello world

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the index of a specific element in a list using a method.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 959
Write a Python program to find the index of a specific element in a list using a method.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

numbers = [10, 20, 30, 40, 50]
index_30 = numbers.index(30)
print(index_30)  # Expected output: 2

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a list of numbers in ascending order using a method.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 960
Write a Python program to sort a list of numbers in ascending order using a method.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

numbers = [5, 2, 8, 1, 3]
numbers.sort()
print(numbers)  # Expected output: [1, 2, 3, 5, 8]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to reverse the order of elements in a list using a method.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 961
Write a Python program to reverse the order of elements in a list using a method.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # Expected output: [5, 4, 3, 2, 1]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to add an element at the end of a list using a method.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 962
Write a Python program to add an element at the end of a list using a method.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # Expected output: [1, 2, 3, 4]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove the last element from a list using a method.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 963
Write a Python program to remove the last element from a list using a method.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

numbers = [10, 20, 30]
last_item = numbers.pop()
print(numbers)  # Expected output: [10, 20]
print(last_item)  # Expected output: 30

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove a specific element from a list using a method.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 964
Write a Python program to remove a specific element from a list using a method.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

numbers = [5, 10, 15, 20]
numbers.remove(10)
print(numbers)  # Expected output: [5, 15, 20]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get all the keys from a dictionary using a method.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 965
Write a Python program to get all the keys from a dictionary using a method.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

person = {"name": "Alice", "age": 25, "city": "New York"}
keys = person.keys()
print(list(keys))  # Expected output: ['name', 'age', 'city']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get all the values from a dictionary using a method.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 966
Write a Python program to get all the values from a dictionary using a method.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

person = {"name": "Alice", "age": 25, "city": "New York"}
values = person.values()
print(list(values))  # Expected output: ['Alice', 25, 'New York']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to merge two dictionaries using a method.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 967
Write a Python program to merge two dictionaries using a method.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)  # Expected output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove an item from a dictionary using a method.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 968
Write a Python program to remove an item from a dictionary using a method.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

person = {"name": "Alice", "age": 25, "city": "New York"}
person.pop("age")
print(person)  # Expected output: {'name': 'Alice', 'city': 'New York'}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a set contains a specific element using a method.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 969
Write a Python program to check if a set contains a specific element using a method.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

numbers = {1, 2, 3, 4, 5}
result = 3 in numbers
print(result)  # Expected output: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove and return an arbitrary element from a set using a method.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 970
Write a Python program to remove and return an arbitrary element from a set using a method. 
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

numbers = {10, 20, 30, 40}
removed_element = numbers.pop()
print(removed_element)  # Expected output: A random element from the set
print(numbers)  # Expected output: The set without the removed element

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to clear all elements from a list using a method.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 971
Write a Python program to clear all elements from a list using a method.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  # Expected output: []

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse an integer from a string.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 972
Write a Python program to parse an integer from a string.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

num_str = "42"
num = int(num_str)
print(num)  # Expected output: 42

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse a float from a string.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 973
Write a Python program to parse a float from a string.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

num_str = "3.14"
num = float(num_str)
print(num)  # Expected output: 3.14

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse a boolean from a string.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 974
Write a Python program to parse a boolean from a string.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

bool_str = "True"
boolean_value = bool_str.lower() == "true"
print(boolean_value)  # Expected output: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse multiple integers from a comma-separated string.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 975
Write a Python program to parse multiple integers from a comma-separated string.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

num_str = "10,20,30,40"
numbers = list(map(int, num_str.split(",")))
print(numbers)  # Expected output: [10, 20, 30, 40]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse a date from a string in the format 'YYYY-MM-DD'.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 976
Write a Python program to parse a date from a string in the format 'YYYY-MM-DD'.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

from datetime import datetime

date_str = "2024-03-22"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
print(parsed_date)  # Expected output: 2024-03-22 00:00:00

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract numbers from a mixed string.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 977
Write a Python program to extract numbers from a mixed string.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

import re  # Import module

text = "My order number is 12345 and tracking ID is 67890."
numbers = re.findall(r"\d+", text)
print(numbers)  # Expected output: ['12345', '67890']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse a JSON string into a Python dictionary.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 978
Write a Python program to parse a JSON string into a Python dictionary.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import json  # Import module

json_str = '{"name": "Alice", "age": 25, "city": "New York"}'
data = json.loads(json_str)
print(data)  # Expected output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to convert a dictionary to a JSON string.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 979
Write a Python program to convert a dictionary to a JSON string.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import json  # Import module

data = {"name": "Bob", "age": 30, "city": "London"}
json_str = json.dumps(data)
print(json_str)  # Expected output: '{"name": "Bob", "age": 30, "city": "London"}'

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse an XML string and extract specific data.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 980
Write a Python program to parse an XML string and extract specific data.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import xml.etree.ElementTree as ET  # Import module

xml_str = "<person><name>Charlie</name><age>28</age></person>"
root = ET.fromstring(xml_str)
name = root.find("name").text
print(name)  # Expected output: Charlie

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse key-value pairs from a query string.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 981
Write a Python program to parse key-value pairs from a query string.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

from urllib.parse import parse_qs

query_str = "name=David&age=35&city=Paris"
parsed_data = parse_qs(query_str)
print(parsed_data)  # Expected output: {'name': ['David'], 'age': ['35'], 'city': ['Paris']}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse a CSV string into a list of lists.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 982
Write a Python program to parse a CSV string into a list of lists.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

import csv  # Import module
from io import StringIO

csv_str = "name,age,city\nAlice,25,New York\nBob,30,London"
csv_file = StringIO(csv_str)
reader = csv.reader(csv_file)
data = list(reader)
print(data)  
# Expected output: [['name', 'age', 'city'], ['Alice', '25', 'New York'], ['Bob', '30', 'London']]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse HTML and extract all links.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 983
Write a Python program to parse HTML and extract all links.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

from bs4 import BeautifulSoup

html = '<a href="https://example.com">Example</a> <a href="https://google.com">Google</a>'
soup = BeautifulSoup(html, "html.parser")
links = [a["href"] for a in soup.find_all("a")]
print(links)  # Expected output: ['https://example.com', 'https://google.com']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse a time string in the format 'HH:MM:SS' into a `datetime.time` object.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 984
Write a Python program to parse a time string in the format 'HH:MM:SS' into a `datetime.time` object.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

from datetime import datetime

time_str = "14:30:45"
parsed_time = datetime.strptime(time_str, "%H:%M:%S").time()
print(parsed_time)  # Expected output: 14:30:45

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse a hexadecimal number string into an integer.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 985
Write a Python program to parse a hexadecimal number string into an integer.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

hex_str = "0x1A"
num = int(hex_str, 16)
print(num)  # Expected output: 26

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse a binary number string into an integer.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 986
Write a Python program to parse a binary number string into an integer.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

binary_str = "1010"
num = int(binary_str, 2)
print(num)  # Expected output: 10

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse a scientific notation string into a float.
# 
# This problem demonstrates various Python programming concepts and features.
# 
# Key Requirements:
# - Follow the problem specification exactly
# - Implement the required functionality
# - Ensure the solution produces the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 987
Write a Python program to parse a scientific notation string into a float.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using Python's built-in
# features and syntax. The code follows Python best practices.

sci_str = "3.5e4"
num = float(sci_str)
print(num)  # Expected output: 35000.0

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse a configuration file (.ini format) and extract a setting.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 988
Write a Python program to parse a configuration file (.ini format) and extract a setting.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

import configparser  # Import module

config_str = "[Settings]\nusername=admin\npassword=1234"
config = configparser.ConfigParser()
config.read_string(config_str)
username = config["Settings"]["username"]
print(username)  # Expected output: admin

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse a markdown string and extract the text from a header.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 989
Write a Python program to parse a markdown string and extract the text from a header.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

import re  # Import module

markdown = "# Hello World\nThis is a markdown file."
header = re.findall(r"^# (.+)", markdown, re.MULTILINE)
print(header)  # Expected output: ['Hello World']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse a YAML string into a Python dictionary.
# 
# This problem requires using Python's built-in modules or external libraries
# to accomplish a specific task.
# 
# Key Requirements:
# - Import the necessary modules
# - Use the module's functions or classes as required
# - Produce the expected output
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 990
Write a Python program to parse a YAML string into a Python dictionary.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's built-in modules or libraries to accomplish the
# task efficiently. Importing modules gives access to additional functionality.

import yaml  # Import module

yaml_str = "name: Alice\nage: 25\ncity: New York"
data = yaml.safe_load(yaml_str)
print(data)  # Expected output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse a JSON array into a Python list.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 991
Write a Python program to parse a JSON array into a Python list.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

import json  # Import module

json_str = '[1, 2, 3, 4, 5]'
data = json.loads(json_str)
print(data)  # Expected output: [1, 2, 3, 4, 5]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse a currency string and extract the numeric value.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 992
Write a Python program to parse a currency string and extract the numeric value.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

import re  # Import module

currency_str = "$123.45"
value = float(re.sub(r"[^\d.]", "", currency_str))
print(value)  # Expected output: 123.45

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to parse command-line arguments.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 993
Write a Python program to parse command-line arguments.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

import argparse  # Import module

parser = argparse.ArgumentParser()
parser.add_argument("--name", type=str, default="User")
args = parser.parse_args(args=["--name", "Alice"])
print(args.name)  # Expected output: Alice

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to slice the first 5 characters from a string.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 994
Write a Python program to slice the first 5 characters from a string.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

text = "Hello, world!"
sliced_text = text[:5]
print(sliced_text)  # Expected output: Hello

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to slice the last 4 characters from a string.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 995
Write a Python program to slice the last 4 characters from a string.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

text = "Programming"
sliced_text = text[-4:]
print(sliced_text)  # Expected output: ming

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to slice all elements from a list except the first two.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 996
Write a Python program to slice all elements from a list except the first two.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

numbers = [10, 20, 30, 40, 50]
sliced_list = numbers[2:]
print(sliced_list)  # Expected output: [30, 40, 50]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to slice the last 3 elements from a list.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 997
Write a Python program to slice the last 3 elements from a list.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

numbers = [1, 2, 3, 4, 5, 6]
sliced_list = numbers[-3:]
print(sliced_list)  # Expected output: [4, 5, 6]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract only the even-indexed characters from a string using slicing.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 998
Write a Python program to extract only the even-indexed characters from a string using slicing.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

text = "PythonSlicing"
sliced_text = text[::2]
print(sliced_text)  # Expected output: PtoSln

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract only the odd-indexed characters from a string using slicing.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 999
Write a Python program to extract only the odd-indexed characters from a string using slicing.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

text = "PythonSlicing"
sliced_text = text[1::2]
print(sliced_text)  # Expected output: yhnicig

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to reverse a string using slicing.
# 
# This problem demonstrates Python's slicing syntax, which allows extracting
# portions of sequences (strings, lists, tuples) using index ranges.
# 
# Key Requirements:
# - Use slicing syntax [start:stop:step] to extract elements
# - Understand positive and negative indexing
# - Apply the correct slice to get the desired result
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# ============================================================================

"""
Problem: 1000
Write a Python program to reverse a string using slicing.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax [start:stop:step] to extract
# portions of a sequence. Slicing is a powerful and efficient way to work
# with strings, lists, and other sequences.

text = "abcdef"
reversed_text = text[::-1]
print(reversed_text)  # Expected output: fedcba

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.