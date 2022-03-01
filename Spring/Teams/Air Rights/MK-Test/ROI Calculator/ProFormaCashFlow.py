# Free and Clear Cash Flow represents the total funds available to service debt in the event of a foreclosure

# Capitalizing Cash Flow Constants

CashFlow = 1000000
CapitalizationRate = .11
LoanToValueRatio = .75

initialEquityValue = (CashFlow * LoanToValueRatio)/CapitalizationRate
     #return intialEquityValue

print (initialEquityValue)