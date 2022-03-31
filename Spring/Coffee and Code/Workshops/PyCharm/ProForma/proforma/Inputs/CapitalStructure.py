from proforma.Inputs  import CapitalStructureHelper as CSHelper

class CapitalStructure:
    equity_calc_percent = 0.75
    debt_calc = 1 - equity_calc_percent

    def __init__(self,
                 total_development_cost):

        self.total_development_cost = total_development_cost
        self.debt_calcService_rate = 0.068805


        self.equity_calc = CSHelper.equity_calc(myTotaldev_cost= total_development_cost,
                        eqPerc= self.equity_calc_percent)

        self.totaldebt_calc = CSHelper.debt_calc(myTotaldev_cost= total_development_cost,
                      equity_calcPercent= self.equity_calc_percent)

        self.debt_calcService = CSHelper.debt_calcService(mytotaldebt_calc= self.totaldebt_calc, debt_calcServPerc= self.debt_calcService_rate)
