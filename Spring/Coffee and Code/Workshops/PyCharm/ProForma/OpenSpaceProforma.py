import proforma.ProFormaForm as ProFormaForm
from statistics import mean



myAMI_1P2 = {'Affordable 1': ['Studio', 0.06,  400, 1150],
          'Affordable 2': ['1-Bed', 0.18, 600, 1250],
          'Affordable 3': ['2-Bed', 0.16, 800, 1500],
          'Market 1': ['Studio', 0.08,  400, 3200],
          'Market 2': ['1-Bed', 0.28, 600, 4000],
          'Market 3': ['2-Bed', 0.24, 800, 5700],
          }

myProFormaP2 = ProFormaForm.ProForma(verbose= False,
                                   exportToExcel= False,
                                   yrs = 3,
                                   start_year = 2032,
                                   lot_area= 839831,
                                   equity = 0.75,
                                   net_loss_factor= 0.15,
                                   landscape_gross_sqft= 47000,
                                   existingBuildingFloorArea=0,
                                   existingBuildingPurchase=0,
                                   residential_gross_sqft= 188000,
                                   commercial_gross_sqft= 49210,
                                   manufacturing_gross_sqft=0,
                                   community_gross_sqft= 24335,
                                   avgUnitSize_residential= 600,
                                   avgUnitSize_commercial= 2000,
                                   avgUnitSize_manufacturing=0,
                                   avgUnitSize_community= 1500,
                                   residential_cost= 375,
                                   residential_rent= 2800,
                                   commercial_cost= 275,
                                   commercial_rent= 120000,
                                   manufacturing_cost=0,
                                   manufacturing_rent=0,
                                   community_cost= 275,
                                   community_rent= 60000,
                                   hard_cost= 206,
                                   soft_cost= 88,
                                   land_cost=1,
                                   landscape_cost= 50,
                                   residential_AMI=myAMI_1P2)

