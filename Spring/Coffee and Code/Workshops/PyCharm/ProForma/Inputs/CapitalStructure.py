import CapitalStructureHelper as CSHelper

class CapitalStructure:
    equity_percent = 0.35
    debt = 1 - equity_percent
    debtService = 0

    def __init__(self, total_development_cost, debtServPerv):
        self.total_development_cost = total_development_cost
        self.debtServPerv = debtServPerv


        CSHelper.Equity(myTotalDevCost= self.total_development_cost,
                        EqPerc= self.equity_percent)

        myTotalDebt = CSHelper.Debt(myTotalDevCost=self.total_development_cost,
                      equityPercent= self.equity_percent)

        CSHelper.DebtService(mytotalDebt= myTotalDebt, debtServPerc= debtServPerv)

testCapitalStructure = CapitalStructure(total_development_cost= 270518750, debtServPerv = 0.0688)