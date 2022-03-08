##DevelopmentCostsPartAofProforma##
    #0.StartingAssumptions#
DevelopmentTimeline = 11
LotArea = 10375
ExistingBuildingFloorArea = 132420.00
ResidentialFAR = 7.52
CommercialFAR = 1.00
ManufacturingFAR = 0.00
ResidentialZoningFloorArea = 100000.00
CommercialZoningFloorArea = 100000.00
ManufacturingZoningFloorArea = 100000.00
#AirRightsSquareFeet =
TotalGrossZoningFloorArea = ResidentialZoningFloorArea+CommercialZoningFloorArea+ManufacturingZoningFloorArea
print(TotalGrossZoningFloorArea)
InnacuracyFactor = 0.03
InnacuracyFloorLoss = TotalGrossZoningFloorArea*InnacuracyFactor
print(InnacuracyFloorLoss)
NetLossFactor = 0.15
TotalNetZoningFloorArea = TotalGrossZoningFloorArea-(TotalGrossZoningFloorArea*NetLossFactor)
print(TotalNetZoningFloorArea)
    #A.DevelopmentCosts#
ResidentialCostpsf = 500.00
CommercialCostpsf = 500.00
ManufacturingCostpsf = 500.00
HardCostpsf = 200.00
SoftCostpsf = 200.00
LandCostpsf = 50
ExistingBuildingPurchase = 0
LandPurchase = LandCostpsf*LotArea
print('$',LandPurchase)
ResidentialCost = ResidentialZoningFloorArea*ResidentialCostpsf
print('$',ResidentialCost)
CommercialCost = CommercialZoningFloorArea*CommercialCostpsf
print('$',CommercialCost)
ManufacturingCost = ManufacturingZoningFloorArea*ManufacturingCostpsf
print('$',ManufacturingCost)
#AirRightsPurchase =
HardCost = TotalGrossZoningFloorArea*HardCostpsf
print('$',HardCost)
SoftCost = TotalGrossZoningFloorArea*SoftCostpsf
print('$',SoftCost)
TotalDevelopmentCost = ExistingBuildingPurchase+LandPurchase+ResidentialCost+CommercialCost+ManufacturingCost+HardCost+SoftCost
print('$',TotalDevelopmentCost)
    #B.CapitalStructure#
EquityPercentage = 0.35
DebtPercentage = 0.65
DebtServicePercentage = 0.0688
Equity = TotalDevelopmentCost*EquityPercentage
print('$',Equity)
Debt = TotalDevelopmentCost-Equity
print('$',Debt)
DebtService = Debt*DebtServicePercentage
print('$',DebtService)
    #C.ProjectedResidentialProceeds#
CommonAreaAndCirculation = ResidentialZoningFloorArea*NetLossFactor
print(CommonAreaAndCirculation)
NetResidentialArea = ResidentialZoningFloorArea-CommonAreaAndCirculation
print(NetResidentialArea)
AverageMarketRateUnitSizepsf = 900.00
AproximateUnits = NetResidentialArea/AverageMarketRateUnitSizepsf
print(int(AverageMarketRateUnitSizepsf))
MarketRateRentpyr = 12000.00
ResidentialVacancyRate = 0.05
IncomeExpenseEscalation = 0.02
TotalResidentialIncome = AproximateUnits*MarketRateRentpyr
print('$',TotalResidentialIncome)
TotalResidentialVacancy = -TotalResidentialIncome*ResidentialVacancyRate
print('$',TotalResidentialVacancy)
    #ResidentialExpenses#
OperationalExpensespsf = 6.50
RealEstateTaxespsf = 2.50
ReplacementReservepsf = 1.00
TotalOperationalExpenses = NetResidentialArea*OperationalExpensespsf
print('$',TotalOperationalExpenses)
TotalRealEstateTaxes = NetResidentialArea*RealEstateTaxespsf
print('$',TotalRealEstateTaxes)
TotalReplacementReserve = ResidentialZoningFloorArea*ReplacementReservepsf
print('$',TotalReplacementReserve)
    #Depreciation#
ResidentailDepreciationinyrs = 27.5
TotalCostResidential = NetResidentialArea*ResidentialCostpsf
print('$',TotalCostResidential)
ResidentialDepreciation = -TotalCostResidential/ResidentailDepreciationinyrs
print('$',ResidentialDepreciation)