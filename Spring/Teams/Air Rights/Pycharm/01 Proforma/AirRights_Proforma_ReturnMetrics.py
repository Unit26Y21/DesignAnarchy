import AirRights_Proforma_NetProceedsFromSale
#import NumPy.py

#############################
# Return Metrics

values = [588, 0.9, 1, 1.1, 1.2, 1.2, 1.3, 1.4, 1.5, 15000]
rate = 0

NPV = np.npv(rate, values)
print("Net Present Value(npv) : ", NPV)

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

def NPV(holdingPeriod, IHR, CFAT, equity, value):
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

def CapitalizeValueCalculator (netOperatingIncome, capRateSale):
    """calculate capitalize value, the current worth of an asset based on expected income"""
    capitalizeValue = netOperatingIncome / capRateSale
    print("Capitalize Value:", capitalizeValue)
    return capitalizeValue

CapitalizeValue = CapitalizeValueCalculator (netOperatingIncome, capRateSale)

################################
#ROTA- Return on Total Assets
TotalDevelopmentCost = AirRights_Proforma_NetProceedsFromSale.totalDevelopmentCost

def ReturnOnTotalAssetsCalculator (netOperatingIncome, totalDevelopmentCost):
    """to determine how profitable in relation to total assets, based on financial ratio"""
    ReturnOnTotalAssets = (netOperatingIncome / totalDevelopmentCost) * 100
    print ("ROTA %: ", ReturnOnTotalAssets)
    return ReturnOnTotalAssets

ReturnOnTotalAssets = ReturnOnTotalAssetsCalculator (netOperatingIncome, TotalDevelopmentCost)

################################
# Return on Equity
TaxPayment = AirRights_Proforma_NetProceedsFromSale.taxPayment
cashFlowAfterFinancing = 9
cashFlowAfterTaxes = cashFlowAfterFinancing + TaxPayment

def ReturnOnEquityCalculator (cashFlowAfterFinancing, cashFlowAfterTaxes):
    """measure of financial performance"""
    ReturnOnEquity = (cashFlowAfterFinancing / cashFlowAfterTaxes)
    print ("Return on Equity %: ", ReturnOnEquity)
    return ReturnOnEquity

ReturnOnEquity = ReturnOnEquityCalculator (cashFlowAfterTaxes, Equity)

