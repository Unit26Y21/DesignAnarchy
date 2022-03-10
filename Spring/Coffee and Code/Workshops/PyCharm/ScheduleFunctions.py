'''
Scheduling cash flow functions for proforma
functions used in Scheduling Class

credit: htarrido, SSA, CCNY, CUNY
source: Poorvu, William J., and Samuel Plimpton. "Financial analysis of real property investments."
        Harvard Business School (2003).

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
    '''
    Income as the sum of potential gross income and vacancy (usually it is negative)
    '''

    effective_gross_income = {'potential_gross_income': potential_gross_income,
                              'vacancy': -vacancy}

    print("### Income ###")

    pp.pprint(effective_gross_income)
    
    print(json.dumps(effective_gross_income, indent = 4))

    output = sum(effective_gross_income.values())

    print("Income", output)

    return output


def expenses(operating_expenses, real_estate_taxes, replacement_reserve):
    '''
    Expensesas the sum of operating an asset, real estate taxes and replacement reserves

    '''
    total_expenses = {'operating_expenses': operating_expenses,
                      'real_estate_taxes':real_estate_taxes,
                      'replacement_reserve':replacement_reserve}

    print("### Expense ###")

    for k, v in total_expenses:
        print(k, v)

    output = sum(total_expenses.values())

    print("Expenses", output)

    return output


def endYear_net_operating_income(effective_gross_income, endYear_total_expenses):
    return effective_gross_income +  endYear_total_expenses


def net_operating_income(incomeTotal, expense_total):
    '''
    Calculation of the tax effect for a real estate investment involves simply a
    multiplication of the stream of taxable income by the appropriate tax rates of the investor concerned.
    Starting  in  2003,  the  maximum  marginal  tax  rate  is  assumed  to  be  35%  for  ordinary  income  (the
    capital  gains  rate  is  15%).    On  this  basis,  every  dollar  of  losses  will  reduce  taxes  paid  by  35%.    This
    tax  savings  can  then  be  added  back  to  increase  the  total  return,  assuming  that  the  investor  has
    “passive” income to match against the “passive” loss.
    '''

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
    '''
    Annual debt service is the amount paid of the debt multiplied by the debt service
    '''

    debServiceValues = {'debt': debt,
                        'debt_service':debt_service}

    output = -(debt * debt_service)

    for k,v in debServiceValues:
        print(k, v)

    print("Annual Debt Service", output)

    return output


def cash_flow_after_taxes(operating_income, annual_dbs, tax_payment):
    '''
    The  calculation  of  CFAT  is  completed  by  deducting  the  taxes  paid  or
    adding  the  tax  benefit  received  to  the  before-tax  cash  flow.    This  is  equivalent  to  applying  the  tax
    effect  to  the  operating  cash  flow  reduced  by  financial  payments.    For  many  investors,  CFAT  is  the
    appropriate  annual  cash  flow  for  the  evaluation  of  an  equity  investment.

    Cash  flow  after  financing  return  on  equity  or  cash  on  cash  return This  measure  of
    return may be stated thus:
        Cash flow after financing / equity

    Before-tax  cash  flow  +  first  year’s  amortization  return  on  equity This measure is
    defined in the following way:
        Before-tax cash flow + Mortgage principal payment (year 1) / equity
    '''

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
def net_sale_price(total_development_cost, total_replacement_reserves):
    return total_development_cost +  total_replacement_reserves

def total_sales(salePrice, saleExpense):
    '''
    Total sales per year as the sum of sales price and sale expenses
    '''
    
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

    return sum(unleveragedIRR.values())

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
def debt_service_components(beginYearBalance, debtService, interestRate, ammortization):
    print("### Debt Service Components ###")

    endYearBalance = beginYearBalance - debtService
    interest = beginYearBalance - interestRate
    amortization = debtService - interest

    debtComponents = {'beginYearBalance': beginYearBalance,
                  'endYearBalance': endYearBalance,
                  'interest': interest,
                  'ammortization': ammortization
                      }

    for k,v in debtComponents:
        print(k, v)

    return amortization


def tax_paymentScheduler(cashFlowAfterFinancing,
                         amortization,
                         replacementReserve,
                         depreciation,
                         ordinaryTaxIncome):

    taxableIncome = cashFlowAfterFinancing + amortization + -replacementReserve + -depreciation
    taxPayment = taxableIncome * ordinaryTaxIncome

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

    return taxableIncome, taxPayment


def total_amortization(amortizationValues):
    '''
    Amortization is an accounting technique used to periodically lower the book value of a loan or an intangible asset over a set period of time.
    Concerning a loan, amortization focuses on spreading out loan payments over time.
    '''

    return sum(amortizationValues)

