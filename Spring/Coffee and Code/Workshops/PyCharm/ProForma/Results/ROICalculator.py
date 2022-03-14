import ProForma_ROI

#Define the Variables#
Investment = 40000
Rent = 700
Loss = 100000

def ROI(Investment, Rent, Loss):
    '''Defining ROI as a rudimentary gauge of an investment’s profitability'''

    NetProfit = ProForma_ROI.tidsProforma(80) - Loss
    ROI = (NetProfit/Investment) * 100
    print(ROI)
    return ROI

my_ROI = ROI(Investment, Rent, Loss)