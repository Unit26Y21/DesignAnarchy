import Manufacturing_Constants as MC
import Starting_Assumptions as SA


def common_area_and_circulation (zoningFloorArea, netLossFactor):
    return zoningFloorArea * netLossFactor

'''
def net_manufacturing_area (SA.manufacturingZoningFloorArea, MC.commonAreaAndCirculation):
    return SA.manufacturingZoningFloorArea - MC.commonAreaAndCirculation()

def total_manufacturing_income (SA.manufacturingZoningFloorArea):
    return SA.manufacturingZoningFloorArea

def total_manufacturing_vacancy_cost (MC.manufacturingVacancyRate, MC.manufacturingIncome):
    return -1 * MC.manufacturingVacancyRate * MC.manufacturingIncome

#Manufacturing Expenses
def total_operational_expenses (netManufacturingArea, MC.operationalExpensesPerSqft):
    return netManufacturingArea * MC.operationalExpensesPerSqft

def total_real_estate_taxes (netManufacturingArea, MC.realEstateTaxesPerSqft):
    return netManufacturingArea * MC.realEstateTaxesPerSqft

def total_replacement_reserve (SA.manufacturingZoningFloorArea, MC.replacementReservesPerSqft):
    return SA.manufacturingZoningFloorArea * MC.replacementReservesPerSqft

#Depreciation
def total_cost_manufacturing (manufacturingCost, SA.manufacturingZoningFloorArea):
    return manufacturingCost * SA.manufacturingZoningFloorArea

def mandepreciationufacturing_ (totalCostManufacturing, MC.manufacturingDepreciationInYears):
    return -1 * (totalCostManufacturing / MC.manufacturingDepreciationInYears)
'''

manuCommonAreaCirculation = common_area_and_circulation(SA.manufacturingZoningFloorArea, SA.netLossFactor)
resiCommonAreaCirculation = common_area_and_circulation(SA.residentialZoningFloorArea, SA.netLossFactor)

print(manuCommonAreaCirculation)
