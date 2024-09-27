import DevelopmentCostsInputs as devCost

#0.StartingAssumptions#

def TotalGrossZoningFloorArea(residZFA, comZFA, manZFA):
    totalGZFA = [residZFA,comZFA,manZFA]
    sumGZFA = sum(totalGZFA)
##for i in totalGZFA- how would we be able to it that way but print what each one is only one time##
    print("ResidentialZoningFloorArea")
    print(residZFA)
    print("CommercialZoningFloorArea")
    print(comZFA)
    print("ManufacturingZoningFloorArea")
    print(manZFA)
    return sumGZFA

def InacuracyFloorLoss(myTotalGZFA, InacFact):
    floorLoss = myTotalGZFA * InacFact
    print("InaccuracyFactor")
    print(InacFact)
    return floorLoss

def TotalZoningFloorArea(myTotalGZFA, LossFact):
    totalZFA = myTotalGZFA - (myTotalGZFA * LossFact)
    print("NetLossFactor")
    print(LossFact)
    return totalZFA

myTotalGZFA = TotalGrossZoningFloorArea(residZFA= devCost.ResidentialZoningFloorArea,
                                       comZFA= devCost.CommercialZoningFloorArea,
                                       manZFA= devCost.ManufacturingZoningFloorArea)
print("InitialTotalGrossZoningFloorArea")
print(myTotalGZFA)

myFloorLoss = InacuracyFloorLoss(myTotalGZFA= myTotalGZFA,
                                InacFact= devCost.InacuracyFactor)
print("Inacuracy+/-FloorLoss")
print(myFloorLoss)

myTotalZFA = TotalZoningFloorArea(myTotalGZFA= myTotalGZFA,
                                  LossFact= devCost.NetLossFactor)
print("FinalTotalZoningFloorArea")
print(myTotalZFA)

#A.DevelopmentCosts#

def LandPurchaseCost(landCost, lotArea):
    totalPurchCost = landCost * lotArea
    print("LandCost")
    print(landCost)
    print("LotArea")
    print(lotArea)
    return totalPurchCost

def ResidentialCost(residZFA, residCost):
    totalResidCost = residZFA * residCost
    print("ResidentialCostpsf")
    print(residCost)
    return totalResidCost

def CommercialCost(comZFA, comCost):
    totalComCost = comZFA * comCost
    print("CommercialCostpsf")
    print(comCost)
    return totalComCost

def ManufacturingCost(manZFA, manCost):
    totalManCost = manZFA * manCost
    print("ManufacturingCostpsf")
    print(manCost)
    return totalManCost

def HardCost(myTotalGZFA, hardCost):
    totalHardCost = myTotalGZFA * hardCost
    print("HardCostpsf")
    print(hardCost)
    return totalHardCost

def SoftCost(myTotalGZFA, softCost):
    totalSoftCost = myTotalGZFA * softCost
    print("SoftCostpsf")
    print(softCost)
    return totalSoftCost

def TotalDevelopmentCost(BuildPurch, mytotalPurchCost, mytotalResidCost, mytotalComCost, mytotalManCost, mytotalHardCost, mytotalSoftCost):
    totalDevCost = [BuildPurch, mytotalPurchCost, mytotalResidCost, mytotalComCost, mytotalManCost, mytotalHardCost, mytotalSoftCost]
    sumDevCost: int = sum(totalDevCost)
    print("ExistingBuildingPurchase")
    print(BuildPurch)
    return sumDevCost

mytotalPurchCost = LandPurchaseCost(landCost= devCost.LandCostpsf,
                                    lotArea= devCost.LotArea)
print("TotalLandPurchaseCost")
print(mytotalPurchCost)

mytotalResidCost = ResidentialCost(residZFA= devCost.ResidentialZoningFloorArea,
                                   residCost= devCost.ResidentialCostpsf)
print("TotalResidentialCost")
print(mytotalResidCost)

mytotalComCost = CommercialCost(comZFA= devCost.CommercialZoningFloorArea,
                                comCost= devCost.CommercialCostpsf)
print("TotalCommercialCost")
print(mytotalComCost)

mytotalManCost = ManufacturingCost(manZFA= devCost.ManufacturingZoningFloorArea,
                                   manCost= devCost.ManufacturingCostpsf)
print("TotalManufacturingCost")
print(mytotalManCost)

mytotalHardCost = HardCost(myTotalGZFA= myTotalGZFA,
                           hardCost= devCost.HardCostpsf)
print("TotalHardCost")
print(mytotalHardCost)

mytotalSoftCost = SoftCost(myTotalGZFA= myTotalGZFA,
                           softCost= devCost.SoftCostpsf)
print("TotalSoftCost")
print(mytotalSoftCost)

myTotalDevCost = TotalDevelopmentCost(BuildPurch= devCost.ExistingBuildingPurchase,
                                      mytotalPurchCost= mytotalPurchCost,
                                      mytotalResidCost= mytotalResidCost,
                                      mytotalComCost= mytotalComCost,
                                      mytotalManCost= mytotalManCost,
                                      mytotalHardCost= mytotalHardCost,
                                      mytotalSoftCost= mytotalSoftCost)
print("TotalDevelopmentCost")
print(myTotalDevCost)

#B.CapitalStructure#

def Equity(myTotalDevCost, EqPerc):
    totalEq = myTotalDevCost * EqPerc
    print("EquityPercentage")
    print(EqPerc)
    return totalEq

def Debt(myTotalDevCost, mytotalEq):
    totalDebt = myTotalDevCost - mytotalEq
    return totalDebt

def DebtService(mytotalDebt, DebtServPerc):
    totalDebtServ = mytotalDebt * DebtServPerc
    print("DebtServicePercentage")
    print(DebtServPerc)
    return totalDebtServ

mytotalEq = Equity(myTotalDevCost= myTotalDevCost,
                       EqPerc= devCost.EquityPercentage)
print("TotalEquity")
print(mytotalEq)

mytotalDebt = Debt(myTotalDevCost= myTotalDevCost,
                   mytotalEq= mytotalEq)
print("TotalDebt")
print(mytotalDebt)

mytotalDebtServ = DebtService(mytotalDebt= mytotalDebt,
                              DebtServPerc= devCost.DebtServicePercentage)
print("TotalDebtServicingCost")
print(mytotalDebtServ)

#C.ProjectedResidentialProceeds#

#ResidentialExpenses#

#Depreciation#



