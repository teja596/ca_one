from Employee import Employee #we are importing from Employee module(Employee.py) class Employee

class Main:#this is the main class
   #Creating a function name read_data for reading the text from files where we are taking the filenames
    def read_data(self, filename):
        with open(filename, 'r', encoding = 'utf-8') as f:
            lines = f.read().split('\n')
            for i in range(len(lines)): lines[i] = lines[i].split(' ')
            return lines
    #creating a function named parseEmployees for passing the values of employee and returning a dictionary employees 
    def parseEmployees(self, content):
        employees = {}
        for data in content: employees[data[0]] = Employee(staffId=data[0], lastName=data[1], firstName=data[2], regHours=int(data[3]), hourlyRate=float(data[4]), otMultiple=float(data[5]), taxCredit=float(data[6]), standardBand=int(data[7]))
        return employees
    #creating a function name compute by taking the arguements employees and employee_work_data and printing the result
    def compute(self, employees, employee_work_data):
        for data in employee_work_data:
            employee = employees[data[0]]
            result = employee.computePayment(int(data[2]), data[1])
            print(result)
#creating a function run and using this function to call the defined compute function
    def run(self):
        employees_data = self.read_data('data/employees.txt')#Reading the file employees.txt stored in folder name data and keeping in employees_data
        employees = self.parseEmployees(employees_data)#calling the functionparseEmployee to pass the values into employees dictionary
        
        employee_work_data = self.read_data('data/hours.txt')#Reading the data from file hours.txt stored in data folder and keeping it Employee_work_data
        self.compute(employees, employee_work_data)#calling the compute function by using the arguements employees and employee_work_data

if __name__ == "__main__":
    Main().run()
    
