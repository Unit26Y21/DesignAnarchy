import Inputs, Costs, CapitalStructure, Proceeds, OtherRates, Totals
import pprint as pp


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

        print(avgUnitSize)
        print(myDevelopmentCosts.total_development_cost)

        myResidentialProceeds = Proceeds.myProceeds(proceedsType= "Residential",
                                                    GFA= myDevelopment.totalFloorArea,
                                                    avg_unit_size= avgUnitSize,
                                                    total_dev_cost= myDevelopmentCosts.total_development_cost)

        myRates = OtherRates.OtherRates

        print("\n")
        print("Tax Rates, Rates, Etc:")
        pp.pprint(myRates.ratesDictionary)
        print("\n")

        print(myResidentialProceeds.income)
        print(myResidentialProceeds.vacancy)
        print(round(myResidentialProceeds.units,1))

        myTotals = Totals.Totals(total_Residential_Income = myResidentialProceeds.income,
                                 total_Residential_Vacancy=myResidentialProceeds.vacancy,
                                 residential_Depreciation = 0,
                                 total_Property_Operational_Expenses = 0,
                                 total_Property_Real_Estate_Taxes=0,
                                 total_Property_Replacement_Reserve=0,
                                 total_Commercial_Income = 0,
                                 total_Commercial_Vacancy=0,
                                 commercial_Depreciation=0,
                                 total_Manufacturing_Income = 0,
                                 total_Manufacturing_Vacancy= 0,
                                 manufacturing_Depreciation = 0)
