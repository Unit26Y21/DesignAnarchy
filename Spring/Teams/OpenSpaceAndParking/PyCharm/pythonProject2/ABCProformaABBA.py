def function_to_do_something(DevelopmentTimeline, LotArea, ExistingBuildingFloorArea, ResidentialFAR, CommercialFAR, ManufacturingFAR, ResidentialZoningFloorArea, CommercialZoningFloorArea, ManufacturingZoningFloorArea, InnacuracyFactor, NetLossFactor, ResidentialCostpsf, CommercialCostpsf, ManufacturingCostpsf, HardCostpsf, SoftCostpsf, LandCostpsf, ExistingBuildingPurchase, EquityPercentage, DebtPercentage, DebtServicePercentage, AverageMarketRateUnitSizepsf, MarketRateRentpyr, ResidentialVacancyRate, IncomeExpenseEscalation, OperationalExpensespsf, RealEstateTaxespsf, ReplacementReservepsf, ResidentailDepreciationinyrs):
    ##DevelopmentCostsPartAofProforma##
    # 0.StartingAssumptions#
    # AirRightsSquareFeet =
    TotalGrossZoningFloorArea = ResidentialZoningFloorArea + CommercialZoningFloorArea + ManufacturingZoningFloorArea
    print(TotalGrossZoningFloorArea)
    InnacuracyFloorLoss = TotalGrossZoningFloorArea * InnacuracyFactor
    print(InnacuracyFloorLoss)
    TotalNetZoningFloorArea = TotalGrossZoningFloorArea - (TotalGrossZoningFloorArea * NetLossFactor)
    print(TotalNetZoningFloorArea)
    # A.DevelopmentCosts#
    LandPurchase = LandCostpsf * LotArea
    print('$', LandPurchase)
    ResidentialCost = ResidentialZoningFloorArea * ResidentialCostpsf
    print('$', ResidentialCost)
    CommercialCost = CommercialZoningFloorArea * CommercialCostpsf
    print('$', CommercialCost)
    ManufacturingCost = ManufacturingZoningFloorArea * ManufacturingCostpsf
    print('$', ManufacturingCost)
    # AirRightsPurchase =
    HardCost = TotalGrossZoningFloorArea * HardCostpsf
    print('$', HardCost)
    SoftCost = TotalGrossZoningFloorArea * SoftCostpsf
    print('$', SoftCost)
    TotalDevelopmentCost = ExistingBuildingPurchase + LandPurchase + ResidentialCost + CommercialCost + ManufacturingCost + HardCost + SoftCost
    print('$', TotalDevelopmentCost)
    # B.CapitalStructure#
    Equity = TotalDevelopmentCost * EquityPercentage
    print('$', Equity)
    Debt = TotalDevelopmentCost - Equity
    print('$', Debt)
    DebtService = Debt * DebtServicePercentage
    print('$', DebtService)
    # C.ProjectedResidentialProceeds#
    CommonAreaAndCirculation = ResidentialZoningFloorArea * NetLossFactor
    print(CommonAreaAndCirculation)
    NetResidentialArea = ResidentialZoningFloorArea - CommonAreaAndCirculation
    print(NetResidentialArea)
    AproximateUnits = NetResidentialArea / AverageMarketRateUnitSizepsf
    print(int(AverageMarketRateUnitSizepsf))
    TotalResidentialIncome = AproximateUnits * MarketRateRentpyr
    print('$', TotalResidentialIncome)
    TotalResidentialVacancy = -TotalResidentialIncome * ResidentialVacancyRate
    print('$', TotalResidentialVacancy)
    # ResidentialExpenses#
    TotalOperationalExpenses = NetResidentialArea * OperationalExpensespsf
    print('$', TotalOperationalExpenses)
    TotalRealEstateTaxes = NetResidentialArea * RealEstateTaxespsf
    print('$', TotalRealEstateTaxes)
    TotalReplacementReserve = ResidentialZoningFloorArea * ReplacementReservepsf
    print('$', TotalReplacementReserve)
    # Depreciation#
    TotalCostResidential = NetResidentialArea * ResidentialCostpsf
    print('$', TotalCostResidential)
    ResidentialDepreciation = -TotalCostResidential / ResidentailDepreciationinyrs
    print('$', ResidentialDepreciation)




function_to_do_something(11, 10375, 132420.00, 7.52, 1.00, 0.00, 100000.00, 100000.00, 100000.00, 0.03, 0.15, 500.00, 500.00, 500.00, 200.00, 200.00, 50, 0, 0.35, 0.65, 0.0688, 900.00, 12000.00, 0.05, 0.02, 6.50, 2.50, 1.00, 27.5)

function_to_do_something(1, 1075, 13420.00, 7.2, 1.00, 0.00, 10000.00, 10000.00, 10000.00, 0.03, 0.15, 50.00, 50.00, 50.00, 20.00, 200.00, 50, 0, 0.35, 0.65, 0.0688, 900.00, 12000.00, 0.05, 0.02, 6.50, 2.50, 1.00, 27.5)
