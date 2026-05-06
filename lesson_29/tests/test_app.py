import pytest
import allure
from sqlalchemy import text


from app.homework_21 import (
    engine,
    Base,
    get_session,
    create_course,
    get_course_by_name,
    create_student,
    get_student_by_name,
    update_course_name,
    delete_student_by_name,
)


# ---------- FIXTURE ----------

@pytest.fixture
def session():
    # create tables
    Base.metadata.create_all(engine)
    session = get_session()
    yield session

    session.close()


# ---------- CONNECTION TEST ----------
@allure.feature("DB connection test")
def test_db_connection():
    conn = engine.connect()
    result = conn.execute(text("SELECT 1"))
    assert result.scalar() == 1
    conn.close()


# ---------- INSERT ----------
@allure.feature("Insert operations test")
def test_create_course(session):
    with allure.step("Creating course 'TestCourse'"):
        create_course(session, "TestCourse")

    with allure.step("Retrieving course 'TestCourse'"):
        course = get_course_by_name(session, "TestCourse")

    with allure.step("Asserting course creation"):
        assert course is not None
        assert course.name == "TestCourse"


# ---------- SELECT ----------
@allure.feature("Select operations test")
def test_get_student(session):
    with allure.step("Creating course 'Python'"):
        course = create_course(session, "Python")

    with allure.step("Creating student 'TestUser'"):
        create_student(session, "TestUser", [course])

    with allure.step("Retrieving student 'TestUser'"):
        student = get_student_by_name(session, "TestUser")

    with allure.step("Asserting student retrieval"):
        assert student is not None
        assert student.name == "TestUser"
        assert len(student.courses) > 0


# ---------- UPDATE ----------
@allure.feature("Update operations test")
def test_update_course(session):
    with allure.step("Creating course 'OldName'"):
        create_course(session, "OldName")

    with allure.step("Updating course name"):
        update_course_name(session, "OldName", "NewName")

    with allure.step("Retrieving updated course"):
        updated = get_course_by_name(session, "NewName")


    with allure.step("Asserting course update"):
        assert updated is not None
        assert updated.name == "NewName"


# ---------- DELETE ----------
@allure.feature("Delete operations test")
def test_delete_student(session):
    course = create_course(session, "JS")
    create_student(session, "DeleteMe", [course])

    with allure.step("Deleting student 'DeleteMe'"):
        delete_student_by_name(session, "DeleteMe")

    with allure.step("Retrieving deleted student"):
        student = get_student_by_name(session, "DeleteMe")

    with allure.step("Asserting student deletion"):
        assert student is None