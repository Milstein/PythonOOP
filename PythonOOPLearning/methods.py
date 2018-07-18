class Employee:
    def employee_details(self):
        self.name = "Ben"

    @staticmethod
    def welcome_message():
        print("Welcome to our Organization!")


employee = Employee()
employee.employee_details()
print(employee.name)
employee.welcome_message()
#Employee.welcome_message()