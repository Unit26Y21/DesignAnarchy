# Net Book Value

"""multiply everything times 1,000,000"""
totalDevelopmentCost = 270
accReplacementReserve = 2
accDepreciation = AirRights_Proforma_Taxes.testDepreciation

def NetBookValueCalculator(developmentCost, replacementReserve, depreciation):
    """is calculated as the original cost of an asset, minus any accumulated depreciation, accumulated depletion, accumulated amortization, and accumulated impairment"""
    NetBookValueCalculator = developmentCost - replacementReserve - depreciation
    print("Netbook Value : " + str(NetBookValueCalculator))
    return NetBookValueCalculator

netBookValue = NetBookValueCalculator(totalDevelopmentCost, accReplacementReserve, accDepreciation)

#################################################################################################
# Gain On Sale
salePrice = 20000
saleExpenses = 1000

def gainOnSaleCalculator (SalePrice,SaleExpenses,NetBookValue):
    """is the amount of money that is made when selling a property for more than its original value"""
    gainOnSaleCalculator = SalePrice - SaleExpenses - NetBookValue
    print("Gain on Sale : " + str(gainOnSaleCalculator))
    return gainOnSaleCalculator

gainOnSale = gainOnSaleCalculator (salePrice, saleExpenses, netBookValue)

##################################################################################################
# Tax Payment
capitalGainsTaxPercentage = 0.20 # extracted from Assumptions
depreciationRecaptureTax = 9
capitalGainInExcessOfDebt = gainOnSale - accDepreciation

def capitalGainTaxCalculator (CapitalGainInExcessOfDebt, CapitalGainsTaxPercentage):
    """federal fee paid on the profit made from selling a property"""
    capitalGainTaxCalculator = CapitalGainInExcessOfDebt * CapitalGainsTaxPercentage
    print("Capital Gain Tax : " + str(capitalGainTaxCalculator))
    return capitalGainTaxCalculator

capitalGainTax = capitalGainTaxCalculator(capitalGainInExcessOfDebt, capitalGainsTaxPercentage)

##################################################################################################
# Net Proceeds from Sale
mortgagePayoff = 115
taxPayment = capitalGainTax + depreciationRecaptureTax

def NetProceedsFromSaleCal (MortgagePayoff, SalePrice, SaleExpenses, TaxPayment):
    """the amounts received by the seller after deducting all costs and expenses from the gross proceeds"""
    NetProceedsFromSaleCal = SalePrice - SaleExpenses - MortgagePayoff - TaxPayment
    print("Net Proceeds from Sale : " + str(NetProceedsFromSaleCal))
    return NetProceedsFromSaleCal

NetProceedsFromSale = NetProceedsFromSaleCal(mortgagePayoff, salePrice, saleExpenses, taxPayment)




