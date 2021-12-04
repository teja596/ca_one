#This is the python program for test case methods
import unittest #We are importing the unittest
from Employee import Employee #We are using Employee class from Employee module

class EmployeeTest(unittest.TestCase): #creating a Employeetest class for unit test
    
    #Creating function named testNetLessEqualGross for testing the net pay is less than equal to gross pay  
    def testNetLessEqualGross(self):
        e = Employee(123456, 'Green', 'Joe', 37, 16, 1.5, 70, 700) 
        pi = e.computePayment(1,'31/10/2021')
        self.assertLessEqual(pi['Net Pay'], pi['Gross Pay'])
        
         #Creating function named testOverTimeNotNeg for testing Overtime pay is not negative
    def testOverTimeNotNeg(self):
        e = Employee(123456, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        pi = e.computePayment(40, '31/10/2021')
        self.assertFalse(pi['Overtime Pay'] < 0)
        
        #Create function testRegHourExceed for testing Regular Hours Worked cannot exceed hours worked
    def testRegHourExceed(self):
        e = Employee(123456, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        pi = e.computePayment(30, '31/10/2021')
        self.assertLessEqual(pi['Regular Hours Worked'], 30)
        
        #Create functiom testHighTaxNotNeg for testing Higher Tax cannot be negative.
    def testHighTaxNotNeg(self):
        e = Employee(123456, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        pi = e.computePayment(300, '31/10/2021')
        self.assertFalse(pi['Higher Tax'] < 0)
        
        #Create function testNetPayNotNeg for tetsing Net Pay is not negative
    def testNetPayNotNeg(self):
        e = Employee(123456, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        pi = e.computePayment(0, '31/10/2021')
        self.assertFalse(pi['Net Pay'] < 0)

 #Running the tests below line
unittest.main()
