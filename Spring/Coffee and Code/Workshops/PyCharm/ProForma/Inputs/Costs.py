import CostHelper


class DevelopmentCosts():

    currency = "USD"
    residential_Cost = 500  # $ per sqft
    commercial_Cost = 500  # $ per sqft
    manufacturing_Cost = 500  # $ per sqft
    hardCost = 200  # $ per sqft
    softCost = 200  # $ per sqft
    landCost = 0  # $ per sqft
    existingBuildingPurchase = 0  # flat purchase price

    def __init__(self,
                 gross_ZFA,
                 residential_ZFA,
                 commercial_ZFA,
                 manufacturing_ZFA,
                 ):

        # Development Costs
        self.gross_ZFA = gross_ZFA
        self.residential_ZFA = residential_ZFA
        self.commerical_ZFA = commercial_ZFA
        self.manufacturing_ZFA = manufacturing_ZFA

        print("")
        print("My development costs ({})".format(self.currency))

        my_residential_costs = CostHelper.ResidentialCost(residZFA= residential_ZFA,
                                                      residCost= self.residential_Cost)

        my_commercial_costs = CostHelper.CommercialCost(comZFA= commercial_ZFA,
                                                        comCost= self.commercial_Cost)

        my_manufacturing_costs = 0

        my_hard_costs = CostHelper.HardCost(myTotalGZFA= gross_ZFA,
                                            hardCost= self.hardCost)

        my_soft_costs = CostHelper.SoftCost(myTotalGZFA= gross_ZFA,
                                            softCost= self.softCost)

        total_development_costs = CostHelper.TotalDevelopmentCost(myBuildingPurchase = self.existingBuildingPurchase,
                                                                  mytotalResidCost= my_residential_costs,
                                                                  mytotalComCost= my_commercial_costs,
                                                                  mytotalManCost= my_manufacturing_costs,
                                                                  mytotalHardCost= my_hard_costs,
                                                                  mytotalSoftCost= my_soft_costs)

testCosts = DevelopmentCosts(gross_ZFA = 100000,
                  residential_ZFA = 100000,
                  commercial_ZFA = 0,
                  manufacturing_ZFA = 0 )

testCosts.residential_Cost = 1000

print(testCosts.residential_Cost)
