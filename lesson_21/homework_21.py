from sqlalchemy import create_engine, text, Table, Column, Integer, ForeignKey, String, MetaData
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import psycopg2
import psycopg2.extras
import random

DATABASE_URL = "postgresql+psycopg2://admin:admin@localhost:5432/hillel_db"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Check connection to the database
# with engine.connect() as connection:
#     result = connection.execute(text("SELECT * FROM categories"))
#     for row in result:
#         print(row)

students_courses = Table(   # створюємо таблицю для зв'язку між студентами та курсами
    'students_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):    # створюємо модель для таблиці students
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    courses = relationship(
        'Course', 
        secondary=students_courses, 
        back_populates='students'
        )
    
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"

class Course(Base): # створюємо модель для таблиці courses
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship(    # створюємо зв'язок між курсами та студентами через таблицю students_courses
        'Student', 
        secondary=students_courses, 
        back_populates='courses'
        )
    
    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}')>"
    
# Створюємо таблиці в базі даних та додаємо студентів та курси
Base.metadata.create_all(engine)
course_name = ['Java', 'Python', 'JavaScript']  # список назв курсів

courses = []

for name in course_name:    # проходимо по списку назв курсів та створюємо об'єкти Course, додаємо їх до сесії та зберігаємо в список courses
    course = Course(name=name)
    session.add(course)
    courses.append(course)

student_names = ['Andrii', 'Masha', 'Alex', 'Tanya', 'Sergii']  # список імен студентів

students = []

for name in student_names:  # проходимо по списку імен студентів та створюємо об'єкти Student, додаємо їх до сесії та зберігаємо в список students
    student = Student(name=name)
    student.courses = random.sample(courses, random.randint(1, 2))  # випадковим чином призначаємо студенту від 1 до 2 курсів
    session.add(student)
    students.append(student)
session.commit()


# Виводимо всіх студентів та їх курси
courses = session.query(Course).all()  # отримуємо всі курси з бази даних
for course in courses:  # проходимо по кожному курсу та виводимо його назву та імена студентів, які його відвідують
    print(f"Course: {course.name}")
    for student in course.students:
        print(f" - Student: {student.name}")

# Виводимо курси студента з ім'ям "Andrii"
student = session.query(Student).filter_by(name="Andrii").first()  # отримуємо студента з ім'ям "Andrii" з бази даних
if student:  # якщо студент знайдений, виводимо його курси
    print(f"Student: {student.name}")
    for course in student.courses:
        print(f" - Course: {course.name}")
else:  # якщо студент не знайдений, виводимо повідомлення
    print("Student 'Andrii' not found.")

# Виводимо студентів, які відвідують курс з ім'ям "Python"
course = session.query(Course).filter_by(name="Python").first()  # отримуємо курс з ім'ям "Python" з бази даних
if course:  # якщо курс знайдений, виводимо його студентів
    print(f"Course: {course.name}")
    for student in course.students:
        print(f" - Student: {student.name}")
else:  # якщо курс не знайдений, виводимо повідомлення
    print("Course 'Python' not found.")

# Оновлюємо ім'я курсу "JavaScript" на "JS"
course = session.query(Course).filter_by(name="JavaScript").first()  # отримуємо курс з ім'ям "JavaScript" з бази даних
if course:  # якщо курс знайдений, оновлюємо його ім'я та зберігаємо зміни
    course.name = "JS"
    session.commit()
    print("Course name updated to 'JS'.")

# Видаляємо студента з ім'ям "Alex"
student = session.query(Student).filter_by(name="Alex").first()  # отримуємо студента з ім'ям "Alex" з бази даних
if student:  # якщо студент знайдений, видаляємо його та зберігаємо зміни
    session.delete(student)
    session.commit()
    print("Student 'Alex' deleted.")

# Виводимо стейт студента з ім'ям "Alex" після видалення
print("\nCheck if student 'Alex' still exists:")
student = session.query(Student).filter_by(name="Alex").first()
if student:  # якщо студент знайдений, виводимо його ім'я
    print(f"Student: {student.name}")
else:  # якщо студент не знайдений, виводимо повідомлення
    print("Student 'Alex' not found.")

