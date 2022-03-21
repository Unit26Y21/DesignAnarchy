

# Net Book Value
def NetBookValueCalculator(developmentCost, replacementReserve, total_depreciation):
    """NetBookValue is calculated as the original cost of an asset,
    minus any accumulated depreciation, accumulated depletion,
    accumulated amortization, and accumulated impairment"""

    NetBookValue = developmentCost - replacementReserve - total_depreciation

    print('### Net Book Value ###')
    print("Total Development Cost: {:,}".format(round(developmentCost, 2)))
    print("Accumulated Replacement Reserve: {:,}".format(round(replacementReserve, 2)))
    print("Accumulated Depreciation: {:,}".format(round(total_depreciation, 2)))
    print("Total Netbook Value: {:,}".format(round(NetBookValue, 2)))
    print('###'*10)

    return NetBookValue

# Gain On Sale
def gainOnSaleCalculator (SalePrice, SaleExpenses,NetBookValue):
    """Gain on Sale is the amount of money that is made when selling a property
    for more than its original value"""
    gainOnSale= SalePrice - SaleExpenses - NetBookValue

    print('### Gain on Sale ###')
    print('Sale Price: {:,}'.format(round(SalePrice, 2)))
    print('Sale Expenses: {:,}'.format(round(-SaleExpenses, 2)))
    print('Net Book Value: {:,}'.format(round(-NetBookValue, 2)))
    print("Gain on Sale : {:,}".format(round(gainOnSale, 2)))
    print('###' * 10)

    return gainOnSale

# Tax Payment
def TaxCalculator (total_depreciation,
                   depreciation_recapture_rate,
                   gain_on_sale,
                   capital_gains_tax):
    """Capital Gains Tax is a federal fee paid on the profit made from selling a property"""
    depreciation_recapture_tax = depreciation_recapture_rate * total_depreciation
    CapitalGainInExcessOfDebt = -total_depreciation + gain_on_sale
    CapitalGainTax = CapitalGainInExcessOfDebt * capital_gains_tax

    print('### Tax Payment ###')
    print('Accumulated Depreciation: {:,}'.format(round(total_depreciation, 2)))
    print('Depreciation Recapture Tax: {:,}'.format(round(depreciation_recapture_tax, 2)))
    print('Capital Gain in Excess of Debt: {:,}'.format(round(CapitalGainInExcessOfDebt, 2)))
    print("Capital Gain Tax : {:,}".format(round(CapitalGainTax, 2)))
    print('###' * 10)

    return CapitalGainTax


##################################################################################################
# Net Proceeds from Sale
def NetProceedsFromSaleCalculator (MortgagePayoff, SalePrice, SaleExpenses, TaxPayment):
    """Net Proceeds from Sale is the amount received by the seller after deducting
    all costs and expenses from the gross proceeds"""
    NetProceedsFromSale = SalePrice - SaleExpenses - MortgagePayoff - TaxPayment

    print('### Sale Price ###')
    print('Sale Price: {:,}'.format(round(SalePrice, 2)))
    print('Sales Expenses: {:,}'.format(round(SaleExpenses, 2)))
    print('Mortage Payoff: {:,}'.format(round(MortgagePayoff, 2)))
    print('Tax Payment: {:,}'.format(round(TaxPayment, 2)))
    print("Net Proceeds from Sale : {:,}".format(round(NetProceedsFromSale, 2)))
    print('###' * 10)

    return NetProceedsFromSale




