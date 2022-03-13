"""Attributes"""

'''Import from tab A Development costs'''
#import DevelopmentCosts
#DC = DevelopmentCosts


'''import form tab C capital structures'''
#import CapitalStructure
#CS = CapitalStructure

annualIncreaseInExpenses = .02
annualPublicSubsidiesIncrease = .02
capRateAtSale = .06
salesExpense = .05
ordinaryIncomeTax = .35
depreciationRecapture = .25
capitalGainsTax = .2
discountRate = 0
interestRate = .05
constantRate = 0.66 #constantLoanRate

loanAmount = 1000000 #TODO: import from Car legacies -> DC.totalDevelopmentCost?

debtService = 2000000 #TODO: import from Car legacies -> CS.debtService?

def constantLoanRate():
    return loanAmount/debtService

print(constantLoanRate())
print("100")