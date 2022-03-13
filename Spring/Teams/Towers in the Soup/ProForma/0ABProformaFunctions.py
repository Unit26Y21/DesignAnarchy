import DevelopmentCostsInputs as devCost

#0.StartingAssumptions#

def TotalGrossZoningFloorArea(residZFA, comZFA, manZFA):
    totalGZFA = [residZFA,comZFA,manZFA]
    sumGZFA = sum(totalGZFA)
    for i in totalGZFA:
        print(i)
    return sumGZFA

def InacuracyFloorLoss(myTotalGZFA, InacFact):
    floorLoss = myTotalGZFA * InacFact
    print(InacFact)
    return floorLoss

def TotalZoningFloorArea(myTotalGZFA, LossFact):
    totalZFA = myTotalGZFA - (myTotalGZFA * LossFact)
    print(LossFact)
    return totalZFA

myTotalGZFA = TotalGrossZoningFloorArea(residZFA= devCost.ResidentialZoningFloorArea,
                                       comZFA= devCost.CommercialZoningFloorArea,
                                       manZFA= devCost.ManufacturingZoningFloorArea)
print(myTotalGZFA)

myFloorLoss = InacuracyFloorLoss(myTotalGZFA= myTotalGZFA,
                                InacFact= devCost.InacuracyFactor)
print(myFloorLoss)

myTotalZFA = TotalZoningFloorArea(myTotalGZFA= myTotalGZFA,
                                  LossFact= devCost.NetLossFactor)
print(myTotalZFA)

#A.DevelopmentCosts#

def LandPurchaseCost(landCost, lotArea):
    totalPurchCost = landCost * lotArea
    print(landCost)
    print(lotArea)
    return totalPurchCost

def ResidentialCost(residZFA, residCost):
    totalResidCost = residZFA * residCost
    print(residCost)
    return totalResidCost

def CommercialCost(comZFA, comCost):
    totalComCost = comZFA * comCost
    print(comCost)
    return totalComCost

def ManufacturingCost(manZFA, manCost):
    totalManCost = manZFA * manCost
    print(manCost)
    return totalManCost

def HardCost(myTotalGZFA, hardCost):
    totalHardCost = myTotalGZFA * hardCost
    print(hardCost)
    return totalHardCost

def SoftCost(myTotalGZFA, softCost):
    totalSoftCost = myTotalGZFA * softCost
    print(softCost)
    return totalSoftCost

def TotalDevelopmentCost(BuildPurch, mytotalPurchCost, mytotalResidCost, mytotalComCost, mytotalManCost, mytotalHardCost, mytotalSoftCost):
    totalDevCost = [BuildPurch, mytotalPurchCost, mytotalResidCost, mytotalComCost, mytotalManCost, mytotalHardCost, mytotalSoftCost]
    sumDevCost = sum(totalDevCost)
    print(BuildPurch)
    return sumDevCost

mytotalPurchCost = LandPurchaseCost(landCost= devCost.LandCostpsf,
                                    lotArea= devCost.LotArea)
print(mytotalPurchCost)

mytotalResidCost = ResidentialCost(residZFA= devCost.ResidentialZoningFloorArea,
                                   residCost= devCost.ResidentialCostpsf)
print(mytotalResidCost)

mytotalComCost = CommercialCost(comZFA= devCost.CommercialZoningFloorArea,
                                comCost= devCost.CommercialCostpsf)
print(mytotalComCost)

mytotalManCost = ManufacturingCost(manZFA= devCost.ManufacturingZoningFloorArea,
                                   manCost= devCost.ManufacturingCostpsf)
print(mytotalManCost)

mytotalHardCost = HardCost(myTotalGZFA= myTotalGZFA,
                           hardCost= devCost.HardCostpsf)
print(mytotalHardCost)

mytotalSoftCost = SoftCost(myTotalGZFA= myTotalGZFA,
                           softCost= devCost.SoftCostpsf)
print(mytotalSoftCost)

myTotalDevCost = TotalDevelopmentCost(BuildPurch= devCost.ExistingBuildingPurchase,
                                      mytotalPurchCost= mytotalPurchCost,
                                      mytotalResidCost= mytotalResidCost,
                                      mytotalComCost= mytotalComCost,
                                      mytotalManCost= mytotalManCost,
                                      mytotalHardCost= mytotalHardCost,
                                      mytotalSoftCost= mytotalSoftCost)
print(myTotalDevCost)

#B.CapitalStructure#

def Equity(myTotalDevCost, EqPerc):
    totalEq = myTotalDevCost * EqPerc
    print(EqPerc)
    return totalEq

def Debt(myTotalDevCost, mytotalEq):
    totalDebt = myTotalDevCost - mytotalEq
    return totalDebt

def DebtService(mytotalDebt, DebtServPerc):
    totalDebtServ = mytotalDebt * DebtServPerc
    print(DebtServPerc)
    return totalDebtServ

mytotalEq = Equity(myTotalDevCost= myTotalDevCost,
                       EqPerc= devCost.EquityPercentage)
print(mytotalEq)

mytotalDebt = Debt(myTotalDevCost= myTotalDevCost,
                   mytotalEq= mytotalEq)
print(mytotalDebt)

mytotalDebtServ = DebtService(mytotalDebt= mytotalDebt,
                              DebtServPerc= devCost.DebtServicePercentage)
print(mytotalDebtServ)

#C.ProjectedResidentialProceeds#

#ResidentialExpenses#

#Depreciation#



