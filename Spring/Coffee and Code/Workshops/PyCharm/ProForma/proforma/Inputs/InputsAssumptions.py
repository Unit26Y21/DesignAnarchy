from proforma.Inputs import Inputs, Costs, CapitalStructure, Proceeds, OtherRates, Totals

class MyInputsAssumptions:

    def __init__(self,
                 lot_area: float,
                 existingBuildingFloorArea: float,
                 existingBuildingPurchase: int,
                 residential_FAR: float,
                 commercial_FAR: float,
                 manufacturing_FAR: float,
                 communityFAR: float,
                 avgUnitSize_residential: int,
                 avgUnitSize_commercial: int,
                 avgUnitSize_manufacturing: int,
                 avgUnitSize_community: int,
                 residential_cost: int,
                 commercial_cost: int,
                 manufacturing_cost: int,
                 community_cost: int,
                 hard_cost: int,
                 soft_cost: int,
                 land_cost: int,
                 ):

        self.existinBuildingFloorArea = 0 #assumes not building or attaching to existing building
        self.existinBuildingPurchase = existingBuildingPurchase
        self.lot_area = lot_area
        self.residential_FAR = residential_FAR
        self.commercial_FAR = commercial_FAR
        self.manufacturing_FAR = manufacturing_FAR
        self.communityFAR = communityFAR
        self.residential_cost = residential_cost
        self.commercial_cost: commercial_cost
        self.manufacturing_cost: manufacturing_cost
        self.community_cost: community_cost
        self.hard_cost: hard_cost
        self.soft_cost: soft_cost
        self.land_cost = land_cost


        self.development = Inputs.PropertyInputs(lot_area= self.lot_area,
                                                 existingBuildingFloorArea = self.existinBuildingFloorArea,
                                                 residential_FAR = self.residential_FAR,
                                                 commercial_FAR = self.commercial_FAR,
                                                 manufacturing_FAR= self.manufacturing_FAR,
                                                 community_FAR= self.communityFAR)

        self.development_costs = Costs.development_costs( existingBuildingPurchase= existingBuildingPurchase,
                                                          residential_ZFA= self.development.residential_ZFA,
                                                          commercial_ZFA= self.development.commercial_ZFA,
                                                          manufacturing_ZFA= self.development.manufacturing_ZFA,
                                                          community_ZFA= self.development.community_ZFA,
                                                          residential_cost = residential_cost,
                                                          commercial_cost= commercial_cost,
                                                          manufacturing_cost= manufacturing_cost,
                                                          community_cost= community_cost,
                                                          hard_cost= hard_cost,
                                                          soft_cost= soft_cost,
                                                          land_cost= land_cost)

        self.capitalStructure = CapitalStructure.CapitalStructure(total_development_cost= self.development_costs.total_development_cost)


        self.residentialProceeds = Proceeds.myProceeds(proceeds_type= "Residential",
                                                       gross_floor_area= self.development.residential_ZFA,
                                                       avg_unit_size= avgUnitSize_residential,
                                                       total_dev_cost= self.development_costs.total_development_cost)

        self.commercialProceeds = Proceeds.myProceeds(proceeds_type="Commercial",
                                                      gross_floor_area=self.development.commercial_ZFA,
                                                      avg_unit_size= avgUnitSize_commercial,
                                                      total_dev_cost=self.development_costs.total_development_cost)

        self.manufacturingProceeds = Proceeds.myProceeds(proceeds_type="Manufacturing",
                                                         gross_floor_area=self.development.manufacturing_ZFA,
                                                         avg_unit_size= avgUnitSize_manufacturing,
                                                         total_dev_cost=self.development_costs.total_development_cost)

        self.communityProceeds = Proceeds.myProceeds(proceeds_type="Community Facility",
                                                     gross_floor_area=self.development.community_ZFA,
                                                     avg_unit_size= avgUnitSize_community,
                                                     total_dev_cost=self.development_costs.total_development_cost)

        self.rates = OtherRates.OtherRates

        print("\n")
        print("Tax Rates, Rates, Etc:")
        print("\n")

        print(self.residentialProceeds.income)
        print(self.residentialProceeds.vacancy)
        print(round(self.residentialProceeds.units,1))

        self.total_property_operational_expenses = sum([self.residentialProceeds.operation_expense,
                                                        self.commercialProceeds.operation_expense,
                                                        self.manufacturingProceeds.operation_expense,
                                                        self.commercialProceeds.operation_expense])

        self.total_property_real_estate_taxes = sum([self.residentialProceeds.realestate_taxes,
                                                     self.commercialProceeds.realestate_taxes,
                                                     self.manufacturingProceeds.realestate_taxes,
                                                     self.communityProceeds.realestate_taxes])

        self.total_property_replacement_reserve = sum([self.residentialProceeds.replacement_reserve,
                                                       self.commercialProceeds.replacement_reserve,
                                                       self.manufacturingProceeds.replacement_reserve,
                                                       self.communityProceeds.replacement_reserve])

        self.totals = Totals.Totals(total_residential_income = self.residentialProceeds.income,
                                    total_residential_vacancy=self.residentialProceeds.vacancy,
                                    total_residential_depreciation=self.residentialProceeds.depreciation,
                                    total_commercial_income=self.commercialProceeds.income,
                                    total_commercial_vacancy=self.commercialProceeds.vacancy,
                                    total_commercial_depreciation=self.commercialProceeds.depreciation,
                                    total_manufacturing_income=self.manufacturingProceeds.income,
                                    total_manufacturing_vacancy=self.manufacturingProceeds.vacancy,
                                    total_manufacturing_depreciation=self.manufacturingProceeds.depreciation,
                                    total_community_income= self.communityProceeds.income,
                                    total_community_vacancy= self.communityProceeds.vacancy,
                                    total_community_depreciation= self.communityProceeds.depreciation,
                                    total_property_operational_expenses = self.total_property_operational_expenses ,
                                    total_property_real_estate_taxes= self.total_property_real_estate_taxes,
                                    total_property_replacement_reserve= self.total_property_replacement_reserve
                                    )
