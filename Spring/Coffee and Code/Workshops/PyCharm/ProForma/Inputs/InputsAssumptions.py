import Inputs, Costs, CapitalStructure, Proceeds, OtherRates, Totals

class MyInputsAssumptions:

    def __init__(self,
                 lotArea,
                 existingBuildingFloorArea,
                 residentialFAR,
                 commercialFAR,
                 manufacturingFAR,
                 avgUnitSize
                 ):

        self.existinBuildingFloorArea = 0 #assumes not building or attaching to existing building
        self.lotArea = lotArea
        self.residentialFAR = residentialFAR
        self.commercialFAR = commercialFAR
        self.manufacturingFAR = manufacturingFAR
        self.avgUnitSize = avgUnitSize

        myDevelopment = Inputs.PropertyInputs(lotArea= self.lotArea,
                              existingBuildingFloorArea = self.existinBuildingFloorArea,
                              residentialFAR = self.residentialFAR,
                              commercialFAR = self.commercialFAR,
                              manufacturingFAR= self.manufacturingFAR)

        myDevelopmentCosts = Costs.DevelopmentCosts(residential_ZFA= myDevelopment.residentialZoningFloorArea,
                               commercial_ZFA= myDevelopment.commercialZoningFloorArea,
                               manufacturing_ZFA= myDevelopment.manufacturingZoningFloorArea)

        myCapitalStructure = CapitalStructure.CapitalStructure(total_development_cost= myDevelopmentCosts.total_development_cost)

        myProceeds = Proceeds.myProceeds(GFA= myDevelopment.totalFloorArea,
                                         avg_unit_size= self.avgUnitSize,
                                         total_dev_cost= myDevelopmentCosts.total_development_cost)

        myRates = OtherRates.OtherRates

        # myTotals = Totals(total_Residential_Income,
        #              total_Commercial_Income,
        #              total_Manufacturing_Income,
        #              total_Residential_Vacancy,
        #              total_Commercial_Vacancy,
        #              total_Manufacturing_Vacancy,
        #              total_Property_Operational_Expenses,
        #              total_Property_Real_Estate_Taxes,
        #              total_Property_Replacement_Reserve,
        #              residential_Depreciation,
        #              commercial_Depreciation,
        #              manufacturing_Depreciation)
