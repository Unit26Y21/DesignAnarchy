import ScheduleFunctions as sF

class Schedule:
    def __init__(self,
                potential_gross_income,
                vacancy):

        self.potential_gross_income = potential_gross_income
        self.vacancy = vacancy

        sF.income(potential_gross_income, vacancy)

testSchedule = Schedule(10, 5)