
import Starting_Assumptions as SA
import Proceeds_Constants as PC


def common_area_and_circulation (zoningFloorArea, netLossFactor):
    return zoningFloorArea * netLossFactor

resCommonAreaCirculation = common_area_and_circulation(SA.residentialZoningFloorArea, SA.netLossFactor)
comCommonAreaCirculation = common_area_and_circulation(SA.commercialZoningFloorArea, SA.netLossFactor)
manuCommonAreaCirculation = common_area_and_circulation(SA.manufacturingZoningFloorArea, SA.netLossFactor)

print(resCommonAreaCirculation)
print(comCommonAreaCirculation)
print(manuCommonAreaCirculation)


def net_area (zoningFloorArea, common_area_and_circulation):
    return zoningFloorArea - common_area_and_circulation

resNetArea = net_area(SA.residentialZoningFloorArea, resCommonAreaCirculation)
comNetArea = net_area(SA.residentialZoningFloorArea, comCommonAreaCirculation)
manuNetArea = net_area(SA.residentialZoningFloorArea, manuCommonAreaCirculation)

print(resNetArea)
print(comNetArea)
print(manuNetArea)


def approximate_units (resNetArea, avgmarketRateUnitSize):
    return resNetArea / avgmarketRateUnitSize

print(approximate_units)


def total_income (approxUnits, marketRateRent):
    return approxUnits * marketRateRent

resTotalIncome = total_income(PC.res_approxunits, PC.res_marketRateRent)
comTotalIncome = total_income(comNetArea, PC.com_marketRateRent)

manuTotalIncome = SA.manufacturingZoningFloorArea


print(resTotalIncome)
print(comTotalIncome)
print(manuTotalIncome)


def total_vacancy (vacancyRate, total_income):
    return vacancyRate * total_income

resTotalVacancy = total_vacancy(PC.res_vacancyRate, resTotalIncome)
comTotalVacancy = total_vacancy(PC.com_vacancyRate, comTotalIncome)
manuTotalVacancy = total_vacancy(PC.manu_vacancyRate, manuTotalIncome)

print(resTotalVacancy)
print(comTotalVacancy)
print(manuTotalVacancy)


def operational_expenses (operationalExpenses, net_area):
    return operationalExpenses * net_area

resOperationalExpenses = operational_expenses(PC.res_operationalExpenses, resNetArea)
comOperationalExpenses = operational_expenses(PC.com_operationalExpenses, comNetArea)
manuOperationalExpenses = operational_expenses(PC.manu_operationalExpenses, manuNetArea)

print(resOperationalExpenses)
print(comOperationalExpenses)
print(manuOperationalExpenses)


def real_estate_taxes (realestateTaxes, net_area):
    return realestateTaxes * net_area

resRealEstateTaxes = real_estate_taxes(PC.res_realEstateTaxes, resNetArea)
comRealEstateTaxes = real_estate_taxes(PC.com_realEstateTaxes, comNetArea)
manuRealEstateTaxes = real_estate_taxes(PC.manu_realEstateTaxes, manuNetArea)

print(resRealEstateTaxes)
print(comRealEstateTaxes)
print(manuRealEstateTaxes)


def replacement_reserve (zoningFloorArea, replacementReserve):
    return zoningFloorArea * replacementReserve

resReplacementReserve = replacement_reserve(SA.residentialZoningFloorArea, PC.res_replacementReserve)
comReplacementReserve = replacement_reserve(SA.commercialZoningFloorArea, PC.com_replacementReserve)
manuReplacementReserve = replacement_reserve(SA.manufacturingZoningFloorArea, PC.manu_replacementReserves)

print(resReplacementReserve)
print(comReplacementReserve)
print(manuReplacementReserve)


def total_cost (net_area, devCost):
    return (net_area * devCost)

resTotalCost = replacement_reserve(resNetArea, SA.resDevCost)
comTotalCost = replacement_reserve(comNetArea, SA.comDevCost)
manuTotalCost = replacement_reserve(manuNetArea, SA.ManuDevCost)

print (resTotalCost)
print(comTotalCost)
print(manuTotalCost)


def depreciation (total_cost, depreciation):
    return (-1 * (total_cost / depreciation))

resDepreciation = replacement_reserve(resTotalCost, PC.res_depreciation)
comDepreciation = replacement_reserve(comTotalCost, PC.com_depreciation)
manuDepreciation = replacement_reserve(manuTotalCost, PC.manu_Depreciation)

print(resDepreciation)
print(comDepreciation)
print(manuDepreciation)