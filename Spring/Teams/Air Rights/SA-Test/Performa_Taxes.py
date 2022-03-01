#Cash Flow After Taxes

#measures to find the  effect of income taxes after setup and before cashflow have been established
#important to real estate to know after taxes
#CFAT  is  determined  by  first  calculating  the  net  taxable  income  and  then  multiplying  by  the  appropriate  tax  rate.

# Python 3 program to find depreciation of the value
# initial value, rate and time are given



# Function to return the depreciation of value
AnnualAmount = 100000
DepreciableYears = 25
def Depreciation(AnnualAmount, DepreciableYears):
    D = (AnnualAmount/DepreciableYears)

    #return D



#Mortgage Interest
#PRI = Period of Interest Rate

AnnualInterestRate = 6
StartingPrincipleBalance = 100000
NumberofPeriodicPayment = 25

def MortgageIntrest(AnnualInterestRate,StartingPrincipleBalance,NumberofPeriodicPayment):
    PIR = (AnnualInterestRate/12)
    PMT = ((StartingPrincipleBalance/(1-(1+PIR)**(-NumberofPeriodicPayment))/PIR))

    #return PMT



#Cash Flow After Taxes
CashFlowfromOperations = 100000
ReplacementReserve = 10000
TaxRate = .10
Depreciation = 3000
MortgageInterest = .0325
MortgageAmortization = 664

def CashFlowAfterTaxes (CashFlowfromOperations,ReplacementReserve,TaxRate,Depreciation,MortgageInterest,MortgageAmortization):
    NetTaxIncome = (CashFlowfromOperations + ReplacementReserve - MortgageInterest - Depreciation)
    Tax = (NetTaxIncome * TaxRate)

    CashFlowAfterFinancing = (CashFlowfromOperations - MortgageInterest)
    CashFlowAfterTaxes = (CashFlowAfterFinancing - Tax)

    return CashFlowAfterTaxes