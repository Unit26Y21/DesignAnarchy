
class PropertyInputs():
    devTimeline = 11
    netLossFactor = .15

    def __init__(self,
                 lotArea,
                 existingBuildingFloorArea,
                 residentialFAR,commercialFAR, manufacturingFAR
                 ):

        # Starting Assumptions Constants
        self.lotArea = lotArea
        self.existingBuildingFloorArea = existingBuildingFloorArea
        self.residentialFAR = residentialFAR
        self.commercialFAR = commercialFAR
        self.manufacturingFAR = manufacturingFAR


        residentialZoningFloorArea = lotArea * residentialFAR
        commercialZoningFloorArea = lotArea * commercialFAR
        manufacturingZoningFloorArea = lotArea * manufacturingFAR
        totalFloorArea = sum([residentialZoningFloorArea,commercialZoningFloorArea,manufacturingZoningFloorArea])
        netZoningFloorArea = totalFloorArea - (totalFloorArea * self.netLossFactor)




