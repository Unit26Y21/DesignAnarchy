from proforma.Inputs  import CapitalStructureHelper as CSHelper

class CapitalStructure:
    equity_percent = 0.75
    debt = 1 - equity_percent

    def __init__(self,
                 total_development_cost):

        self.total_development_cost = total_development_cost
        self.debtService_rate = 0.068805


        self.equity = CSHelper.Equity(myTotalDevCost= total_development_cost,
                        EqPerc= self.equity_percent)

        self.totalDebt = CSHelper.Debt(myTotalDevCost= total_development_cost,
                      equityPercent= self.equity_percent)

        self.debtService = CSHelper.DebtService(mytotalDebt= self.totalDebt, debtServPerc= self.debtService_rate)
