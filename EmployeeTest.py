import unittest
from Employee import Employee

class EmployeeTest(unittest.TestCase):

    def testNetLessEqualGross(self):
        e = Employee(123456, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        pi = e.computePayment(1,'31/10/2021')
        self.assertLessEqual(pi['Net Pay'], pi['Gross Pay'])

if __name__ == "__main__":
    EmployeeTest().testNetLessEqualGross()