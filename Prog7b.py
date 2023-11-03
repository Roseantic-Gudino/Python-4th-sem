class Employee:
    def __init__(self):
        self.name = ""
        self.Id = ""
        self.department = ""
        self.salary = 0
        
    def readEmpDetails(self):
        self.name = input("Enter Employee name: ")
        self.Id = input("Enter Employee Id: ")
        self.department = input("Enter Employee dept: ")
        self.salary = int(input("Enter Employee salary: "))

    def updateSalary(self):
        self.salary = int(input("Enter new salary: "))
        print("Updated salary is ",self.salary)

    def displayEmpDetails(self):
        print("Employee Details")
        print("Name: ",self.name)
        print("ID: ",self.Id)
        print("Department: ",self.department)
        print("Salary: ",self.salary)

EmployeeList = []

while True:
    e1=Employee()
    e1.readEmpDetails()
    EmployeeList.append(e1)
    ch = input("Add more y/n ? ")
    if (ch=='n'):
        break

#print("Employee details: ")
dept = input("Enter department: ")
for e in EmployeeList:
    if ( dept == e.department ):
        e.updateSalary()
        break

for e in EmployeeList:
    e.displayEmpDetails()














