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
                 residential_Depreciation: int,
                 commercial_Depreciation: int,
                 manufacturing_Depreciation: int,
                 community_Depreciation: int):

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

        print("#" * 5)

        self.total_Gross_Incomes = sum([total_Residential_Income,
                                   total_Commercial_Income,
                                   total_Manufacturing_Income,
                                   total_Community_Income])

        print("Total Residential Income: ${:,}".format(total_Residential_Income))
        print("Total Commercial Income: ${:,}".format(total_Commercial_Income))
        print("Total Manufacturing Income: ${:,}".format(total_Manufacturing_Income))
        print("Total Gross Income: ${:,}".format(total_Gross_Incomes))

        self.total_Vacancy = sum([total_Residential_Vacancy,
                             total_Commercial_Vacancy,
                             total_Manufacturing_Vacancy,
                             total_Community_Vacancy])

        print("\n")
        print("Total Residential Vacancy: ${:,}".format(total_Residential_Vacancy))
        print("Total Commercial Vacancy: ${:,}".format(total_Commercial_Vacancy))
        print("Total Manufacturing Vacancy: ${:,}".format(total_Manufacturing_Vacancy))
        print("Total Vacancy: ${:,}".format(total_Vacancy))


        self.total_Expenses = sum([total_Property_Operational_Expenses,
                              total_Property_Real_Estate_Taxes,
                              total_Property_Replacement_Reserve])

        print("\n")
        print("Total Property Operational Expenses: ${:,}".format(total_Property_Operational_Expenses))
        print("Total Property Real Estate Tax: ${:,}".format(total_Property_Real_Estate_Taxes))
        print("Total Property Replacement Reserve: ${:,}".format(total_Property_Replacement_Reserve))
        print("Total Expenses: ${:,}".format(total_Expenses))

        self.total_Depreciation = sum([residential_Depreciation,
                                  commercial_Depreciation,
                                  manufacturing_Depreciation,
                                  community_Depreciation ])

        print("\n")
        print("Total Residential Depreciation: ${:,}".format(residential_Depreciation))
        print("Total Commercial Depreciation: ${:,}".format(commercial_Depreciation))
        print("Total Manufacturing Depreciation: ${:,}".format(manufacturing_Depreciation))
        print("Total Depreciation: ${:,}".format(total_Depreciation))