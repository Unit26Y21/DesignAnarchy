from proforma.Inputs import Inputs, Costs, CapitalStructure, Proceeds, OtherRates, Totals

class MyInputsAssumptions:

    def __init__(self,
                 lotArea,
                 existingBuildingFloorArea,
                 residentialFAR,
                 commercialFAR,
                 manufacturingFAR,
                 communityFAR,
                 avgUnitSize_residential,
                 avgUnitSize_commercial,
                 avgUnitSize_manufacturing,
                 avgUnitSize_community,
                 ):

        self.existinBuildingFloorArea = 0 #assumes not building or attaching to existing building
        self.lotArea = lotArea
        self.residentialFAR = residentialFAR
        self.commercialFAR = commercialFAR
        self.manufacturingFAR = manufacturingFAR
        self.communityFAR = communityFAR


        self.development = Inputs.PropertyInputs(lotArea= self.lotArea,
                                                 existingBuildingFloorArea = self.existinBuildingFloorArea,
                                                 residentialFAR = self.residentialFAR,
                                                 commercialFAR = self.commercialFAR,
                                                 manufacturingFAR= self.manufacturingFAR)

        self.developmentCosts = Costs.DevelopmentCosts(residential_ZFA= self.development.residentialZoningFloorArea,
                                                       commercial_ZFA= self.development.commercialZoningFloorArea,
                                                       manufacturing_ZFA= self.development.manufacturingZoningFloorArea)

        self.capitalStructure = CapitalStructure.CapitalStructure(total_development_cost= self.developmentCosts.total_development_cost)


        self.residentialProceeds = Proceeds.myProceeds(proceedsType= "Residential",
                                                       GFA= self.development.residentialZoningFloorArea,
                                                       avg_unit_size= avgUnitSize_residential,
                                                       total_dev_cost= self.developmentCosts.total_development_cost)

        self.commercialProceeds = Proceeds.myProceeds(proceedsType="Commercial",
                                                      GFA=self.development.commercialZoningFloorArea,
                                                      avg_unit_size= avgUnitSize_commercial,
                                                      total_dev_cost=self.developmentCosts.total_development_cost)

        self.manufacturingProceeds = Proceeds.myProceeds(proceedsType="Manufacturing",
                                                         GFA=self.development.manufacturingZoningFloorArea,
                                                         avg_unit_size= avgUnitSize_manufacturing,
                                                         total_dev_cost=self.developmentCosts.total_development_cost)

        self.communityProceeds = Proceeds.myProceeds(proceedsType="Community Facility",
                                                     GFA=self.development.commercialZoningFloorArea,
                                                     avg_unit_size= avgUnitSize_community,
                                                     total_dev_cost=self.developmentCosts.total_development_cost)

        self.rates = OtherRates.OtherRates

        print("\n")
        print("Tax Rates, Rates, Etc:")
        print("\n")

        print(self.residentialProceeds.income)
        print(self.residentialProceeds.vacancy)
        print(round(self.residentialProceeds.units,1))

        self.total_Property_Operational_Expenses = sum([self.residentialProceeds.operation_expense,
                                                   self.commercialProceeds.operation_expense,
                                                   self.manufacturingProceeds.operation_expense,
                                                   self.commercialProceeds.operation_expense])

        self.total_Property_Real_Estate_Taxes = sum([self.residentialProceeds.realestate_taxes,
                                                self.commercialProceeds.realestate_taxes,
                                                self.manufacturingProceeds.realestate_taxes,
                                                self.communityProceeds.realestate_taxes])

        self.total_Property_Replacement_Reserve = sum([self.residentialProceeds.replacement_reserve,
                                                  self.commercialProceeds.replacement_reserve,
                                                  self.manufacturingProceeds.replacement_reserve,
                                                  self.communityProceeds.replacement_reserve])

        self.totals = Totals.Totals(total_Residential_Income = self.residentialProceeds.income,
                                    total_Residential_Vacancy=self.residentialProceeds.vacancy,
                                    total_residential_Depreciation=self.residentialProceeds.depreciation,
                                    total_Commercial_Income=self.commercialProceeds.income,
                                    total_Commercial_Vacancy=self.commercialProceeds.vacancy,
                                    total_commercial_Depreciation=self.commercialProceeds.depreciation,
                                    total_Manufacturing_Income=self.manufacturingProceeds.income,
                                    total_Manufacturing_Vacancy=self.manufacturingProceeds.vacancy,
                                    total_manufacturing_Depreciation=self.manufacturingProceeds.depreciation,
                                    total_Community_Income= self.communityProceeds.income,
                                    total_Community_Vacancy= self.communityProceeds.vacancy,
                                    total_community_Depreciation= self.communityProceeds.depreciation,
                                    total_Property_Operational_Expenses = self.total_Property_Operational_Expenses ,
                                    total_Property_Real_Estate_Taxes= self.total_Property_Real_Estate_Taxes,
                                    total_Property_Replacement_Reserve= self.total_Property_Replacement_Reserve
                                    )
