import pandas as pd

class ScheduleGrid:

    yrs = 10
    schedule_dates = pd.Series(pd.date_range(start='2022',periods=10, freq= 'YS')).dt.year

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
            'Net Sales Price', 'Total Sales',
            ' ',
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
    df.insert(len(df.columns), 'Total', ' ')

    offsheet_df = pd.DataFrame(index=offsheet_rows, columns=schedule_dates)
    offsheet_df.insert(len(offsheet_df.columns), 'Total', ' ')

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
                 net_proceeds_fromSale: int,
                 beginYearBalance: int,
                 interestRate: int,
                 depreciation: int,
                 odinaryTaxIncome: int,
                 amortizationValues: int,
                 gain_sale_price: int,
                 gain_sale_expenses: int,
                 total_development_cost: int
                 ):

        ### #FIRST ROW


        # Income
        self.df.iat[1, 0] = total_gross_income
        self.df.iat[2, 0] = total_vacancy
        self.df.iat[3, 0] = sum([total_gross_income, total_vacancy])

        # Expenses
        self.df.iat[6, 0] = operating_expenses
        self.df.iat[7, 0] = real_estate_taxes
        self.df.iat[8, 0] = replacement_reserve
        self.df.iat[9, 0] = sum([operating_expenses,real_estate_taxes,replacement_reserve])

        # Net Operating Income
        self.df.iat[11, 0] = sum([self.df.iat[8, 0] , self.df.iat[3, 0]])

        # OffSheet Calculations
        self.offsheet_df.iat[3, 0] = 1000

        self.df.iat[13, 0] = -(debt * debt_service)
        self.df.iat[14, 0] = sum([self.df.iat[11, 0], self.df.iat[13, 0]]) #Cash Flow after Financing
        self.df.iat[13, 0] = 0 #Tax Payment
        self.df.iat[14, 0] = sum([self.df.iat[14, 0], self.df.iat[13, 0]])

        # Return Measures

        self.df.style.format(formatter= int, thousands='{:,}')




myScheduleGrid = ScheduleGrid(total_gross_income= 100000,
                              total_vacancy= -100,
                              operating_expenses= 100000,
                              real_estate_taxes= 100000,
                              replacement_reserve= 100000,
                              debt= 100000,
                              debt_service= 100000,
                              net_proceeds_fromSale= 100000,
                              beginYearBalance= 100000,
                              interestRate= 100000,
                              depreciation= 100000,
                              odinaryTaxIncome= 100000,
                              amortizationValues= 100000,
                              gain_sale_price= 100000,
                              gain_sale_expenses= 100000,
                              total_development_cost= 100000
                              )


print(myScheduleGrid.df.to_string())
print('\n')
print(myScheduleGrid.offsheet_df.to_string())

