from typing import Optional
from sqlmodel import SQLModel, Field
from sqlmodel import create_engine
from sqlmodel import Session, select


class Courses(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    name : str
    hours : int
    is_active : bool = True


engine = create_engine("sqlite:///courses.db", echo=True)

#this will create the tabes if they don't exist already
def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def add_course(name: str, hours: int, is_active: bool = True) -> None:
    with Session(engine) as session:
        course = Courses(name=name, hours=hours, is_active=is_active)
        session.add(course)
        session.commit()
        session.refresh(course)
        print(f"Course added: {course.id}")


def get_active_courses()->list[Courses]:
    with Session(engine) as session:
        statement = select(Courses).where(Courses.is_active == True)
        result = session.exec(statement)
        courses = result.all()
        return courses




