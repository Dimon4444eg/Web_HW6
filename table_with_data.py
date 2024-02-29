from faker import Faker
import random
import sqlite3
import logging

logging.basicConfig(level=logging.INFO)

conn = sqlite3.connect('test.sqlite')
cursor = conn.cursor()

fake = Faker('uk_UA')


def main():
    for _ in range(3):
        group_name = fake.word()
        cursor.execute("INSERT INTO groups (name) VALUES (?)", (group_name,))
        group_id = cursor.lastrowid

        for _ in range(random.randint(10, 20)):
            student_name = fake.name()
            cursor.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (student_name, group_id))

    for _ in range(5):
        teacher_name = fake.name()
        cursor.execute("INSERT INTO teachers (name) VALUES (?)", (teacher_name,))

        for _ in range(random.randint(5, 8)):
            subject_name = fake.word()
            cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject_name, cursor.lastrowid))

    students_ids = [row[0] for row in cursor.execute("SELECT id FROM students")]
    subjects_ids = [row[0] for row in cursor.execute("SELECT id FROM subjects")]

    for student_id in students_ids:
        for subject_id in subjects_ids:
            grade = random.randint(1, 12)
            date = fake.date_between(start_date='-1y', end_date='today')
            cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                           (student_id, subject_id, grade, date))

    conn.commit()
    logging.info("Данные сохранены успешно")
    conn.close()
    logging.info("Соединение с базой данных закрыто")


if __name__ == "__main__":
    main()
