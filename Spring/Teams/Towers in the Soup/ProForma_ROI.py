
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

def tidsProforma(userInputNumber):
    print("Towers In The Soup")
    print("Pro Forma")

    percentAffordable = userInputNumber
    percentMarketRate = 100 - userInputNumber

    development_totalsqft = total_sqft()

    print("######"*10)
    print(percentAffordable, percentMarketRate)
    print(development_totalsqft)
    print("######" * 10)

def total_sqft():
    #Python Collection
    #{} or [] or ()
    return (studioSqFt * numberStudios) + (oneBedroomSqFt * numberOneBedrooms) + (twoBedroomSqFt * numberTwoBedrooms)
    (threeBedroomSqFt * numberThreeBedrooms)

'''
def number_of_units():
    return {numberStudios + numberOneBedrooms + numberTwoBedrooms + numberThreeBedrooms}


def affordable_sqft():
    return{total_sqft() * percentAffordable/100}


def market_sqft():
    return{total_sqft() * percentMarketRate/100}


def total_construction_expense():
    return {total_sqft() * constructionCostPerSqFt}


def annual_principle_and_interest():
    return{(total_construction_expense() * principlePercent) + (total_construction_expense() * interestPercent)}


def affordable_rent():
    return{affordable_sqft() * affordableRentPerSqft}


def market_rent():
    return{market_sqft() * marketRentPerSqft}


def total_rental_income():
    return{affordable_rent() + market_rent()}


def profitability():
    return{(total_rental_income * 12) - annual_principle_and_interest}


userInput = input("What percentage of housing would you like to be affordable?")
userInputNumber = int(userInput)

calculatedValue = profitability(userInputNumber)
print(profitability)
'''