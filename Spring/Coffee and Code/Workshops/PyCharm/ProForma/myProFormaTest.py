import proforma.ProFormaForm as ProFormaForm
from statistics import mean

myUnits = mean([900,1000,1500]) #unit in sqft

# type, sqft, rent
myAMI = { "Coliving Affordable": ['Coliving', 0.1, 325, 1301],
          "Studio Affordable": ['Studio', 0.07, 400, 1593],
          "1-Bed Affordable": ['1-Bed', 0.05, 600, 1626],
          "2-Bed Affordable": ['2-Bed', 0.02, 900, 1951],
          "3-Bed Affordable": ['3-Bed', 0.01, 1175, 2255],
          "Coliving Market": ['Coliving', 0.2, 325, 2302],
          "Studio Market": ['Studio', 0.2, 400, 2782],
          "1-Bed Market": ['1-Bed', 0.2, 600, 2982],
          "2-Bed Market": ['2-Bed', 0.1, 900, 3578],
          "3-Bed Market": ['3-Bed', 0.5, 1175, 4133]
}

#
# # CarPark Legacy
# myProForma = ProFormaForm.ProForma(verbose= True,
#                                    exportToExcel= False,
#                                    yrs = 10,
#                                    start_year = 2022,
#                                    lot_area=0,
#                                    equity = 0.70,
#                                    net_loss_factor= 0.15,
#                                    existingBuildingFloorArea=0,
#                                    existingBuildingPurchase=0,
#                                    landscape_gross_sqft= 1000000,
#                                    residential_gross_sqft= 1900000,
#                                    commercial_gross_sqft=100000,
#                                    manufacturing_gross_sqft=0,
#                                    community_gross_sqft=0,
#                                    avgUnitSize_residential=750,
#                                    avgUnitSize_commercial=3000,
#                                    avgUnitSize_manufacturing=0,
#                                    avgUnitSize_community=0,
#                                    residential_cost=375,
#                                    residential_rent=3600,
#                                    commercial_cost=700,
#                                    commercial_rent=285000,
#                                    manufacturing_cost=0,
#                                    manufacturing_rent=0,
#                                    community_cost=0,
#                                    community_rent=0,
#                                    hard_cost=0,
#                                    soft_cost=0,
#                                    land_cost=0,
#                                    landscape_cost= 150)


# Towers in the soup
# myProForma = ProFormaForm.ProForma(verbose= False,
#                                    exportToExcel= False,
#                                    yrs = 10,
#                                    start_year = 2022,
#                                    lot_area=0,
#                                    equity = 0.70,
#                                    net_loss_factor= 0.15,
#                                    landscape_gross_sqft= 1170892,
#                                    existingBuildingFloorArea=0,
#                                    existingBuildingPurchase=0,
#                                    residential_gross_sqft= 1900000,
#                                    commercial_gross_sqft=100000,
#                                    manufacturing_gross_sqft=0,
#                                    community_gross_sqft=0,
#                                    avgUnitSize_residential=750,
#                                    avgUnitSize_commercial=3000,
#                                    avgUnitSize_manufacturing=0,
#                                    avgUnitSize_community=0,
#                                    residential_cost=375,
#                                    residential_rent=3600,
#                                    commercial_cost=700,
#                                    commercial_rent=285000,
#                                    manufacturing_cost=0,
#                                    manufacturing_rent=0,
#                                    community_cost=0,
#                                    community_rent=0,
#                                    hard_cost=0,
#                                    soft_cost=0,
#                                    land_cost=0,
#                                    landscape_cost= 50,
#                                    residential_AMI=myAMI)

#Air rights
myProForma = ProFormaForm.ProForma(verbose= False,
                                   exportToExcel= False,
                                   yrs = 20,
                                   start_year = 2022,
                                   lot_area=637132,
                                   equity = 0.70,
                                   net_loss_factor= 0.15,
                                   landscape_gross_sqft= 580382,
                                   existingBuildingFloorArea=0,
                                   existingBuildingPurchase=0,
                                   residential_gross_sqft= 2103979,
                                   commercial_gross_sqft=485533,
                                   manufacturing_gross_sqft=0,
                                   community_gross_sqft=161845,
                                   avgUnitSize_residential=680,
                                   avgUnitSize_commercial=475,
                                   avgUnitSize_manufacturing=0,
                                   avgUnitSize_community=905,
                                   residential_cost=470,
                                   residential_rent=2450,
                                   commercial_cost=400,
                                   commercial_rent=19000,
                                   manufacturing_cost=0,
                                   manufacturing_rent=0,
                                   community_cost=400,
                                   community_rent=18100,
                                   hard_cost=312,
                                   soft_cost=134,
                                   land_cost=0,
                                   landscape_cost= 50,
                                   residential_AMI=myAMI)

# myProForma = ProFormaForm.ProForma(verbose= True,
#                                    exportToExcel= False,
#                                    yrs = 10,
#                                    start_year = 2022,
#                                    lot_area=0,
#                                    equity = 0.70,
#                                    net_loss_factor= 0.00,
#                                    existingBuildingFloorArea=0,
#                                    existingBuildingPurchase=0,
#                                    residential_gross_sqft= 2000000,
#                                    commercial_gross_sqft= 0,
#                                    manufacturing_gross_sqft=0,
#                                    community_gross_sqft=0,
#                                    avgUnitSize_residential=680,
#                                    avgUnitSize_commercial = 0,
#                                    avgUnitSize_manufacturing = 0,
#                                    avgUnitSize_community = 0,
#                                    residential_cost= 470,
#                                    residential_rent= 590, #per month, 1000
#                                    commercial_cost= 0,
#                                    commercial_rent= 0,
#                                    manufacturing_cost= 0,
#                                    manufacturing_rent=0,
#                                    community_cost= 0,
#                                    community_rent = 0,
#                                    hard_cost= 0,
#                                    soft_cost= 0,
#                                    land_cost= 0)


