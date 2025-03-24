import random
import sqlite3

# students_db = sqlite3.connect("students.db")
# cursor = students_db.cursor()
#
# cursor.execute("CREATE TABLE students ("
#                "id INTEGER, "
#                "full_name TEXT, "
#                "age INTEGER, "
#                "course INTEGER)")
# students_db.close()

def add_student():
    students_db = sqlite3.connect("students.db")
    cursor = students_db.cursor()

    id = random.randint(1, 10000)
    full_name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    course = int(input("Введите курс студента: "))

    cursor.execute("INSERT INTO students (id, full_name, age, course) "
                   "VALUES (?, ?, ?, ?)", (id, full_name, age, course))

    students_db.commit()

    students_db.close()

def delete_student():
    students_db = sqlite3.connect("students.db")
    cursor = students_db.cursor()

    id = int(input("Введите ID студента: "))

    cursor.execute("SELECT id FROM students")

    all_id = []
    for student_id in cursor.fetchall():
        all_id.extend(list(student_id))

    if id in all_id:
        print("пользователь удален")
        cursor.execute("DELETE FROM students WHERE id = ?", (id,))
    else:
        print("пользователя не существует")

    students_db.commit()

    students_db.close()

def show_students():
    students_db = sqlite3.connect("students.db")
    cursor = students_db.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    for student in students:
        print(*student)

    students_db.close()


while True:
    print("1. Добавить студента \n"
          "2. удалить студента \n"
          "3. посмотреть всех студентов")
    action = input("Введите номер действия")

    match action:
        case "1":
            add_student()
        case "2":
            delete_student()
        case "3":
            show_students()
        case _:
            print("не верная команда")






