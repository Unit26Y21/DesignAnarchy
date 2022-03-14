# Helpers to calculate development cost summaries


def LandPurchaseCost(landCost, lotArea):
    totalLandPurchaseCost = landCost * lotArea
    print("---")
    print("Land Cost per SqFt: {:,}".format(landCost))
    print("Total Land Area Cost: {:,}".format(totalLandPurchaseCost))
    return totalLandPurchaseCost

def ResidentialCost(residZFA, residCost):
    totalResidCost = residZFA * residCost
    print("---")
    print("Residential Cost per SqFt: {:,}".format(residCost))
    print("Total Residential Area Cost: {:,}".format(totalResidCost))
    return totalResidCost

def CommercialCost(comZFA, comCost):
    totalComCost = comZFA * comCost
    print("---")
    print("Commercial Cost per SqFt: {:,}".format(comCost))
    print("Total Commercial Area Cost: {:,}".format(totalComCost))
    return totalComCost

def ManufacturingCost(manZFA, manCost):
    totalManCost = manZFA * manCost
    print("---")
    print("Manufacturing Cost per SqFt: {:,}".format(totalManCost))
    print("Total Manufacturing Area Cost: {:,}".format(totalManCost))
    return totalManCost

def HardCost(myTotalGZFA, hardCost):
    totalHardCost = myTotalGZFA * hardCost
    print("---")
    print("Hard Costs per SqFf: {:,}".format(hardCost))
    print("Total Hard Costs: {:,}".format(hardCost))
    return totalHardCost

def SoftCost(myTotalGZFA, softCost):
    totalSoftCost = myTotalGZFA * softCost
    print("---")
    print("Soft Costs per SqFf: {:,}".format(softCost))
    print("Total Soft Costs: {:,}".format(softCost))
    return totalSoftCost

def TotalDevelopmentCost(myBuildingPurchase,  mytotalResidCost, mytotalComCost, mytotalManCost, mytotalHardCost, mytotalSoftCost):
    totalDevCost = [myBuildingPurchase, mytotalResidCost, mytotalComCost, mytotalManCost, mytotalHardCost, mytotalSoftCost]
    sumDevCost = sum(totalDevCost)
    print("---")
    print("Total Development Costs: {:,}".format(sumDevCost))
    return sumDevCost