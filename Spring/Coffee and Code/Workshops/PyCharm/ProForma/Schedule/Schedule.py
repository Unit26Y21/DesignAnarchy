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
                 potential_gross_income,
                 vacancy,
                 operating_expenses,
                 real_estate_taxes,
                 replacement_reserve,
                 debt,
                 debt_service,
                 net_proceeds_fromSale,
                 beginYearBalance,
                 interestRate,
                 depreciation,
                 odinaryTaxIncome,
                 amortizationValues,
                 gain_sale_price,
                 gain_sale_expenses,
                 total_development_cost):

        Schedule.num_of_proformas += 1

        ############################################
        # Offsheet Calculation
        ############################################
        self.beginYearBalance = beginYearBalance
        self.interestRate = interestRate
        self.depreciation = depreciation
        self.odinaryTaxIncome = odinaryTaxIncome
        self.amortizationValues = amortizationValues

        amortization = debt_service - interestRate

        myAmortizationCalculator = scheduleHelper.debt_service_components(beginYearBalance=beginYearBalance,
                                                                          debtService= debt_service,
                                                                          interestRate = interestRate,
                                                                          ammortization = amortization)

        scheduleHelper.total_amortization(amortizationValues)

        ##########Totals ################
        self.total_development_cost = total_development_cost
        total_replacement_reserves = 0  # TODO tie it to the function

        net_sale_price = scheduleHelper.net_sale_price(total_development_cost=total_development_cost,
                                      total_replacement_reserves=total_replacement_reserves)

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

        yearly_operating_income = scheduleHelper.net_operating_income(yearly_income, yearly_expenses)
        endYear_net_operating_income = scheduleHelper.endYear_net_operating_income(yearly_income,
                                                                                   yearly_expenses)

        # Debt Service
        self.debt = debt
        self.debt_service = debt_service

        my_annual_debt_service = scheduleHelper.annual_debt_service(debt, debt_service)

        # Cash flow
        my_caFF =  endYear_net_operating_income + my_annual_debt_service

        my_operating_income = yearly_income + yearly_expenses

        annual_dbs = debt * debt_service

        tax_payment = scheduleHelper.tax_paymentScheduler(cashFlowAfterFinancing=my_caFF,
                                                         amortization = amortization,
                                                         replacementReserve=replacement_reserve,
                                                         depreciation=depreciation,
                                                         ordinaryTaxIncome=odinaryTaxIncome)

        my_caFT = scheduleHelper.cash_flow_after_taxes(operating_income = my_operating_income,
                                                           annual_dbs = annual_dbs,
                                                           tax_payment = tax_payment)



        ############################################
        # Return Measures
        ############################################

        # self.salePrice = salePrice
        # self.saleExpense = saleExpense
        #
        # scheduleHelper.total_sales(salePrice, saleExpense)
        #
        # self.net_proceeds_fromSale = net_proceeds_fromSale
        #
        yearBeforeSale = False #TODO connect with for loop logic

        my_unleveragedIRR = scheduleHelper.unleveraged_irr( my_caFF,
                                                            tax_payment,
                                                            net_proceeds_fromSale,
                                                            yearBeforeSale)

        my_future_cash_flow = scheduleHelper.leveraged_before_taxIRR(total_cashFlow_afterTaxes = my_caFT,
                                                                     net_proceeds_fromSale = net_proceeds_fromSale)

