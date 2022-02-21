### 1. Research what is a back of the envelope proforma (or a simple ROI)
    
### 2 . Write a series of python functions that take inputs used to calculated value and return you a simple ROI .###


#Creating ROI Calculator#

#Define the Variables#
#Investment = 40000
Rent = 700
Loss = 1000

#defining the investments can have breakdown of liquid capital, loans, grants, etc.

investmentDictionary = {}

###Ownership Investment Variables###
stock= 2000 #Suppose is the value of Housing Authority
business= None
realEstate= 10000 #Suppose is LandValue
objectsCollectibles= None

###Lending Investment Variables###
savingAccount= 5000
bonds= 20000 #Suppose is a loan from BoFA

###Cash Equivalent Investment Variables###
moneyMarket= None

for variable in ["stock", "business", "realEstate", "objectsCollectibles", "savingAccount", "bonds", "moneyMarket"]:
    investmentDictionary[variable] = eval(variable)

def sumOfInvestments (investmentDictionary):
    Investment= sum(investmentDictionary)
#    print(Investment)

"""
    #defining Rent can be a culmination of number of units and rent per type
def Rent
"""

    # defining ROI as a rudimentary gauge of an investment’s profitability
def ROI (Investment, Rent, Loss):
    NetProfit = Rent * 12 - Loss
    ROI = (NetProfit/Investment) *100
    print(ROI)

ROI (Investment, Rent, Loss)

#Rate of Return- takes into account the project's time frame
