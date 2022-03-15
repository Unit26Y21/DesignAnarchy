# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




## Dictionary for ProForma
# Farragut
# Adderess = 237 Nassau Street
# Borough = Brooklyn
# City = New York City
# State = New York
# Total Area = 0.026 sq mile
# Lot1 Area =
# Lot1 Depth =
# Lot1 Width =
# Lot2 Area =
# Lot2 Depth =
# Lot2 Width =
# Lot3 Area =
# Lot3 Depth =
# Lot3 Width =
# Land Use =
# Easements =
# BBL =
# BIN =
# Zoning District =
# Historic District =
# Landmark =
# Special District =
# District Overlay =
# Inclusionary Housing =
# Mandatory Inclusionary =
# Built FAR =
# Existing Building(s) =
# Year Built =
# Total Built Area =
# Lot1 Built Area =
# Lot2 Built Area =
# Lot3 Built Area =
# Building Use =
# Building Height = 13, 14 stories

# Parking Space Area = 162 ft
# Parking Space Length = 18 ft
# Parking Space Width = 9 ft
# MicroUnit Area = 324 ft
# MicroUnit Length = 18 ft
# MicroUnit Width = 18 ft
# OneBedroom Area = 648 ft
# OneBedroom Length = 36 ft
# OneBedroom Width = 18 ft
# TwoBedroom Area = 729 ft
# TwoBedroom Length = 27 ft
# TwoBedroom Width = 27 ft
    ## Create a function that takes the dimensions of a parking space and then outputs it into different layouts ##
    ## Create function that takes units and outputs in different arrangements ##

ParkingDimensions = (9,18,27,36,45,56)

    ## Typical sizes and dimensions ##
ParkingSpaceDimensions = {'Area':162, 'Length':18, 'Width':9}
print(ParkingSpaceDimensions)
MicroUnitDimensions = dict(Area=324, Length=18, Width=18)
print(MicroUnitDimensions)
OneBedroomDimensions = dict(Area=648, Length=36, Width=18)
print(OneBedroomDimensions)
TwoBedroomDimensions = dict(Area=729, Length=27, Width=27)
print(TwoBedroomDimensions)
    ## How can I input a function that takes the area of the unit type and then outputs widths and lengths? example: A TwoBedroom has area of 729 and then it'll list the options such as 27x27, 18x36... ##
    ## Basically to take the parking space and rearrange it in different numbers and arrangements ##
#MicroUnitNumber =
#OneBedroomNumber =
#TwoBedroomNumber =
## Now I want to extract the first value in the dictionaries ##
MicroUnitArea = 324 # 0 from MicroUnitDimensions dict #
OneBedroomArea = 648 # 0 from OneBedroomDimensions dict #
TwoBedroomArea = 729 # 0 from TwoBedroomDimensions dict #
