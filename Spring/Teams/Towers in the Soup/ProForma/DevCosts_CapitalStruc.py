import DevelopmentCostsInputs as devCost
##push attempt##

#0.StartingAssumptions#

def TotalGrossZoningFloorArea(residZFA, comZFA, manZFA):
    totalGZFA = [residZFA,comZFA,manZFA]
    sumGZFA = sum(totalGZFA)
    #for i in totalGZFA:
    print("Residential", residZFA,)
    print("Commercial", comZFA)
    print("Manufacturing", manZFA)
    return sumGZFA

def InacuracyFloorLoss(myTotalGZFA, InacFact):
    floorLoss = myTotalGZFA * InacFact
    print("Inaccuracy factor")
    print(InacFact)
    return floorLoss

def TotalZoningFloorArea(myTotalGZFA, LossFact):
    totalZFA = myTotalGZFA - (myTotalGZFA * LossFact)
    print("Net loss factor")
    print(LossFact)
    return totalZFA

myTotalGZFA = TotalGrossZoningFloorArea(residZFA= devCost.ResidentialZoningFloorArea,
                                       comZFA= devCost.CommercialZoningFloorArea,
                                       manZFA= devCost.ManufacturingZoningFloorArea)
print("My total gross zoning floor area")
print(myTotalGZFA)

myFloorLoss = InacuracyFloorLoss(myTotalGZFA= myTotalGZFA,
                                InacFact= devCost.InacuracyFactor)
print("my total floor loss")
print(myFloorLoss)

myTotalZFA = TotalZoningFloorArea(myTotalGZFA= myTotalGZFA,
                                  LossFact= devCost.NetLossFactor)
print("My total zoning floor area")
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
    sumDevCost: int = sum(totalDevCost)
    print(BuildPurch)
    return sumDevCost

mytotalPurchCost = LandPurchaseCost(landCost= devCost.LandCostpsf,
                                    lotArea= devCost.LotArea)
print("My total purchasing costs")
print(mytotalPurchCost)

mytotalResidCost = ResidentialCost(residZFA= devCost.ResidentialZoningFloorArea,
                                   residCost= devCost.ResidentialCostpsf)
print("My total residential Cost")
print(mytotalResidCost)

mytotalComCost = CommercialCost(comZFA= devCost.CommercialZoningFloorArea,
                                comCost= devCost.CommercialCostpsf)
print("My total commercial cost")
print(mytotalComCost)

mytotalManCost = ManufacturingCost(manZFA= devCost.ManufacturingZoningFloorArea,
                                   manCost= devCost.ManufacturingCostpsf)
print("My total manufacturing cost")
print(mytotalManCost)

mytotalHardCost = HardCost(myTotalGZFA= myTotalGZFA,
                           hardCost= devCost.HardCostpsf)
print("My total hard cost")
print(mytotalHardCost)

mytotalSoftCost = SoftCost(myTotalGZFA= myTotalGZFA,
                           softCost= devCost.SoftCostpsf)
print("My total soft cost")
print(mytotalSoftCost)

myTotalDevCost = TotalDevelopmentCost(BuildPurch= devCost.ExistingBuildingPurchase,
                                      mytotalPurchCost= mytotalPurchCost,
                                      mytotalResidCost= mytotalResidCost,
                                      mytotalComCost= mytotalComCost,
                                      mytotalManCost= mytotalManCost,
                                      mytotalHardCost= mytotalHardCost,
                                      mytotalSoftCost= mytotalSoftCost)
print("My total development cost")
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
print("My total equity")
print(mytotalEq)

mytotalDebt = Debt(myTotalDevCost= myTotalDevCost,
                   mytotalEq= mytotalEq)
print("My total debt")
print(mytotalDebt)

mytotalDebtServ = DebtService(mytotalDebt= mytotalDebt,
                              DebtServPerc= devCost.DebtServicePercentage)
print("My total debt servicing cost")
print(mytotalDebtServ)

#C.ProjectedResidentialProceeds#

#ResidentialExpenses#

#Depreciation#



