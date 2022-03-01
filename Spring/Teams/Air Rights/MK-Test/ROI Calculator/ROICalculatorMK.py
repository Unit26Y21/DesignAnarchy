### 1. Research what is a back of the envelope pro forma (or a simple ROI)
    #Back of envelope is a rough estimate that filters out less desirable deals
### 2 . Write a series of python functions that take inputs used to calculated value and return you a simple ROI .###


#defining the investments can have breakdown of liquid capital, loans, bonds, , etc.
#def Investment (Cash, Loans, Bonds,
#   Incremental Funding: from NYC + HUD, 10-year 2.2 billion dollars starting in 2019)

#defining Rent can be a culmination of number of units and rent charged per UnitType
#AMI= AreaMediumIncome
##Source for average price per MarketRate DwellingType:
# https://www.elliman.com/resources/siteresources/commonresources/static%20pages/images/corporate-resources/q3_2021/rental-09_2021.pdf

##Cost:
ConstructionCostAffordable = 350
ConstructionCostMarket = 500

##Financial Factors:
    #Interest
    #Principle
    #Loans
    #Grants

##DwellingTypes Constants##

    #StudioUnitsRent:

StudioExtAffordable = (0-419) #0-30%AMI (419)
StudioSeniorAffordable = (419-598) #30-40%AMI (419, 598)
StudioCoAffordable = (419-777) #30-50%AMI (419, 598, 777)
StudioAffordable = (420-1314) #40-80%AMI (598, 777, 956, 1135, 1314)
StudioSeniorMarket = (956-1314) #60-80%AMI (956, 1135, 1314)
StudioCoMarket = (956-1547) #60-90%AMI (956, 1135, 1314)
StudioMarket = (1547-2889) #90-165%AMI (1547, 1726, 1905, 2084, 2263, 2889)

    #StudioUnitsArea:

StudioExtAffordableArea= 300 #no kitchen
StudioSeniorAffordableArea = 400
StudioCoAffordableArea = 300
StudioAffordableArea = 400
StudioSeniorMarketArea = 400
StudioCoMarketArea = 300
StudioMarketArea = 400

    #1BrUnitsRent:

Bdrm1ExtAffordable = (0-532) #0-30%AMI (532)
Bdrm1SeniorAffordable = (532-756) #30-40%AMI (532, 756)
Bdrm1Affordable = (756-1651) #40-80%AMI (756, 980, 1204, 1427, 1651)
Bdrm1SeniorMarket = (1204-1651) #60-80%AMI (1204,1427,1651)
Bdrm1MarketRate = (1942-3621) #90-165%AMI (1942, 2166, 2390, 2614, 2838, 3621)

    #Bdrm1UnitsArea:

Bdrm1ExtAffordableArea = 600
Bdrm1SeniorAffordableArea = 700
Bdrm1AffordableArea = 700
Bdrm1SeniorMarketArea = 700
Bdrm1MarketArea = 700

    #Bdrm2UnitsRent:

Bdrm2ExtAffordable = (0 - 631)  # 0-30%AMI (631)
Bdrm2SeniorAffordable = (631 - 900)  # 30-40%AMI (631, 900)
Bdrm2Affordable = (900 - 1947)  # 40-80%AMI (900, 1168, 1437, 1705, 1947)
Bdrm2SeniorMarket = (1437 - 1974)  # 60-80%AMI (1437, 1705, 1974)
Bdrm2Market = (2323 - 4337)  # 90-165%AMI (2323, 2592, 2860, 3129, 3397, 4337)

#Bdrm2UnitsArea: 870

Bdrm2ExtAffordableArea = 870
Bdrm2SeniorAffordableArea = 870
Bdrm2AffordableArea = 870
Bdrm2SeniorMarketArea = 870
Bdrm2MarketArea = 870

#Bdrm3Units: 1100

Bdrm3ExtAffordable = (0 - 722)  # 0-30%AMI (722)
Bdrm3Affordable = (1032 - 2273)  # 40-80%AMI (1032, 1343, 1653, 1963, 2273)
Bdrm3MarketRate = (2677 - 5004)  # 90-165%AMI (2677, 2987, 3297, 3608, 3918, 5004)

#def SumofRent [(NumUnitA * PricePerUnitA1),

#def DevelopmentMix, 80:20 (Market v Affordable)

'''investmentDictionary = {}

###Ownership Investment Variables###
stock= 2000 #Suppose is the value of Housing Authority
business= None
realEstate= 10000 #Suppose is LandValue
objectsCollectibles= None

###Lending Investment Variables###
savingAccount= 5000
bonds= 20000 #Suppose is a loan from BoFA

###Cash Equivalent Investment Variables###
moneyMarket= None


for variable in ["stock", "business", "realEstate", "objectsCollectibles", "savingAccount", "bonds", "moneyMarket"]:
    investmentDictionary[variable] = eval(variable)


def sumOfInvestments (investmentDictionary):
    Investment= sum(investmentDictionary)
    print(Investment)'''


###Creating ROI Calculator###
    #Source: https://www.youtube.com/watch?v=sW-an04-ubI

#Define the Variables#
Investment = 40000
Rent = 700
Loss = 1000

#defining ROI as a rudimentary gauge of an investment’s profitability
def ROI (Investment, Rent, Loss):
    NetProfit = Rent * 12 - Loss
    ROI = (NetProfit/Investment) *100
    print(ROI)

ROI (Investment, Rent, Loss)

#Rate of Return- takes into account the project's time frame

#SROI- Social return on investment, to understand the environmental,
        #social and governance (ESG) criteria used in Socially responsible Investing (SRI)
