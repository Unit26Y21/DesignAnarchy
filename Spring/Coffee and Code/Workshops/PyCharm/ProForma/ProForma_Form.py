import Inputs.InputsAssumptions as Inputs
import Results.Results as Results
from statistics import mean


myUnits = mean([900,1000,500])

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
    Inputs.MyInputsAssumptions(lotArea=11000,
                               existingBuildingFloorArea=0,
                               residentialFAR=9,
                               commercialFAR=0,
                               manufacturingFAR=0,
                               avgUnitSize=myUnits
                               )

    # 2. Assumptions About Cost and Capital Structure: Left as is for now...

    # 3. Schedule

    # 4. Results
    futureCashFlowTest = [880323, 956599, 1033967, 1112448, 1192064, 1272838, 1354794, 1437953, 1522342, 24248132]

    Results.Results(equity = 9712500,
                      net_operating_income= 1995000,
                      future_cash_flow_list= futureCashFlowTest,
                      cash_flow_after_taxes= 880323,
                      total_net_operating_income= 2431894,
                      total_development_cost= 27750000,
                      total_replacement_reserve= 1084022 ,
                      accumulated_depreciation= -8310023,
                      mortgage_payoff= -11853140)


testProforma = ProForma()