'''
Scheduling cash flow for proforma

functions used in Scheduling Class
'''

import pprint as pp
import json
# def columnConstructor(inputList):
#     inputList = []
#
#     dict = {}
#
#     for i in inputList:
#         dict["'" + i +"'"]= i
#
#     output = sum(futureCashFlow.values())
#
#     for k, v in futureCashFlow:
#         print(k, v)
#
#     print(" Total Future Cash Flow", output)
#
#     return output

############################################
# ProForma Market Rate
############################################

# Income and Expenses
def income(potential_gross_income, vacancy):
    effective_gross_income = {'potential_gross_income': potential_gross_income,
                              'vacancy': vacancy}

    print("### Income ###")

    pp.pprint(effective_gross_income)
    
    print(json.dumps(effective_gross_income, indent = 4))

    output = sum(effective_gross_income.values())

    print("Income", output)

    return output


def expenses(operating_expenses, real_estate_taxes, replacement_reserve):
    total_expenses = {'operating_expenses': operating_expenses,
                      'real_estate_taxes':real_estate_taxes,
                      'replacement_reserve':replacement_reserve}

    print("### Expense ###")

    for k, v in total_expenses:
        print(k, v)

    output = sum(total_expenses.values())

    print("Expenses", output)

    return output


def net_operating_income(incomeTotal, expense_total):

    netOperatingIncome = {'incomeTotal': incomeTotal,
                          'expense_total':expense_total
                          }

    for k,v in netOperatingIncome:
        print(k, v)

    output = sum(netOperatingIncome.values())

    print("Net Operating Income", output)

    return output


# Cash flow and Tax Payments

def annual_debt_service(debt, debt_service):
    debServiceValues = {'debt': debt,
                        'debt_service':debt_service}

    output = -(debt * debt_service)

    for k,v in debServiceValues:
        print(k, v)

    print("Annual Debt Service", output)

    return output


def cash_flow_after_taxes(operating_income, annual_dbs, tax_payment):

    cash_flow_after_financing = operating_income + annual_dbs
    caFT = cash_flow_after_financing + -tax_payment  #cash flow after taxes

    cashFlowDictionary = {'operating_income': operating_income,
              'annual_dbs': annual_dbs,
              'tax_payment': tax_payment,
              'Cash Flow After Finance': cash_flow_after_financing,
              'Cash Flow After Taxes': caFT
              }

    for k,v in cashFlowDictionary:
        print(k, v)

    return caFT

############################################
# Return Measures
############################################

def total_sales(salePrice, saleExpense):
    totalSales = salePrice + saleExpense

    salesDictionary = { 'salePrice': salePrice,
                        'saleExpense':  saleExpense,
                        'totalSales': totalSales
                        }

    for k,v in salesDictionary:
        print(k, v)

    return totalSales

def unleveraged_irr(cashFlowAfterFinancing,
                    taxPayments,
                    net_proceeds_fromSale,
                    yearBeforeSale ):

    beforeTaxSalesProceeds = taxPayments + net_proceeds_fromSale

    if yearBeforeSale:
        unleveragedIRR= { 'Cash Flow After Financing': cashFlowAfterFinancing,
                        'Before Tax Sales Proceeds': beforeTaxSalesProceeds
                          }
    else:
        unleveragedIRR = {'Cash Flow After Financing': cashFlowAfterFinancing,
                          'Before Tax Sales Proceeds': cashFlowAfterFinancing
                          }

    return unleveragedIRR

def leveraged_before_taxIRR(total_cashFlow_afterTaxes, net_proceeds_fromSale):

    futureCashFlow = { 'Total Cash Flow After Taxes': total_cashFlow_afterTaxes,
                       'Net Proceeds From Sale': net_proceeds_fromSale
                       }

    output = sum(futureCashFlow.values())

    for k, v in futureCashFlow:
        print(k, v)

    print(" Total Future Cash Flow", output)

    return output

############################################
# Offsheet Calculation
############################################
def debt_service_components(beginYearBalance, endYearBalance, interest, ammortization):
    print("### Debt Service Components ###")

    debtComponents = {'beginYearBalance': beginYearBalance,
                  'endYearBalance': endYearBalance,
                  'interest': interest,
                  'ammortization': ammortization
                      }

    for k,v in debtComponents:
        print(k, v)



def tax_paymentScheduler(cashFlowAfterFinancing,
                         amortization,
                         replacementReserve,
                         depreciation,
                         ordinaryTaxIncome):

    taxableIncome = cashFlowAfterFinancing + amortization + -replacementReserve + -depreciation
    taxPayment = taxableIncome* ordinaryTaxIncome

    print("### Tax Payment ###")

    taxPaymentLineItems = {'cashFlowAfterFinancing': cashFlowAfterFinancing,
                           'amortization': amortization,
                           'replacementReserve': replacementReserve,
                           'depreciation': depreciation,
                           'ordinaryTaxIncome': ordinaryTaxIncome,
                           'taxableIncome': taxableIncome,
                           'taxPayment': taxPayment
                           }

    for k, v in taxPaymentLineItems:
        print(k, v)


def total_amortization(amortizationValues):
    return sum(amortizationValues)

