import ProceedsHelper
from statistics import mean

class myProceeds:
    '''
    A generic proceeds class that can be used for any type of use:
    Residential, Commercial, Manufacturing
    '''

    # NYCHA Vacancy
    residential_vacancy = 0.012
    income_escalation = 0.01

    def __init__(self,
                 residential_GFA,
                 netLossFactor,
                 avg_unit_size,
                 total_dev_cost,
                 residential_rent,
                 residential_operation_expense_persqft,
                 residential_realestate_taxes_persqft,
                 residential_replacement_reserve_persqft,
                 residential_depreciation_yrs, #in years
                 ):

        self.total_dev_cost = total_dev_cost
        self.residential_GFA = residential_GFA
        self.netLossFactor = netLossFactor
        self.avg_unit_size = mean(avg_unit_size)
        self.residential_Rent = residential_rent
        self.residential_operation_expense_persqft = residential_operation_expense_persqft
        self.residential_realestate_taxes_persqft = residential_realestate_taxes_persqft
        self.residential_replacement_reserve_persqft = residential_replacement_reserve_persqft


        # Residential Proceeds
        res_common_circulation = ProceedsHelper.common_area_and_circulation(zoningFloorArea= residential_GFA,
                                                                            netLossFactor=netLossFactor)

        res_netArea = ProceedsHelper.net_area(zoningFloorArea= residential_GFA,
                                common_area_and_circulation= res_common_circulation)


        res_units = ProceedsHelper.approximate_units(resNetArea= res_netArea,
                                                     avgmarketRateUnitSize= avg_unit_size)

        res_income = ProceedsHelper.total_income(approxUnits= res_units,
                                                 marketRateRent= residential_rent)

        res_vacancy = ProceedsHelper.total_vacancy(vacancyRate= self.residential_vacancy,
                                                   total_income= res_income)

        # Residential Expenses
        residential_operation_expense = ProceedsHelper.operational_expenses(net_area= res_netArea,
                                                                            operationalExpenses= residential_operation_expense_persqft)

        residential_realestate_taxes = ProceedsHelper.real_estate_taxes(realestateTaxes= residential_realestate_taxes_persqft,
                                                                        net_area= res_netArea)

        residential_replacement_reserve = ProceedsHelper.replacement_reserve(zoningFloorArea= residential_GFA,
                                                                             replacementReserve= residential_replacement_reserve_persqft)

        # Residential Depreciation

        residential_depreciation = ProceedsHelper.depreciation(depreciation= residential_depreciation_yrs,
                                                               total_cost= total_dev_cost)

