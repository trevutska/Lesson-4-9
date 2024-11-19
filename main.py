
'''
Домашнє завдання №7
Реалищація блоку 1

Завдання: створити проект python будь-яким способом, що реалізує архітектуру програмного 
скрипта блоку 1

'''

from pack_functions import s_circle, s_triangle, s_rectangle, cv
import os

from pack_classes import (
    Person,
    Employee,
    Student
)


def package_functions_main_def():
    print('--------------------- звернення до модуля s_rectangle ---------------')
    text = 'Площа прямокутника'
    width = 5.0
    heigh = 7.0
    s_1 = s_rectangle.rectangle_area(width, heigh)
    print(text, ' S =', s_1, '\n')

    print('--------------------- звернення до модуля s_circle ---------------')
    text = 'Площа круга'
    radius = 5.0
    s_2 = s_circle.circle_area(radius)
    print(text, ' S =', s_2, '\n')

    print('--------------------- звернення до модуля s_triangle ---------------')
    text = 'Площа трикутника'
    base = 10.0
    height = 8.0
    s_3 = s_triangle.triangle_area(base, height)
    print(text, ' S =', s_3, '\n')

    print('--------------------- звернення до модуля cv ---------------')
    if not os.path.exists("HW_7/all_CV"):
        os.makedirs("HW_7/all_CV")
    cv.save_cv_to_file(cv.create_person_cv(), "HW_7/all_CV/person_cv.txt")
    cv.save_cv_to_file(cv.create_employee_cv(), "HW_7/all_CV/employee_cv.txt")
    cv.save_cv_to_file(cv.create_student_cv(), "HW_7/all_CV/student_cv.txt")
  
    return


def package_class_main_def(name = None, age = None, contact_phone = None, email = None, job_title = None, company = None, university = None, major = None):
    choice = input("Виберіть тип персони для резюме (1 - працівник, 2 - студент, 3 - інший варіант): ")
    
    if choice == "1":
        file_cv = "HW_7/all_CV/cv_працівник.txt"
        cv_data = Employee(name = None, age = None, contact_phone = None, email = None, job_title = None, company = None)
        cv_data.save_cv_to_file(file_cv)
    
    elif choice == "2":
        file_cv = "HW_7/all_CV/cv_студент.txt"
        cv_data = Student(name = None, age = None, contact_phone = None, email = None, university = None, major = None)
        cv_data.save_cv_to_file(file_cv)
    
    else:
        file_cv = "HW_7/all_CV/cv.txt"
        cv_data = Person(name = None, age = None, contact_phone = None, email = None)
        cv_data.save_cv_to_file(file_cv)

    return



if __name__ == '__main__':
    print ('\n',"----- Блок виклику модулів з пакету pack_functions ----",'\n')
    package_functions_main_def()
    print('\n',"----- Блок виклику модулів з пакету pack_classes -----",'\n')
    package_class_main_def()