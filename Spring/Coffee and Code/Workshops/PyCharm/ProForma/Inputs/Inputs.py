
class PropertyInputs():
    devTimeline = 11
    netLossFactor = .15
    residentialZoningFloorArea = 0
    commercialZoningFloorArea = 0
    manufacturingZoningFloorArea = 0

    totalFloorArea = 0

    def __init__(self,
                 lotArea,
                 existingBuildingFloorArea,
                 residentialFAR,
                 commercialFAR,
                 manufacturingFAR,
                 ):

        # Starting Assumptions Constants
        self.lotArea = lotArea
        self.existingBuildingFloorArea = existingBuildingFloorArea

        self.residentialFAR = residentialFAR
        self.commercialFAR = commercialFAR
        self.manufacturingFAR = manufacturingFAR

        self.residentialZoningFloorArea = lotArea * residentialFAR
        self.commercialZoningFloorArea = lotArea * commercialFAR
        self.manufacturingZoningFloorArea = lotArea * manufacturingFAR

        self.totalFloorArea = sum([self.residentialZoningFloorArea,
                              self.commercialZoningFloorArea,
                              self.manufacturingZoningFloorArea])

        netZoningFloorArea = self.totalFloorArea - (self.totalFloorArea * self.netLossFactor)

        print("Lot Area: {}".format(lotArea))
        print("Existing Building Floor Area: {}".format(existingBuildingFloorArea))

        if residentialFAR:
            print("Residential FAR: {0} | Residential Floor Area  {1:,}".format(residentialFAR,self.residentialZoningFloorArea))

        if commercialFAR:
            print("Commercial FAR: {0} | Commercial Floor Area  {1:,}".format(commercialFAR, self.commercialZoningFloorArea))

        if manufacturingFAR:
            print("Manufacturing FAR: {0} | Manufacturing Floor Area  {1:,}".format(manufacturingFAR, self.manufacturingZoningFloorArea))



