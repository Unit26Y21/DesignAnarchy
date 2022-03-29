import numpy_financial as npf

#############################
# Return Metrics
#############################

# Net Present Value
def net_present_value_calculator(equity, list_future_cash_flow,discount_rate):
    net_present_value = npf.npv(discount_rate, list_future_cash_flow ) - equity
    print("Net Present Value: {:,}".format(round(net_present_value, 2)))
    return net_present_value

# Leveraged after Internar Rate of Return
def leveraged_IRR_calculator(future_cash_flow_list):
    leveraged_IRR = npf.irr(future_cash_flow_list)
    print("Leveraged IRR After Taxes: {:,}".format(round(leveraged_IRR, 2)))
    return leveraged_IRR

# Capitalized Value
def CapitalizeValueCalculator (net_operating_income, cap_rate_atSale):
    capitalizeValue = net_operating_income/ cap_rate_atSale
    print("Capitalize Value: {:,}".format(round(capitalizeValue, 2)))
    return capitalizeValue

# ROTA- Return on Total Assets
def ReturnOnTotalAssetsCalculator (net_operating_income_1yr, total_development_cost):
    ReturnOnTotalAssets = (net_operating_income_1yr / total_development_cost)
    print ("ROTA %: {}".format(round(ReturnOnTotalAssets, 2)))
    return ReturnOnTotalAssets

# Return on Equity
def ReturnOnEquityCalculator (equity, cash_flow_after_taxes):
    ReturnOnEquity = (cash_flow_after_taxes / equity)
    print ("Return on Equity %: {}".format(round(ReturnOnEquity, 2)))
    return ReturnOnEquity
