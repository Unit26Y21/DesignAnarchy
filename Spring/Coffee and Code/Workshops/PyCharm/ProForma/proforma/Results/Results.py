
from proforma.Results import ResultsMetricHelper, ResultsHelper
from proforma.Inputs import OtherRates as rates
import pandas as pd


class Results:
    discount_rate = rates.OtherRates.ratesDictionary['discountRate']
    cap_rate_atSale = rates.OtherRates.ratesDictionary['capRateAtSale']
    capital_gains_tax_rate = rates.OtherRates.ratesDictionary['capitalGainsTax']
    depreciation_recapture_rate =  rates.OtherRates.ratesDictionary['depreciationRecapture']
    sale_expense_rate =  rates.OtherRates.ratesDictionary['salesExpense']

    def __init__(self,
                 equity: int,
                 debt_cash_flow_list: list,
                 cash_flow_after_taxes: int,
                 total_net_operating_income: int,
                 total_development_cost: int,
                 total_replacement_reserve: int,
                 accumulated_depreciation: int,
                 mortgage_payoff: int,
                 net_operating_income: int
                 ):

        self.equity = equity
        self.debt_cash_flow_list = debt_cash_flow_list
        self.cash_flow_after_taxes = cash_flow_after_taxes
        self.total_net_operating_income = total_net_operating_income
        self.total_development_cost = total_development_cost
        self.total_replacement_reserve = total_replacement_reserve
        self.accumulated_depreciation = accumulated_depreciation
        self.mortgage_payoff = mortgage_payoff
        self.net_operating_income = net_operating_income

        depreciation_recapture_total = accumulated_depreciation * self.depreciation_recapture_rate

        #### Net Proceeds From Sale ###
        sale_price = total_net_operating_income / self.cap_rate_atSale
        sale_expenses = sale_price * self.sale_expense_rate

        net_book_value = ResultsHelper.net_book_value_calculator(development_cost=total_development_cost,
                                                              replacement_reserve=total_replacement_reserve,
                                                              total_depreciation=-accumulated_depreciation)

        gain_on_sale = ResultsHelper.gain_onSale_calculator (sale_price=sale_price,
                                                          sale_expenses=sale_expenses,
                                                          net_book_value=net_book_value)

        capital_gains_tax = ResultsHelper.tax_calculator(capital_gains_tax=self.capital_gains_tax_rate,
                                                        total_depreciation=accumulated_depreciation,
                                                        depreciation_recapture_tax=depreciation_recapture_total,
                                                        gain_on_sale=gain_on_sale)

        net_proceeds_from_sale = ResultsHelper.net_proceeds_fromSale_calculator(mortgage_payoff=mortgage_payoff,
                                                                             sale_price=sale_price,
                                                                             sale_expenses= -sale_expenses,
                                                                             tax_payment= -(capital_gains_tax + abs(depreciation_recapture_total)))






        ### Return Metrics ###
        print("#" * 30)
        print("#" * 30)
        print("\n")
        # Net Present Value
        ResultsMetricHelper.net_present_value_calculator(equity=equity,
                                                         debt_cash_flow_list=debt_cash_flow_list,
                                                         discount_rate=self.discount_rate)

        # Leveraged IRR after Taxes
        ResultsMetricHelper.leveraged_IRR_calculator(debt_cash_flow_list=debt_cash_flow_list)

        # Capitalized Value
        ResultsMetricHelper.capitalize_value_calculator(net_operating_income=net_operating_income,
                                                      cap_rate_atSale=self.cap_rate_atSale)

        # ROTA
        ResultsMetricHelper.return_onTotalAssets_calculator(net_operating_income_1yr=net_operating_income,
                                                          total_development_cost=total_development_cost)

        # Return on equity
        ResultsMetricHelper.return_on_equity_calculator(equity=equity,
                                                     cash_flow_after_taxes=cash_flow_after_taxes)

        resultsDictionary = {

        }
        # TODO: Create a dataFrame for this Class
        df =pd.DataFrame()