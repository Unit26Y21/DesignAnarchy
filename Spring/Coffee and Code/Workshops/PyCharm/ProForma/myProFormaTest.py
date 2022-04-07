import proforma.ProFormaForm as ProFormaForm
from statistics import mean

myUnits = mean([900,1000,1500]) #unit in sqft

myProForma = ProFormaForm.ProForma(verbose= True,
                                   exportToExcel= False,
                                   yrs = 10,
                                   start_year = 2022,
                                   lot_area=0,
                                   equity = 0.35,
                                   net_loss_factor= 0.09,
                                   existingBuildingFloorArea=0,
                                   existingBuildingPurchase=0,
                                   residential_gross_sqft= 99000,
                                   commercial_gross_sqft= 0,
                                   manufacturing_gross_sqft=0,
                                   community_gross_sqft=0,
                                   avgUnitSize_residential=990,
                                   avgUnitSize_commercial = 0,
                                   avgUnitSize_manufacturing = 0,
                                   avgUnitSize_community = 0,
                                   residential_cost= 250,
                                   residential_rent= 3600, #per month
                                   commercial_cost= 0,
                                   commercial_rent= 0,
                                   manufacturing_cost= 0,
                                   manufacturing_rent=0,
                                   community_cost= 0,
                                   community_rent = 0,
                                   hard_cost= 0,
                                   soft_cost= 0,
                                   land_cost= 0)

