###Creating ROI Calculator###
    #Source: https://www.youtube.com/watch?v=sW-an04-ubI

#Define the Variables#
Investment = 40000
Rent = 700
Loss = 1000

#defining ROI as a rudimentary gauge of an investment’s profitability
def ROI (Investment, Rent, Loss):
    NetProfit = Rent * 12 - Loss
    ROI = (NetProfit/Investment) *100
    print(ROI)

ROI (Investment, Rent, Loss)

