###### Basic Data Representation ######

# string, numbers, boolean, floats, integers


# print(1 + 1)
# # print(1 + '1') causes error
# print('1' + '1')
# print(True)
# print(False)
# print( 6 * 4)

# Collections
# Dictionary
# Zones --> FAR
# String: Float

zoningDictionary = {
        "R1": 0.5,
        "R2": 0.5,
        "R2X": 0.85,
        "R3": 0.5,
        "R4": 0.75,
        "R4B": 0.9,
        "R5": 1.25,
        "R5A": 1.1,
        "R5B": 1.35,
        "R5D": 2,
        "R6": 2.43,
        "R6A": 3.6,
        "R7": 3.44,
        "R7-1": 3.44,
        "R7-2": 3.44,
        "R7A": 4.6,
        "R7B": 3,
        "R8": 6.02,
        "R8A": 7.2,
        "R8X": 7.2,
        "R8B": 4,
        "R9": 8,
        "R9A": 8.5,
        "R9D": 10,
        "R9X": 9.7
}

randomList = [10, 0,1,2,5452,12314]

newZoning = {
    "R9 Extreme":{
        "FAR":100,
        "Front Setback": 10,
        "Maximum Height": 1776,
    }
}

myBuildingUseDictionary = {
    "Community": "Community"
}
# Dictionary has a key and a value
# To extract value base on a key...
print(newZoning["R9 Extreme"])
#print(randomList[1])


def grabItemFromDictionary(input, dictionary):
    return dictionary[input]

def permittedFAR(inputZone):
    grabItemFromDictionary(inputZone, zoningDictionary)

def pemittedUse(inputUse):
    grabItemFromDictionary(inputUse, myBuildingUseDictionary)