
# Global Constants
constructionCostPerSqFt = 362
studioSqFt = 400
oneBedroomSqFt = 575
twoBedroomSqFt = 775
threeBedroomSqFt = 950
numberStudios = 20
numberOneBedrooms = 20
numberTwoBedrooms = 40
numberThreeBedrooms = 20
affordableRentPerSqft = 1
marketRentPerSqft = 3
principlePercent = 0.003
interestPercent = 0.002

def userInput():
    userInput = input("What percentage of housing would you like to be affordable? ")
    userInputNumber = int(userInput)

    tidsProforma(userInputNumber)


def tidsProforma(userInputNumberAffordable):
    print("Towers In The ProForma - Soup")
    print("ProForma")

    percentAffordable = userInputNumberAffordable
    percentMarketRate = 100 - percentAffordable

    development_totalSqFt = totalSqft()
    affordable_totalSqFt = totalAffordableSqft(development_totalSqFt, percentAffordable)
    market_totalSqFt = totalMarketSqft(development_totalSqFt, percentMarketRate)
    construction_expenses = totalConstructionExpense(development_totalSqFt, constructionCostPerSqFt)
    principal_interest = annualPrincipleAndInterest(construction_expenses, principlePercent, interestPercent)
    affordable_rent = affordableRent(affordable_totalSqFt, affordableRentPerSqft)
    market_rent = marketRent(market_totalSqFt, marketRentPerSqft)
    total_rent_income = totalRentalIncome(affordable_rent, market_rent)
    profitability_output = profitability(total_rent_income, principal_interest)

    print("######"*10)
    print("Amount of percent affordable: " + str(percentAffordable) + "%")
    print("Amount of market rate: {0}%".format(percentMarketRate))
    print("Amount of affordable -> {0}% | Amount of market rate -> {1}%".format(percentAffordable, percentMarketRate))
    print(development_totalSqFt)
    print("######" * 10)
    print("The profitability output of your development is: {0}".format(profitability_output))

    return profitability_output

def totalSqft():
    #Python Collection
    #{} or [] or ()
    return (studioSqFt * numberStudios) + (oneBedroomSqFt * numberOneBedrooms) + (twoBedroomSqFt * numberTwoBedrooms)
    (threeBedroomSqFt * numberThreeBedrooms)


def numberOfUnits():
    return numberStudios + numberOneBedrooms + numberTwoBedrooms + numberThreeBedrooms


def totalAffordableSqft(total_sqft,percentAffordable):
    return total_sqft * percentAffordable/100


def totalMarketSqft(total_sqft,percentMarketRate):
    return total_sqft * percentMarketRate/100


def totalConstructionExpense(total_sqft, constructionCostPerSqFt):
    return total_sqft * constructionCostPerSqFt


def annualPrincipleAndInterest(total_construction_expense, principlePercent, interestPercent):
    return (total_construction_expense * principlePercent) + (total_construction_expense * interestPercent)


def affordableRent(affordable_sqft, affordableRentPerSqft):
    return affordable_sqft * affordableRentPerSqft


def marketRent(market_sqft, marketRentPerSqft):
    return market_sqft * marketRentPerSqft


def totalRentalIncome(affordable_rent, market_rent):
    return affordable_rent + market_rent


def profitability(total_rental_income, annual_principle_and_interest):
    return (total_rental_income * 12) - annual_principle_and_interest


