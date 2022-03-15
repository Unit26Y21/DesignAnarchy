import numpy as np

class Bedroom:
    nychaUnits = {'studio':  [34, 14],
                  'bedroom1':  [50, 20],
                  'bedroom2':  [60, 30],
                  }

    def __init__(self,
                 price_per_sqft: float,
                 unitSelection: str):
        self.price_per_sqft = price_per_sqft
        self.unitSelection = unitSelection

        unitOptions = self.nychaUnits[unitSelection]

        def calculateArea(bedroom_unit):
            area = np.prod(bedroom_unit)
            return area

        self.unitArea = calculateArea(bedroom_unit= unitOptions )

        def calculateUnitPrice(price, area):
            unitPrice= price * area
            return unitPrice

        self.unitPrice = calculateUnitPrice(price_per_sqft, self.unitArea)

testBedroom = Bedroom(price_per_sqft=100,
                      unitSelection= "studio")

print(testBedroom.unitArea, testBedroom.unitPrice)