import CapitalStructureHelper as CSHelper

class CapitalStructure:
    equity_percent = 0.75
    debt = 1 - equity_percent

    def __init__(self,
                 total_development_cost):

        self.total_development_cost = total_development_cost
        self.debtService = 0.068805


        myEquity = CSHelper.Equity(myTotalDevCost= total_development_cost,
                        EqPerc= self.equity_percent)

        myTotalDebt = CSHelper.Debt(myTotalDevCost= total_development_cost,
                      equityPercent= self.equity_percent)

        myDebtService = CSHelper.DebtService(mytotalDebt= myTotalDebt, debtServPerc= self.debtService)
