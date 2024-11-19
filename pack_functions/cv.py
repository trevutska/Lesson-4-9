
"""
Класи для створення резюме будь-якої персони (студента, працівника, непрацюючого).

Реалізовано відповідно до вимог Групи ІI:
з використанням механізмів наслідування / інкапсуляції / поліморфізму передбачити можливості формування резюме для будь-якої персони

"""
def create_person_cv():
    name = input("Прізвище та ім'я: ")
    contact_phone = input("Контактний телефон: ")
    email = input("email: ")
    while True:
        age = input("Вік: ")
        if not age.isnumeric() or int(age) <= 0:
            print("Вік має бути додатнім числом")
        else:
            break
    return {
        "name": name,
        "age": age,
        "contact_phone": contact_phone,
        "email": email
    }

def create_employee_cv():
    person_cv = create_person_cv()
    job_title = input("Посада: ")
    company = input("Назва компанії: ")
    person_cv.update({
        "job_title": job_title,
        "company": company
    })
    return person_cv

def create_student_cv():
    person_cv = create_person_cv()
    university = input("Навчальний заклад: ")
    major = input("Спеціальність: ")
    person_cv.update({
        "university": university,
        "major": major
    })
    return person_cv

def save_cv_to_file(cv, file_cv):
    with open(file_cv, "w") as file:
        file.write("========================================================================\n")
        file.write("                        ****  CV  ****\n")
        file.write("========================================================================\n\n")
        for key, value in cv.items():
            file.write(f"{key.capitalize()}: {value}\n")
        file.write("========================================================================\n")
    print(f"Інформацію збережено в файлі {file_cv}")

