def common_area_and_circulation (zoningFloorArea, netLossFactor):
    return zoningFloorArea * netLossFactor

def net_area (zoningFloorArea, common_area_and_circulation):
    return zoningFloorArea - common_area_and_circulation

def approximate_units (resNetArea, avgmarketRateUnitSize):
    return resNetArea / avgmarketRateUnitSize

def total_income (approxUnits, marketRateRent):
    return approxUnits * marketRateRent

def total_vacancy (vacancyRate, total_income):
    return vacancyRate * total_income

def operational_expenses (operationalExpenses, net_area):
    return operationalExpenses * net_area

def real_estate_taxes (realestateTaxes, net_area):
    return realestateTaxes * net_area

def replacement_reserve (zoningFloorArea, replacementReserve):
    return zoningFloorArea * replacementReserve

def total_cost (net_area, devCost):
    return (net_area * devCost)

def depreciation (total_cost, depreciation):
    return (-1 * (total_cost / depreciation))