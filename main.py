from courses_orm import create_db_and_tables, add_course, get_active_courses

if __name__ == "__main__":
    create_db_and_tables()
    add_course("yossi", 15)
    add_course("Python Intro", 30, True)
    add_course("Legacy System", 10, False)
    print(get_active_courses())
