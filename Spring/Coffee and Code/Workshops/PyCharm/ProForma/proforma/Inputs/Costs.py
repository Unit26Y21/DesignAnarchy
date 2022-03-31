from proforma.Inputs  import CostHelper


class development_costs():

    currency = "USD"
    total_development_cost = 0

    def __init__(self,
                 residential_ZFA: int,
                 commercial_ZFA: int,
                 manufacturing_ZFA: int,
                 community_ZFA: int,
                 residential_cost: int,
                 commercial_cost: int,
                 manufacturing_cost: int,
                 community_cost: int,
                 hard_cost: int,
                 soft_cost: int,
                 land_cost: int,
                 existingBuildingPurchase: int
                 ):

        # Development Costs
        self.residential_ZFA = residential_ZFA
        self.commerical_ZFA = commercial_ZFA
        self.manufacturing_ZFA = manufacturing_ZFA
        self.community_ZFA = community_ZFA
        self.residential_cost = residential_cost  # $ per sqft
        self.commercial_cost = commercial_cost  # $ per sqft
        self.manufacturing_cost = manufacturing_cost  # $ per sqft
        self.community_cost = community_cost
        self.hard_cost = hard_cost  # $ per sqft
        self.soft_cost = soft_cost  # $ per sqft
        self.land_cost = land_cost  # $ per sqft
        self.existingBuildingPurchase = existingBuildingPurchase # flat purchase price


        gross_ZFA = sum([residential_ZFA,commercial_ZFA,manufacturing_ZFA])

        print("")
        print("My development costs ({})".format(self.currency))

        my_residential_costs = CostHelper.use_cost_calculator(ZFA= residential_ZFA,
                                                              cost_per_sqft= self.residential_cost)

        my_commercial_costs = CostHelper.use_cost_calculator(ZFA= commercial_ZFA,
                                                        cost_per_sqft= self.commercial_cost)

        my_manufacturing_costs = CostHelper.use_cost_calculator(ZFA= manufacturing_ZFA,
                                                              cost_per_sqft= self.manufacturing_cost)

        my_community_costs = CostHelper.use_cost_calculator(ZFA = community_ZFA,
                                                            cost_per_sqft= self.community_cost)

        my_hard_costs = CostHelper.hard_cost(gross_ZFA= gross_ZFA,
                                            hard_cost= self.hard_cost)

        my_soft_costs = CostHelper.soft_cost(gross_ZFA= gross_ZFA,
                                            soft_cost= self.soft_cost)

        self.total_development_cost = CostHelper.total_development_cost(existing_building_purchase = self.existingBuildingPurchase,
                                                                      total_residential_cost= my_residential_costs,
                                                                      total_commercial_cost= my_commercial_costs,
                                                                      total_manufacturing_cost= my_manufacturing_costs,
                                                                      total_community_cost= my_community_costs,
                                                                      total_hard_cost= my_hard_costs,
                                                                      total_soft_cost= my_soft_costs)


