import pandas as pd

class ScheduleGrid:

    pd.options.display.float_format = '${:,}'.format
    # pd.options.display.
    yrs = 10
    startYear = 2022
    schedule_dates = pd.Series(pd.date_range(start=str(startYear), periods=yrs, freq= 'YS')).dt.year

    rows = ['Income',
            'Potential Gross Income',
            'Vacancy',
            'Effective Gross Income',
            ' ',
            'Expenses',
            'Operating Expenses',
            'Real Estate Taxes',
            'Replacement Reserve',
            'Total Expenses',
            ' ',
            'NET OPERATING INCOME',
            ' ',
            'Annual Debt Service',
            'Cash flow after financing',
            'Tax Payment',
            'Cash flow after taxes',
            ' ',
            'RETURN MEASURES',
            'Unleveraged IRR', 'Cash Flow After Financing', 'Before Tax Sales Proceed',
            ' ',
            'Leverahed Before Tax IRR', 'Cash Flow After Taxes', 'Net Procceeds form Sale', 'Total Future Cash Flow',
            ]

    offsheet_rows = [' ',
            'OFFSHEET CALCLULATION',
            'Debt Service Components',
            'Beginning of Year Balance',
            'End of Year Balance',
            'Interest',
            'Ammortization',
            ' ',
            'TAX PAYMENT',
            'Cash Flow After Financing',
            'Amortization',
            'Replacement Reserve',
            'Depreciation',
            'Taxable Income',
            'Tax Payment'
            ]

    df = pd.DataFrame(index=rows, columns=schedule_dates)
    offsheet_df = pd.DataFrame(index=offsheet_rows, columns=schedule_dates)

    df.loc['Income', 'Expenses', 'RETURN MEASURES',
           'Unleveraged IRR', 'Leverahed Before Tax IRR',' '] = ' '

    offsheet_df.loc['OFFSHEET CALCLULATION', 'Debt Service Components', 'TAX PAYMENT',' '] = ' '


    def __init__(self,
                 total_gross_income: int,
                 total_vacancy: int,
                 operating_expenses: int,
                 real_estate_taxes: int,
                 replacement_reserve: int,
                 debt: int,
                 debt_service: int,
                 debt_service_rate: float,
                 net_proceeds_fromSale: int,
                 beginYearBalance: int,
                 interestRate: int,
                 depreciation: int,
                 odinaryTaxIncome: float,
                 amortizationValues: int,
                 gain_sale_price: int,
                 gain_sale_expenses: int,
                 total_development_cost: int,
                 total_future_cashflow_atStart: int,
                 annual_public_subsidy_increase: float
                 ):

        for i in range(0, len(self.df.columns)):
            ### #FIRST ROW
            if i == 0:
                # Income
                self.df.iat[1, i] = total_gross_income
                self.df.iat[2, i] = total_vacancy
                self.df.iat[3, i] = sum([total_gross_income, total_vacancy])  # effective gross income

                # Expenses
                self.df.iat[6, i] = -operating_expenses
                self.df.iat[7, i] = -real_estate_taxes
                self.df.iat[8, i] = -replacement_reserve
                self.df.iat[9, i] = -sum([operating_expenses, real_estate_taxes, replacement_reserve])  # total expenses

                # Net Operating Income & Others
                net_operating_income = sum([self.df.iat[9, i], self.df.iat[3, i]])
                self.df.iat[11, i] = net_operating_income  # Net Operating Income

                annual_debt_service = round(-(debt * debt_service_rate), 2)  # annual debt service
                self.df.iat[13, i] = annual_debt_service

                cash_flow_after_financing = round(sum([net_operating_income, annual_debt_service]),
                                                  2)  # cash flow after financing
                self.df.iat[14, i] = cash_flow_after_financing

                # OffSheet Calculations
                self.offsheet_df.iat[3, i] = beginYearBalance  # begin of year balance

                end_year_balance = beginYearBalance - debt_service  # end of year balance
                self.offsheet_df.iat[4, i] = end_year_balance

                interest = round(beginYearBalance * interestRate, 2)  # interest
                self.offsheet_df.iat[5, i] = interest

                ammortization = round(debt_service - interest, 2)
                self.offsheet_df.iat[6, i] = ammortization

                self.offsheet_df.iat[9, i] = cash_flow_after_financing
                self.offsheet_df.iat[10, i] = ammortization
                self.offsheet_df.iat[11, i] = replacement_reserve
                self.offsheet_df.iat[12, i] = depreciation

                taxable_income = round(
                    sum([cash_flow_after_financing, ammortization, replacement_reserve, depreciation]), 2)
                self.offsheet_df.iat[13, i] = taxable_income

                tax_payment = round(taxable_income * odinaryTaxIncome, 2)
                self.offsheet_df.iat[14, i] = tax_payment

                # Operatin Income Part 2
                self.df.iat[15, i] = tax_payment

                cash_flow_after_taxes = cash_flow_after_financing - tax_payment
                self.df.iat[16, i] = cash_flow_after_taxes

                # Return Measures
                # Unleveraged
                self.df.iat[20, i] = cash_flow_after_financing
                self.df.iat[21, i] = cash_flow_after_financing

                # Leveraged
                self.df.iat[24, i] = cash_flow_after_taxes
                self.df.iat[25, i] = 0
                self.df.iat[26, i] = sum([self.df.iat[24, i], self.df.iat[25, i]])

            else:
                #Other rows
                annual_subsidy_adjust = 1 + annual_public_subsidy_increase

                # Income
                self.df.iat[1, i] = round(self.df.iat[1, i - 1] * annual_subsidy_adjust, 2)
                self.df.iat[2, i] = round(self.df.iat[2, i - 1] * annual_subsidy_adjust, 2)
                self.df.iat[3, i] = round(sum([self.df.iat[1, i], self.df.iat[2, i]]), 2)  # effective gross incom

                #Expenses
                # Expenses
                self.df.iat[6, i] = round(self.df.iat[6, i - 1] * annual_subsidy_adjust, 2)
                self.df.iat[7, i] = round(self.df.iat[7, i - 1] * annual_subsidy_adjust, 2)
                self.df.iat[8, i] = round(self.df.iat[8, i - 1] * annual_subsidy_adjust, 2)
                self.df.iat[9, i] = round(sum([self.df.iat[6, i], self.df.iat[7, i], self.df.iat[8, i]]), 2)  # total expenses

                # Net Operating Income & Others
                net_operating_income = round(sum([self.df.iat[9, i], self.df.iat[3, i]]), 2)
                self.df.iat[11, i] = net_operating_income  # Net Operating Income

                annual_debt_service = round(-(debt * debt_service_rate), 2)  # annual debt service
                self.df.iat[13, i] = annual_debt_service

                cash_flow_after_financing = round(sum([net_operating_income, annual_debt_service]),
                                                  2)  # cash flow after financing

                self.df.iat[14, i] = cash_flow_after_financing

                # OffSheet Calculations
                beginYearBalance = self.offsheet_df.iat[4,i-1]
                self.offsheet_df.iat[3, i] = beginYearBalance # begin of year balance

                end_year_balance = beginYearBalance - debt_service  # end of year balance
                self.offsheet_df.iat[4, i] = end_year_balance

                interest = round(beginYearBalance * interestRate, 2)  # interest
                self.offsheet_df.iat[5, i] = interest

                ammortization = round(debt_service - interest, 2)
                self.offsheet_df.iat[6, i] = ammortization

                self.offsheet_df.iat[9, i] = cash_flow_after_financing
                self.offsheet_df.iat[10, i] = ammortization

                replacement_reserve = round(self.offsheet_df.iat[11, i-1] * annual_subsidy_adjust, 2)
                self.offsheet_df.iat[11, i] = replacement_reserve
                self.offsheet_df.iat[12, i] = depreciation

                taxable_income = round(
                    sum([cash_flow_after_financing, ammortization, replacement_reserve, depreciation]), 2)
                self.offsheet_df.iat[13, i] = taxable_income

                tax_payment = round(taxable_income * odinaryTaxIncome, 2)
                self.offsheet_df.iat[14, i] = tax_payment

                # Operatin Income Part 2
                self.df.iat[15, i] = tax_payment

                cash_flow_after_taxes = round(cash_flow_after_financing - tax_payment, 2)
                self.df.iat[16, i] = cash_flow_after_taxes

                # Return Measures
                # Unleveraged
                self.df.iat[20, i] = cash_flow_after_financing
                self.df.iat[21, i] = cash_flow_after_financing

                # Leveraged
                self.df.iat[24, i] = cash_flow_after_taxes
                self.df.iat[25, i] = 0
                self.df.iat[26, i] = sum([self.df.iat[24, i], self.df.iat[25, i]])





        #Total
        total_future_cashflow_atStart

        endYear_net_operating_income = self.df.iat[11, -2]

        net_sale_price = gain_sale_price + gain_sale_expenses

        total_sales = net_sale_price + endYear_net_operating_income





myScheduleGrid = ScheduleGrid(total_gross_income= 1021228000.00,
                              total_vacancy= - 102061400.00,
                              operating_expenses=  1147500.00,
                              real_estate_taxes=  425000.00,
                              replacement_reserve=  225000.00,
                              debt=  175837188.00 ,
                              debt_service=  12098478.00 ,
                              debt_service_rate= 0.068805,
                              net_proceeds_fromSale= 100000.00,
                              beginYearBalance= 175837188.00,
                              interestRate= 0.05,
                              annual_public_subsidy_increase = 0.02,
                              depreciation=  -3917249.42,
                              odinaryTaxIncome= 0.35,
                              amortizationValues= 100000.00,
                              gain_sale_price= 0,
                              gain_sale_expenses= 0,
                              total_development_cost=  270518750.00,
                              total_future_cashflow_atStart=  94681562.50
                              )

print(myScheduleGrid.df.to_string())
print('\n')
print(myScheduleGrid.offsheet_df.to_string())

