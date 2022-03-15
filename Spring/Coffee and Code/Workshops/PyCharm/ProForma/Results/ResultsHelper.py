
# Net Book Value
def NetBookValueCalculator(developmentCost, replacementReserve, total_depreciation):
    """NetBookValue is calculated as the original cost of an asset,
    minus any accumulated depreciation, accumulated depletion,
    accumulated amortization, and accumulated impairment"""

    NetBookValue = developmentCost - replacementReserve - total_depreciation

    print('### Net Book Value ###')
    print("Total Development Cost: {:,}".format(developmentCost))
    print("Accumulated Replacement Reserve: {:,}".format(replacementReserve))
    print("Accumulated Depreciation: {:,}".format(total_depreciation))
    print("Total Netbook Value: {:,}".format(NetBookValue))
    print('###'*10)

    return NetBookValue

# Gain On Sale
def gainOnSaleCalculator (SalePrice, SaleExpenses,NetBookValue):
    """Gain on Sale is the amount of money that is made when selling a property
    for more than its original value"""
    gainOnSale= SalePrice - SaleExpenses - NetBookValue

    print('### Gain on Sale ###')
    print('Sale Price: {:,}'.format(SalePrice))
    print('Sale Expenses: {:,}'.format(-SaleExpenses))
    print('Net Book Value: {:,}'.format(-NetBookValue))
    print("Gain on Sale : {:,}".format(gainOnSale))
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
    print('Accumulated Depreciation: {:,}'.format(total_depreciation))
    print('Depreciation Recapture Tax: {:,}'.format(depreciation_recapture_tax))
    print('Capital Gain in Excess of Debt: {:,}'.format(CapitalGainInExcessOfDebt))
    print("Capital Gain Tax : {:,}".format(CapitalGainTax))
    print('###' * 10)

    return CapitalGainTax


##################################################################################################
# Net Proceeds from Sale
def NetProceedsFromSaleCalculator (MortgagePayoff, SalePrice, SaleExpenses, TaxPayment):
    """Net Proceeds from Sale is the amount received by the seller after deducting
    all costs and expenses from the gross proceeds"""
    NetProceedsFromSale = SalePrice - SaleExpenses - MortgagePayoff - TaxPayment

    print('### Sale Price ###')
    print('Sale Price: {:,}'.format(SalePrice))
    print('Sales Expenses: {:,}'.format(SaleExpenses))
    print('Mortage Payoff: {:,}'.format(MortgagePayoff))
    print('Tax Payment: {:,}'.format(TaxPayment))
    print("Net Proceeds from Sale : {:,}".format(NetProceedsFromSale))
    print('###' * 10)

    return NetProceedsFromSale




