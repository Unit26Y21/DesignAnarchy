from proforma.Inputs import ProceedsHelper

class myProceeds:
    '''
    A generic proceeds class that can be used for any type of use:
    Residential, Commercial, Manufacturing
    '''

    # NYCHA Vacancy
    vacancy_rate = 0.012
    income_escalation = 0.01
    rent = 500

    #NYCHA Operation Costs
    operation_expense_persqft = 7 #USD
    realestate_taxes_persqft = 0 #USD
    replacement_reserve_persqft = 1 #USD
    depreciation_yrs = 27.5   # in years
    netLossFactor = 0.15

    income = 0
    vacancy = 0
    units = 0
    netArea = 0


    def __init__(self,
                 proceedsType: str,
                 GFA: int,
                 avg_unit_size: float,
                 total_dev_cost: int,
                 ):

        self.total_dev_cost = total_dev_cost
        self.GFA = GFA
        self.avg_unit_size = avg_unit_size
        self.proceedsType = proceedsType

        #Proceeds
        common_circulation = ProceedsHelper.common_area_and_circulation(totalFloorArea= GFA,
                                                                        netLossFactor= self.netLossFactor)

        self.netArea = ProceedsHelper.net_area(totalFloorArea= GFA,
                                               common_area_and_circulation= GFA * self.netLossFactor)

        self.units = ProceedsHelper.approximate_units(netArea= self.netArea,
                                                      avgmarketRateUnitSize= avg_unit_size)

        self.income = ProceedsHelper.total_income(approxUnits= self.units,
                                                  marketRateRent= self.rent)

        self.vacancy = ProceedsHelper.total_vacancy(vacancyRate= self.vacancy_rate,
                                                    total_income= self.income)

        #Expenses
        self.operation_expense = ProceedsHelper.operational_expenses(netArea= self.netArea,
                                                                     operationalExpenses= self.operation_expense_persqft)

        self.realestate_taxes = ProceedsHelper.real_estate_taxes(realestateTaxes= self.realestate_taxes_persqft,
                                                                 netArea= self.netArea)

        self.replacement_reserve = ProceedsHelper.replacement_reserve(totalFloorArea= GFA,
                                                                      replacementReserve= self.replacement_reserve_persqft)

        #Depreciation

        self.depreciation = ProceedsHelper.depreciation(depreciation= self.depreciation_yrs,
                                                        total_cost= total_dev_cost)

        print("\n")
        print("{} Proceeds".format(proceedsType))
        print("Common Area and Circulation: ${:,}".format(common_circulation))
        print("Net {} Area: ${:,}".format(proceedsType, self.netArea))
        print("{} Market Rate Rent: ${:,}".format(proceedsType, self.rent))
        print("{} Vacancy Rate: ${:,}".format(proceedsType, self.vacancy_rate))
        print("{} Total Income --> ${:,}".format(proceedsType,self.income))
        print("{} Total Vacancy Cost --> ${:,}".format(proceedsType,self.vacancy))

        print("\n")
        print("{} Expenses".format(proceedsType))
        print("{} Operational Expense per SqFt: ${:,}".format(proceedsType, self.operation_expense_persqft))
        print("{} Real Estate Taxes per SqFt: ${:,}".format(proceedsType, self.realestate_taxes_persqft))
        print("{} Replacement Reserve per SqFt: ${:,}".format(proceedsType, self.replacement_reserve_persqft))
        print("{} Operational Expense Total: ${:,}".format(proceedsType, self.operation_expense))
        print("{} Real Estate Taxes Total: ${:,}".format(proceedsType, self.realestate_taxes))
        print("{} Replacement Reserve Total: ${:,}".format(proceedsType, self.replacement_reserve))

        print("\n")
        print("{} Depreciation".format(proceedsType))
        print("{} Depreciation in Yrs: {}".format(proceedsType, self.depreciation_yrs))
        print("Total Depreciation ${:,}".format(self.depreciation))