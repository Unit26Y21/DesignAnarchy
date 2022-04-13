# Helper methods to calculate capital structure

def equity(my_totaldev_cost, equity_percent):
    totalEq = my_totaldev_cost * equity_percent
    output = totalEq, equity_percent
    print("Total Equity: ${0:,} | {1}".format(output[0], output[1]))
    return totalEq

def debt_calc(my_totaldev_cost, debt_percent):
    totaldebt_calc = my_totaldev_cost* debt_percent
    output = totaldebt_calc, debt_percent
    print("Total Debt: ${0:,} | {1}".format(output[0], output[1]))
    return totaldebt_calc

def debt_calcService(my_total_debt, debt_service_percent):
    total_debt_service = my_total_debt * debt_service_percent
    output = total_debt_service, debt_service_percent
    print("Total Debt Service: ${0:,} | {1}".format(round(output[0], 2), output[1]))
    return total_debt_service