### 1. Research what is a back of the envelope proforma (or a simple ROI)
### 2 . Write a series of python functions that take inputs used to calculated value and return you a simple ROI .###


#Creating ROI Calculator#
#Define the Variables#

Investment = 40000
Rent = 700
Loss = 1000

def ROI (Investment, Rent, Loss):
    NetProfit = Rent * 12 - Loss
    ROI = (NetProfit/Investment) *100
    print(ROI)

ROI (Investment, Rent, Loss)