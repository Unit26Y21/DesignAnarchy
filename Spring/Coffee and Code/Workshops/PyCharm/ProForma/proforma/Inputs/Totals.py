class Totals:
    def __init__(self,
                 total_Residential_Income: int,
                 total_Commercial_Income: int,
                 total_Manufacturing_Income: int,
                 total_Community_Income: int,
                 total_Residential_Vacancy: int,
                 total_Commercial_Vacancy: int,
                 total_Manufacturing_Vacancy: int,
                 total_Community_Vacancy: int,
                 total_Property_Operational_Expenses: int,
                 total_Property_Real_Estate_Taxes: int,
                 total_Property_Replacement_Reserve: int,
                 total_residential_Depreciation: int,
                 total_commercial_Depreciation: int,
                 total_manufacturing_Depreciation: int,
                 total_community_Depreciation: int):

        self.total_Residential_Income = total_Residential_Income
        self.total_Commercial_Income = total_Commercial_Income
        self.total_Manufacturing_Income = total_Manufacturing_Income
        self.total_Community_Income = total_Community_Income

        self.total_Residential_Vacancy = total_Residential_Vacancy
        self.total_Commercial_Vacancy = total_Commercial_Vacancy
        self.total_Manufacturing_Vacancy = total_Manufacturing_Vacancy
        self.total_Community_Vacancy = total_Community_Vacancy

        self.total_Property_Operational_Expenses = total_Property_Operational_Expenses
        self.total_Property_Real_Estate_Taxes = total_Property_Real_Estate_Taxes
        self.total_Property_Replacement_Reserve = total_Property_Replacement_Reserve

        self.total_residential_Depreciation = total_residential_Depreciation
        self.total_commercial_Depreciation = total_commercial_Depreciation
        self.total_manufacturing_Depreciation = total_manufacturing_Depreciation
        self.total_community_Depreciation = total_community_Depreciation

        print("#" * 5)

        self.total_Gross_Incomes = sum([total_Residential_Income,
                                   total_Commercial_Income,
                                   total_Manufacturing_Income,
                                   total_Community_Income])

        print("Total Residential Income: ${:,}".format(self.total_Residential_Income))
        print("Total Commercial Income: ${:,}".format(self.total_Commercial_Income))
        print("Total Manufacturing Income: ${:,}".format(self.total_Manufacturing_Income))
        print("Total Gross Income: ${:,}".format(self.total_Gross_Incomes))

        self.total_Vacancy = sum([self.total_Residential_Vacancy,
                                  self.total_Commercial_Vacancy,
                                  self.total_Manufacturing_Vacancy,
                                  self.total_Community_Vacancy])

        print("\n")
        print("Total Residential Vacancy: ${:,}".format(self.total_Residential_Vacancy))
        print("Total Commercial Vacancy: ${:,}".format(self.total_Commercial_Vacancy))
        print("Total Manufacturing Vacancy: ${:,}".format(self.total_Manufacturing_Vacancy))
        print("Total Vacancy: ${:,}".format(self.total_Vacancy))


        self.total_Expenses = sum([self.total_Property_Operational_Expenses,
                              self.total_Property_Real_Estate_Taxes,
                              self.total_Property_Replacement_Reserve])

        print("\n")
        print("Total Property Operational Expenses: ${:,}".format(self.total_Property_Operational_Expenses))
        print("Total Property Real Estate Tax: ${:,}".format(self.total_Property_Real_Estate_Taxes))
        print("Total Property Replacement Reserve: ${:,}".format(self.total_Property_Replacement_Reserve))
        print("Total Expenses: ${:,}".format(self.total_Expenses))

        self.total_Depreciation = sum([self.total_residential_Depreciation,
                                  self.total_commercial_Depreciation,
                                  self.total_manufacturing_Depreciation,
                                  self.total_community_Depreciation ])

        print("\n")
        print("Total Residential Depreciation: ${:,}".format(self.total_residential_Depreciation))
        print("Total Commercial Depreciation: ${:,}".format(self.total_commercial_Depreciation))
        print("Total Manufacturing Depreciation: ${:,}".format(self.total_manufacturing_Depreciation))
        print("Total Depreciation: ${:,}".format(self.total_Depreciation))