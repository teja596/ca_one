import unittest
from Employee import Employee

class EmployeeTest(unittest.TestCase):

    def testNetLessEqualGross(self):
        e = Employee(123456, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        pi = e.computePayment(1,'31/10/2021')
        self.assertLessEqual(pi['Net Pay'], pi['Gross Pay'])

    def testOverTimeNotNeg(self):
        e = Employee(123456, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        pi = e.computePayment(40, '31/10/2021')
        self.assertFalse(pi['Overtime Pay'] < 0)

    def testRegHourExceed(self):
        e = Employee(123456, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        pi = e.computePayment(30, '31/10/2021')
        self.assertLessEqual(pi['Regular Hours Worked'], 30)

    def testHighTaxNotNeg(self):
        e = Employee(123456, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        pi = e.computePayment(300, '31/10/2021')
        self.assertFalse(pi['Higher Tax'] < 0)

    def testNetPayNotNeg(self):
        e = Employee(123456, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        pi = e.computePayment(0, '31/10/2021')
        self.assertFalse(pi['Net Pay'] < 0)

unittest.main()
