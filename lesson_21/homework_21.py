from sqlalchemy import create_engine, Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
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


### Створюємо функції
# Створюємо курс, якщо він ще не існує в базі даних, та повертаємо його
def create_course(session, course_name):
    existing = get_course_by_name(session, course_name)  # перевіряємо, чи курс з таким ім'ям вже існує в базі даних

    if existing:
        print(f"Course '{course_name}' already exists. Skipping creation.")
        return existing  # повертаємо існуючий курс, якщо він вже є в базі даних
    
    course = Course(name=course_name)  # створюємо новий курс
    session.add(course)
    session.commit()
    return course

# Створюємо студента, якщо він ще не існує в базі даних, та призначаємо йому випадкові курси, потім повертаємо його
def create_student(session, student_name, courses):
    existing_student = get_student_by_name(session, student_name)  # перевіряємо, чи студент з таким ім'ям вже існує в базі даних

    if existing_student:
        print(f"Student '{student_name}' already exists. Skipping creation.")
        return existing_student  # повертаємо існуючого студента, якщо він уже є в базі даних
        
    student = Student(name=student_name)  # створюємо нового студента
    student.courses = random.sample(courses, random.randint(1, 2))  # випадковим чином призначаємо студенту від 1 до 2 курсів
    session.add(student)
    session.commit()

    return student


# Виводимо всіх студентів та їх курси
def get_all_courses_and_students(session):
    courses = session.query(Course).all()  # отримуємо всі курси з бази даних

    for course in courses:  # проходимо по кожному курсу та виводимо його назву та імена студентів, які його відвідують
        print(f"Course: {course.name}")
        for student in course.students:
            print(f" - Student: {student.name}")

# Вертаємо курс за ім'ям
def get_course_by_name(session, course_name):
    return session.query(Course).filter_by(name=course_name).first()  # отримуємо курс з ім'ям з бази даних

# Вертаємо студента за ім'ям
def get_student_by_name(session, student_name):
    return session.query(Student).filter_by(name=student_name).first()  # отримуємо студента з ім'ям з бази даних


# Виводимо курси студента з ім'ям
def print_student_by_name(session, student_name):
    student = get_student_by_name(session, student_name)  # отримуємо студента з ім'ям з бази даних

    if student:  # якщо студент знайдений, виводимо його курси
        print(f"Student: {student.name}")
        for course in student.courses:
            print(f" - Course: {course.name}")
    else:  # якщо студент не знайдений, виводимо повідомлення
        print(f"Student '{student_name}' not found.")

# Виводимо студентів, які відвідують курс за ім'ям
def print_students_by_course_name(session, course_name):
    course = get_course_by_name(session, course_name)  # отримуємо курс з ім'ям з бази даних

    if course:  # якщо курс знайдений, виводимо його студентів
        print(f"Course: {course.name}")
        for student in course.students:
            print(f" - Student: {student.name}")
    else:  # якщо курс не знайдений, виводимо повідомлення
        print(f"Course '{course_name}' not found.")

# Оновлюємо ім'я курсу
def update_course_name(session, old_name, new_name):
    course = get_course_by_name(session, old_name)  # отримуємо курс з ім'ям з бази даних

    if course:  # якщо курс знайдений, оновлюємо його ім'я та зберігаємо зміни
        course.name = new_name
        session.commit()
        print(f"Course '{old_name}' updated to '{new_name}'.")
    else:
        print(f"Course '{old_name}' not found.")

# Видаляємо студента за ім'ям
def delete_student_by_name(session, student_name):
    student = get_student_by_name(session, student_name)  # отримуємо студента з ім'ям з бази даних

    if student:  # якщо студент знайдений, видаляємо його та зберігаємо зміни
        session.delete(student)
        session.commit()
        print(f"Student '{student_name}' deleted.")


### Викликаємо функції
# Створення курсів та студентів
student_names = ['Andrii', 'Masha', 'Alex', 'Tanya', 'Sergii']  # список імен студентів
course_name = ['Java', 'Python', 'JavaScript']  # список назв курсів

courses = []
for name in course_name:    # проходимо по списку назв курсів та створюємо об'єкти Course, додаємо їх до сесії та зберігаємо в список courses
    course = create_course(session, name)
    courses.append(course)

for name in student_names:   # проходимо по списку імен студентів та створюємо об'єкти Student, призначаємо їм випадкові курси та додаємо їх до сесії
    create_student(session, name, courses) 

# Виводимо інформацію про студентів та курси за допомогою функцій, а також демонструємо оновлення та видалення даних (зокрема, спробу вивести інформацію про видаленого студента)
print_student_by_name(session, "Andrii")
delete_student_by_name(session, "Alex")
print_student_by_name(session, "Alex") # спроба вивести інформацію про видаленого студента
update_course_name(session, "JavaScript", "JS")
print_students_by_course_name(session, "JS")
get_all_courses_and_students(session)