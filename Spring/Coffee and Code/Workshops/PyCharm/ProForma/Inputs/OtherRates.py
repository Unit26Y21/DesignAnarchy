import pprint as pp

class OtherRates:
    ratesDictionary = { 'annualIncreaseInExpenses' : .02,
                        'annualPublicSubsidiesIncrease' : .02,
                        'capRateAtSale' : .06,
                        'salesExpense' : .05,
                        'ordinaryIncomeTax' : .35,
                        'depreciationRecapture' : .25,
                        'capitalGainsTax' : .2,
                        'discountRate' : 0,
                        'interestRate' : .05,
                        'constantRate': 0.0688
    }


testRates = OtherRates

testRates.ratesDictionary['constantRate'] = 0.08

pp.pprint(testRates.ratesDictionary)