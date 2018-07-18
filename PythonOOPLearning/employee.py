# check if an employee has achieved his weekly target or not
class Employee:
    """class attributes"""
    name = "Ben"
    designation = "Sales Executive"
    salesMadeThisWeek = 6


    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print(self.name + " Target has been achieved")
        else:
            print(self.name + " Target has not been achieved")

if __name__ == '__main__':
    employeeOne = Employee()
    employeeOne.name = "Nisha"
    employeeOne.salesMadeThisWeek = 10
    employeeOne.hasAchievedTarget()

    numbers = [1, 2, 3]
    print(type(numbers))
    numbers.append(4)
    print(numbers)

