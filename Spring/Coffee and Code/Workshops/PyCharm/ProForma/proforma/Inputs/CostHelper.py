# Helpers to calculate development cost summaries


def land_purchase_cost(land_cost, lot_area):
    total_land_purchase_cost = land_cost * lot_area
    print("---")
    print("Land Cost per SqFt: {:,}".format(land_cost))
    print("Total Land Area Cost: {:,}".format(total_land_purchase_cost))
    return total_land_purchase_cost

def use_cost_calculator(ZFA, cost_per_sqft):
    total_cost_per_sqft = ZFA * cost_per_sqft
    print("---")
    print("Residential Cost per SqFt: {:,}".format(cost_per_sqft))
    print("Total Residential Area Cost: {:,}".format(total_cost_per_sqft))
    return total_cost_per_sqft


def hard_cost(gross_ZFA, hard_cost):
    total_hard_cost = gross_ZFA * hard_cost
    print("---")
    print("Hard Costs per SqFf: {:,}".format(hard_cost))
    print("Total Hard Costs: {:,}".format(hard_cost))
    return total_hard_cost

def soft_cost(gross_ZFA, soft_cost):
    total_soft_cost = gross_ZFA * soft_cost
    print("---")
    print("Soft Costs per SqFf: {:,}".format(soft_cost))
    print("Total Soft Costs: {:,}".format(soft_cost))
    return total_soft_cost

def total_development_cost(existing_building_purchase,  total_residential_cost, total_commercial_cost, total_manufacturing_cost,total_community_cost, total_hard_cost, total_soft_cost):
    totaldev_cost = [existing_building_purchase,
                     total_residential_cost,
                     total_commercial_cost,
                     total_manufacturing_cost,
                     total_community_cost,
                     total_hard_cost,
                     total_soft_cost]

    sum_dev_cost = sum(totaldev_cost)
    print("---")
    print("Total Development Costs: {:,}".format(sum_dev_cost))
    return sum_dev_cost