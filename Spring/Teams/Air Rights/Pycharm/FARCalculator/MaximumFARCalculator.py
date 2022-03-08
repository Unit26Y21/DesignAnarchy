# it is better to create a dictionary
zoningDictionary = {
    "residentialZoning": {
        "R2": 0.5,
        "R2A": 0.5,
        "R3-1": 0.5,
        "R3-2": 0.5,
        "R3A": 0.5,
        "R3X": 0.5,
        "R4": 0.75,
        "R4-1": 0.75,
        "R4A": 0.75,
        "R4B": 0.9,
        "R5": 1.25,
        "R5A": 1.1,
        "R5B": 1.35,
        "R5D": 2,
        "R6": 2.43,
        "R6A": 3.6,
        "R6B": 3.6,
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
        "R9X": 9.7,
    },
    "commercialZoning": {
        "C1-8A": 2,
        "C1-9": 2,
        "C2-8": 2,
        "C4-3": 3.4,
        "C4-4A": 4,
        "C4-4D":3.4,
        "C4-5X": 4,
        "C6-1G": 6,
        "C6-3": 6,
        "C6-4": 10,
        "C8-1": 1,
        "C8-2": 2,
    },
    "manufacturingZoning": {
        "M1-1": 1,
        "M1-2/R6B": 2,
        "M3-1": 2,
        "M3-2": 2,
        "PARK": None,
    }
}

"""
# A more detailed dictionary
newZoning = {
    "R9 Extreme": {
            "FAR": 100,
            "Front Setback": 10,
            "Maximum Height": 1776,
        }
}

# To extract a value from the dictionary
print (zoningDictionary["R9"])
print (zoningDictionary.values())
print (zoningDictionary.keys())
randomList = [10,0,2,4,8]
print (newZoning["R9 Extreme"])

def permittedFAR(inputZone):
    switch = {
        "R6": 2.43,
        "R6A": 3.6,
        "R7-2": 3.44,
        "R7A": 4.6,
        "R7B": 3,
        "R8": 6.02,
        "R8A": 7.2,
        "R8B": 4,
        "R9A": 8.5,
        }
    return switch.get(inputZone, 0)

"""
# Example
def permittedFARComplex(inputZone):
    if inputZone[0] == "R":
        return zoningDictionary["residentialZoning"][inputZone]

    elif inputZone[0] == "C":
        return zoningDictionary["commercialZoning"][inputZone]

    else:
        return zoningDictionary["manufacturingZoning"][inputZone]


zoningDictionaryFlat = {
        "R2": 0.5,
        "R2A": 0.5,
        "R3-1": 0.5,
        "R3-2": 0.5,
        "R3A": 0.5,
        "R3X": 0.5,
        "R4": 0.75,
        "R4-1": 0.75,
        "R4A": 0.75,
        "R4B": 0.9,
        "R5": 1.25,
        "R5A": 1.1,
        "R5B": 1.35,
        "R5D": 2,
        "R6": 2.43,
        "R6A": 3.6,
        "R6B": 3.6,
        "R7": 3.44,
        "R7-1": 3.44,
        "R7-2": 3.44,
        "R7A": 4.6,
        "R7B": 3,
        "R7D": 5.6,
        "R8": 6.02,
        "R8A": 7.2,
        "R8X": 7.2,
        "R8B": 4,
        "R9": 8,
        "R9A": 8.5,
        "R9D": 10,
        "R9X": 9.7,
        "C1-8A": 2,
        "C1-9": 2,
        "C2-8": 2,
        "C4-3": 3.4,
        "C4-4A": 4,
        "C4-4D":3.4,
        "C4-5X": 4,
        "C6-1G": 6,
        "C6-3": 6,
        "C6-4": 10,
        "C8-1": 1,
        "C8-2": 2,
        "M1-1": 1,
        "M1-2/R6B": 2,
        "M3-1": 2,
        "M3-2": 2,
        "PARK": None,
}

def permittedFAR(inputZone):
    return zoningDictionaryFlat[inputZone]