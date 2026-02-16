# from abc import ABC, abstractmethod
# import math

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def get_salary(self):
#         return self.salary

# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         Employee.__init__(self, name, salary)
#         self.department = department

#     def get_department(self):
#         return self.department

# class Developer(Employee):
#     def __init__(self, name, salary, programming_language):
#         Employee.__init__(self, name, salary)
#         self.programming_language = programming_language

#     def get_programming_language(self):
#         return self.programming_language
    
# class TeamLead(Manager, Developer):
#     def __init__(self, name, salary, department, programming_language, team_size):
#         Manager.__init__(self, name, salary, department)
#         Developer.__init__(self, name, salary, programming_language)
#         self.team_size = team_size

#     def get_team_size(self):
#         return self.team_size


# test_user = TeamLead(name="Andrii", salary=1000000, department="QA", programming_language="Python", team_size=5)

# print('Test for the salary: ' + str(test_user.get_salary()))
# print('Test for the department: ' + str(test_user.get_department()))
# print('Test fpr the programming language: ' + str(test_user.get_programming_language()))
# print('Test for the team size: ' + str(test_user.get_team_size()))

# ########################################################################################################################

# class Figure(ABC):
#     def __init__(self):
#         pass

#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Circle(Figure):
#     def __init__(self, radius):
#         if radius <= 0:
#             raise ValueError('Radius must be positive')
#         self.__radius = radius

#     def area(self):
#         return math.pi * self.__radius ** 2

#     def perimeter(self):
#         return 2 * math.pi * self.__radius



# class Triangle(Figure):
#     def __init__(self, a, b, c):
#         if a <= 0 or b <= 0 or c <= 0:
#             raise ValueError('All sides must be positive')

#         if (a + b <= c or
#             a + c <= b or
#             b + c <= a):
#             raise ValueError('One side more than two combined is not allowed')

#         self.__a = a
#         self.__b = b
#         self.__c = c

#     def area(self):
#         s = (self.__a + self.__b + self.__c) / 2  # half of the perimeter
#         return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c)) # returning the area using formula from google

#     def perimeter(self):
#         return self.__a + self.__b + self.__c #returning the perimeter by adding all sides together
    

# test_circle = Circle(radius=5)
# print(f"Test for the area of the circle: {test_circle.area():.2f}")
# print(f"Test for the perimeter of the circle: {test_circle.perimeter():.2f}")

# test_triangle = Triangle(a=3, b=4, c=5)
# print('Test for the area of the triangle: ' + str(test_triangle.area()))
# print('Test for the perimeter of the triangle: ' + str(test_triangle.perimeter()))
