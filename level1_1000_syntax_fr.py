# Syntax documentation
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Bird, Penguin()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 501 :
créer un base class Bird avec une méthode fly(). créer un derived class Penguin qui overrides le fly() méthode à print “Cannot fly”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Book, EBook, super()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 502 :
créer un base class Book avec attributes title et author. créer un derived class EBook qui ajoute an attribute file_size.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Guitar, Instrument()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 503 :
créer un base class Instrument avec une méthode play(). créer un derived class Guitar qui overrides le play() méthode à print “Strum”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Chess, Game()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 504 :
créer un base class Game avec une méthode start(). créer un derived class Chess qui overrides le start() méthode à print “Start Chess”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : Bicycle, Vehicle()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 505 :
créer un base class Vehicle avec une méthode drive(). créer un derived class Bicycle qui overrides le drive() méthode à print “Pedal”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Computer, Laptop, super()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 506 :
créer un base class Computer avec attributes brand et processor. créer un derived class Laptop qui ajoute an attribute weight.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Device, Smartphone()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 507 :
créer un base class Device avec une méthode turn_on(). créer un derived class Smartphone qui ajoute an attribute apps.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Child, Parent()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 508 :
créer un base class Parent avec une méthode display(). créer un derived class Child qui overrides le display() méthode à print “This est un child”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Building, Skyscraper, super()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 509 :
créer un base class Building avec attributes floors et address. créer un derived class Skyscraper qui ajoute an attribute height.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Flower, Plant()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 510 :
créer un base class Plant avec une méthode grow(). créer un derived class Flower qui overrides le grow() méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : MathTeacher, Teacher, super()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 511 :
créer un base class Teacher avec attributes nom et subject. créer un derived class MathTeacher qui ajoute une méthode teach_math().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Poet, Writer, super()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 512 :
créer un base class Writer avec attributes nom et genre. créer un derived class Poet qui overrides le genre attribute à “Poetry”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Appliance, Oven()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 513 :
créer un base class Appliance avec une méthode Utilisez(). créer un derived class Oven qui overrides le Utilisez() méthode à print “Bake”
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Operators: +
# Fonctions intégrées : Artist, Painter()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 514 :
créer un base class Artist avec attributes nom et medium. créer un derived class Painter qui ajoute une méthode paint().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Electrician, Worker()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 515 :
créer un base class Worker avec une méthode work(). créer un derived class Electrician qui overrides le work() méthode à print “Fix wires”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Animal, Lion()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 516 :
créer un base class Animal avec une méthode eat(). créer un derived class Lion qui overrides le eat() méthode à print “Eat meat”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Appliance, Fan()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 517 :
créer un base class Appliance avec une méthode run(). créer un derived class Fan qui overrides le run() méthode à print “Spin blades”
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Employee, Intern()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 518 :
créer un base class Employee avec une méthode get_salary(). créer un derived class Intern qui overrides le get_salary() méthode à retourner un lower salary.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Motorcycle, Vehicle, super()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 519 :
créer un base class Vehicle avec an attribute wheels. créer un derived class Motorcycle qui overrides wheels à 2.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Hammer, Tool()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 520 :
créer un base class Tool avec une méthode Utilisez(). créer un derived class Hammer qui overrides le Utilisez() méthode à print “Hammer nails”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : BankAccount, SavingsAccount, super()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 521 :
créer un base class BankAccount avec attributes balance et owner. créer un derived class SavingsAccount qui ajoute an attribute interest_rate.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Sword, Weapon()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 522 :
créer un base class Weapon avec une méthode attack(). créer un derived class Sword qui overrides le attack() méthode à print “Slash”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Appliance, Microwave, super()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 523 :
créer un base class Appliance avec an attribute power. créer un derived class Microwave qui ajoute une méthode heat_food().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : ElectricCar, Vehicle()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 524 :
créer un base class Vehicle avec une méthode start(). créer un derived class ElectricCar qui overrides le start() méthode à print “Silent start”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Cat, Pet()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 525 :
créer un base class Pet avec une méthode make_sound(). créer un derived class Cat qui overrides le make_sound() méthode à print “Meow”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Chef, PastryChef()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 526 :
créer un base class Chef avec une méthode cook(). créer un derived class PastryChef qui overrides le cook() méthode à print “Bake cake”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : Chair, super()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return Chair(material, color, legs)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 527 :
créer un base class Furniture avec attributes material et color. créer un derived class Chair qui ajoute an attribute legs.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Game, Soccer, super()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 528 :
créer un base class Game avec an attribute players. créer un derived class Soccer qui overrides le players attribute à 22.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Musician, Pianist()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 529 :
créer un base class Musician avec une méthode play_instrument(). créer un derived class Pianist qui overrides le play_instrument() méthode à print “Play piano”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Company, TechCompany, super()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 530 :
créer un base class Company avec attributes nom et location. créer un derived class TechCompany qui ajoute an attribute products.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Gadget, Smartwatch, super()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 531 :
créer un base class Gadget avec une méthode operate(). créer un derived class Smartwatch qui ajoute an attribute heart_rate_monitor.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : FitnessTrainer, Trainer()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 532 :
créer un base class Trainer avec une méthode train(). créer un derived class FitnessTrainer qui overrides le train() méthode à print “Train body”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Book, ComicBook()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 533 :
créer un base class Book avec une méthode read(). créer un derived class ComicBook qui overrides le read() méthode à print “Read avec pictures”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : GameSoftware, Software, super()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 534 :
créer un base class Software avec attributes nom et version. créer un derived class GameSoftware qui ajoute an attribute genre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → count = 0
#   → for c in s:
#   →     if c == 'a':
#   →         count += 1
#   → return count
#   → count = 0
#   → for c in s:
#   →     if c == 'a':
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 535 :
Écrivez un programme Python à compter le nombre de fois la lettre ‘a’ apparaît dans une chaîne. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → count = 0
#   → for c in num:
#   →     if c == 5:
#   →         count += 1
#   → return count
#   → count = 0
#   → for c in num:
#   →     if c == 5:
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 536 :
Write un Python fonction à compter le occurrences de le nombre 5 dans une liste d'entiers. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → count = 0
#   → for c in string:
#   →     if c == 'hello':
#   →         count += 1
#   → return count
#   → count = 0
#   → for c in string:
#   →     if c == 'hello':
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 537 :
Écrivez un programme Python à compter combien de fois mot “hello” apparaît dans une phrase. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → count = 0
#   → for c in string:
#   →     if c == '#':
#   →         count += 1
#   → return count
#   → count = 0
#   → for c in string:
#   →     if c == '#':
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 538 :
Écrivez une fonction qui compte combien de fois caractère # apparaît dans une chaîne. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : str, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → count = 0
#   → for c in num:
#   →     if c == 0:
#   →         count += 1
#   → return count
#   → total = 0
#   → for num in lst:
#   →     total += str(num).count('0')
#   → print(total)
#   → count = 0
#   → for c in num:
#   →     if c == 0:
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 540 :
Write un Python fonction à compter combien de fois chiffre 0 apparaît dans une liste de nombres. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return total_count
#   → return total_count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 544 :
Écrivez une fonction à compter combien de fois la lettre ‘e’ apparaît dans une liste de chaînes. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → count = 0
#   → for c in lst:
#   →     if c == element:
#   →         count += 1
#   → return count
#   → count = 0
#   → for c in lst:
#   →     if c == element:
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 545 :
Écrivez un programme Python à compter le nombre de fois un certain élément apparaît dans une liste de mixte tapez. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → count = 0
#   → for c in s:
#   →     if c == 'test':
#   →         count += 1
#   → return count
#   → count = 0
#   → for c in s:
#   →     if c == 'test':
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 546 :
Écrivez une fonction à compter le occurrences de la chaîne “test” dans une chaîne où multiple “test” substrings pourrait exist. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → count = 0
#   → for c in lst:
#   →     if c == number:
#   →         count += 1
#   → return count
#   → count = 0
#   → for c in lst:
#   →     if c == number:
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 547 :
Écrivez un programme Python à compter combien de fois un spécifique nombre occurs dans une liste de floating-point nombres. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → count = 0
#   → for c in lst:
#   →     if c == number:
#   →         count += 1
#   → return count
#   → count = 0
#   → for c in lst:
#   →     if c == number:
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 548 :
Écrivez une fonction à compter le nombre de voyelles (a, e, i, o, u) dans une donnée chaîne. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return total_uppercase
#   → return total_uppercase
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 549 :
Écrivez un programme Python à compter le nombre de uppercase lettre dans une chaîne. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return str(num).count(str(digit))
#   → return str(num).count(str(digit))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 550 :
Écrivez une fonction qui compte le occurrences de un spécifié chiffre dans un nombre. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : input()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return letter_count
#   → return letter_count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 551 :
Écrivez un programme Python à compter combien de fois chaque lettre apparaît dans une donnée chaîne. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → count = 0
#   → for c in string:
#   →     if c == 'python':
#   →         count += 1
#   → return count
#   → count = 0
#   → for c in string:
#   →     if c == 'python':
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 552 :
Écrivez une fonction à compter le nombre de fois mot “Python” apparaît dans un paragraphe de text. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → count = 0
#   → for c in dict_list:
#   →     if c == item:
#   →         count += 1
#   → return count
#   → count = 0
#   → for c in dict_list:
#   →     if c == item:
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 553 :
Écrivez un programme Python à compter le occurrences de un spécifique élément dans une liste de dictionnaires. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return total_count
#   → return total_count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 554 :
Écrivez une fonction à compter combien de fois la lettre ‘z’ apparaît dans une liste de chaînes. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → count = 0
#   → for c in s:
#   →     if c == '*':
#   →         count += 1
#   → return count
#   → count = 0
#   → for c in s:
#   →     if c == '*':
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 555 :
Écrivez un programme Python à compter le occurrences de le caractère ‘*’ dans une donnée chaîne. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → count = 0
#   → for c in s:
#   →     if c == substring:
#   →         count += 1
#   → return count
#   → count = 0
#   → for c in s:
#   →     if c == substring:
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 556 :
Écrivez une fonction à compter combien de fois substring “123” apparaît dans une chaîne. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : len, open, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len([line for line in file if line.lower().count(word.lower()) > 0])
#   → return len([line for line in file if line.lower().count(word.lower()) > 0])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 557 :
Écrivez un programme Python à compter le nombre de lines dans un fichier texte qui contien le mot “error”. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len([email for email in email_list if email_domain == domain])
#   → return len([email for email in email_list if email_domain == domain])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 558 :
Écrivez une fonction à compter le nombre de fois un particular email domain apparaît dans une liste de email addresses. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 559 :
Écrivez un programme Python à compter le occurrences de le mot “happy” dans une donnée list de phrases. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 560 :
Écrivez une fonction à compter le nombre de fois caractère ‘!’ apparaît dans une liste de chaînes. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → count = 0
#   → for c in lst:
#   →     if c == word:
#   →         count += 1
#   → return count
#   → count = 0
#   → for c in lst:
#   →     if c == word:
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 562 :
Écrivez une fonction à compter le nombre de occurrences de un mot dans une liste de mots. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Fonctions intégrées : isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 563 :
Écrivez un programme Python à compter combien de fois la lettre ‘x’ apparaît dans une liste de mixte données tapez. Utilisez count().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: **
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(square, lst))
#   → return list(map(square, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 565 :
carré List éléments: Write une fonction qui prend une liste de nombres et retourne une liste de leur squares en utilisant map().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: % !=
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(filter(is_odd, lst))
#   → return list(filter(is_odd, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 566 :
filtrer impair nombres: Write une fonction qui prend une liste de nombres et retourne seulement les nombres impairs en utilisant filtrer().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: % ==
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(filter(even_num, lst))
#   → return num % 2 == 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 567 :
filtrer même nombres: Write une fonction qui filtre tous les nombres pairs de une liste en utilisant filtrer().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(str.upper, lst))
#   → return list(map(str.upper, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 568 :
Convert à Uppercase: Write une fonction qui prend une liste de chaînes et retourne le même list avec chaque chaîne converted à uppercase en utilisant map().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: !=
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(filter(call_filter, lst))
#   → return list(filter(call_filter, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 569 :
Remove vide Strings: Write une fonction qui filtre out vide strings de une liste en utilisant filtrer().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : list, map, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(x, 5)
#   → return pow(x, 5)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 570 :
Multiply List éléments: Write une fonction qui prend une liste de nombres et retourne une liste où chaque nombre est multiplied by 5 en utilisant map().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, list, map, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sum((1 for _ in word))
#   → return sum((1 for _ in word))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 571 :
chaîne Lengths: Write une fonction qui prend une liste de chaînes et retourne leur lengths en utilisant map().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: ==
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return word == word[::-1]
#   → return word == word[::-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 572 :
filtrer Palindromes: Write une fonction qui filtre out palindromes (words qui read le même backward) de une liste en utilisant filtrer().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: +
# Fonctions intégrées : reduce, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return reduce(add, lst)
#   → return reduce(add, lst)
#   → import operator
#   → return operator.add(x, y)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 573 :
Sum de List: Write une fonction qui calcule le somme de une liste de nombres en utilisant reduce().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : pow, range, reduce, sum_of_list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return reduce(multiply, lst)
#   → return pow(x, y)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 574 :
produit de List: Write une fonction qui calcule le produit de une liste de nombres en utilisant reduce().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(str.capitalize, lst))
#   → def capitalize_lst(word):
#   →     word = word.capitalize()
#   →     return word
#   → return list(map(capitalize_lst, lst))
#   → return list(map(str.capitalize, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 575 :
Capitalize Strings: Write une fonction qui prend une liste de chaînes et retourne la liste avec chaque chaîne capitalized en utilisant map().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: <
# Fonctions intégrées : reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return reduce(min_number, lst)
#   → return x if x < y else y
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problem 576:
def min_number(x, y):  # defines a function with parameters x, y
    return x if x < y else y  # return sends the result back to the caller
