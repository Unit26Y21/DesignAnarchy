import CostHelper


class DevelopmentCosts():

    currency = "USD"
    residential_Cost = 250  # $ per sqft
    commercial_Cost = 0  # $ per sqft
    manufacturing_Cost = 0  # $ per sqft
    hardCost = 0  # $ per sqft
    softCost = 0  # $ per sqft
    landCost = 0  # $ per sqft
    existingBuildingPurchase = 0  # flat purchase price
    total_development_cost = 0

    def __init__(self,
                 residential_ZFA: int,
                 commercial_ZFA: int,
                 manufacturing_ZFA: int,
                 ):

        # Development Costs
        self.residential_ZFA = residential_ZFA
        self.commerical_ZFA = commercial_ZFA
        self.manufacturing_ZFA = manufacturing_ZFA


        gross_ZFA = sum([residential_ZFA,commercial_ZFA,manufacturing_ZFA])

        print("")
        print("My development costs ({})".format(self.currency))

        my_residential_costs = CostHelper.ResidentialCost(residZFA= residential_ZFA,
                                                      residCost= self.residential_Cost)

        my_commercial_costs = CostHelper.CommercialCost(comZFA= commercial_ZFA,
                                                        comCost= self.commercial_Cost)

        my_manufacturing_costs = CostHelper.ManufacturingCost(manZFA= manufacturing_ZFA,
                                                              manCost= self.manufacturing_Cost)

        my_hard_costs = CostHelper.HardCost(myTotalGZFA= gross_ZFA,
                                            hardCost= self.hardCost)

        my_soft_costs = CostHelper.SoftCost(myTotalGZFA= gross_ZFA,
                                            softCost= self.softCost)

        self.total_development_cost = CostHelper.TotalDevelopmentCost(myBuildingPurchase = self.existingBuildingPurchase,
                                                                  mytotalResidCost= my_residential_costs,
                                                                  mytotalComCost= my_commercial_costs,
                                                                  mytotalManCost= my_manufacturing_costs,
                                                                  mytotalHardCost= my_hard_costs,
                                                                  mytotalSoftCost= my_soft_costs)


