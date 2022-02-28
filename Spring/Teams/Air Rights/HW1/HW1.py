CurrentValue = 40000
InputCost = 7000
Loss = 2000

def ROI(CurrentValue, InputCost, Loss):
    NetProfit = CurrentValue * 12 - Loss
    ROI = (NetProfit / InputCost)*100
    print(ROI)


my_ROI = ROI(CurrentValue, InputCost, Loss)
