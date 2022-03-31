
class PropertyInputs():
    development_timeline = 11
    net_loss_factor = 0.15

    residential_ZFA= 0
    commercial_ZFA= 0
    manufacturing_ZFA = 0
    community_ZFA = 0

    total_floor_area = 0

    def __init__(self,
                 lot_area,
                 existingBuildingFloorArea,
                 residential_FAR,
                 commercial_FAR,
                 manufacturing_FAR,
                 community_FAR
                 ):

        # Starting Assumptions Constants
        self.lot_area = lot_area
        self.existingBuildingFloorArea = existingBuildingFloorArea

        self.residential_FAR = residential_FAR
        self.commercial_FAR = commercial_FAR
        self.manufacturing_FAR = manufacturing_FAR
        self.community_FAR = community_FAR

        self.residential_ZFA= lot_area * residential_FAR
        self.commercial_ZFA= lot_area * commercial_FAR
        self.manufacturing_ZFA = lot_area * manufacturing_FAR
        self.community_ZFA = lot_area * community_FAR

        self.total_floor_area = sum([self.residential_ZFA,
                                     self.commercial_ZFA,
                                     self.manufacturing_ZFA,
                                     self.community_ZFA])

        netZoningFloorArea = self.total_floor_area - (self.total_floor_area * self.net_loss_factor)

        print("Lot Area: {}".format(lot_area))
        print("Existing Building Floor Area: {}".format(existingBuildingFloorArea))

        if residential_FAR:
            print("Residential FAR: {0} | Residential Floor Area  {1:,}".format(residential_FAR,self.residential_ZFA))

        if commercial_FAR:
            print("Commercial FAR: {0} | Commercial Floor Area  {1:,}".format(commercial_FAR, self.commercial_ZFA))

        if manufacturing_FAR:
            print("Manufacturing FAR: {0} | Manufacturing Floor Area  {1:,}".format(manufacturing_FAR, self.manufacturing_ZFA))



