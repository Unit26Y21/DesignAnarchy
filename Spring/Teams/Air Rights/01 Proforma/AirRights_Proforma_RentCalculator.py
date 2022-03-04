 #defining Rent can be a culmination of number of units and rent charged per UnitType
    #AMI= AreaMediumIncome
    ##Source for average price per MarketRate DwellingType:
    #https://www.elliman.com/resources/siteresources/commonresources/static%20pages/images/corporate-resources/q3_2021/rental-09_2021.pdf

    ##Cost per sqft:
constructionCostAffordable = 350
constructionCostMarket = 500

    ##DwellingTypes Constants##
        #Determined by NYC HPD %AMI:
        #https://www1.nyc.gov/site/hpd/services-and-information/area-median-income.page

    #MicroUnitsRent:
coLivingAffordableRent = (19, 598, 777) #30-50%AMI
coLivingMarketRent = (956, 1135, 1314) #60-90%AMI

    #MicroUnitsArea (sqft):
coLivingAffordableArea = 300
CoLivingMarketArea = 300

    #StudioUnitsRent:

studioExtAffordableRent = (419) #0-30%AMI
studioSeniorAffordableRent = (419, 598) #30-40%AMI
studioAffordableRent = (598, 777, 956, 1135, 1314) #40-80%AMI
studioSeniorMarketRent = (956, 1135, 1314) #60-80%AMI
studioMarketRent = (1547, 1726, 1905, 2084, 2263, 2889) #90-165%AMI

    #StudioUnitsArea (sqft):

studioExtAffordableArea= 250 #no kitchen
studioSeniorAffordableArea = 400
studioAffordableArea = 400
studioSeniorMarketArea = 400
studioMarketArea = 400

    #1BrUnitsRent:

bdrm1ExtAffordableRent = (532) #0-30%AMI
bdrm1SeniorAffordableRent = (532, 756) #30-40%AMI
bdrm1AffordableRent = (756, 980, 1204, 1427, 1651) #40-80%AMI
bdrm1SeniorMarketRent = (1204, 1427, 1651) #60-80%AMI
bdrm1MarketRent = (1942, 2166, 2390, 2614, 2838, 3621) #90-165%AMI

    #Bdrm1UnitsArea (sqft):

bdrm1ExtAffordableArea = 600
bdrm1SeniorAffordableArea = 700
bdrm1AffordableArea = 700
bdrm1SeniorMarketArea = 700
bdrm1MarketArea = 700

    #Bdrm2UnitsRent:

bdrm2ExtAffordableRent = (631)  # 0-30%AMI
bdrm2SeniorAffordableRent = (631, 900)  # 30-40%AMI
bdrm2AffordableRent = (900, 1168, 1437, 1705, 1947)  # 40-80%AMI
bdrm2SeniorMarketRent = (1437, 1705, 1974)  # 60-80%AMI
bdrm2MarketRent = (2323, 2592, 2860, 3129, 3397, 4337)  # 90-165%AMI

    #Bdrm2UnitsArea (sqft): 870

bdrm2ExtAffordableArea = 870
bdrm2SeniorAffordableArea = 870
bdrm2AffordableArea = 870
bdrm2SeniorMarketArea = 870
bdrm2MarketArea = 870

    #Bdrm3Units:

bdrm3ExtAffordableRent = (722)  # 0-30%AMI (722) These might not be profitable
bdrm3AffordableRent = (1032, 1343, 1653, 1963, 2273)  # 40-80%AMI
bdrm3MarketRent = (2677, 2987, 3297, 3608, 3918, 5004)  # 90-165%AMI

    #bdrm3UnitArea (sqft): 1100

bdrm3ExtAffordableArea = 1100
bdrm3AffordableArea = 1100
bdrm3MarketArea = 1100



    #def SumofRent [(NumUnitA * PricePerUnitA1),

    #def DevelopmentMix, 80:20 (Market v Affordable)