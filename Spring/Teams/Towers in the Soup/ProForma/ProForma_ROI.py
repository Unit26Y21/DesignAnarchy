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
i = .03
n = 12

def userInput():
    userInput = input("What percentage of housing would you like to be affordable? ")
    try:
        userInputNumber = int(userInput)
        if 0 < userInputNumber < 100:
            return tidsProforma(userInputNumber)
        elif userInputNumber > 100:
            print("You can't have more than 100% of anything. Who taught you math?")
        elif userInputNumber == 0:
            print("Why did you enter zero? Do you hate poor people?")
        elif userInputNumber < 0:
            print("You entered a negative number. That's not possible.")
    except ValueError:
        print("You didn't put and integer... Stop Trying to break my program!")

def tidsProforma(userInputNumberAffordable):
    print("Towers In The Soup")
    print("Pro Forma")

    percentAffordable = userInputNumberAffordable
    percentMarketRate = 100 - percentAffordable

    development_totalSqFt = totalSqft()
    affordable_totalSqFt = totalAffordableSqft(development_totalSqFt, percentAffordable)
    market_totalSqFt = totalMarketSqft(development_totalSqFt, percentMarketRate)
    construction_expenses = totalConstructionExpense(development_totalSqFt, constructionCostPerSqFt)
    affordable_rent = affordableRent(affordable_totalSqFt, affordableRentPerSqft)
    market_rent = marketRent(market_totalSqFt, marketRentPerSqft)
    total_rent_income = totalRentalIncome(affordable_rent, market_rent)
    payment_output = annualFinancingPayment(construction_expenses, i, n)
    profitability_output = profitability(total_rent_income, payment_output)

    print("######"*10)
    print("Amount of percent affordable: " + str(percentAffordable) + "%")
    print("Amount of market rate: {0}%".format(percentMarketRate))
    print("Amount of affordable -> {0}% | Amount of market rate -> {1}%".format(percentAffordable, percentMarketRate))
    print(development_totalSqFt)
    print("######" * 10)
    print("The profitability output of your development is: {0}".format(profitability_output))
    print("annual payments are: {0}" .format(payment_output))
    print(total_rent_income * 12)

def totalSqft():
    #Python Collection
    #{} or [] or ()
    return (studioSqFt * numberStudios) + (oneBedroomSqFt * numberOneBedrooms) + (twoBedroomSqFt * numberTwoBedrooms) + (threeBedroomSqFt * numberThreeBedrooms)


def numberOfUnits():
    return numberStudios + numberOneBedrooms + numberTwoBedrooms + numberThreeBedrooms


def totalAffordableSqft(total_sqft,percentAffordable):
    return total_sqft * percentAffordable/100


def totalMarketSqft(total_sqft,percentMarketRate):
    return total_sqft * percentMarketRate/100


def totalConstructionExpense(total_sqft, constructionCostPerSqFt):
    return total_sqft * constructionCostPerSqFt


def annualFinancingPayment(construction_expenses, i, n):
    return construction_expenses/(1 + pow((1 + i), -n) / i)
    #annual financing payment for loan + principle


def affordableRent(affordable_sqft, affordableRentPerSqft):
    return affordable_sqft * affordableRentPerSqft


def marketRent(market_sqft, marketRentPerSqft):
    return market_sqft * marketRentPerSqft


def totalRentalIncome(affordable_rent, market_rent):
    return affordable_rent + market_rent


def profitability(total_rental_income, payment_output):
    return (total_rental_income * 12) - payment_output