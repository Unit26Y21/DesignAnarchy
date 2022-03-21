class Totals:
    def __init__(self,
                 total_Residential_Income: int,
                 total_Commercial_Income: int,
                 total_Manufacturing_Income: int,
                 total_Residential_Vacancy: int,
                 total_Commercial_Vacancy: int,
                 total_Manufacturing_Vacancy: int,
                 total_Property_Operational_Expenses: int,
                 total_Property_Real_Estate_Taxes: int,
                 total_Property_Replacement_Reserve: int,
                 residential_Depreciation: int,
                 commercial_Depreciation: int,
                 manufacturing_Depreciation: int):

        self.total_Residential_Income = total_Residential_Income
        self.total_Commercial_Income = total_Commercial_Income
        self.total_Manufacturing_Income = total_Manufacturing_Income

        self.total_Residential_Vacancy = total_Residential_Vacancy
        self.total_Commercial_Vacancy =  total_Commercial_Vacancy
        self.total_Manufacturing_Vacancy = total_Manufacturing_Vacancy

        self.total_Property_Operational_Expenses = total_Property_Operational_Expenses
        self.total_Property_Real_Estate_Taxes = total_Property_Real_Estate_Taxes
        self.total_Property_Replacement_Reserve = total_Property_Replacement_Reserve

        self.residential_Depreciation = residential_Depreciation
        self.commercial_Depreciation = commercial_Depreciation
        self.manufacturing_Depreciation = manufacturing_Depreciation


        total_Gross_Incomes = sum([total_Residential_Income, total_Commercial_Income, total_Manufacturing_Income])
        total_Vacancy = sum([total_Residential_Vacancy,total_Commercial_Vacancy,total_Manufacturing_Vacancy])
        total_Expenses = sum([total_Property_Operational_Expenses, total_Property_Real_Estate_Taxes, total_Property_Replacement_Reserve])
        total_Depreciation_Cost = sum([residential_Depreciation, commercial_Depreciation, manufacturing_Depreciation])