#Cash Flow After Taxes

#measures to find the  effect of income taxes after setup and before cashflow have been established
#important to real estate to know after taxes
#CFAT  is  determined  by  first  calculating  the  net  taxable  income  and  then  multiplying  by  the  appropriate  tax  rate.

# Python 3 program to find depreciation of the value
# initial value, rate and time are given


def Depreciation(annualAmount, depreciableYears):
    """ Depreciation is... """
    depreciation = (annualAmount/depreciableYears)

    return depreciation

def MortgageInterest(annualInterestRate,startingPrincipleBalance,numberofPeriodicPayment):
    """
    Mortgage interest calculator.

    returns PIR and PMT as a tuple (PIR, PMT)

    """
    PIR = (annualInterestRate/12)
    PMT = ((startingPrincipleBalance/(1-(1+PIR)**(-numberofPeriodicPayment))/PIR))

    return (PIR, PMT)


def CashFlowAfterTaxes (CashFlowfromOperations,ReplacementReserve,TaxRate,Depreciation,MortgageInterest,MortgageAmortization):
    NetTaxIncome = (CashFlowfromOperations + ReplacementReserve - MortgageInterest - Depreciation)
    Tax = (NetTaxIncome * TaxRate)

    CashFlowAfterFinancing = (CashFlowfromOperations - MortgageInterest)
    CashFlowAfterTaxes = (CashFlowAfterFinancing - Tax)

    return CashFlowAfterTaxes

# Function to return the depreciation of value
AnnualAmount = 100000
DepreciableYears = 25

testDepreciation = Depreciation(AnnualAmount,DepreciableYears)

#Mortgage Interest
#PRI = Period of Interest Rate

AnnualInterestRate = 6
StartingPrincipleBalance = 100000
NumberofPeriodicPayment = 25

testMortgageInterest = MortgageInterest(annualInterestRate=AnnualInterestRate,
                                        startingPrincipleBalance=StartingPrincipleBalance,
                                        numberofPeriodicPayment=NumberofPeriodicPayment)


#Cash Flow After Taxes
CashFlowfromOperations = 100000
ReplacementReserve = 10000
TaxRate = .10
Depreciation = 3000
MortgageInterest = .0325
MortgageAmortization = 664

testCashFlowAfterTaxes = CashFlowAfterTaxes(CashFlowfromOperations=CashFlowfromOperations,
                                            ReplacementReserve=ReplacementReserve,
                                            TaxRate=TaxRate,
                                            Depreciation=testDepreciation,
                                            MortgageInterest=testMortgageInterest[1],
                                            MortgageAmortization=MortgageAmortization)

print("My depreciation:")
print(testDepreciation)
print("Mortgage Interest")
print(testMortgageInterest)
print("Cash Flow After Taxes")
print(testCashFlowAfterTaxes)