
"""
Класи для створення резюме будь-якої персони (студента, працівника, непрацюючого).

"""

class Person:
        
    def __init__(self, name, age, contact_phone, email):
        self.name = input("Прізвище та ім'я: ")
        self.contact_phone = input("Контактний телефон: ")
        self.email = input("email: ")
        while True:
            self.age = input("Вік: ")
            if self.age.isnumeric() == False or int(self.age) <= 0:
                print("Вік має бути додатнім числом")
            else:
                break

    def get_cv(self):
        return [
                    f"Прізвище та ім'я: {self.name}",
                    f"Вік: {self.age}",
                    f"Контактний телефон: {self.contact_phone}", 
                    f"email: {self.email}"
                ]
    def save_cv_to_file(self, file_cv):
        
        with open(file_cv, "w") as file:
            file.write("========================================================================\n")
            file.write("                        ****  CV  ****\n")
            file.write("========================================================================\n\n")
            for line in self.get_cv():
                file.write(line + "\n")
            file.write("========================================================================\n")
        print(f"Інформацію збережено в файлі {file_cv}")

class Employee(Person):
    
    def __init__(self, name, age, contact_phone, email, job_title, company):
        super().__init__(name, age, contact_phone, email)
        self.job_title = input("Посада: ")
        self.company = input("Назва компанії: ")
        
    def get_cv(self):
        base_resume = super().get_cv()
        return base_resume + [
            f"Посада: {self.job_title}",
            f"Компанія: {self.company}"
        ]

class Student(Person):
    def __init__(self, name, age, contact_phone, email, university, major):
        super().__init__(name, age, contact_phone, email)
        self.university = input("Навчальний заклад: ")
        self.major = input("Спеціальність: ")
        
    def get_cv(self):
        base_resume = super().get_cv()
        return base_resume + [
            f"Навчальний заклад: {self.university}",
            f"Спеціальність: {self.major}"
        ]

