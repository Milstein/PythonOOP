

class Employee:
    age = 30

    def employee_detail(self):
        self.name ='Matthew'
        print("Name = ", self.name)

        print("age = ", age)

    def print_employee_detail(self):
        print("Porinting in another method")
        print("name = ", self.name)
        print("age = ", age)

if __name__ == '__main__':
    employee = Employee()
    employee.employee_detail()
    print(employee.name)
    print(employee.age)
    #Employee.employee_detail(employee)