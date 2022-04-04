from proforma.Results import Results as myResults

futureCashFlowTest = [880323,956599,1033967,1112448,1192064,1272838,1354794,1437953,1522342,24248132]
futureCashFlowTest1 = [588560875,956599,1033967,1112448,1192064,1272838,1354794,1437953,1522342,15669067674]

testResults = myResults.Results(equity_calc = 9712500,
                      net_operating_income= 1995000,
                      future_cash_flow_list= futureCashFlowTest,
                      cash_flow_after_taxes= 880323,
                      total_net_operating_income= 2431894,
                      total_development_cost= 27750000,
                      total_replacement_reserve= 1084022 ,
                      accumulated_depreciation= -8310023,
                      mortgage_payoff= -11853140)