print(number_lst(lst))  # number_lst() runs first, then print() outputs the result
min_number(x, y)  # arguments evaluated first, then function body runs
print(min_number(3, 14))  # min_number() runs first, then print() outputs the result
x < y  # evaluated as True or False → picks which branch
from functools import reduce
def min_number(x, y):  # stored in memory, not executed yet
def number_lst(lst):  # stored in memory, not executed yet
lst = ...  # assigns a value to the variable
print(number_lst(...))  # number_lst() runs with lst=lst
def min_number(x, y):  # stored in memory, not executed yet
def min_number(x, y):  # stored in memory, not executed yet
x = ...  # assigns a value to the variable
y = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(min_number(...))  # min_number() runs with x=3, y=14


#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: >
# Fonctions intégrées : reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return x
#   → return reduce(max_num, lst)
#   → return reduce(min_number, lst)
#   → return x
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 577 :
trouver Maximum: Write une fonction qui trouve le maximum nombre dans une liste en utilisant reduce(). (hint helper fonction)
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: >
# Fonctions intégrées : filter, len, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return word
#   → return word
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 578 :
filtrer Short Words: Write une fonction qui filtre out words shorter que 4 caractères de une liste en utilisant filtrer().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: % +
# Fonctions intégrées : reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return '%s%s' % (x, y)
#   → return '%s%s' % (x, y)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 579 :
Concatenate Strings: Write une fonction qui concatenates tous strings dans une liste en utilisant reduce().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: > <=
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return not num <= 0
#   → return not num <= 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 580 :
filtrer positif nombres: Write une fonction qui filtre seulement les nombres positifs de une liste en utilisant filtrer().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: **
# Fonctions intégrées : list, map, pow()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import math
#   → return math.pow(num, 3)
#   → import math
#   → return math.pow(num, 3)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 581 :
cube List éléments: Write une fonction qui retourne une liste où chaque élément de le entrée list est cubed en utilisant map().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: + **
# Fonctions intégrées : map, pow, reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import math
#   → return math.pow(num, 2)
#   → import math
#   → return math.pow(num, 2)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 582 :
Sum de Squares: Write une fonction qui retourne le somme de squares de une liste de nombres en utilisant map() et reduce().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return f'{first_last[0]} {first_last[1]}'
#   → return f'{first_last[0]} {first_last[1]}'
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 583 :
combiner noms: Write une fonction qui prend deux listes (premier noms, dernier noms) et retourne une liste de full noms en utilisant map().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return word.isalpha()
#   → return word.isalpha()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 584 :
filtrer Non-Alphabetic Strings: Write une fonction qui filtre out strings qui contien non-alphabetic caractères en utilisant filtrer().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: in
# Fonctions intégrées : reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return counts
#   → return counts
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 585 :
Count Words: Write une fonction qui compte combien de fois chaque mot apparaît dans une liste en utilisant reduce(). (hint, résultat dictionnaire)
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: not in
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 586 :
Unique Words: Write une fonction qui filtre out seulement unique words de une liste en utilisant filtrer() et un helper fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: >
# Fonctions intégrées : filter, len, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len(word) > n
#   → return len(word) > n
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 587 :
mot Lengths Greater que N: Write une fonction qui filtre words avec un longueur greater que n en utilisant filtrer().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: % * !=
# Fonctions intégrées : filter, list, map, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(num, num)
#   → return pow(num, num)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 588 :
Apply Multiple fonctions: Write une fonction qui applies deux different fonctions à une liste, l'une après un autre (e.g., premier squares le nombres, puis filtre out même ones).
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: +
# Fonctions intégrées : reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return reduce(lambda total, number: total + number, flattened, 0)
#   → return reduce(lambda total, number: total + number, flattened, 0)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 589 :
Sum de Nested listes: Write une fonction qui aplatit et sums tous éléments de une liste imbriquée en utilisant map() et reduce().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: + -
# Fonctions intégrées : range, reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return acc + [acc[-1] + acc[-2]]
#   → return acc + [acc[-1] + acc[-2]]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 590 :
premier N Fibonacci nombres: Write une fonction qui génère les n premiers Fibonacci nombres en utilisant reduce().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : len, list, map, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len([char for char in word if char in vowels])
#   → return len([char for char in word if char in vowels])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 591 :
Count voyelles dans Strings: Write une fonction qui compte combien de voyelles sont present dans chaque chaîne de une liste en utilisant map() et un helper fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: % + ==
# Fonctions intégrées : filter, reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return num % 2 == 0
#   → return num % 2 == 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 592 :
Sum de même nombres: Write une fonction qui calcule le somme de tous les nombres pairs dans une liste en utilisant filtrer() et reduce().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: >
# Fonctions intégrées : len, reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return x
#   → return x
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 593 :
trouver le plus long chaîne: Write une fonction qui trouve le plus long chaîne dans une liste en utilisant reduce().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: +
# Fonctions intégrées : reduce, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import operator
#   → return operator.add(x, y)
#   → import operator
#   → return operator.add(x, y)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 594 :
Cumulative Sum: Write une fonction qui retourne une liste de cumulative sums de une donnée list en utilisant reduce().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: +
# Fonctions intégrées : reduce, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import operator
#   → return operator.add(x, y)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 595 :
Flatten Nested listes: Write une fonction qui aplatit une liste de listes dans un seul list en utilisant reduce().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: in
# Fonctions intégrées : reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 596 :
mot fréquence Count: Write une fonction qui compte la fréquence de chaque mot dans une liste en utilisant reduce().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: !=
# Fonctions intégrées : filter, list, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted(word) != sorted(target_word)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 597 :
Anagram filtrer: Write une fonction qui filtre out words qui sont anagrams de une donnée mot en utilisant filtrer().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: * +
# Fonctions intégrées : composed_function, func1, func2()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return func2(func1(x))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 598 :
Compose fonctions: Write une fonction qui prend deux fonctions et composes them (c'est-à-dire., applies l'une après un autre).
"""

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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# No top-level code runs — functions must be called externally
"""
Problème 599 :
Group By longueur: Write une fonction qui groups words by leur lengths en utilisant reduce().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % + ** <= ==
# Fonctions intégrées : filter, int, list, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return False
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 600 :
filtrer Prime nombres: Write une fonction qui filtre prime nombres de une liste en utilisant filtrer() et un helper fonction à check pour primality.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: *
# Fonctions intégrées : enumerate, func, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return func(index, item)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 601 :
Map avec Index: Write une fonction qui utilise map() but passes le index de chaque élément à le mapping fonction as well.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: == in
# Fonctions intégrées : any, filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return any((element == x for element in list2))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 602 :
Intersection des deux listes: Write une fonction qui trouve le l'intersection des deux listes en utilisant filtrer().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: + /
# Fonctions intégrées : len, reduce, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import operator
#   → return operator.add(x, y)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 603 :
Average de List: Write une fonction qui calcule le moyenne de une liste de nombres en utilisant reduce().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: * +
# Fonctions intégrées : func, reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return func(x)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 604 :
Compose Multiple fonctions: Write une fonction qui prend une liste de fonctions et an initial valeur, et applies le fonctions sequentially à le valeur en utilisant reduce().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(dic.keys())
#   → return list(dic.keys())
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 605 :
Écrivez un programme à créer un dictionnaire et retrieve une liste de ses clés. Utilisez clé().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted(lst, key=len)
#   → return sorted(lst, key=len)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 606 :
Écrivez une fonction qui trie une liste de chaînes by leur longueur en utilisant la clé paramètre. Utilisez clé().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return x[1]
#   → return x[1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 607 :
Écrivez un programme Python à trier une liste de tuples based on le deuxième élément de chaque tuple en utilisant clé().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return d[target_key]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 608 :
Écrivez une fonction à trier une liste de dictionnaires by un spécifique clé dans chaque dictionnaire en utilisant clé().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return name.split()[-1]
#   → return name.split()[-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 609 :
Écrivez un programme Python à trier une liste de noms by leur dernier nom en utilisant la clé().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: + <=
# Fonctions intégrées : chr, ord, sorted, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return str(s).lower()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 610 :
Écrivez une fonction qui trie une liste de mixte cas strings, en ignorant la casse. Utilisez clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return x
#   → return x
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 611 :
Écrivez un programme Python à trier une liste de flottants dans l'ordre décroissant. Utilisez clé().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 612 :
Écrivez une fonction qui trie une liste de mots by le nombre de voyelles they contien en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return person['age']
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 613 :
Écrivez un programme Python à trier une liste de people by leur age de une liste de dictionnaires.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : int, sorted, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return total
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 614 :
Écrivez une fonction qui trie une liste d'entiers based on le somme de leur les chiffres en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return product['price']
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 615 :
Écrivez un programme Python à trier une liste de products by price en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : map, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (year, month, day)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 616 :
Écrivez une fonction qui trie une liste de dates dans chaîne format (e.g., “YYYY-MM-DD”) en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (tup[0], tup[1])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 617 :
Écrivez un programme Python à trier une liste de tuples by le premier élément, puis by le deuxième si le premier éléments sont equal en utilisant clé.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, sorted, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sum((1 for _ in name))
#   → return sum((1 for _ in name))
#   → return sum((1 for _ in name))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 618 :
Écrivez une fonction qui trie une liste de noms based on le nombre de caractères dans chaque nom en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return employee[1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 619 :
Écrivez un programme Python à trier une liste de employees by leur hire date en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : Counter, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return letter_count[word[0]]
#   → return letter_count[word[0]]
#   → return letter_count[word[0]]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 621 :
Écrivez un programme Python à trier une liste de mots based on la fréquence de leur premier lettre en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : abs, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return abs(x[0])
#   → return abs(x[0])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 622 :
Écrivez une fonction qui trie une liste de tuples by le absolute valeur de le premier élément en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return word
#   → return word
#   → return word
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 623 :
Écrivez un programme Python à trier une liste de chaînes by leur reverse order en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: * + /
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return fahrenheit
#   → return fahrenheit
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 624 :
Écrivez une fonction qui trie une liste de temperatures dans Celsius, converting them à Fahrenheit pour sorting en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return x
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 625 :
Écrivez un programme Python à trier une liste de scores de un game, taking dans account qui certains scores peut be négatif en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return email.split('@')[1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 626 :
Écrivez une fonction qui trie une liste de email addresses by le domain part en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return city[1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 627 :
Écrivez un programme Python à trier une liste de cities by leur population en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return word[-1]
#   → return word[-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 628 :
Écrivez une fonction qui trie une liste de mots by le dernier lettre de chaque mot en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return frequency[number]
#   → return frequency[number]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 629 :
Écrivez un programme Python à trier une liste de nombres by le nombre de fois y appear dans un autre list en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return student[1]
#   → return student[1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 630 :
Écrivez une fonction qui trie une liste de students by leur grades en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return book[1]
#   → return book[1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 631 :
Écrivez un programme Python à trier une liste de book titles by le year they were published en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return file.split('.')[-1]
#   → return file.split('.')[-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 632 :
Écrivez une fonction qui trie une liste de files based on leur file extension en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return movie['release_date']
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 633 :
Écrivez un programme Python à trier une liste de movies by leur release date en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, set, sorted, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sum((1 for _ in unique_words))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 634 :
Écrivez une fonction qui trie une liste de phrases based on le nombre de unique words dans chaque phrase en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(dic.keys())
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 635 :
Écrivez un programme à créer un dictionnaire et retrieve une liste de ses clés.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 636 :
Écrivez une fonction qui prend un dictionnaire et retourne une liste de clés qui ont valeurs greater que 10.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(fruit_prices.keys())
#   → return list(fruit_prices.keys())
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 637 :
créer un dictionnaire de fruits avec leur prices, et print tous le clés.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return max(dic.keys())
#   → return max(dic.keys())
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 638 :
Écrivez un programme à trouver le maximum clé dans un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return dic[name]
#   → return dic[name]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 639 :
créer un dictionnaire de noms et ages, et retourner le clés trié by age.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 640 :
Écrivez une fonction qui accepts un dictionnaire et retourne le clés as un seul concatenated chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for country, capital in dic.items():
#   →     print(f'{country}: {capital}')
#   → for country, capital in dic.items():
#   →     print(f'{country}: {capital}')
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 641 :
créer un dictionnaire de countries et leur capitals, et print chaque clé avec ses corresponding valeur.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 642 :
Écrivez un programme à créer un dictionnaire et compter combien de clés il a.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 643 :
Écrivez une fonction qui prend un dictionnaire et retourne seulement le clés qui start avec un spécifique lettre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted(dic.keys())
#   → return sorted(dic.keys())
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 644 :
créer un dictionnaire de students et leur grades, et print le clés trié alphabetically.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return dic
#   → return dic
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 645 :
Écrivez un programme à créer un dictionnaire des deux listes: l'une pour clés et l'une pour valeurs.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(dic.keys())[::-1]
#   → return list(dic.keys())[::-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 646 :
créer un dictionnaire de colors et leur hexadecimal valeurs, et print le clés en ordre inverse order.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : iter, next()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return next(iter(dic))
#   → return next(iter(dic))
#   → return next(iter(dic))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 647 :
Écrivez une fonction qui retourne le premier clé dans un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for item in cart.keys():
#   →     print(item)
#   → for item in cart.keys():
#   →     print(item)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 648 :
créer un dictionnaire representing un shopping cart, et print le clés de le éléments dans le cart.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return True
#   → return True
#   → return True
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 649 :
Écrivez un programme qui vérifie si un spécifique clé existe dans un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for item, quantity in dic.items():
#   →     if quantity > 5:
#   →         print(item)
#   → for item, quantity in dic.items():
#   →     if quantity > 5:
#   →         print(item)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 650 :
créer un dictionnaire d'éléments et leur quantities, et print clés avec quantities greater que 5.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Fonctions intégrées : isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 651 :
Écrivez une fonction qui accepts un dictionnaire et retourne une liste de clés qui sont des chaînes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sports_dict[sport]
#   → return sports_dict[sport]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 652 :
créer un dictionnaire de sports et leur popularity rankings, et retourner le clés trié by ranking.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Fonctions intégrées : isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 653 :
Écrivez un programme qui retrieves clés de un dictionnaire qui sont de tapez integer.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for index, book in enumerate(dic.keys(), start=1):
#   →     print(f'{index}. {book}')
#   → for index, book in enumerate(dic.keys(), start=1):
#   →     print(f'{index}. {book}')
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 654 :
créer un dictionnaire de books et leur authors, et print le clés formatted as un numbered list.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 655 :
Écrivez une fonction qui prend un dictionnaire et retourne une liste de clés qui sont palindromes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: == in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 656 :
créer un dictionnaire de pets et leur owners, et print tous le clés qui contien la lettre “o”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Fonctions intégrées : isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 657 :
Écrivez un programme qui compte combien de clés dans un dictionnaire sont de tapez tuples.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted(dic.keys())
#   → return sorted(dic.keys())
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 658 :
créer un dictionnaire de movies et leur release years, et retourner le clés as un liste triée.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Fonctions intégrées : isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return key
#   → result = []
#   → for key, value in dic.items():
#   →     if isinstance(value, list):
#   →         result.append(key)
#   → return result
#   → return key
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 659 :
Écrivez une fonction qui retourne le clés de un dictionnaire whose valeurs sont listes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → print('Car Brands:')
#   → for index, brand in enumerate(dic.keys(), start=1):
#   →     print(f'{index}. {brand}')
#   → print('Car Brands:')
#   → for index, brand in enumerate(dic.keys(), start=1):
#   →     print(f'{index}. {brand}')
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 660 :
créer un dictionnaire de car brands et leur models, et print le clés dans un formatted manner.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: >
# Fonctions intégrées : len, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return keys_list[1] if len(keys_list) > 1 else None
#   → return keys_list[1] if len(keys_list) > 1 else None
#   → return keys_list[1] if len(keys_list) > 1 else None
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 661 :
Écrivez un programme qui retrieves le deuxième clé de un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return upper_keys
#   → return upper_keys
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 662 :
créer un dictionnaire de temperatures et leur units, et retourner le clés as uppercase strings.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 663 :
Écrivez une fonction qui prend un dictionnaire et retourne clés qui sont trouvé dans une donnée list.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: <
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → devices = {'Phone': 999, 'Headphones': 50, 'Keyboard': 80, 'Mouse': 25, 'Charger': 15}
#   → affordable = [device for device, price in devices.items() if price < 100]
#   → for device in affordable:
#   →     print(device)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 664 :
créer un dictionnaire de electronic devices et leur prices, et print tous clés avec un price less que $100.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → result = []
#   → for key, value in dic.items():
#   →     if value > 10:
#   →         result.append(key)
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 665 :
Écrivez une fonction qui prend un dictionnaire et retourne une liste de clés qui ont valeurs greater que 10.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for key in fruits.keys():
#   →     print(key)
#   → for key in fruits.keys():
#   →     print(key)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 666 :
créer un dictionnaire de fruits avec leur prices, et print tous le clés. Utilisez clé().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return values
#   → return values
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 667 :
créer un dictionnaire de noms et ages, et retourner le clés trié by age.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 668 :
Écrivez une fonction qui accepts un dictionnaire et retourne le clés as un seul concatenated chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sum((1 for _ in dic))
#   → return sum((1 for _ in dic))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 670 :
Écrivez un programme à créer un dictionnaire et compter combien de clés il a.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 671 :
Écrivez une fonction qui prend un dictionnaire et retourne seulement le clés qui start avec un spécifique lettre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → sorted_keys = sorted(dic.keys())
#   → for key in sorted_keys:
#   →     print(key)
#   → sorted_keys = sorted(dic.keys())
#   → for key in sorted_keys:
#   →     print(key)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 672 :
créer un dictionnaire de students et leur grades, et print le clés trié alphabetically.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 673 :
Écrivez un programme à créer un dictionnaire des deux listes: l'une pour clés et l'une pour valeurs.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(dic.keys())[::-1]
#   → return list(dic.keys())[::-1]
#   → return list(dic.keys())[::-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 674 :
créer un dictionnaire de colors et leur hexadecimal valeurs, et print le clés en ordre inverse order.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : iter, next()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return next(iter(dic))
#   → return next(iter(dic))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 675 :
Écrivez une fonction qui retourne le premier clé dans un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for item in cart.keys():
#   →     print(item)
#   → for item in cart.keys():
#   →     print(item)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 676 :
créer un dictionnaire representing un shopping cart, et print le clés de le éléments dans le cart.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 678 :
créer un dictionnaire d'éléments et leur quantities, et print clés avec quantities greater que 5.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Fonctions intégrées : isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 679 :
Écrivez une fonction qui accepts un dictionnaire et retourne une liste de clés qui sont des chaînes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sports_dict[sport]
#   → return sports_dict[sport]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 680 :
créer un dictionnaire de sports et leur popularity rankings, et retourner le clés trié by ranking.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Fonctions intégrées : isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 681 :
Écrivez un programme qui retrieves clés de un dictionnaire qui sont de tapez integer.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for index, items in enumerate(dic.keys(), start=1):
#   →     print(f'{index}. {items}')
#   → for index, items in enumerate(dic.keys(), start=1):
#   →     print(f'{index}. {items}')
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 682 :
créer un dictionnaire de books et leur authors, et print le clés formatted as un numbered list.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 683 :
Écrivez une fonction qui prend un dictionnaire et retourne une liste de clés qui sont palindromes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 684 :
créer un dictionnaire de pets et leur owners, et print tous le clés qui contien la lettre “o”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Fonctions intégrées : isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 685 :
Écrivez un programme qui compte combien de clés dans un dictionnaire sont de tapez list.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted(movies.keys())
#   → return sorted(movies.keys())
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 686 :
créer un dictionnaire de movies et leur release years, et retourner le clés as un liste triée.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Fonctions intégrées : isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 687 :
Écrivez une fonction qui retourne le clés de un dictionnaire whose valeurs sont listes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for brand in dic.keys():
#   →     print(f'Brand: {brand}')
#   → for brand in dic.keys():
#   →     print(f'Brand: {brand}')
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 688 :
créer un dictionnaire de car brands et leur models, et print le clés dans un formatted manner.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(dic.keys())[1]
#   → return list(dic.keys())[1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 689 :
Écrivez un programme qui retrieves le deuxième clé de un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 690 :
créer un dictionnaire de temperatures et leur units, et retourner le clés as uppercase strings. clés seulement ("Celsius": [0, 20, 37, 100]).
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: > is or
# Fonctions intégrées : max, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → result = dic[0]
#   → for item in dic:
#   →     if item > result:
#   →         result = item
#   → return result
#   → result = dic[0]
#   → for item in dic:
#   →     if item > result:
#   →         result = item
#   → return result
#   → result = dic[0]
#   → for item in dic:
#   →     if item > result:
#   →         result = item
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 691 :
Écrivez un programme à trouver le maximum clé dans un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: **
# Fonctions intégrées : list, map, pow()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import math
#   → return math.pow(num, 2)
#   → import math
#   → return math.pow(num, 2)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 692 :
Écrivez un programme qui prend une liste de nombres et retourne une nouvelle liste avec chaque nombre au carré en utilisant map().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, list, map, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sum((1 for _ in string))
#   → return sum((1 for _ in string))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 693 :
créer un programme qui prend une liste de chaînes et retourne une liste de leur lengths en utilisant map().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: - <=
# Fonctions intégrées : chr, list, map, ord, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return str(word).upper()
#   → return str(word).upper()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 694 :
Écrivez une fonction qui prend une liste de chaînes et convertit tous de them à uppercase en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map, round()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return round(x, 2)
#   → return round(x, 2)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 695 :
donné une liste de flottants, Utilisez `map()` à round tous le nombres à deux decimal places.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: * + /
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return celsius * 9 / 5 + 32
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 696 :
Écrivez un programme qui convertit une liste de temperatures dans Celsius à Fahrenheit en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : chr, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return chr(number)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 697 :
Utilisez `map()` à convert une liste de nombres dans leur corresponding ASCII caractères.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : list, map, reversed()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → result = ''
#   → for char in word:
#   →     result = char + result
#   → return result
#   → result = ''
#   → for char in word:
#   →     result = char + result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 698 :
Écrivez une fonction qui prend une liste de mots et retourne le inversé version de chaque mot en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : list, map, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(number, 2)
#   → return pow(number, 2)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 700 :
créer un programme qui prend une liste d'entiers et retourne une liste où chaque nombre est doubled en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return word[0]
#   → return word[0]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 701 :
Écrivez un programme à take une liste de chaînes et retourner une liste de leur premier caractères en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : int, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return int(word, 2)
#   → return int(word, 2)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 702 :
Utilisez `map()` à convert une liste de binary strings à leur decimal equivalents.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: + <=
# Fonctions intégrées : chr, list, map, ord, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return str(string).lower()
#   → return str(string).lower()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 703 :
Écrivez un programme qui prend une liste de mixte-cas strings et retourne tous strings en minuscule en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : list, map, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(num1, num2)
#   → return pow(num1, num2)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 704 :
donné deux listes de nombres, Utilisez `map()` à multiply chaque pair de nombres de le deux listes together.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: + **
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return math.sqrt(point[0] ** 2 + point[1] ** 2)
#   → return math.sqrt(point[0] ** 2 + point[1] ** 2)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 705 :
Utilisez `map()` à convert une liste de tuples (representing x, y points) dans une liste de leur Euclidean distances de le origin.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return string.split('@')[1]
#   → return string.split('@')[1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 706 :
Écrivez une fonction qui prend une liste de email addresses et extrait le domain noms en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: % ==
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return 'Even'
#   → return 'Even'
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 707 :
Utilisez `map()` à take une liste de nombres et retourner une liste indicating si chaque nombre est pair ou impair.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return not value
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 708 :
Écrivez un programme qui utilise `map()` à convert une liste de chaîne representations de nombres à une liste d'entiers.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return not value
#   → return not value
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 709 :
créer un programme qui prend une liste de Boolean valeurs et negates chaque valeur en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return not value
#   → return not value
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 710 :
Écrivez une fonction qui prend une liste de chaînes et retourne une liste de booleans indicating si chaque chaîne est un palindrome en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return str(word).capitalize()
#   → return str(word).capitalize()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 712 :
Utilisez `map()` à take une liste de chaînes et retourner une liste de chaînes où chaque mot un ses premier lettre capitalized.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return word.replace(' ', '')
#   → return word.replace(' ', '')
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 713 :
Écrivez un programme qui prend une liste de chaînes et supprime tous spaces de chaque chaîne en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : list, map, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(width, height)
#   → return pow(width, height)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 714 :
créer un programme qui prend une liste de tuples representing (width, height) et retourne une liste de leur areas en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return url.split('//')[-1].split('/')[0]
#   → return url.split('//')[-1].split('/')[0]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 715 :
Utilisez `map()` à take une liste de URLs et extraire le domain nom de chaque l'une.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (num, string)
#   → return (num, string)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 716 :
Écrivez une fonction qui prend deux listes: l'une de nombres et l'une de chaînes, et retourne une liste de tuples pairing le éléments en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: - <=
# Fonctions intégrées : chr, list, map, ord, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return str(letter).upper()
#   → return str(letter).upper()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 717 :
créer un programme qui convertit une liste de lowercase lettre à uppercase en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : list, map, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 718 :
Utilisez `map()` à calculate la factorielle de chaque nombre dans une liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda word: word[::-1], words))
#   → return list(map(lambda word: word[::-1], words))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 719 :
Écrivez un programme qui prend une liste de phrases et retourne une liste de phrases dans qui chaque mot est inversé en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return True
#   → return True
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 720 :
Utilisez `map()` à vérifier si le éléments de une liste de chaînes contien seulement alphabetic caractères.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : list, map, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(num, num)
#   → return pow(num, num)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 721 :
Écrivez une fonction qui prend une liste de flottants et retourne une liste où chaque float est au carré en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: %
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return '+1-%s' % number
#   → return '+1-%s' % number
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 722 :
donné une liste de phone nombres, Utilisez `map()` à format them as international phone nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : abs, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return abs(num)
#   → return abs(num)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 723 :
Utilisez `map()` à trouver le absolute valeur de chaque nombre dans une liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (num1, num2)
#   → return (num1, num2)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 724 :
Écrivez un programme qui prend deux listes de integers et retourne une liste de tuples pairing corresponding nombres de chaque list en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: + **
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (r, theta)
#   → return (r, theta)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 725 :
Utilisez `map()` à convert une liste de tuples representing (x, y) coordinates dans polar coordinates.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: **
# Fonctions intégrées : list, map, pow()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import math
#   → return math.pow(num, 3)
#   → import math
#   → return math.pow(num, 3)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 726 :
Écrivez un programme qui utilise `map()` à trouver le cube de chaque nombre dans une liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: **
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (num ** 2, num ** 3)
#   → return (num ** 2, num ** 3)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 727 :
Utilisez `map()` à créer un programme qui prend une liste d'entiers et retourne une liste de leur squares et cubes as tuples.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
#   → return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 728 :
Écrivez un programme qui utilise `map()` à convert une liste de RGB tuples dans hexadecimal color codes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: +
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return word[0] + word[1].upper() + word[2:]
#   → return word[0] + word[1].upper() + word[2:]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 729 :
donné une liste de mixte-cas strings, Utilisez `map()` à retourner une liste de chaînes où chaque deuxième chaîne est converted à uppercase.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return datetime.strptime(date_string, '%Y-%m-%d')
#   → return datetime.strptime(date_string, '%Y-%m-%d')
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 730 :
Écrivez une fonction qui utilise `map()` à convert une liste de dates (dans chaîne format) dans Python `datetime` objets.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return math.sqrt(x)
#   → return math.sqrt(x)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 731 :
Utilisez `map()` à calculate le carré roots de chaque nombre dans une liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: * /
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return score / max_score * 100
#   → return score / max_score * 100
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 732 :
créer un programme qui utilise `map()` à calculate le percentage de chaque score dans une liste de scores based on le maximum score.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import operator
#   → return operator.add(a, b)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 733 :
Écrivez un programme Python qui defines un helper fonction `add(a, b)` à retourner le somme des deux nombres, et utilise it à somme une liste de nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: % ==
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return n % 2 == 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 734 :
créer un programme avec un helper fonction `is_even(n)` qui retourne `True` si un nombre est pair et `False` otherwise, et Utilisez it à filtrer une liste de nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(capitalize_first_letter, lst))
#   → return list(map(capitalize_first_letter, lst))
#   → return str(word).capitalize()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 735 :
Écrivez un programme qui utilise un helper fonction `capitalize_first_letter(word)` à capitalize le premier lettre de chaque mot dans une liste de chaînes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return find_max(lst)
#   → return find_max(lst)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 736 :
Define un helper fonction `find_max(nombres)` qui retourne le maximum nombre de une liste, et Utilisez it dans un programme à trouver le plus grand nombre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: - /
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(convert_to_celsius, lst))
#   → return list(map(convert_to_celsius, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 737 :
créer un helper fonction `convert_to_celsius(fahrenheit)` qui convertit un temperature de Fahrenheit à Celsius, et Utilisez it à convert une liste de temperatures.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(reverse_string, lst))
#   → return list(map(reverse_string, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 738 :
Écrivez un programme qui defines un helper fonction `reverse_string(s)` qui retourne le inversé version de une chaîne, et utilise it à reverse tous strings dans une liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return max(lst, key=count_vowels)
#   → return max(lst, key=count_vowels)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 739 :
Define un helper fonction `count_vowels(word)` qui compte le nombre de voyelles dans un mot, et Utilisez it à trouver le mot avec la plupart voyelles dans une liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: ==
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(filter(is_palindrome, lst))
#   → return list(filter(is_palindrome, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 740 :
créer un programme avec un helper fonction `is_palindrome(word)` qui vérifie si un mot est un palindrome et utilise it à filtrer une liste de mots.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: * **
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(calculate_area, lst))
#   → return list(map(calculate_area, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 741 :
Écrivez un programme qui defines un helper fonction `calculate_area(radius)` à calculate le area de un circle donné ses radius, et utilise it pour une liste de radii.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: *
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(sqaure_number, lst))
#   → return list(map(sqaure_number, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 742 :
Define un helper fonction `square(n)` qui retourne le carré de un nombre, et Utilisez it à carré chaque élément dans une liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → lst = [1, 2, 3, 4, 5, 6]
#   → num = 3
#   → return get_first_n_elements(lst, num)
#   → return lst[:num]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 743 :
créer un programme avec un helper fonction `get_first_n_elements(lst, n)` qui retourne le premier `n` éléments de une liste, et Utilisez it on un sample list.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → result = {}
#   → for d in dicts:
#   →     result = merge_dicts(result, d)
#   → return result
#   → return {**dict1, **dict2}
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 744 :
Écrivez un programme qui defines un helper fonction `merge_dicts(dict1, dict2)` qui fusionne deux dictionnaires, et utilise it à combiner multiple dictionnaires.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: %
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return '%s %s' % (first_name, last_name)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 745 :
Define un helper fonction `format_name(first_name, last_name)` qui retourne un formatted full nom, et Utilisez it à format une liste de noms.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: %
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return a
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 746 :
créer un programme avec un helper fonction `find_gcd(a, b)` qui trouve le greatest commun divisor des deux nombres, et Utilisez it à trouver le GCD de une liste de pairs.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count_occurrences(lst, element)
#   → return count_occurrences(lst, element)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 747 :
Écrivez un programme qui defines un helper fonction `count_occurrences(lst, element)` qui compte occurrences de un élément dans une liste, et utilise it pour une donnée list.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (sort_lst(lst1), sort_lst(lst2))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 748 :
Define un helper fonction `sort_list(lst)` qui trie une liste et retourne le liste triée, et Utilisez it à trier several listes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(extract_URL, lst))
#   → return list(map(extract_URL, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 749 :
créer un programme avec un helper fonction `extract_domain(url)` qui extrait le domain de un URL, et Utilisez it on une liste de URLs.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return remove_duplicates(lst)
#   → return remove_duplicates(lst)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 750 :
Écrivez un programme qui defines un helper fonction `remove_duplicates(lst)` qui supprime en double éléments de une liste, et utilise it on un sample list.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda i: j, lst))
#   → return flatten_list(nested_list)
#   → return list(map(lambda i: j, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 751 :
Define un helper fonction `flatten_list(nested_list)` qui aplatit une liste imbriquée, et Utilisez it à flatten une liste de listes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % + ** <= ==
# Fonctions intégrées : filter, int, list, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(filter(is_prime, lst))
#   → return list(filter(is_prime, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 752 :
créer un programme avec un helper fonction `is_prime(n)` qui vérifie si un nombre est prime, et utilise it à filtrer une liste de nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : list, map, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return factorial
#   → return list(map(calculate_factorial, lst))
#   → return factorial
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 753 :
Écrivez un programme qui defines un helper fonction `calculate_factorial(n)` qui calcule la factorielle de un nombre, et utilise it pour un range de nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : dict, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sort_dict_by_value(dic)
#   → return sort_dict_by_value(dic)
#   → return sort_dict_by_value(dic)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 754 :
Define un helper fonction `sort_dict_by_value(d)` qui trie un dictionnaire by ses valeurs, et Utilisez it à trier une donnée dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return get_unique_elements(lst)
#   → return get_unique_elements(lst)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 755 :
créer un programme avec un helper fonction `get_unique_elements(lst)` qui retourne le unique éléments de une liste, et utilise it on un sample list.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: ==
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return check_anagram(str1, str2)
#   → return check_anagram(str1, str2)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 756 :
Écrivez un programme qui defines un helper fonction `check_anagram(str1, str2)` qui vérifie si deux strings sont anagrams, et utilise it on une liste de chaîne pairs.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return find_index(lst, target1)
#   → return find_index(lst, target1)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 757 :
Define un helper fonction `find_index(lst, element)` qui retourne le index de un élément dans une liste, et utilise it pour une donnée list.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return generate_fibonacci(n)
#   → return generate_fibonacci(n)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 758 :
créer un programme avec un helper fonction `generate_fibonacci(n)` qui génère le premier `n` Fibonacci nombres, et utilise it à print Fibonacci sequences.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: /
# Fonctions intégrées : len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (avg1, avg2)
#   → return (avg1, avg2)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 759 :
Écrivez un programme qui defines un helper fonction `calculate_average(lst)` qui calcule le moyenne de une liste, et utilise it on multiple listes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: *
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(convert_to_kilometers, lst))
#   → return list(map(convert_to_kilometers, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 760 :
Define un helper fonction `convert_to_kilometers(miles)` qui convertit miles à kilometers, et utilise it à convert une liste de distances.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return get_last_n_elements(lst, n)
#   → return get_last_n_elements(lst, n)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 761 :
créer un programme avec un helper fonction `get_last_n_elements(lst, n)` qui retourne le dernier `n` éléments de une liste, et utilise it on un sample list. par exemple
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: >
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(filter(get_positive_numbers, lst))
#   → return list(filter(get_positive_numbers, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 763 :
Define un helper fonction `get_positive_numbers(lst)` qui retourne seulement les nombres positifs de une liste, et utilise it on un sample list.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in and not in
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda word: word, lst1))
#   → return get_common_elements(lst1, lst2)
#   → return list(map(lambda word: word, lst1))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 764 :
créer un programme avec un helper fonction `get_common_elements(lst1, lst2)` qui retourne commun éléments entre deux listes, et utilise it on deux sample listes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % ==
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(check_even_odd, lst))
#   → return list(map(check_even_odd, lst))
#   → return list(map(check_even_odd, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 765 :
Écrivez un programme qui defines un helper fonction `check_even_odd(n)` qui retourne "même" ou "impair" pour un nombre, et utilise it pour une liste de nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(convert_to_uppercase, lst))
#   → return list(map(convert_to_uppercase, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 766 :
Define un helper fonction `convert_to_uppercase(word)` qui convertit un mot à uppercase, et utilise it on une liste de mots.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : len, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len(s)
#   → return list(map(count_characters, lst_str))
#   → return list(map(count_characters, lst_str))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 767 :
créer un programme avec un helper fonction `count_characters(s)` qui compte le caractères dans une chaîne, et utilise it on une liste de chaînes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(remove_special_characters, lst))
#   → return list(map(remove_special_characters, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 768 :
Écrivez un programme qui defines un helper fonction `remove_special_characters(s)` qui supprime les caractères spéciaux de une chaîne, et utilise it on un sample list de chaînes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return results
#   → return results
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 769 :
Define un helper fonction `is_substring(s1, s2)` qui vérifie si `s1` est un substring de `s2`, et utilise it on une liste de chaîne pairs.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sum_of_list(lst)
#   → return sum_of_list(lst)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 770 :
créer un programme avec un helper fonction `sum_of_list(lst)` qui retourne le somme de tous nombres dans une liste, et utilise it on un sample list.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: % ==
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(filter(get_even_numbers, lst))
#   → return list(filter(get_even_numbers, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 771 :
Écrivez un programme qui defines un helper fonction `get_even_numbers(lst)` qui filtre et retourne les nombres pairs de une liste, et utilise it on un sample list.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: +
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return merge_sorted_lists(lst1, lst2)
#   → return merge_sorted_lists(lst1, lst2)
#   → return merge_sorted_lists(lst1, lst2)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 772 :
Define un helper fonction `merge_sorted_lists(lst1, lst2)` qui fusionne et trie deux listes, et utilise it à combiner multiple listes triées.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, range, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 773 :
Écrivez un programme Python à créer un dictionnaire des deux listes, l'une contenant clés et le autre contenant valeurs.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return dic.get(key_to_find, None)
#   → return dic.get(key_to_find, None)
#   → for key, value in dic.items():
#   →     if key == target:
#   →         return value
#   → return None
#   → for key, value in dic.items():
#   →     if key == target:
#   →         return value
#   → return None
#   → return dic.get(key_to_find, None)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 774 :
Écrivez un programme Python à get le valeur de un spécifique clé de un dictionnaire, ou retourner une valeur par défaut si la clé est pas trouvé.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return merge_dic
#   → merged_dict = {**dic1, **dic2}
#   → return merged_dict
#   → return merge_dic
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 775 :
Écrivez un programme Python à merge deux dictionnaires dans l'une.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: != in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return dic
#   → result = {}
#   → for key, value in dic.items():
#   →     if key != target:
#   →         result[key] = value
#   → return result
#   → return dic
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 776 :
Écrivez un programme Python à remove une clé de un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: == in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return True
#   → for key in dic.keys():
#   →     if key == target:
#   →         return 'key exists'
#   → return 'key does not exist'
#   → for key in dic.keys():
#   →     if key == target:
#   →         return 'key exists'
#   → return 'key does not exist'
#   → return True
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 778 :
Écrivez un programme Python à vérifier si une clé donnée existe dans un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : dict, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return dict(sorted(dic.items()))
#   → return dict(sorted(dic.items()))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 779 :
Écrivez un programme Python à trier un dictionnaire by ses clés.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : dict, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return item[1]
#   → sorted_items = sorted(dic.items(), key=sort_key)
#   → return dict(sorted_items)
#   → return item[1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 780 :
Écrivez un programme Python à trier un dictionnaire by ses valeurs.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 781 :
Écrivez un programme Python à compter la fréquence d'éléments dans une liste et store le résultat dans un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: **
# Fonctions intégrées : range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 782 :
Écrivez un programme Python à créer un dictionnaire où le clés sont nombres de 1 à 5, et le valeurs sont le squares de le clés.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return dic
#   → if key in dic:
#   →     dic[key] = new_value
#   → return dic
#   → return dic
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 783 :
Écrivez un programme Python à update le valeur de an existing clé dans un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return dic.keys()
#   → for key in dic:
#   →     print(key)
#   → return dic.keys()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 784 :
Écrivez un programme Python à get tous le clés de un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return dic.values()
#   → return dic.values()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 785 :
Écrivez un programme Python à get tous le valeurs de un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return dic.values()
#   → return dic.values()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 786 :
Écrivez un programme Python à get tous le valeurs de un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return max(dic.values())
#   → return max(dic.values())
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 787 :
Écrivez un programme Python à trouver la clé avec le plus grand valeur dans un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : min()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return min(dic.values())
#   → return min(dic.values())
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 788 :
Écrivez un programme Python à trouver la clé avec le plus petit valeur dans un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, min, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 789 :
Écrivez un programme Python à convert deux listes dans un dictionnaire, où l'une list contient clés et le autre contient valeurs, but skip valeurs si le listes sont de unequal longueur.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 790 :
Écrivez un programme Python à combiner deux dictionnaires by adding valeurs de commun clés.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return inverted
#   → return inverted
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 791 :
Écrivez un programme Python à invert le clés et valeurs de un dictionnaire (c'est-à-dire., make le clés le valeurs et le valeurs le clés).
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: not in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return unique_values
#   → return unique_values
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 792 :
Écrivez un programme Python à remove en double valeurs de un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: ==
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return dic1.keys() == dic2.keys()
#   → return dic1.keys() == dic2.keys()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 793 :
Écrivez un programme Python à vérifier si deux dictionnaires ont le même clés.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 794 :
Écrivez un programme Python à multiply tous le valeurs dans un dictionnaire by 2.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sum((1 for _ in dic))
#   → return sum((1 for _ in dic))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 795 :
Écrivez un programme Python à trouver la longueur (c'est-à-dire., nombre de les paires clé-valeur) de un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → result = {}
#   → for word in lst:
#   →     count = 0
#   →     for char in word:
#   →         count += 1
#   →     result[word] = count
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 796 :
Écrivez un programme Python à map une liste de chaînes à leur lengths en utilisant un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return dic
#   → return dic
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 797 :
Écrivez un programme Python à add une nouvelle la paire clé-valeur à an existing dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: **
# Fonctions intégrées : range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 798 :
Écrivez un programme Python à créer un dictionnaire avec clés as nombres de 1 à 10 et valeurs as leur cubes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return 'Dictionary is empty'
#   → return 'Dictionary is empty'
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 799 :
Écrivez un programme Python à vérifier si un dictionnaire est vide.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: not in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 800 :
Écrivez un programme Python à remove un ensemble de clés de un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(dic.items())
#   → return list(dic.items())
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 801 :
Écrivez un programme Python à convert un dictionnaire dans une liste de tuples, où chaque tuple contient une paire clé-valeur.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : tuple()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return tuple(result.keys())
#   → result = {}
#   → for key, value in dic.items():
#   →     if value == target_value:
#   →         result[key] = value
#   → return result
#   → return tuple(result.keys())
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 802 :
Écrivez un programme Python à trouver tous clés dans un dictionnaire qui map à une donnée valeur.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Fonctions intégrées : isinstance()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return dic
#   → return dic
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 803 :
Écrivez un programme Python à replace le valeur de une clé dans un dictionnaire avec une liste de valeurs si le valeur est pas already une liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: **
# Fonctions intégrées : range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 804 :
Écrivez un programme Python à créer un dictionnaire imbriqué où clés sont nombres et valeurs sont dictionnaires contenant le squares et cubes de le clés.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : dict, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return item[1]
#   → return item[1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 806 :
Écrivez un programme Python à trier un dictionnaire by ses valeurs dans l'ordre décroissant.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : dict()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return dict(lst)
#   → return dict(lst)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 807 :
Écrivez un programme Python à créer un dictionnaire de une liste de tuples.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 808 :
Écrivez un programme Python à filtrer out clés de un dictionnaire qui ont une valeur less que 10.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >=
# Fonctions intégrées : list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(result)
#   → return list(result)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 810 :
Écrivez un programme Python à créer un dictionnaire de students et leur grades, et print tous students who scored plus que 75.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 811 :
Écrivez un programme Python à créer un dictionnaire de mots et leur lengths de une donnée phrase.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 812 :
Écrivez un programme Python à créer un dictionnaire de mots et leur lengths de une donnée phrase.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: not in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → result = {}
#   → for key, value in dic.items():
#   →     first_letter = key[0]
#   →     result[first_letter] = key
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 813 :
Écrivez un programme Python à group words dans un dictionnaire based on leur starting lettre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 814 :
Écrivez un programme Python à iterate à travers un dictionnaire et change le cas de tous clés (upper ou lower).
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 815 :
Écrivez un programme Python à trouver le l'intersection des deux dictionnaires (c'est-à-dire., clés qui sont commun dans les deux dictionnaires).
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 816 :
Écrivez un programme Python à compter combien de fois chaque voyelle occurs dans une donnée phrase en utilisant un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: is not
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 817 :
Écrivez un programme Python à remove tous les paires clé-valeur de un dictionnaire où le valeur est None.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: == in and
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return True
#   → return True
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 818 :
Écrivez un programme Python à vérifier si un dictionnaire contient un spécifique clé et valeur pair.
"""

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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# No top-level code runs — functions must be called externally
"""
Problème 819 :
Écrivez un programme Python à convert un dictionnaire à JSON format en utilisant `json.dumps()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return merged_dict
#   → return merged_dict
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 820 :
Écrivez un programme Python à merge multiple dictionnaires dans l'une.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return product
#   → return product
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 821 :
Écrivez un programme Python à iterate à travers un dictionnaire et calculate le produit de tous ses valeurs.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: * /
# Fonctions intégrées : Fraction, float, len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → from fractions import Fraction
#   → return float(Fraction(sum_values, len_values))
#   → from fractions import Fraction
#   → return float(Fraction(sum_values, len_values))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 822 :
Écrivez un programme Python à calculate le moyenne de tous valeurs dans un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: not in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return dic
#   → return dic
#   → return dic
#   → dic[key1], dic[key2] = (dic[key2], dic[key1])
#   → return dic
#   → return dic
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 823 :
Écrivez un programme Python à swap le valeurs des deux clés dans un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : float()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return largest_key
#   → return largest_key
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 824 :
Écrivez un programme Python à trouver la clé avec le plus grand valeur dans un dictionnaire. N'utilisez pas max().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: <
# Fonctions intégrées : float()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return smallest_key
#   → return smallest_key
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 825 :
Écrivez un programme Python à trouver la clé avec le plus grand valeur dans un dictionnaire. N'utilisez pas min().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return dic
#   → dic.update(new_pairs)
#   → return dic
#   → return dic
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 826 :
Écrivez un programme Python à add multiple new la paire clé-valeur à an existing dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: <=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 827 :
Écrivez un programme Python qui affiche nombres de 1 à 10 en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: <=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 828 :
Écrivez un programme Python qui affiche les nombres pairs entre 1 et 20 en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: >=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 829 :
Écrivez un programme Python à print tous le nombres de 10 à 1 (en ordre inverse order) en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: <
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
#   → count = number
#   → i = 0
#   → while i < count:
#   →     return 'Hello'
#   →     i += 1
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 830 :
Écrivez un programme Python qui asks le utilisateur pour un nombre et keeps printing “Hello” qui many fois en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: <=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 832 :
Écrivez un programme Python qui keeps doubling un nombre (starting de 1) jusqu'à it exceeds 1000 en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: * <=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 833 :
Écrivez un programme Python qui affiche le multiplication table de 5 en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Keywords: while
# Operators: <=
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → total = ...  # stored in memory
#   → print(total)
#
# Loop: check condition → if True run body → check again
"""
Problème 834 :
Écrivez un programme Python qui asks le utilisateur pour nombres et stops lorsque le somme exceeds 50 en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Keywords: while
# Operators: % !=
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → number = ...  # stored in memory
#
# Loop: check condition → if True run body → check again
"""
Problème 835 :
Écrivez un programme Python qui keeps asking le utilisateur pour entrée jusqu'à they saisir an même nombre en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Keywords: while
# Operators: !=
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 836 :
Écrivez un programme Python qui asks le utilisateur à entrée nombres, et affiche le somme lorsque they entrée le nombre 0 en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: + <
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 837 :
Écrivez un programme Python qui affiche la suite de Fibonacci up à le 10th nombre en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Keywords: while
# Operators: !=
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → secret_number = ...  # stored in memory
#   → guess = ...  # stored in memory
#
# Loop: check condition → if True run body → check again
"""
Problème 838 :
Écrivez un programme Python qui keeps asking le utilisateur à guess un secret nombre entre 1 et 10 jusqu'à they guess it correctement en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else | while
# Operators: < in
# Fonctions intégrées : input, len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
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
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 839 :
Écrivez un programme Python qui compte le nombre de voyelles dans un utilisateur-fourni chaîne en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Fonctions intégrées : input()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
#   → string = text
#   → while string:
#   →     return string
#   →     string = string[:-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 840 :
Écrivez un programme Python qui asks le utilisateur à entrée une chaîne et keeps removing le dernier caractère de la chaîne jusqu'à it’s vide en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: >=
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
#   → number = number
#   → while number >= 0:
#   →     return number
#   →     number -= 1
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 841 :
Écrivez un programme Python à count down de un utilisateur-fourni nombre à 0 en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: >=
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
#   → total = 0
#   → num = number
#   → while num >= 0:
#   →     total += num
#   → num = number1
#   → return total
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 842 :
Écrivez un programme Python à keep asking le utilisateur pour les nombres positifs et print le somme lorsque un négatif nombre est entered en utilisant un tandis que loop.\
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Keywords: while
# Operators: !=
# Fonctions intégrées : input()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → password = ...  # stored in memory
#
# Loop: check condition → if True run body → check again
"""
Problème 844 :
Écrivez un programme Python qui asks le utilisateur pour un password et keeps asking jusqu'à le correct password (“python”) est entered en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: <=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 845 :
Écrivez un programme Python qui repeatedly squares un nombre jusqu'à it exceeds 10,000 en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: % * + >
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
#   → num = number
#   → reversed_num = 0
#   → while num > 0:
#   →     reversed_num = reversed_num * 10 + num % 10
#   →     num //= 10
#   → return reversed_num
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 846 :
Écrivez un programme Python à reverse les chiffres de un nombre en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: >
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
#   → num = number
#   → while num > 0:
#   →     return num
#   →     num -= 1
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 848 :
Écrivez un programme Python qui asks le utilisateur à entrée un positif nombre et keeps subtracting 1 jusqu'à it reaches zero en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: % !=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 849 :
Écrivez un programme Python qui génère aléatoire nombres entre 1 et 100 et stops lorsque it génère un nombre divisible by 7 en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Keywords: if/else | while
# Operators: < not in
# Fonctions intégrées : input, len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 851 :
Écrivez un programme Python qui affiche tous le lettre de une chaîne except la voyelles en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: >
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
#   → num = number
#   → count = 0
#   → while num > 0:
#   →     count += 1
#   →     num //= 10
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 852 :
Écrivez un programme Python à compter le nombre de les chiffres dans un nombre en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Keywords: while
# Operators: <
# Fonctions intégrées : input, int, len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(lst)
#
# Loop: check condition → if True run body → check again
"""
Problème 853 :
Écrivez un programme Python à keep adding nombres à une liste jusqu'à la liste contient 10 éléments en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: >=
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
#   → num = number
#   → while num >= 1:
#   →     return num
#   →     num /= 2
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 854 :
Écrivez un programme Python qui keeps dividing un nombre by 2 jusqu'à C'est smaller que 1 en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: ** <=
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
#   → num = number
#   → while num ** 2 <= 1000:
#   →     return num ** 2
#   →     num += 1
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 856 :
Écrivez un programme Python qui asks le utilisateur pour un nombre et keeps printing son carré jusqu'à le carré exceeds 1000 en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else | while
# Operators: % != <=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 857 :
Écrivez un programme Python qui affiche tous le nombres de 1 à 50, skipping multiples de 3, en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: <=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 858 :
Écrivez un programme Python qui keeps adding 5 à un nombre starting de 0 jusqu'à le nombre est greater que 100 en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: <
# Fonctions intégrées : len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 859 :
Écrivez un programme Python qui affiche tous le éléments de une liste en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else | while
# Operators: % != <=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 860 :
Écrivez un programme Python à somme tous les nombres impairs de 1 à 100 en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: <=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 861 :
Écrivez un programme Python qui keeps doubling un nombre (starting de 2) et affiche combien de fois it doubled avant exceeding 1000 en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: >
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 863 :
Écrivez un programme Python qui simule un countdown timer by printing le nombres de 10 à 1, et puis “Lift off!” en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Keywords: while
# Operators: <
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 865 :
Écrivez un programme Python qui asks le utilisateur à entrée 5 nombres et calcule leur produit en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 866 :
Écrivez un programme Python à créer un dictionnaire des deux listes, l'une contenant clés et le autre contenant valeurs. Utilisez zip()
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return dictionary
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 867 :
Écrivez un programme Python à créer un dictionnaire des deux listes, l'une contenant clés et le autre contenant valeurs. N'utilisez pas zip().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return str(name).capitalize()
#   → return str(name).capitalize()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 868 :
Écrivez un programme Python qui defines une fonction `capitalize_words()` qui contient un imbriqué fonction `capitalize()` qui capitalizes un mot. Le `capitalize_words()` fonction devrait retourner une liste avec chaque mot capitalized.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 869 :
Écrivez un programme Python à décompresser une liste de trois éléments dans trois variables.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 870 :
Écrivez un programme Python à décompresser le premier et dernier éléments de une liste tandis que collecting le middle éléments dans un autre variable.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 871 :
Écrivez un programme Python à swap deux variables en utilisant unpacking.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : zip()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 872 :
Écrivez un programme Python à décompresser le clés et valeurs de un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 873 :
Écrivez un programme Python à assign multiple retourner valeurs de une fonction à separate variables en utilisant unpacking.
"""

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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → word = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(first, second, ''.join(...))
"""
Problème 874 :
Écrivez un programme Python à extraire le premier deux caractères et le rest de une chaîne en utilisant unpacking.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 875 :
Écrivez un programme Python à extraire le premier et dernier éléments de un tuple en utilisant unpacking.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 876 :
Écrivez un programme Python à décompresser une liste imbriquée dans separate variables.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : range()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 877 :
Écrivez un programme Python à décompresser un range dans separate variables.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 878 :
Écrivez un programme Python à split un full nom dans premier et dernier nom en utilisant unpacking.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → result = f'Hello, {name}. You are {age} years old.'
#   → return result
#   → result = f'Hello, {name}. You are {age} years old.'
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 879 :
Écrivez un programme Python à assign fonction arguments en utilisant unpacking.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 880 :
Écrivez un programme Python à merge deux listes en utilisant unpacking.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 881 :
Écrivez un programme Python à merge deux dictionnaires en utilisant unpacking.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 882 :
Écrivez un programme Python à décompresser et ignore certain valeurs en utilisant `_`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: +
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return a + b + c
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 883 :
Écrivez un programme Python à décompresser une liste dans positional fonction arguments.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: %
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return '%s is %s years old and lives in %s.' % (name, age, city)
#   → return '%s is %s years old and lives in %s.' % (name, age, city)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 884 :
Écrivez un programme Python à décompresser un dictionnaire dans keyword fonction arguments.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 885 :
Écrivez un programme Python à extraire individual caractères de une chaîne en utilisant unpacking.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 886 :
Écrivez un programme Python à décompresser une liste avec unknown longueur en utilisant le starred expression.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 887 :
Écrivez un programme Python à Utilisez unpacking à l'intérieur de une boucle à iterate à travers une liste de tuples.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 888 :
Écrivez un programme Python à décompresser un tuple returned de une fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sum, zip()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 889 :
Écrivez un programme Python à décompresser une liste de listes et somme corresponding éléments en utilisant le `zip()` fonction. Utilisez List comprehension.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 890 :
Écrivez un programme Python à décompresser un dictionnaire’s éléments et reformat them as les paires clé-valeur.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 891 :
Écrivez un programme Python à Utilisez unpacking à split une phrase dans words et capture le premier et dernier words separately.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 892 :
Écrivez un programme Python à décompresser seulement la voyelles de une donnée mot en utilisant List comprehension.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 893 :
Écrivez un programme Python à décompresser un tuple contenant mixte données tapez.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 894 :
Écrivez un programme Python à décompresser et trier une liste de tuples by le deuxième élément.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: % ==
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 895 :
Écrivez un programme Python à extraire seulement les nombres pairs de une liste en utilisant unpacking à l'intérieur de List comprehension.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 896 :
Écrivez un programme Python à swap trois variables en utilisant unpacking.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : range()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 897 :
Écrivez un programme Python à décompresser un range de nombres dans trois variables et collect le remaining dans un autre variable.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Operators: +
# Fonctions intégrées : add_three()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → add_three = ...  # stored in memory
#   → numbers = ...  # stored in memory
#   → print(add_three(...))
"""
Problème 898 :
Écrivez un programme Python à Utilisez unpacking à l'intérieur de une fonction lambda à add trois nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, str()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 899 :
Écrivez un programme Python à extraire et reverse les chiffres de un nombre en utilisant unpacking.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : max, min()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (min(lst), max(lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 900 :
Écrivez un programme Python à Utilisez unpacking dans une fonction qui retourne le minimum et maximum de une liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → pass
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 901 :
Écrivez un programme Python à décompresser une liste de tuples et extraire le premier éléments en utilisant List comprehension.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return ages
#   → return ages
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 902 :
Écrivez un programme Python à décompresser une liste de dictionnaires et extraire tous le valeurs under un spécifique clé.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 903 :
Écrivez un programme Python à Utilisez unpacking à separate nombres dans un mathematical expression.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 904 :
Écrivez un programme Python à décompresser et reassign dictionnaire valeurs dynamically.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 905 :
Écrivez un programme Python à Utilisez unpacking à extraire domain et subdomain de an email address.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 906 :
Écrivez un programme Python à décompresser imbriqué tuples à l'intérieur de une liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : divmod()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 907 :
Écrivez un programme Python à décompresser valeurs returned de `divmod()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 908 :
Écrivez un programme Python à générer un aléatoire integer entre 1 et 100.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 909 :
Écrivez un programme Python à générer un aléatoire floating-point nombre entre 0 et 1.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 910 :
Écrivez un programme Python à générer un aléatoire même integer entre 10 et 50.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 911 :
Écrivez un programme Python à randomly select un élément de une donnée list.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 912 :
Écrivez un programme Python à shuffle une liste randomly.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, range()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 913 :
Écrivez un programme Python à select 3 unique aléatoire nombres de une liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 914 :
Écrivez un programme Python à générer un aléatoire floating-point nombre entre 5 et 10.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 915 :
Écrivez un programme Python à générer un aléatoire lettre de le anglais alphabet.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 916 :
Écrivez un programme Python à simulate le rolling de un six-sided die.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 917 :
Écrivez un programme Python à simulate flipping un coin.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 918 :
Écrivez un programme Python à randomly select un premier nom et dernier nom de separate listes et combiner them.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: +
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 919 :
Écrivez un programme Python à générer un aléatoire password avec 8 caractères y compris lettre, les chiffres, et les caractères spéciaux.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 920 :
Écrivez un programme Python à générer un aléatoire boolean valeur (vrai ou False).
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : range()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 921 :
Écrivez un programme Python à générer 5 aléatoire nombres entre 1 et 100 et store them dans une liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, range()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 922 :
Écrivez un programme Python à select un aléatoire subset de 4 éléments de une liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: + -
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 923 :
Écrivez un programme Python à générer un aléatoire date dans le year 2023.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 924 :
Écrivez un programme Python à randomly pick un élément de un ensemble.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 925 :
Écrivez un programme Python à randomly générer un 6-chiffre verification code.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 926 :
Écrivez un programme Python à générer un aléatoire hexadecimal color code.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 927 :
Écrivez un programme Python à générer un aléatoire phone nombre dans le format (XXX) XXX-XXXX.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 928 :
Écrivez un programme Python à générer un aléatoire 4-chiffre PIN code.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 929 :
Écrivez un programme Python à simulate un aléatoire dice roll avec deux six-sided dice.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : range, str()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 930 :
Écrivez un programme Python à générer un aléatoire IP address.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: +
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 931 :
Écrivez un programme Python à générer un aléatoire strong password de 12 caractères.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 932 :
Écrivez un programme Python à randomly pick an élément de un tuple.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: try/except
# Operators: /
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(result)
#   → print(result)
#   → print(result)
"""
Problème 933 :
Écrivez un programme Python à handle division by zero exception lorsque dividing deux nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(value)
#   → print(value)
#   → print(value)
"""
Problème 934 :
Écrivez un programme Python à handle an IndexError lorsque accessing an out-de-range list index.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(value)
#   → print(value)
#   → print(value)
"""
Problème 935 :
Écrivez un programme Python à handle un KeyError lorsque accessing un non-existent clé dans un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: try/except
# Fonctions intégrées : int()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(num)
#   → print(num)
#   → print(num)
"""
Problème 936 :
Écrivez un programme Python à handle un ValueError lorsque converting an invalid chaîne à un entier.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: try/except
# Operators: +
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(result)
#   → print(result)
#   → print(result)
"""
Problème 937 :
Écrivez un programme Python à handle un TypeError lorsque trying à concatenate une chaîne avec un entier.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: try/except
# Fonctions intégrées : open()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(content)
#   → print(content)
#   → print(content)
"""
Problème 938 :
Écrivez un programme Python à handle un FileNotFoundError lorsque trying à open un non-existent file.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Keywords: try/except
# Fonctions intégrées : Person()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 939 :
Écrivez un programme Python à catch an AttributeError lorsque accessing un non-existent attribute de un objet.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: try/except
# Operators: +
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(result)
#   → print(result)
#   → print(result)
"""
Problème 940 :
Écrivez un programme Python à catch un NameError lorsque accessing an undefined variable.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: try/except
# Fonctions intégrées : open()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(result)
#   → print(result)
#   → print(result)
"""
Problème 941 :
Écrivez un programme Python à handle un PermissionError lorsque trying à write à un read-seulement file.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: try/except
# Operators: /
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(result)
#   → print(result)
#   → print(result)
"""
Problème 942 :
Écrivez un programme Python à Utilisez un try-except-else block à catch errors dans division.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: try/except
# Operators: /
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(result)
#   → print(result)
#   → print(result)
"""
Problème 943 :
Écrivez un programme Python à Utilisez un finally block à always print un message après exception handling.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Keywords: if/else | try/except
# Operators: <
# Fonctions intégrées : NegativeNumberError()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → if n < 0:
#   →     raise NegativeNumberError('Negative numbers are not allowed')
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 944 :
Écrivez un programme Python à raise un custom exception si un nombre est négatif.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: try/except
# Operators: /
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(result)
#   → print(result)
#   → print(result)
"""
Problème 945 :
Écrivez un programme Python à handle un multiple exception scenario (ZeroDivisionError et TypeError).
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: try/except
# Operators: >=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
"""
Problème 946 :
Écrivez un programme Python à Utilisez le `assert` statement à raise an AssertionError si une condition est false.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: try/except
# Fonctions intégrées : MemoryError()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
"""
Problème 947 :
Écrivez un programme Python à handle un MemoryError safely by simulating l'exception.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: try/except
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 948 :
Écrivez un programme Python à catch un RecursionError lorsque une fonction appelle itself infinitely.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
"""
Problème 949 :
Écrivez un programme Python à catch un ModuleNotFoundError lorsque trying à import un non-existent module.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: try/except
# Fonctions intégrées : open()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
"""
Problème 950 :
Écrivez un programme Python à catch an IOError lorsque trying à read un fichier qui fait pas exist.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
"""
Problème 951 :
Écrivez un programme Python à catch un KeyboardInterrupt exception safely by simulating le interrupt.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 952 :
Écrivez un programme Python à convert une chaîne à uppercase en utilisant un construit-dans méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 953 :
Écrivez un programme Python à compter le occurrences de un spécifique caractère dans une chaîne en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 954 :
Écrivez un programme Python à vérifier si une chaîne commence par un spécifique prefix en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 955 :
Écrivez un programme Python à replace tous occurrences de un mot dans une chaîne en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 956 :
Écrivez un programme Python à split une phrase dans words en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 957 :
Écrivez un programme Python à join une liste de mots dans une phrase en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 958 :
Écrivez un programme Python à remove leading et trailing spaces de une chaîne en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 959 :
Écrivez un programme Python à trouver le index de un spécifique élément dans une liste en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 960 :
Écrivez un programme Python à trier une liste de nombres dans l'ordre croissant en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 961 :
Écrivez un programme Python à reverse le order d'éléments dans une liste en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 962 :
Écrivez un programme Python à add un élément at le end de une liste en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 963 :
Écrivez un programme Python à remove le dernier élément de une liste en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 964 :
Écrivez un programme Python à remove un spécifique élément de une liste en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Fonctions intégrées : list()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → person = ...  # stored in memory
#   → keys = ...  # stored in memory
#   → print(list(...))
"""
Problème 965 :
Écrivez un programme Python à get tous le clés de un dictionnaire en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Fonctions intégrées : list()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → person = ...  # stored in memory
#   → values = ...  # stored in memory
#   → print(list(...))
"""
Problème 966 :
Écrivez un programme Python à get tous le valeurs de un dictionnaire en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 967 :
Écrivez un programme Python à merge deux dictionnaires en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 968 :
Écrivez un programme Python à remove an élément de un dictionnaire en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 969 :
Écrivez un programme Python à vérifier si un ensemble contient un spécifique élément en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 970 :
Écrivez un programme Python à remove et retourner an arbitrary élément de un ensemble en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 971 :
Écrivez un programme Python à clear tous éléments de une liste en utilisant une méthode.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : int()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 972 :
Écrivez un programme Python à parse un entier de une chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : float()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 973 :
Écrivez un programme Python à parse un flottant de une chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: ==
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 974 :
Écrivez un programme Python à parse un booléen de une chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 975 :
Écrivez un programme Python à parse multiple integers de un séparés par des virgules chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 976 :
Écrivez un programme Python à parse un date de une chaîne dans le format'YYYY-MM-DD'.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 977 :
Écrivez un programme Python à extraire nombres de un mixte chaîne.
"""

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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# No top-level code runs — functions must be called externally
"""
Problème 978 :
Écrivez un programme Python à parse un JSON chaîne dans un Python dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 979 :
Écrivez un programme Python à convert un dictionnaire à un JSON chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 980 :
Écrivez un programme Python à parse an XML chaîne et extraire spécifique données.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : parse_qs()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 981 :
Écrivez un programme Python à parse les paires clé-valeur de une requête chaîne.
"""

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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# No top-level code runs — functions must be called externally
"""
Problème 982 :
Écrivez un programme Python à parse un CSV chaîne dans une liste de listes.
"""

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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# No top-level code runs — functions must be called externally
"""
Problème 983 :
Écrivez un programme Python à parse HTML et extraire tous links en utilisant le standard library.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 984 :
Écrivez un programme Python à parse un fois chaîne dans le format'HH:MM:SS'dans un `datetime.time` objet.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : int()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 985 :
Écrivez un programme Python à parse un hexadecimal nombre chaîne dans un entier.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : int()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 986 :
Écrivez un programme Python à parse un binary nombre chaîne dans un entier.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : float()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 987 :
Écrivez un programme Python à parse un scientific notation chaîne dans un flottant.
"""

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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# No top-level code runs — functions must be called externally
"""
Problème 988 :
Écrivez un programme Python à parse un configuration file (.ini format) et extraire un setting.
"""

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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# No top-level code runs — functions must be called externally
"""
Problème 989 :
Écrivez un programme Python à parse un markdown chaîne et extraire le text de un header.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 991 :
Écrivez un programme Python à parse un JSON array dans un Python list.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : float()
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 992 :
Écrivez un programme Python à parse un currency chaîne et extraire le numeric valeur.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 993 :
Écrivez un programme Python à parse command-line arguments.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → pass
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 994 :
Écrivez un programme Python à slice le premier 5 caractères de une chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 995 :
Écrivez un programme Python à slice le dernier 4 caractères de une chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 996 :
Écrivez un programme Python à slice tous éléments de une liste except le premier deux.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 997 :
Écrivez un programme Python à slice le dernier 3 éléments de une liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 998 :
Écrivez un programme Python à extraire seulement le même-indexed caractères de une chaîne en utilisant slicing.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → pass
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 999 :
Écrivez un programme Python à extraire seulement le impair-indexed caractères de une chaîne en utilisant slicing.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
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
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
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
Problème 1000 :
Écrivez un programme Python à reverse une chaîne en utilisant slicing.
"""

