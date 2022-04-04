import numpy_financial as npf

#############################
# Return Metrics
#############################

# Net Present Value
def net_present_value_calculator(equity_calc, list_future_cash_flow,discount_rate):
    net_present_value = npf.npv(discount_rate, list_future_cash_flow ) - equity_calc
    print("Net Present Value: {:,}".format(round(net_present_value, 2)))
    return net_present_value

# Leveraged after Internar Rate of Return
def leveraged_IRR_calculator(future_cash_flow_list):
    leveraged_IRR = npf.irr(future_cash_flow_list)
    print("Leveraged IRR After Taxes: {:,}".format(round(leveraged_IRR, 2)))
    return leveraged_IRR

# Capitalized Value
def capitalize_value_calculator(net_operating_income, cap_rate_atSale):
    capitalize_value = net_operating_income/ cap_rate_atSale
    print("Capitalize Value: {:,}".format(round(capitalize_value, 2)))
    return capitalize_value

# ROTA- Return on Total Assets
def return_onTotalAssets_calculator(net_operating_income_1yr, total_development_cost):
    return_onTotal_assets = (net_operating_income_1yr / total_development_cost)
    print ("ROTA %: {}".format(round(return_onTotal_assets, 2)))
    return return_onTotal_assets

# Return on equity_calc
def return_onEquity_calculator (equity_calc, cash_flow_after_taxes):
    return_onEquity = (cash_flow_after_taxes / equity_calc)
    print ("Return on equity_calc %: {}".format(round(return_onEquity, 2)))
    return return_onEquity
