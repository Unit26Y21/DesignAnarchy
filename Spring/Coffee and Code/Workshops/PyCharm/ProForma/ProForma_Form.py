import Inputs.Inputs as proformaInputs
import Inputs.Costs as proformaCosts

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
    proformaInputs.PropertyInputs(lotArea = 10315,
                 existingBuildingFloorArea = 132420,
                 residentialFAR = 7.52,commercialFAR = 1, manufacturingF = 0,)

    # 2. Assumptions About Cost and Capital Structure
    proformaCosts.DevelopmentCosts(gross_ZFA = 100000,
                                          residential_ZFA = 100000,
                                          commercial_ZFA = 0,
                                          manufacturing_ZFA = 0 )

    # 3. Projected Proceeds from Residential, Commercial and Manufacturing
    # 4. Tax, Capital and other specific types of rates
    # ---
    # 1. Gross Income Totals
    # 2. A cost schedule
    # 3. Results including: Net Book Value, Gain on Sale, Tax Payment, Net proceed from sale
    # 4. Return Metrics: Net Present Value, Leveraged IRR After Tax, Capitalize Value, ROTA, Return on Equity




testProforma = ProForma()