import pandas as pd

class ScheduleGrid:

    yrs = 10
    schedule_dates = pd.Series(pd.date_range(start='2022',periods=10, freq= 'YS')).dt.year

    rows = ['Income',
            'Potential Gross Income',
            'Vacancy',
            'Effective Gross Income',
            '',
            'Expenses',
            'Operating Expenses',
            'Real Estate Taxes',
            'Replacement Reserve',
            'Total Expenses',
            '',
            'NET OPERATING INCOME',
            '',
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
            ' ',
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


    # Return Measures

    #OffSheet Calculations


    # Print this table
    print(df.to_string())


myScheduleGrid = ScheduleGrid