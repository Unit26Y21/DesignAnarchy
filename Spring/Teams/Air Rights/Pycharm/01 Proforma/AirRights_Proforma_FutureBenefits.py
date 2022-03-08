
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

