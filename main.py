from Employee import Employee

class Main:
    def read_data(self, filename):
        with open(filename, 'r', encoding = 'utf-8') as f:
            lines = f.read().split('\n')
            for i in range(len(lines)): lines[i] = lines[i].split(' ')
            return lines
    
    def parseEmployees(self, content):
        employees = {}
        for data in content: employees[data[0]] = Employee(staffId=data[0], lastName=data[1], firstName=data[2], regHours=int(data[3]), hourlyRate=float(data[4]), otMultiple=float(data[5]), taxCredit=float(data[6]), standardBand=int(data[7]))
        return employees

    def compute(self, employees, employee_work_data):
        for data in employee_work_data:
            employee = employees[data[0]]
            result = employee.computePayment(int(data[2]), data[1])
            print(result)

    def run(self):
        employees_data = self.read_data('data/employees.txt')
        employees = self.parseEmployees(employees_data)
        
        employee_work_data = self.read_data('data/hours.txt')
        self.compute(employees, employee_work_data)
        
        
if __name__ == "__main__":
    Main().run()