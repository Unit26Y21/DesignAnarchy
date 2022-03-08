'''
Scheduling cash flow for proforma

'''

############################################
# ProForma Market Rate
############################################

# Income and Expenses
def income(potential_gross_income, vacancy):
    effective_gross_income = [potential_gross_income, vacancy]

    for i in effective_gross_income:
        print(str(i), i)

    return sum(effective_gross_income)


def expenses(operating_expenses, real_estate_taxes, replacement_reserve):
    total_expenses = [operating_expenses, real_estate_taxes, replacement_reserve]

    for i in total_expenses:
        print(str(i), i)

    return sum(total_expenses)


def net_operating_income(incomeTotal, expense_total):
    return incomeTotal + expense_total


# Cash flow and Tax Payments

def annual_debt_service(debt, debt_service):
    a_debt_service = -(debt * debt_service)
    return a_debt_service


def cash_flow_after_taxes(operating_income, annual_dbs, tax_payment):
    cash_flow_after_financing = operating_income + annual_dbs
    caFT = cash_flow_after_financing + -tax_payment  #cash flow after taxes

    return caFT

############################################
# Return Measures
############################################

def total_sales(netOperatingIncome, netSalesPrice):
    totalSales = netSalesPrice + netOperatingIncome
    return

def unleveraged_irr(cashFlowAfterFinancing, beforeTaxSalesProceeds ):
    pass

def leveraged_before_tax_irr(cash_flow_after_taxes, net_proceeds_from_sale):
    pass

############################################
# Offsheet Calculation
############################################
def debt_service_components():
    pass

def tax_paymentScheduler(cashFlowAfterFinancing, amortization, replacementReserve, depreciation,
                         taxableIncome):
    pass