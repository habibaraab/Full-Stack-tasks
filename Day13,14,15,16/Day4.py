#Q1
# class Book:
#       def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages



# obj = Book("Spring Boot","Mina",980)
# print(obj.author)
# print(obj.title)
# print(obj.pages)


#Q2
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades

#     def avg(self):
       
#         if  not self.grades :
#             return 0
#         else:
#             return sum(self.grades) / len(self.grades)
       
    
# st = Student("habiba", [90, 92, 78, 95])
# avg = st.avg()
# print(f"Average Grade: {avg}")


#Q3
# class Vehicle:
#     def start_engine(self):
#         print("Start Engine...")

# class Car(Vehicle):
#     def start_engine(self):
#         print("Car engine start")


# class Bike(Vehicle):

#     def start_engine(self):
#         print("Bike engine start")


# obj = Vehicle()
# my_car = Car()
# my_bike =Bike()
   
# obj.start_engine()
# my_car.start_engine()
# my_bike.start_engine()


#Q4
# class Engine:
#     def __init__(self, power, engine_type):
#         self.power = power
#         self.type = engine_type

# class Car:
#     def __init__(self, name, model, engine):
#         self.name = name
#         self.model = model 
#         self.engine = engine 
        
#     def get_details(self):
#         print(f"Engine Power: {self.engine.power}")
#         print(f"Engine Type: {self.engine.type}")

# eng = Engine(450, "V8")

# c = Car("BMW", "M5", eng)

# c.get_details()


#Q5
# from abc import ABC, abstractmethod

# class Employee(ABC):
#     def __init__(self, name, salary):
#         self.name = name
#         self.base_salary = salary

#     @abstractmethod
#     def calculate_salary(self):
#         pass

# class Developer(Employee):
#     def calculate_salary(self):
#         bonus = self.base_salary * 0.10
#         return self.base_salary + bonus

# class Designer(Employee):
#     def calculate_salary(self):
#         bonuss = 1000
#         return self.base_salary + bonuss


# employees = [
#         Developer("habiba", 80000),
#         Designer("ali", 75000),
#         Developer("asmaa", 95000)
# ]
   
# for employee in employees:
#         final_salary = employee.calculate_salary()
#         print(f"{employee.name}:  Salary is :{final_salary}")