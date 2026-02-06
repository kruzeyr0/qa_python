class Student:  # Create a Student class with keyword arguments for first name, last name, age, and average score
    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.age = kwargs.get('age')
        self.avg_score = kwargs.get('avg_score')

    def update_average_grade(self, avg_score):  # Define a method to update the average grade of the student
        self.avg_score = avg_score

    def __str__(self):
        return f"First_name: {self.first_name}, Last_name {self.last_name}, Age: {self.age}, Avg_score: {self.avg_score}" # Define the method to return a string representation of the Student object


Andrii = Student(first_name="Andrii", last_name="Katrych", age=33, avg_score=90) # Create an instance of the Student class with my information
print(Andrii)

Andrii.update_average_grade(100)    # Update average grade to 100
print(Andrii)