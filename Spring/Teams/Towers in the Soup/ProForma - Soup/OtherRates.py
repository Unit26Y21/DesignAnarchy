"""Attributes"""

'''Import from Legacies py file'''
import DevCosts_CapitalStruc
DC = DevCosts_CapitalStruc

annualIncreaseInExpenses = .02
annualPublicSubsidiesIncrease = .02
capRateAtSale = .06
salesExpense = .05
ordinaryIncomeTax = .35
depreciationRecapture = .25
capitalGainsTax = .2
discountRate = 0
interestRate = .05



loanAmount = DC.myTotalDevCost #TODO: import from Car legacies -> DC.totalDevelopmentCost?

debtService = DC.mytotalDebtServ #TODO: import from Car legacies -> CS.debtService?

def constantLoanRate(loanAmount, debtService):
    return  debtService / loanAmount
constantRate = constantLoanRate(loanAmount, debtService)
print(constantRate)


'''print(constantLoanRate())'''
print(loanAmount)
print(debtService)