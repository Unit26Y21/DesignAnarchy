# Helper methods to calculate capital structure

def equity_calc(myTotaldev_cost, eqPerc):
    totalEq = myTotaldev_cost * eqPerc
    output = totalEq, eqPerc
    print("Total equity_calc: ${0:,} | {1}".format(output[0], output[1]))
    return totalEq

def debt_calc(myTotaldev_cost, equity_calcPercent):
    equity_calc = myTotaldev_cost * equity_calcPercent
    debt_calcPercent = 1 - equity_calcPercent
    totaldebt_calc = myTotaldev_cost - equity_calc
    output = totaldebt_calc, debt_calcPercent
    print("Total debt_calc: ${0:,} | {1}".format(output[0], output[1]))
    return totaldebt_calc

def debt_calcService(mytotaldebt_calc, debt_calcServPerc):
    totaldebt_calcServ = mytotaldebt_calc * debt_calcServPerc
    output = totaldebt_calcServ, debt_calcServPerc
    print("Total debt_calc Service: ${0:,} | {1}".format(round(output[0], 2), output[1]))
    return totaldebt_calcServ