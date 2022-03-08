# Net Book Value

import AirRights_Proforma_Taxes
import math

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


#############################
# Return Metrics
"""
import numpy as np

values = [588, 0.9, 1, 1.1, 1.2, 1.2, 1.3, 1.4, 1.5, 15000]
rate = 0

NPV =  np.npv(rate,values)
print("Net Present Value(npv) : ", NPV)
"""

# Net Present Value (NPV)
N = 11
# holding period: the amount of time for which an investor plans to hold an asset
IHR = "Investor Hurdle Rate"
# hurdle rate: is the minimum rate of return on a project or investment required by a manager or investor
CFAT = "Cash Flow After Taxes in year N"
# the sum of before-tax cash flow in year n + tax effect in year n + futures in year
Equity = 94
values = [588, 0.9, 1, 1.1, 1.2, 1.2, 1.3, 1.4, 1.5, 15000]
rate = 0

for val in values:
    NPV = (val / (1+rate)*math.pow(1,10)) - Equity
    print("Net Present Value(npv) : ", NPV)
"""
# Leveraged after tax IRR

cashFlows = [Equity, values]

# Calculate the IRR

irr = round(np.irr(cashFlows), 11)

print("Internal rate of return:%3.4f" % irr)
"""

# Capitalized Value
netOperatingIncome = 917
capRateSale = .06

def CapitalizeValueCalculator (input1, input2):
    capitalizeValue = input1 / input2
    print(capitalizeValue)
    return capitalizeValue

CapitalizeValue = CapitalizeValueCalculator (netOperatingIncome, capRateSale)
