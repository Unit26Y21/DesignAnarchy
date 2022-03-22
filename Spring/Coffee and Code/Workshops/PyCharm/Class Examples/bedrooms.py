import numpy as np
import random


class BuildingSpine:

    def __init__(self,angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3



class Bedroom:
    '''
    My Bedroom is an object that creates bedrooms of different
    prices and sizes.
    '''
    nychaUnits = {'studio':  [34, 14],
                  'bedroom1':  [50, 20],
                  'bedroom2':  [60, 30],
                  }

    myPrice = 1000
    myRent = 892

    def __init__(self,
                 price_per_sqft: float,
                 unitSelection: str):

        self.price_per_sqft = price_per_sqft
        self.unitSelection = unitSelection

        unitOptions = self.nychaUnits[unitSelection]

        # my function to calculate area, returns: x * y
        def calculateArea(bedroom_unit):
            area = np.prod(bedroom_unit)
            return area

        self.unitArea = calculateArea(bedroom_unit= unitOptions)

        def calculateUnitPrice(price, area):
            unitPrice= price * area
            return unitPrice

        self.unitPrice = calculateUnitPrice(price_per_sqft, self.unitArea)



testBedroom1 = Bedroom(price_per_sqft=700,
                      unitSelection= "studio")

testBedroom2 = Bedroom(unitSelection='bedroom1',
                       price_per_sqft=1000)

selectionBedrooms = ['studio', 'bedroom1', 'bedroom2']

myPrices = [1000,1100,1400,1500,3000,5000,4000,1230,2345]

# for price in myPrices:
#     myRandomUnit = random.choice(selectionBedrooms)
#     myRandomBedroom = Bedroom(price_per_sqft=price,
#                               unitSelection= myRandomUnit)
#
#     print(myRandomBedroom.unitSelection, myRandomBedroom.unitArea, myRandomBedroom.unitPrice)
