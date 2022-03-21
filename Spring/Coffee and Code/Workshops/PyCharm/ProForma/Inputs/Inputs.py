
class PropertyInputs():
    devTimeline = 11
    netLossFactor = .15

    def __init__(self,
                 lotArea,
                 existingBuildingFloorArea,
                 residentialFAR,commercialFAR, manufacturingFAR,

                 ):

        # Starting Assumptions Constants
        self.manufacturingZoningFloorArea = 0
        self.commercialZoningFloorArea = 0
        self.residentialZoningFloorArea = 0
        self.lotArea = lotArea
        self.existingBuildingFloorArea = existingBuildingFloorArea
        self.residentialFAR = residentialFAR
        self.commercialFAR = commercialFAR
        self.manufacturingFAR = manufacturingFAR



        residentialZoningFloorArea = lotArea * residentialFAR
        commercialZoningFloorArea = lotArea * commercialFAR
        manufacturingZoningFloorArea = lotArea * manufacturingFAR

        self.totalFloorArea = sum([residentialZoningFloorArea,commercialZoningFloorArea,manufacturingZoningFloorArea])

        netZoningFloorArea = self.totalFloorArea - (self.totalFloorArea * self.netLossFactor)




