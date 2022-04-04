
class PropertyInputs():
    development_timeline = 11
    net_loss_factor = 0.15

    total_floor_area = 0

    def __init__(self,
                 lot_area,
                 existingBuildingFloorArea,
                 residential_gross_sqft,
                 commercial_gross_sqft,
                 manufacturing_gross_sqft,
                 community_gross_sqft
                 ):

        # Starting Assumptions Constants
        self.lot_area = lot_area
        self.existingBuildingFloorArea = existingBuildingFloorArea

        self.residential_gross_sqft = residential_gross_sqft
        self.commercial_gross_sqft = commercial_gross_sqft
        self.manufacturing_gross_sqft = manufacturing_gross_sqft
        self.community_gross_sqft = community_gross_sqft


        self.total_floor_area = sum([self.residential_gross_sqft,
                                     self.commercial_gross_sqft,
                                     self.manufacturing_gross_sqft,
                                     self.community_gross_sqft])

        netZoningFloorArea = self.total_floor_area - (self.total_floor_area * self.net_loss_factor)

        print("Lot Area: {}".format(lot_area))
        print("Existing Building Floor Area: {}".format(existingBuildingFloorArea))


