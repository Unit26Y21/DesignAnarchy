CurrentValue = 40000
InputCost = 7000


def ROI(CurrentValue, InputCost):
    NetProfit = CurrentValue - InputCost
    ROI = (NetProfit / InputCost)*100
    print(ROI)


ROI(CurrentValue, InputCost)

