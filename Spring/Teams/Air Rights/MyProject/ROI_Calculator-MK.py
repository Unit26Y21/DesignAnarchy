### 1. Research what is a back of the envelope pro forma (or a simple ROI)
    #Back of envelope
### 2 . Write a series of python functions that take inputs used to calculated value and return you a simple ROI .###


#Creating ROI Calculator#

#Define the Variables#
Investment = 40000
Rent = 700
Loss = 1000

#defining the investments can have breakdown of liquid capital, loans, bonds, , etc.
#def Investment (Cash, Loans, Bonds,
#   Incremental Funding: from NYC + HUD, 10-year 2.2 billion dollars starting in 2019)

#defining Rent can be a culmination of number of units and rent per type
#def Rent (NumUnits,

#defining ROI as a rudimentary gauge of an investment’s profitability
def ROI (Investment, Rent, Loss):
    NetProfit = Rent * 12 - Loss
    ROI = (NetProfit/Investment) *100
    print(ROI)

ROI (Investment, Rent, Loss)

#Rate of Return- takes into account the project's time frame
#SROI- Social return on investment, to understand the environmental, social and governance (ESG) criteria used in Socially responsible Investing (SRI)


##