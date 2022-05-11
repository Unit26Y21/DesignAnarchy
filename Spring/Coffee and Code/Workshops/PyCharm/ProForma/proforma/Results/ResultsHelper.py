

# Net Book Value
def net_book_value_calculator(development_cost, replacement_reserve, total_depreciation):
    """net_book_value is calculated as the original cost of an asset,
    minus any accumulated depreciation, accumulated depletion,
    accumulated amortization, and accumulated impairment"""

    net_book_value = development_cost + replacement_reserve + total_depreciation

    print('### Net Book Value ###')
    print("Total Development Cost: {:,}".format(round(development_cost, 2)))
    print("Accumulated Replacement Reserve: {:,}".format(round(replacement_reserve, 2)))
    print("Accumulated Depreciation: {:,}".format(round(total_depreciation, 2)))
    print("Total Netbook Value: {:,}".format(round(net_book_value, 2)))
    print('###'*10)

    return net_book_value

# Gain On Sale
def gain_onSale_calculator (sale_price, sale_expenses,net_book_value):
    """Gain on Sale is the amount of money that is made when selling a property
    for more than its original value"""
    gain_onSale= sale_price - sale_expenses - net_book_value

    print('### Gain on Sale ###')
    print('Sale Price: {:,}'.format(round(sale_price, 2)))
    print('Sale Expenses: {:,}'.format(round(-sale_expenses, 2)))
    print('Net Book Value: {:,}'.format(round(-net_book_value, 2)))
    print("Gain on Sale : {:,}".format(round(gain_onSale, 2)))
    print('###' * 10)

    return gain_onSale

# Tax Payment
def tax_calculator(total_depreciation,
                   depreciation_recapture_tax,
                   gain_on_sale,
                   capital_gains_tax):
    """Capital Gains Tax is a federal fee paid on the profit made from selling a property"""
    cap_gainExcessOfDebt_calc = total_depreciation + gain_on_sale
    cap_gain_tax= cap_gainExcessOfDebt_calc * capital_gains_tax

    print('### Tax Payment ###')
    print('Accumulated Depreciation: {:,}'.format(round(total_depreciation, 2)))
    print('Depreciation Recapture Tax: {:,}'.format(round(depreciation_recapture_tax, 2)))
    print('Capital Gain in Excess of debt_calc: {:,}'.format(round(cap_gainExcessOfDebt_calc, 2)))
    print("Capital Gain Tax : {:,}".format(round(cap_gain_tax, 2)))
    print('###' * 10)

    return cap_gain_tax


##################################################################################################
# Net Proceeds from Sale
def net_proceeds_fromSale_calculator(mortgage_payoff, sale_price, sale_expenses, tax_payment):
    """Net Proceeds from Sale is the amount received by the seller after deducting
    all costs and expenses from the gross proceeds"""
    net_proceeds_fromSale = sum([sale_price,sale_expenses, mortgage_payoff, tax_payment])

    print('### Sale Price ###')
    print('Sale Price: {:,}'.format(round(sale_price, 2)))
    print('Sales Expenses: {:,}'.format(round(sale_expenses, 2)))
    print('Mortage Payoff: {:,}'.format(round(mortgage_payoff, 2)))
    print('Tax Payment: {:,}'.format(round(tax_payment, 2)))
    print("Net Proceeds from Sale : {:,}".format(round(net_proceeds_fromSale, 2)))
    print('###' * 10)

    return net_proceeds_fromSale




