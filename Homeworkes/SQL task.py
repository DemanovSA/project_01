# Домашняя задача. Написать программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Создание таблицы Students
import sqlite3
connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
query = """CREATE TABLE Students (
Student_Id INTEGER NOT NULL PRIMARY KEY,
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL);
"""
cursor.execute(query)
connection.commit()

# Ввод данных студентов в таблицу Students 
query = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
VALUES
('201', 'Иван', '1'),
('202', 'Петр', '2'),
('203', 'Анастасия', '3'),
('204', 'Игорь', '4');
"""
cursor.execute(query)
connection.commit()
connection.close()

import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_student_detail(Student_Id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT * FROM School 
    JOIN Students ON School.School_Id = Students.School_Id
    WHERE Students.Student_Id = ?"""
    cursor.execute(query,(Student_Id,))
    records = cursor.fetchall()
    print("Данные по студенту \n")
    for row in records:
      print("ID студента: ", row[3])
      print("Имя студента: ", row[4])
      print("ID школы: ", row[0])
      print("Название школы: ", row[1])
    close_connection(connection)
  except(Exception, sqlite3.Error) as erorr:
    print("Ошибка в получении данных", erorr)

get_student_detail(201)