# Helper methods to calculate capital structure

def Equity(myTotalDevCost, EqPerc):
    totalEq = myTotalDevCost * EqPerc
    output = totalEq, EqPerc
    print("Total Equity: ${0:,} | {1}".format(output[0], output[1]))
    return totalEq

def Debt(myTotalDevCost, equityPercent):
    equity = myTotalDevCost * equityPercent
    debtPercent = 1 - equityPercent
    totalDebt = myTotalDevCost - equity
    output = totalDebt, debtPercent
    print("Total Debt: ${0:,} | {1}".format(output[0], output[1]))
    return totalDebt

def DebtService(mytotalDebt, debtServPerc):
    totalDebtServ = mytotalDebt * debtServPerc
    output = totalDebtServ, debtServPerc
    print("Total Debt Service: ${0:,} | {1}".format(round(output[0], 2), output[1]))
    return totalDebtServ