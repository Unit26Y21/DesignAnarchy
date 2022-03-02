# Net Book Value

import AirRights_Proforma_Taxes

"""multiply everything times 1,000,000"""
totalDevelopmentCost = 270
accReplacementReserve = 2
accDepreciation = AirRights_Proforma_Taxes.testDepreciation

def NetBookValueCalculator(DevelopmentCost,replacementReserve, Depreciation):
    """what is this?"""
    NetBookValueCalculator = totalDevelopmentCost - accReplacementReserve - accDepreciation
    print("Netbook Value : " + str(NetBookValueCalculator))
    return NetBookValueCalculator

netBookValue = NetBookValueCalculator(totalDevelopmentCost, accReplacementReserve, accDepreciation)

# Gain On Sale
salePrice = 20000
saleExpenses = 1000

def gainOnSaleCalculator (SalePrice,SaleExpenses,netBookValue):
    gainOnSaleCalculator = salePrice - saleExpenses - netBookValue
    print("Gain on Sale : " + str(gainOnSaleCalculator))
    return gainOnSaleCalculator

gainOnSale = gainOnSaleCalculator (salePrice, saleExpenses, netBookValue)

# Tax Payment
capitalGainsTaxPercentage = 0.20 # extracted from Assumptions
depreciationRecaptureTax = 9
capitalGainInExcessOfDebt = gainOnSale - accDepreciation

def capitalGainTaxCalculator (CapitalGainInExcessOfDebt, CapitalGainsTax):
    capitalGainTaxCalculator = capitalGainInExcessOfDebt * capitalGainsTaxPercentage
    print("Capital Gain Tax : " + str(capitalGainTaxCalculator))
    return capitalGainTaxCalculator

capitalGainTax = capitalGainTaxCalculator(capitalGainInExcessOfDebt, capitalGainsTaxPercentage)

# Net Proceeds from Sale
mortgagePayoff = 115
taxPayment = capitalGainTax + depreciationRecaptureTax

def NetProceedsFromSaleCal (MortgagePayoff, SalePrice, SaleExpenses, TaxPayment):
    NetProceedsFromSaleCal = salePrice - saleExpenses - mortgagePayoff - taxPayment
    print("Net Proceeds from Sale : " + str(NetProceedsFromSaleCal))
    return NetProceedsFromSaleCal

NetProceedsFromSale = NetProceedsFromSaleCal(mortgagePayoff, salePrice, saleExpenses, taxPayment)

