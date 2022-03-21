import ProceedsHelper
from statistics import mean

class myProceeds:
    '''
    A generic proceeds class that can be used for any type of use:
    Residential, Commercial, Manufacturing
    '''

    # NYCHA Vacancy
    vacancy = 0.012
    income_escalation = 0.01
    rent = 500

    #NYCHA Operation Costs
    operation_expense_persqft = 7 #USD
    realestate_taxes_persqft = 0 #USD
    replacement_reserve_persqft = 1 #USD
    depreciation_yrs = 27.5   # in years
    netLossFactor = 0.15

    def __init__(self,
                 GFA: int,
                 avg_unit_size: float,
                 total_dev_cost: int,
                 ):

        self.total_dev_cost = total_dev_cost
        self.GFA = GFA
        self.avg_unit_size = mean(avg_unit_size)

        netArea = GFA - (GFA * self.netLossFactor)
        units = netArea/avg_unit_size

        #Proceeds
        common_circulation = ProceedsHelper.common_area_and_circulation(totalFloorArea= GFA,
                                                                        netLossFactor= self.netLossFactor)

        netArea = ProceedsHelper.net_area(totalFloorArea= GFA,
                                          common_area_and_circulation= GFA * self.netLossFactor)

        units = ProceedsHelper.approximate_units(netArea= netArea,
                                                 avgmarketRateUnitSize= avg_unit_size)

        income = ProceedsHelper.total_income(approxUnits= units,
                                             marketRateRent= self.rent)

        vacancy = ProceedsHelper.total_vacancy(vacancyRate= self.vacancy,
                                               total_income= income)

        #Expenses
        operation_expense = ProceedsHelper.operational_expenses(netArea= netArea,
                                                                operationalExpenses= self.operation_expense_persqft)

        realestate_taxes = ProceedsHelper.real_estate_taxes(realestateTaxes= self.realestate_taxes_persqft,
                                                            netArea= netArea)

        replacement_reserve = ProceedsHelper.replacement_reserve(totalFloorArea= GFA,
                                                                 replacementReserve= self.replacement_reserve_persqft)

        #Depreciation

        depreciation = ProceedsHelper.depreciation(depreciation= self.depreciation_yrs,
                                                   total_cost= total_dev_cost)

