import proforma.ProFormaForm as ProFormaForm
from statistics import mean

myUnits = mean([900,1000,1500])

mySchedule = ProFormaForm.ProForma(verbose= True,
                                   exportToExcel= False,
                                   yrs = 10,
                                   start_year = 2022,
                                   lot_area=0,
                                   existingBuildingFloorArea=0,
                                   existingBuildingPurchase=0,
                                   residential_gross_sqft= 990000,
                                   commercial_gross_sqft= 1000000,
                                   manufacturing_gross_sqft=0,
                                   community_gross_sqft=0,
                                   avgUnitSize_residential=myUnits,
                                   avgUnitSize_commercial = 0,
                                   avgUnitSize_manufacturing = 0,
                                   avgUnitSize_community = 0,
                                   residential_cost= 400,
                                   residential_rent= 36000, #per year
                                   commercial_cost= 500,
                                   commercial_rent= 90000,
                                   manufacturing_cost= 0,
                                   manufacturing_rent=0,
                                   community_cost= 0,
                                   community_rent = 0,
                                   hard_cost= 200,
                                   soft_cost= 200,
                                   land_cost= 0)

