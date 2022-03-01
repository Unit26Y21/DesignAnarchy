# Future Benefits

# Value calculated depends upon estimates of future conditions:

FutureConditions = {
    "FC1": "Physical Conditions",
    "FC2": "Existing Lease Structure",
    "FC3": "Economic & Interest Rate Environment",
    "FC4": "Change Physical Neighborhood",
    "FC5": "Consumer & Investor Preference",
    "FC6": "Expected Inflation Rates",
    "FC7": "Rate Of Return On Alternative Investments",
    "FC8": "Tax Position Of The Seller",
    "FC9": "Contemplated Holding Period"
}


# Changes (can be for better of worse)

ChangesCategories = {
    "OC": "Operating",
    "PC": "Physical", # affecting 1. the property 2. the environment
    "FC": "Financial", #
    "MC": "Market" # the effect of obsolescence, changes in tenants mix or use, government tax policy, owner doing a better selling job
}


# to take into account> critical characteristics
# Extremely low horizon
# Poor liquidity
# Uncertainty concerning the valuation of the property


# Calculation of Net Cash from Sale
# 1. Calculation of Book Value
purchasePrice = 3
capitalImprovements = 2
accumulatedDepreciation = 1

bookValue = (purchasePrice + capitalImprovements) - accumulatedDepreciation
print("Book Value :" + bookValue)

# 2. Calculation of Gain on Sale
netSellingPrice = 3
netBookValue = 4

gainOnSale = netSellingPrice - netBookValue
print("Gain On Sale :" + gainOnSale)

# 3. calculation of tax
taxRate = 0.5

taxLiability = gainOnSale * taxRate
print("Tax Liability :" + taxLiability)

# 4. Calculation of net cash to seller
mortgageBalance = 5
incomeTax = 0.3

netCashFromSale = netSellingPrice - mortgageBalance - incomeTax
print("netCashFromSale :" + netCashFromSale)


# ROI

returnOnAssets = Free&ClearReturn / PropertyCost
# this is static in that it assumes the same cash throughout time. Ignores risk, tax, capital change

CashOnCashReturn = CashFlowAfterFinancing / Equity # equity = Initial cash investment
# rigid because ignores all elements of return not reflected in the end of the month balance. If a deal stand up under this, everything else is a plus

# Net Present Value (NPV)
N = "Holding Period"
# holding period: the amount of time for which an investor plans to hold an asset
IHR = "Investor Hurdle Rate"
# hurdle rate: is the minimum rate of return on a project or investment required by a manager or investor
CFAT = "Cash Flow After Taxes in year N"
# the sum of before-tax cash flow in year n + tax effect in year n + futures in year n

import ProFormaCashFlow
import math
for n in range (1, N):
    NPV = ((1 / math.pow((1+IHR),n))* CFAT) - Equity

# an easier function numpy.npv(rate, values) ... Values are an array

# Internal Rate of Return (IRR)
for n in range ((n-1),N):
    (1 / math.pow((1 + IHR))) - Equity

