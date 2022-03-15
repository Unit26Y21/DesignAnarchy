import totalData
import totalData as TD
#import form C,D,E#

print("Tower in the Soup")

def total(a,b,c):
    return a+b+c

totalGrossIncomes = total(TD.totalResidentialIncome,
                          TD.totalCommercialIncome,
                          TD.totalManufacturingIncome)

totalVacancy = total(TD.totalResidentialVacancy,
                     TD.totalCommercialVacancy,
                     TD.totalManufacturingVacancy)

totalExpenses = total(TD.totalPropertyOperationalExpenses,
                      TD.totalPropertyRealEstateTaxes,
                      TD.totalPropertyReplacementReserve)

totalDepreciationCost = total(TD.residentialDepreciation,
                              TD.commercialDepreciation,
                              TD.manufacturingDepreciation)
print(totalGrossIncomes)
print(totalVacancy)
print(totalExpenses)
print(totalDepreciationCost)



def totalGrossIncomes(totalResidentialIncome,totalCommercialIncome,totalManufacturingIncome):
    return totalResidentialIncome + totalCommercialIncome + totalManufacturingIncome

def totalVacancy(totalResidentialVacancy,totalCommericialVacancy,totalManufacturingVacancy):
    return totalResidentialVacancy + totalCommericialVacancy + totalManufacturingVacancy

def totalExpenses(totalPropertyOperationalEXpenses,totalPropertyRealEstateTaxes,toalPropertyReplacementReserve):
    return totalPropertyOperationalEXpenses + totalPropertyRealEstateTaxes + toalPropertyReplacementReserve

def totalDepreciationCost(totalResidentialDepreciation,totalCommercialDepreciation,totalManufacturingDepreciation):
    return totalResidentialDepreciation + totalCommercialDepreciation + totalManufacturingDepreciation
