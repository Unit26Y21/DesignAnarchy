# Determining Pretax Cash Flow
#NetRevenue Constants:
BaseRentals= 1000000
RentEscalators= 2000
ExpenseReimbursements= 40000
OtherIncome= 2000
Vacancies= 1000
BadDebts= 50000

#Operating Expenses Constants:
RealEstateTaxes=
Administrative=
Insurance=
Utilities=
MainSuppliesTrash=
Repairs=
Replacement=
OtherExpenses=

#Financial Payment Constants:
MortgageInterest=
MortgageAmortization=
LandLeasePayments=
CapitalExpenditures=

NetRevenue= (BaseRentals + RentEscalators + ExpenseReimbursements + OtherIncome) - (Vacancies + BadDebts)
print (NetRevenue)

OperatingExpenses= (RealEstateTaxes + Administrative + Insurance + Utilities + MainSuppliesTrash + Repairs + Replacement + OtherExpenses)
print (OperatingExpenses)

OperationCashFlow= (NetRevenue-OperatingExpenses)
print (OperationCashFlow)

FinancialPayments= (MortgageInterest + MortgageAmortization + LandLeasePayments)
print (FinancialPayments)

CashFlow= (OperationCashFlow- FinancialPayments- CapitalExpenditures)


# Free and Clear Cash Flow represents the total funds available to service debt in the event of a foreclosure
# Capitalizing Free and Clear Cash Flow Constants

CashFlow = 1000000
CapitalizationRate = .11
LoanToValueRatio = .75

initialEquityValue = (CashFlow * LoanToValueRatio)/CapitalizationRate

print (initialEquityValue)