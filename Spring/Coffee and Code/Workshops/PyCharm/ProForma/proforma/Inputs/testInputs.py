from proforma.Inputs import InputsAssumptions
from statistics import mean

myUnits = mean([900,1000,500])

myProformita = InputsAssumptions.MyInputsAssumptions(lotArea=11000,
                                                     existingBuildingFloorArea=0,
                                                     residentialFAR= 9,
                                                     commercialFAR= 0,
                                                     manufacturingFAR=0,
                                                     communityFAR=0,
                                                     avgUnitSize_residential=myUnits,
                                                     avgUnitSize_commercial = 0,
                                                     avgUnitSize_manufacturing = 0,
                                                     avgUnitSize_community = 0,

                                                     )