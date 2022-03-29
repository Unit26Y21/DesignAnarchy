from proforma.Inputs import InputsAssumptions as Inputs
from proforma.Results import Results
from proforma.Schedule import ScheduleDataFrame as Schedule

from statistics import mean


myUnits = mean([900, 1000, 500])

class ProForma:
    '''
    This class builds a proforma using the following inputs:
    1. Property Information
    2. Assumptions About Cost and Capital Structure
    3. Projected Proceeds from Residential, Commercial and Manufacturing
    4. Tax, Capital and other specific types of rates
    ---

    It then calculates:
    1. Gross Income Totals
    2. A cost schedule
    3. Results including: Net Book Value, Gain on Sale, Tax Payment, Net proceed from sale
    4. Return Metrics: Net Present Value, Leveraged IRR After Tax, Capitalize Value, ROTA, Return on Equity
    '''


    # 1. Property Information
    propertyInput = Inputs.MyInputsAssumptions(lotArea=11000,
                                               existingBuildingFloorArea=0,
                                               residentialFAR=9,
                                               commercialFAR=0,
                                               communityFAR=0,
                                               manufacturingFAR=0,
                                               avgUnitSize_residential=myUnits,
                                               avgUnitSize_commercial = 1,
                                               avgUnitSize_manufacturing = 0,
                                               avgUnitSize_community = 0,
                                               )

    # 3. Schedule
    schedule = Schedule.ScheduleGrid(total_gross_income= propertyInput.totals.total_Gross_Incomes,
                                     total_vacancy= -propertyInput.totals.total_Vacancy,
                                     operating_expenses=  propertyInput.totals.total_Expenses,
                                     real_estate_taxes=  propertyInput.totals.total_Property_Real_Estate_Taxes,
                                     replacement_reserve=  propertyInput.totals.total_Property_Replacement_Reserve,
                                     debt=  propertyInput.capitalStructure.debt,
                                     equity = propertyInput.capitalStructure.equity,
                                     debt_service=  propertyInput.capitalStructure.debtService,
                                     debt_service_rate= propertyInput.capitalStructure.debtService_rate,
                                     beginYearBalance= propertyInput.capitalStructure.debt,
                                     interestRate= propertyInput.rates.ratesDictionary['interestRate'],
                                     annual_public_subsidy_increase = propertyInput.rates.ratesDictionary['annualPublicSubsidiesIncrease'],
                                     depreciation= propertyInput.totals.total_Depreciation,
                                     odinaryTaxIncome= propertyInput.rates.ratesDictionary['ordinaryIncomeTax'],
                                     )

    # 4. Results
    results = Results.Results(equity = propertyInput.capitalStructure.equity,
                    net_operating_income= schedule.net_operating_income_atStart,
                    future_cash_flow_list= schedule.future_cashflow_list,
                    cash_flow_after_taxes= schedule.cash_flow_after_taxes_atStart,
                    total_net_operating_income= schedule.final_net_operating_income,
                    total_development_cost= propertyInput.developmentCosts.total_development_cost,
                    total_replacement_reserve= schedule.final_replacement_reserve,
                    accumulated_depreciation= -schedule.final_depreciation,
                    mortgage_payoff= -schedule.mortage_payoff)

    print(schedule.table.to_string())
    print('\n')
