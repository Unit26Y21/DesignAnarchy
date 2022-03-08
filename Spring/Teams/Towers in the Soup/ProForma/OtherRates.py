"""Attributes"""
import DevelopmentCosts
DC = DevelopmentCosts

import CapitalStructure
CS =  CapitalStructure

annualIncreaseInExpenses = .02
annualPublicSubsidiesIncrease = .02
capRateAtSale = .06
salesExpense = .05
ordinaryIncomeTax = .35
depreciationRecapture = .25
capitalGainsTax = .2
discountRate = 0
interestRate = .05
constantRate = constantLoanRate
loanAmount = DC.totalDevelopmentCost
debtService = CS.debtService

def constantLoanRate():
    return loanAmount/debtService

print(constantRate)
print("100")