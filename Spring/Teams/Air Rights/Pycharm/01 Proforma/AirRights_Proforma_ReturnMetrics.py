import AirRights_Proforma_NetProceedsFromSale
import numpy_financial as npf

#############################
# Return Metrics

# Net Present Value (NPV)
rate, values = 0, [588, 0.9, 1, 1.1, 1.2, 1.2, 1.3, 1.4, 1.5, 15000]

NPV = npf.npv(rate, values)
print("Net Present Value(npv) : ", NPV)

"""
# Another way to calculate Net Present Value (NPV)
N = 11
# holding period: the amount of time for which an investor plans to hold an asset
IHR = "Investor Hurdle Rate"
# hurdle rate: is the minimum rate of return on a project or investment required by a manager or investor
CFAT = "Cash Flow After Taxes in year N"
# the sum of before-tax cash flow in year n + tax effect in year n + futures in year
Equity = 94
values = [588, 0.9, 1, 1.1, 1.2, 1.2, 1.3, 1.4, 1.5, 15000]
rate = 0


def NPV(holdingPeriod, IHR, CFAT, equity, value):
    for val in values:
        NPV = (val / (1+rate)*math.pow(1,10)) - Equity
        print("Net Present Value(npv) : ", NPV)
"""

################################
# Leveraged after tax IRR
Equity = 94
cashFlows = 94, 588, 0.9, 1, 1.1, 1.2, 1.2, 1.3, 1.4, 1.5, 15000

# Calculate the IRR
IRR = round(npf.irr([94, 588, 0.9, 1, 1.1, 1.2, 1.2, 1.3, 1.4, 1.5, 15000]), 11)
print("Internal rate of return: " + str(IRR))

# Capitalized Value
netOperatingIncome = 917
capRateSale = .06

def CapitalizeValueCalculator (NetOperatingIncome, CapRateSale):
    """calculate capitalize value, the current worth of an asset based on expected income"""
    capitalizeValue = NetOperatingIncome / CapRateSale
    print("Capitalize Value:", capitalizeValue)
    return capitalizeValue

capitalizeValue = CapitalizeValueCalculator (netOperatingIncome, capRateSale)

################################
#ROTA- Return on Total Assets
totalDevelopmentCost = AirRights_Proforma_NetProceedsFromSale.totalDevelopmentCost

def ReturnOnTotalAssetsCalculator (NetOperatingIncome, TotalDevelopmentCost):
    """to determine how profitable in relation to total assets, based on financial ratio"""
    ReturnOnTotalAssets = (NetOperatingIncome / TotalDevelopmentCost) * 100
    print ("ROTA %: ", ReturnOnTotalAssets)
    return ReturnOnTotalAssets

ReturnOnTotalAssets = ReturnOnTotalAssetsCalculator (netOperatingIncome, totalDevelopmentCost)

################################
# Return on Equity
TaxPayment = AirRights_Proforma_NetProceedsFromSale.taxPayment
cashFlowAfterFinancing = 9
cashFlowAfterTaxes = cashFlowAfterFinancing + TaxPayment

def ReturnOnEquityCalculator (CashFlowAfterFinancing, CashFlowAfterTaxes):
    """measure of financial performance"""
    ReturnOnEquity = (CashFlowAfterFinancing / CashFlowAfterTaxes)
    print ("Return on Equity %: ", ReturnOnEquity)
    return ReturnOnEquity

ReturnOnEquity = ReturnOnEquityCalculator (cashFlowAfterFinancing, cashFlowAfterTaxes)

