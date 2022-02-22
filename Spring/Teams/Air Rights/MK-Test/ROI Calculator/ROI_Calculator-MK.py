### 1. Research what is a back of the envelope pro forma (or a simple ROI)
    #Back of envelope is a rough estimate that filters out less desirable deals
### 2 . Write a series of python functions that take inputs used to calculated value and return you a simple ROI .###


#defining the investments can have breakdown of liquid capital, loans, bonds, , etc.
#def Investment (Cash, Loans, Bonds,
#   Incremental Funding: from NYC + HUD, 10-year 2.2 billion dollars starting in 2019)

#defining Rent can be a culmination of number of units and rent charged per UnitType
#AMI= AreaMediumIncome
##Source:
# https://www.elliman.com/resources/siteresources/commonresources/static%20pages/images/corporate-resources/q3_2021/rental-09_2021.pdf
    #SeniorHousing:
        #UnitA1 = SeniorStudioUnitAffordable, PricePerUnitA1 = 30%AMI ----->
            # OR BETTER way to calculate this?? Set a range from 30-100%AMI,
            # Calculate by average household income by district? Doesn't really work for seniors...
        #UnitA2 = SeniorStudioUnitMarket, PricePerUnitA2 = 100%AMI
        #UnitB1 = Senior1BrUnitAffordable, PricePerUnitB1 = 30%AMI
        #UnitB2 = Senior1BrUnitMarket, PricePerUnitB1 = 100%AMI
        #UnitC1 = Senior2BrUnitAffordable, PricePerUnitB1 = 30%AMI
        #UnitC2 = Senior2BrUnitMarket, PricePerUnitB1 = 100%AMI
    #StudioUnits:
        #UnitB1 = StudioAffordable, PricePerUnitB1 =
        #UnitB2 = StudioMarket, PricePerUnitB2 =
        #UnitB3 = StudioCoLivingAffordable, PricePerUnitB3 =
        #UnitB4 = StudioCoLivingMarket, PricePerUnitB4 =
    #1BrUnits:
        #UnitC1 = 1BrAffordable, PricePerUnitC1 =
        #UnitC2 = 1BrMarket, PricePerUnitC2 =
    #2BrUnits:
        #UnitD1 = 2BrAffordable, PricePerUnitD1 =
        #UnitD2 = 2BrMarket, PricePerUnitD2 =
    #3BrUnits:
        #UnitD1 = 3BrAffordable, PricePerUnitE1 =
        #UnitD2 = 3BrMarket, PricePerUnitE2 =

    #def Rent (NumUnitA * PricePerUnit + )

investmentDictionary = {}

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
    print(Investment)


###Creating ROI Calculator###

#Define the Variables#
#Investment = 40000
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
#   social and governance (ESG) criteria used in Socially responsible Investing (SRI)
