import Manufacturing_Constants
import Starting_Assumptions

def commonAreaAndCirculation ():
    return manufacturingZoningFloorArea * netLossFactor

def netManufacturingArea ():
    return manufacturingZoningFloorArea - commonAreaAndCirculation()

def totalManufacturingIncome ():
    return manufacturingZoningFloorArea

def totalManufacturingVacancyCost ():
    return -1 * manufacturingVacancyRate * totalManufacturingIncome()

'''Manufacturing Expenses'''
def totalOperationalExpenses ():
    return netManufacturingArea() * operationalExpensesPerSqft

def totalRealEstateTaxes ():
    return netManufacturingArea() * realEstateTaxesPerSqft

def totalReplacementReserve ():
    return manufacturingZoningFloorArea * replacementReservesPerSqft

'''Depreciation'''
def totalCostManufacturing ():
    return manufacturingCost * manufacturingZoningFloorArea

def manufacturingDepreciation ():
    return -1 * (totalCostManufacturing()/manufacturingDepreciationInYears)