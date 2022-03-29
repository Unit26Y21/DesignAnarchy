
import ResultsMetricHelper
import ResultsHelper


class Results:
    discount_rate = 0.09
    cap_rate_atSale = 0.06
    capital_gains_tax_rate = 0.2
    depreciation_recapture_rate = 0.25
    sale_expense_rate = 0.05

    def __init__(self,
                 equity: int,
                 future_cash_flow_list: list,
                 cash_flow_after_taxes: int,
                 total_net_operating_income: int,
                 total_development_cost: int,
                 total_replacement_reserve: int,
                 accumulated_depreciation: int,
                 mortgage_payoff: int,
                 net_operating_income: int
                 ):
        self.equity = equity
        self.future_cash_flow_list = future_cash_flow_list
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

        net_book_value = ResultsHelper.NetBookValueCalculator(developmentCost=total_development_cost,
                                                              replacementReserve=total_replacement_reserve,
                                                              total_depreciation=accumulated_depreciation)

        gain_on_sale = ResultsHelper.gainOnSaleCalculator(SalePrice=sale_price,
                                                          SaleExpenses=sale_expenses,
                                                          NetBookValue=net_book_value)

        capital_gains_tax = ResultsHelper.TaxCalculator(capital_gains_tax=self.capital_gains_tax_rate,
                                                        total_depreciation=accumulated_depreciation,
                                                        depreciation_recapture_tax=depreciation_recapture_total,
                                                        gain_on_sale=gain_on_sale)

        net_proceeds_from_sale = ResultsHelper.NetProceedsFromSaleCalculator(MortgagePayoff=mortgage_payoff,
                                                                             SalePrice=sale_price,
                                                                             SaleExpenses= -sale_expenses,
                                                                             TaxPayment= -(capital_gains_tax + abs(depreciation_recapture_total)))






        ### Return Metrics ###
        print("#" * 30)
        print("#" * 30)
        print("\n")
        # Net Present Value
        ResultsMetricHelper.net_present_value_calculator(equity=equity,
                                                         list_future_cash_flow=future_cash_flow_list,
                                                         discount_rate=self.discount_rate)

        # Leveraged IRR after Taxes
        ResultsMetricHelper.leveraged_IRR_calculator(future_cash_flow_list=future_cash_flow_list)

        # Capitalized Value
        ResultsMetricHelper.CapitalizeValueCalculator(net_operating_income=net_operating_income,
                                                      cap_rate_atSale=self.cap_rate_atSale)

        # ROTA
        ResultsMetricHelper.ReturnOnTotalAssetsCalculator(net_operating_income_1yr=net_operating_income,
                                                          total_development_cost=total_development_cost)

        # Return on Equity
        ResultsMetricHelper.ReturnOnEquityCalculator(equity=equity,
                                                     cash_flow_after_taxes=cash_flow_after_taxes)
