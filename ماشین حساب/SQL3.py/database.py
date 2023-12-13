python
import sqlite3

def update_student_grade(student_id, new_grade):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students
        SET grade = ?
        WHERE id = ?
    """, (new_grade, student_id))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM students
        WHERE id = ?
    """, (student_id,))
    conn.commit()
    conn.close()