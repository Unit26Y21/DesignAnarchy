XShapeBldgArea = 9513.84
TShapeBldgArea = 4565.33
numberTshapeBldg = 4
numberXshapeBldg = 9
numberExistingUnits = 1246
"source: ArcGIS"
sqMeterconverter= 10.76

overbaseArea = 6025.54
"Over X shape bldg"

iterationA = 6847.88
"Over X shape bldg"

iterationB = 4552.23
"Over X shape bldg"

iterationC = 5682.08
"Over T shape bldg"

numberIterationAWithOverbase = 3
numberIterationAWithoutOverbase = 1
numberIterationBWithOverbase = 4
numberIterationBWith2Overbases = 1
numberIterationC = 4


def AdditionTotalAreaCalculator(IterationA, IterationB, IterationC, OverbaseArea, NumberofIterationAwithOverbase, NumberofIterationAwithoutOverbase, NumberofIterationBwithOverbase, NumberofIterationBwith2Overbase,NumberofIterationC):
    AddedAreaTshape = (IterationC*NumberofIterationC)*sqMeterconverter
    AddedAreaXshape = (((IterationA+OverbaseArea)*NumberofIterationAwithOverbase)+\
                      (IterationA*NumberofIterationAwithoutOverbase)+\
                      ((IterationB+OverbaseArea)*NumberofIterationBwithOverbase)+\
                      ((IterationB+(OverbaseArea*2)*NumberofIterationBwith2Overbase)))*sqMeterconverter
    AdditionTotalArea = float(AddedAreaTshape+AddedAreaXshape)
    print("Added Area X shape: ", AddedAreaXshape)
    print("Added Area T shape: ", AddedAreaTshape)
    print("Addition Total Area: ", AdditionTotalArea)
    return AddedAreaTshape, AddedAreaXshape, AdditionTotalArea

additionTotalAreaCalculator = AdditionTotalAreaCalculator(iterationA, iterationB, iterationC, overbaseArea, numberIterationAWithOverbase, numberIterationAWithoutOverbase, numberIterationBWithOverbase, numberIterationBWith2Overbases, numberIterationC)

def ExistingTotalArea(XBldgArea, TBldgArea,NumberTBldg,NumberXBldg):
    ExistingTotalArea = ((XBldgArea*NumberXBldg)+(TBldgArea*NumberTBldg))*sqMeterconverter
    print("Existing Bldg Area: ", ExistingTotalArea)
    return(ExistingTotalArea)

ExistingTotalArea = ExistingTotalArea(XShapeBldgArea, TShapeBldgArea, numberTshapeBldg, numberXshapeBldg)

colivingArea = 380
studioArea = 494
oneBArea = 1102
twoBArea = 1402
threeBArea = 1938

def UnitAssigner(additionTotalArea, ColivingArea, StudioArea, OneBArea, TwoBArea, ThreeBArea):
    ColivingUnits = (additionTotalArea*.25)/ColivingArea
    StudioUnits = (additionTotalArea*.30)/StudioArea
    OneBUnits = (additionTotalArea*.30)/OneBArea
    TwoBUnits = (additionTotalArea*.10)/TwoBArea
    ThreeBUnits = (additionTotalArea*.05)/ThreeBArea
    totalUnits = ColivingUnits + StudioUnits + OneBUnits + TwoBUnits + ThreeBUnits
    print("Coliving Units: ", ColivingUnits)
    print("Studio Units: ", StudioUnits)
    print("One Bedroom Units: ", OneBUnits)
    print("Two Bedroom Units: ", TwoBUnits)
    print("Three Bedroom Units: ", ThreeBUnits)
    print("Total Units: ", totalUnits)
    return totalUnits

UnitAssigner = UnitAssigner(additionTotalAreaCalculator[2],colivingArea, studioArea, oneBArea, twoBArea, threeBArea)
