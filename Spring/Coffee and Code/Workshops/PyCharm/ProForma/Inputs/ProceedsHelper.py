def common_area_and_circulation (totalFloorArea, netLossFactor):
    return totalFloorArea * netLossFactor

def net_area (totalFloorArea, common_area_and_circulation):
    return totalFloorArea - common_area_and_circulation

def approximate_units (netArea, avgmarketRateUnitSize):
    return netArea / avgmarketRateUnitSize

def total_income (approxUnits, marketRateRent):
    return approxUnits * marketRateRent

def total_vacancy (vacancyRate, total_income):
    return vacancyRate * total_income

def operational_expenses (operationalExpenses, netArea):
    return operationalExpenses * netArea

def real_estate_taxes (realestateTaxes, netArea):
    return realestateTaxes * netArea

def replacement_reserve (totalFloorArea, replacementReserve):
    return totalFloorArea * replacementReserve

def total_cost (netArea, devCost):
    return (netArea * devCost)

def depreciation (total_cost, depreciation):
    return (-1 * (total_cost / depreciation))