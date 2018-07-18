class Employee:

    def __init__(self, name="Mark"):
        self._name = name

    def display_employee_details(self):
        print(self._name)

employee= Employee()
employee.display_employee_details()

employeeTwo = Employee("Milson")
employeeTwo.display_employee_details()
