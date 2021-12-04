#Github link is https://github.com/teja596/ca_one.git

#This is the python program for test case methods
import unittest #We are importing the unittest
from Employee import Employee #We are using Employee class from Employee module

class EmployeeTest(unittest.TestCase): #creating a Employeetest class for unit test
    
    #Creating three functions named testNetLessEqualGross,testNetLessEqualGrossa,testNetLessEqualGrossb for testing the net pay is less than equal to gross pay  
    def testNetLessEqualGross(self):
        e = Employee(123456, 'Green', 'Joe', 37, 16, 1.5, 70, 700) 
        pi = e.computePayment(1,'31/10/2021')
        self.assertLessEqual(pi['Net Pay'], pi['Gross Pay'])
    def testNetLessEqualGrossa(self):
        e1 = Employee(1234458, 'Shane', 'John', 39, 12, 2.6, 50, 825) 
        pi1= e1.computePayment(23,'12/11/2021')
        self.assertLessEqual(pi1['Net Pay'], pi1['Gross Pay'])
    def testNetLessEqualGrossb(self):
        e2 = Employee(923696, 'Landon', 'Steve', 39, 12, 0.5, 60, 955) 
        pi2= e2.computePayment(48,'12/11/2021')
        self.assertLessEqual(pi2['Net Pay'], pi2['Gross Pay'])
         
        #Creating three functions named testOverTimeNotNeg,testOverTimeNotNega and testOverTimeNotNegb for testing Overtime pay is not negative
    def testOverTimeNotNeg(self):
        e = Employee(123456, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        pi = e.computePayment(40, '31/10/2021')
        self.assertFalse(pi['Overtime Pay'] < 0)
    def testOverTimeNotNega(self):
        e1 = Employee(1234458, 'Shane', 'John', 39, 12, 2.6, 50, 825) 
        pi1= e1.computePayment(23,'12/11/2021')
        self.assertFalse(pi1['Overtime Pay'] < 0)
    def testOverTimeNotNegb(self):
        e2 = Employee(923696, 'Landon', 'Steve', 39, 12, 0.5, 60, 955) 
        pi2= e2.computePayment(48,'12/11/2021')
        self.assertFalse(pi2['Overtime Pay'] < 0)
        
        #Create three functions named testRegHourExceed,testRegHourExceeda,testRegHourExceedb for testing Regular Hours Worked cannot exceed hours worked
    def testRegHourExceed(self):
        e = Employee(123456, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        pi = e.computePayment(30, '31/10/2021')
        self.assertLessEqual(pi['Regular Hours Worked'], 30)
    def testRegHourExceeda(self):
        e1 = Employee(1234458, 'Shane', 'John', 39, 12, 2.6, 50, 825) 
        pi1= e1.computePayment(23,'12/11/2021')
        self.assertLessEqual(pi1['Regular Hours Worked'], 23)
    def testRegHourExceedb(self):
        e2 = Employee(923696, 'Landon', 'Steve', 39, 12, 0.5, 60, 955) 
        pi2= e2.computePayment(48,'12/11/2021')
        self.assertLessEqual(pi2['Regular Hours Worked'], 48)
         

        
        #Create three  functions named testHighTaxNotNeg,testHighTaxNotNega,testHighTaxNotNegb for testing Higher Tax cannot be negative.
    def testHighTaxNotNeg(self):
        e = Employee(123456, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        pi = e.computePayment(300, '31/10/2021')
        self.assertFalse(pi['Higher Tax'] < 0) 
    def testHighTaxNotNega(self):
        e1 = Employee(1234458, 'Shane', 'John', 39, 12, 2.6, 50, 825) 
        pi1= e1.computePayment(23,'12/11/2021')
        self.assertFalse(pi1['Higher Tax'] < 0)
    def testHighTaxNotNegb(self):
        e2 = Employee(923696, 'Landon', 'Steve', 39, 12, 0.5, 60, 955) 
        pi2= e2.computePayment(48,'12/11/2021')
        self.assertFalse(pi2['Higher Tax'] < 0) 
        
        #Create three functions named testNetPayNotNeg,testNetPayNotNega,testNetPayNotNegb for tetsing Net Pay is not negative
    def testNetPayNotNeg(self):
        e = Employee(123456, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        pi = e.computePayment(0, '31/10/2021')
        self.assertFalse(pi['Net Pay'] < 0)
    def testNetPayNotNega(self):
        e1 = Employee(1234458, 'Shane', 'John', 39, 12, 2.6, 50, 825) 
        pi1= e1.computePayment(23,'12/11/2021')
        self.assertFalse(pi1['Net Pay'] < 0)
    def testNetPayNotNegb(self):
        e2 = Employee(923696, 'Landon', 'Steve', 39, 12, 0.5, 60, 955) 
        pi2= e2.computePayment(48,'12/11/2021')
        self.assertFalse(pi2['Net Pay'] < 0)
 #Running the tests below line
unittest.main()
