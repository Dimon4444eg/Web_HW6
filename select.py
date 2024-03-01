import sqlite3
import logging

from connect import create_connection, database

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    sql_expression_01 = """
        SELECT
    s.id,
    s.name,
    ROUND(AVG(g.grade)) AS average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5;
        """
    sql_expression_02 = """
        SELECT
    s.id,
    s.name,
    ROUND(AVG(g.grade)) AS average_grade
    FROM grades g
    JOIN students s ON s.id = g.student_id
    WHERE g.subject_id = 3
    -- WHERE g.subject_id = 1
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT ?;
        """

    try:
        with create_connection(database) as conn:
            if conn is not None:
                c = conn.cursor()
                try:
                    c.execute(sql_expression_01)
                    result = c.fetchall()
                    print(result)
                    c.execute(sql_expression_02, (3,))
                    result = c.fetchall()
                    print(result)
                except sqlite3.Error as err:
                    logging.error(err)
                finally:
                    c.close()
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)
