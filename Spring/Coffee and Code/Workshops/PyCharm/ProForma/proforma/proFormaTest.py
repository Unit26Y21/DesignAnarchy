import ProFormaForm
from statistics import mean

myUnits = mean([900,1000,500])

mySchedule = ProFormaForm.ProForma(yrs = 10,
                                   start_year = 2022,
                                   lot_area=11000,
                                   existingBuildingFloorArea=0,
                                   existingBuildingPurchase=0,
                                   residential_gross_sqft= 99000,
                                   commercial_gross_sqft= 0,
                                   manufacturing_gross_sqft=0,
                                   community_gross_sqft=0,
                                   avgUnitSize_residential=myUnits,
                                   avgUnitSize_commercial = 0,
                                   avgUnitSize_manufacturing = 0,
                                   avgUnitSize_community = 0,
                                   residential_cost= 1200,
                                   residential_rent=500,
                                   commercial_cost= 0,
                                   commercial_rent=0,
                                   manufacturing_cost= 0,
                                   manufacturing_rent=0,
                                   community_cost= 0,
                                   community_rent = 0,
                                   hard_cost= 0,
                                   soft_cost= 200,
                                   land_cost= 0)

print('\n')
print(mySchedule.schedule.df.to_string())
print('\n')