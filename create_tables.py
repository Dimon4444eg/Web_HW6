from sqlite3 import Error
from connect import create_connection, database
import logging

logging.basicConfig(level=logging.INFO)


def create_table(conn, create_table_sql):
    c = conn.cursor()
    try:
        c.execute(create_table_sql)
        conn.commit()
    except Error as err:
        logging.error(err)
        conn.rollback()
    finally:
        c.close()


if __name__ == '__main__':

    sql_create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups(id)
    );
    """

    sql_create_groups_table = """
    CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL
    );
    """

    sql_create_teachers_table = """
    CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(150) NOT NULL
    );
    """

    sql_create_subjects_table = """
    CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
    );
    """

    sql_create_grades_table = """
    CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER CHECK ( grade >= 0 AND grade <= 100),
    date DATE NOT NULL ,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
    );
    """

    sql_create_enrollments_table = """
    CREATE TABLE IF NOT EXISTS enrollments (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
    );
    """

    try:
        with create_connection(database) as conn:
            if conn is not None:
                logging.info(f"Connected to {database} database")
                # Создание таблицы students
                create_table(conn, sql_create_students_table)
                # Создание таблицы groups
                create_table(conn, sql_create_groups_table)
                # Создание таблицы teachers
                create_table(conn, sql_create_teachers_table)
                # Создание таблицы subjects
                create_table(conn, sql_create_subjects_table)
                # Создание таблицы grades
                create_table(conn, sql_create_grades_table)
                # Создание таблицы enrollments
                create_table(conn, sql_create_enrollments_table)

                logging.info("Table created successfully")
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)
