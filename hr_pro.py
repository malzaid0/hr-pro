class Employee:
    def __init__(self, name, age, salary, employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year

    def get_working_years(self):
        return 2020 - self.employment_year

    def __str__(self):
        return "name: " + self.name + ", Age: " + str(self.age) + ", Salary: " + str(
            self.salary) + ", Working Years: " + str(
            self.get_working_years())


class Manager(Employee):
    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        super().__init__(name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage

    def get_bonus(self):
        return self.bonus_percentage * self.salary

    def get_working_years(self):
        return 2020 - self.employment_year

    def __str__(self):
        return "name: " + self.name + ", Age: " + str(self.age) + ", Salary: " + str(
            self.salary) + ", Working Years: " + str(
            self.get_working_years()) + ", Bonus: " + str(self.get_bonus())


def main():
    a = 0
    employees = []
    managers = []
    print("Welcome to HR Pro 2019")

    while a != 5:
        print("Options:")
        print("\t1. Show Employees")
        print("\t2. Show Managers")
        print("\t3. Add An Employee")
        print("\t4. Add A Manager")
        print("\t5. Exit")
        a = int(input("\nWhat would you like to do? "))
        print("-----------------")

        if a == 1:
            print("Employees\n")
            for employee in employees:
                print(employee)
            print("-----------------")

        elif a == 2:
            print("Managers\n")
            for manager in managers:
                print(manager)
            print("-----------------")

        elif a == 3:
            name = input("Name: ")
            age = int(input("Age: "))
            salary = float(input("Salary: "))
            employment_year = int(input("Employment year: "))
            employee = Employee(name, age, salary, employment_year)
            employees.append(employee)
            print()

        elif a == 4:
            name = input("Name: ")
            age = int(input("Age: "))
            salary = float(input("Salary: "))
            employment_year = int(input("Employment year: "))
            bonus_percentage = float(input("Bonus Percentage: "))
            manager = Manager(name, age, salary, employment_year, bonus_percentage)
            managers.append(manager)
            print()

        else:
            continue


if __name__ == '__main__':
    main()
