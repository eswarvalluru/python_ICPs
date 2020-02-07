class Employee():
    emp_num=0
    sal=0
    def __init__(self,n,f,s,d):
        self.name=n
        self.family=f
        self.salary=s
        self.dept=d
        Employee.emp_num+=1
        Employee.sal += s
    def printdet(self):
        print("Name : ",self.name, "\nFamily : ",self.family,"\nSalary : ",self.salary,"\nDept : ",self.dept)
    def averagesal(self):
        print("Average Sal=", (Employee.sal) / (Employee.emp_num))

class FullTimeEmployee(Employee):
    def __init__(self,n,f,s,d):
        Employee.__init__(self, n, f, s, d)
    def printdet(self):
        print("Name : ", self.name, "\nFamily : ", self.family, "\nSalary : ", self.salary, "\nDept : ", self.dept)

employee1=Employee("Eswar","Valluru",100,"CSE")
employee2=Employee("Virat","Kohli",1000,"Cric")
employee3=FullTimeEmployee("Virt","Koli",10000,"Cric")
employee1.printdet()
employee2.printdet()
employee3.printdet()
employee1.averagesal()
print("Total count= ",Employee.emp_num)