#Github link is https://github.com/teja596/ca_one.git

#Create a class Employee
class Employee:
    #Craeating constructor with attributes staffId,lastName,firstName,reghours,hourlyRate,otMultiple,taxCredit,standardBand
    def __init__(self, staffId, lastName, firstName, regHours, hourlyRate, otMultiple, taxCredit, standardBand) -> None:
        self.staffId = staffId
        self.lastName = lastName
        self.firstName = firstName
        self.regHours = regHours
        self.hourlyRate = hourlyRate
        self.otMultiple = otMultiple
        self.taxCredit = taxCredit
        self.standardBand = standardBand

        self.standard_rate = 0.2
        self.higher_rate = 0.4

           #Create a method computePayment having arguements hoursWorked and date and storing it as dictionary and returning it res as dictionary
    def computePayment(self, hoursWorked, date) -> dict:
        res = {}            #We are using an empty dictionary variable res 
        
        res['name'] = self.firstName + ' ' + self.lastName
        res['Date'] = date
        res['Regular Hours Worked'] = min(self.regHours, hoursWorked)
        res['Overtime Hours Worked'] = max(0, hoursWorked - self.regHours)
        res['Regular Rate'] = self.hourlyRate
        res['Overtime Rate'] = res['Regular Rate'] * self.otMultiple
        res['Regular Pay'] = res['Regular Hours Worked'] * res['Regular Rate']
        res['Overtime Pay'] = res['Overtime Hours Worked'] * res['Overtime Rate']
        res['Gross Pay'] = res['Regular Pay'] + res['Overtime Pay']
        res['Standard Rate Pay'] = min(res['Gross Pay'], self.standardBand)
        res['Higher Rate Pay'] = max(res['Gross Pay'] - self.standardBand, 0)
        res['Standard Tax'] = res['Standard Rate Pay'] * self.standard_rate
        res['Higher Tax'] = res['Higher Rate Pay'] * self.higher_rate
        res['Total Tax'] = res['Standard Tax'] + res['Higher Tax']
        res['Tax Credit'] = self.taxCredit
        res['Net Deductions'] = max(0, res['Total Tax'] - res['Tax Credit'])
        res['Net Pay'] = res['Gross Pay'] - res['Net Deductions']

        return res  #used to return res for computePayment method as dictionary(res)
