import ScheduleFunctions as scheduleHelper


class Schedule:
    '''
    Schedule class that manages the creation of a data column for the proforma

    I. Calculating Flow:
    + 1. Income
    + 2. Expenses
    = 3. NetOperating Income

    5. Annual Debt Service
    6. CASH FLOW AFTER FINANCING
    7. Tax Payment
    8. CASH FLOW AFTER TAXES

    II. Calculating Return Measures:
    1. Total Sales
    2. Unleveraged IRR
    3. Leverahed Before Tax IRR

    III. OFFSHEET CALCLULATION
    1. Debt Service Components
    2. Tax Payment

    '''

    num_of_proformas = 0

    def __init__(self,
                 proforma_name,
                 potential_gross_income,
                 vacancy,
                 operating_expenses,
                 real_estate_taxes,
                 replacement_reserve,
                 income_total,
                 expense_total,
                 effective_gross_income,
                 endYear_total_expenses,
                 debt,
                 debt_service,
                 cashFlowAfterFinancing,
                 tax_payment,
                 salePrice,
                 saleExpense,
                 net_proceeds_fromSale,
                 beginYearBalance,
                 interest,
                 amortization,
                 depreciation,
                 odinaryTaxIncome,
                 amortizationValues,
                 net_sale_price,
                 total_development_cost):

        Schedule.num_of_proformas += 1
        # Global
        self.proforma_name = proforma_name

        # Income inputs
        self.potential_gross_income = potential_gross_income
        self.vacancy = vacancy

        yearly_income = scheduleHelper.income(potential_gross_income, vacancy)

        # Expense inputs
        self.operating_expenses = operating_expenses
        self.real_estate_taxes = real_estate_taxes
        self.replacement_reserve = replacement_reserve

        yearly_expenses = scheduleHelper.expenses(operating_expenses, real_estate_taxes, replacement_reserve)

        # Operating Income
        self.income_Total = income_total
        self.expense_total = expense_total
        self.effective_gross_income = effective_gross_income
        self.endYear_total_expenses = endYear_total_expenses

        yearly_operating_income = scheduleHelper.net_operating_income(income_total, expense_total)
        endYear_net_operating_income = scheduleHelper.endYear_net_operating_income(effective_gross_income,
                                                                                   endYear_total_expenses)

        # Debt Service
        self.debt = debt
        self.debt_service = debt_service

        my_annual_debt_service = scheduleHelper.annual_debt_service(debt, debt_service)

        # Cash flow
        self.tax_payment = tax_payment

        my_operating_income = yearly_income + yearly_expenses

        my_caFT = scheduleHelper.cash_flow_after_taxes(operating_income = my_operating_income,
                                                           annual_dbs = 100,
                                                           tax_payment = tax_payment)


        ############################################
        # Return Measures
        ############################################

        self.salePrice = salePrice
        self.saleExpense = saleExpense

        scheduleHelper.total_sales(salePrice, saleExpense)

        self.cashFlowAfterFinancing = cashFlowAfterFinancing
        self.net_proceeds_fromSale = net_proceeds_fromSale

        yearBeforeSale = False #TODO connect with for loop logic

        my_unleveragedIRR = scheduleHelper.unleveraged_irr( cashFlowAfterFinancing,
                                        tax_payment,
                                        net_proceeds_fromSale,
                                        yearBeforeSale)

        my_future_cash_flow = scheduleHelper.leveraged_before_taxIRR(total_cashFlow_afterTaxes = my_caFT,
                                                                     net_proceeds_fromSale = net_proceeds_fromSale)

        ############################################
        # Offsheet Calculation
        ############################################
        self.beginYearBalance = beginYearBalance
        self.interest = interest
        self.amortization = amortization
        self.depreciation = depreciation
        self.odinaryTaxIncome = odinaryTaxIncome
        self.amortizationValues = amortizationValues

        myAmortizationCalculator = scheduleHelper.debt_service_components(beginYearBalance = beginYearBalance,
                                               endYearBalance = beginYearBalance,
                                               interest = interest ,
                                               ammortization = amortization)

        my_taxPayment = scheduleHelper.tax_paymentScheduler(cashFlowAfterFinancing = my_caFT,
                                            amortization = amortization,
                                            replacementReserve = replacement_reserve,
                                            depreciation = depreciation,
                                            ordinaryTaxIncome = odinaryTaxIncome )

        scheduleHelper.total_amortization(amortizationValues)

        ##########Totals ################
        self.net_sale_price = net_sale_price
        self.total_development_cost = total_development_cost
        total_replacement_reserves = 0 #TODO tie it to the function

        scheduleHelper.net_sale_price(total_development_cost= total_development_cost,
                                      total_replacement_reserves= total_replacement_reserves)

# testSchedule = Schedule(profoma_name = "myProforma",
#                         potential_gross_income= 1000000,
#                         vacancy=100,
#                              operating_expenses,
#                              real_estate_taxes,
#                              replacement_reserve,
#                              income_total,
#                              expense_total,
#                              effective_gross_income,
#                              endYear_total_expenses,
#                              debt,
#                              debt_service)
