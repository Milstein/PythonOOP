class Employee:
    def set_no_of_working_hours(self):
        self.no_of_working_hours = 40

    def get_no_of_working_hours(self):
        print(self.no_of_working_hours)

class Trainee(Employee):
    def set_no_of_working_hours(self):
        self.no_of_working_hours = 45

    def reset_no_of_working_hours(self):
        super().set_no_of_working_hours()



employee = Employee()
employee.set_no_of_working_hours()
print("Number of working hours of employee:", end=' ')
employee.get_no_of_working_hours()

trainee = Trainee()
trainee.set_no_of_working_hours()
print("Number of working hours of trainee:", end=' ')
trainee.get_no_of_working_hours()
trainee.reset_no_of_working_hours()
print("Number of working hours of trainee after reset:", end=' ')
trainee.get_no_of_working_hours()