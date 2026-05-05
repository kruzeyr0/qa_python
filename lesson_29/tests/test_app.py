import pytest
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

def test_db_connection():
    conn = engine.connect()
    result = conn.execute(text("SELECT 1"))
    assert result.scalar() == 1
    conn.close()


# ---------- INSERT ----------

def test_create_course(session):
    create_course(session, "TestCourse")

    course = get_course_by_name(session, "TestCourse")

    assert course is not None
    assert course.name == "TestCourse"


# ---------- SELECT ----------

def test_get_student(session):
    course = create_course(session, "Python")
    create_student(session, "TestUser", [course])

    student = get_student_by_name(session, "TestUser")

    assert student is not None
    assert student.name == "TestUser"
    assert len(student.courses) > 0


# ---------- UPDATE ----------

def test_update_course(session):
    create_course(session, "OldName")

    update_course_name(session, "OldName", "NewName")

    updated = get_course_by_name(session, "NewName")

    assert updated is not None
    assert updated.name == "NewName"


# ---------- DELETE ----------

def test_delete_student(session):
    course = create_course(session, "JS")
    create_student(session, "DeleteMe", [course])

    delete_student_by_name(session, "DeleteMe")

    student = get_student_by_name(session, "DeleteMe")

    assert student is None