import proforma.ProFormaForm as ProFormaForm
from statistics import mean

myUnits = mean([900,1000,1500])

mySchedule = ProFormaForm.ProForma(verbose= True,
                                   exportToExcel= False,
                                   yrs = 10,
                                   start_year = 2022,
                                   lot_area=637132,
                                   existingBuildingFloorArea=3236891,
                                   existingBuildingPurchase=0,
                                   residential_gross_sqft=2265824, #70%
                                   commercial_gross_sqft= 323689, #10%
                                   manufacturing_gross_sqft=0,
                                   community_gross_sqft=647378, #20%
                                   avgUnitSize_residential=1063, #myUnits #sqft
                                   avgUnitSize_commercial = 5000,
                                   avgUnitSize_manufacturing = 0,
                                   avgUnitSize_community = 10000,
                                   residential_cost= 470,
                                   residential_rent= 7080, #per month... per sqft? 6.6 same for the others
                                   commercial_cost= 400,
                                   commercial_rent= 960, #peryear, persqft
                                   manufacturing_cost= 0,
                                   manufacturing_rent=0,
                                   community_cost= 400,
                                   community_rent = 600, #peryear, persqft
                                   hard_cost= 188,
                                   soft_cost= 282,
                                   land_cost= 23812383)

