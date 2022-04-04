import math
#THIS IS THE PRO FORMA CTEATED BY THE TEAM TOWER IN THE SOUP
print("TEAM-->TWOER IN THE SOUP")
print("Site Slection:NYCHA BARUCH")

# Global Constants
sitearea=1203998.4
existingunitcount=2194

studioSqFt = 400
onebedroomSqFt = 575
twobedroomSqFt = 775
threeBedroomSqFt = 950
studiocostperunit=1000
onebedroomcostperunit=2000
twobedroomcostperunit=3000
threebedroomcostperunit=4000
colivingcostperunit=5000
firstfloorcostperSqf=300
seconfloorcostperSqf=300
unitcirculationcostperSqf=300


# Changeble Constants
buildingcover=0.134
buildingcoverpercentage="{:.2%}".format(buildingcover)
buildingfloors=14
unitareacover=0.9
studiosrate= 0.2
onebedroomsrate = 0.2
twobedroomsrate= 0.4
threebedroomrate = 0.1
colivingrate=0.1


print("Site Area",sitearea,"square feet")
print("Buiding Cover:",buildingcoverpercentage)
print("Building Floors",buildingfloors)

firstfloorusearea=sitearea*buildingcover                           #this mix cost will cover in the future once define the use
print("First Floor Use Area",firstfloorusearea,"square feet")

secondfloorusearea=sitearea*buildingcover                          #this mix cost will cover in the future once define the use
print("Second Floor Use Area",secondfloorusearea,"square feet")

totalresidencialarea=sitearea*buildingcover*buildingfloors-firstfloorusearea-secondfloorusearea
print("Total Residencial Use Area",totalresidencialarea,"square feet")

totalunitarea=totalresidencialarea*unitareacover
print("Total Unit Use Area",totalunitarea,"square feet")

unitcirculationarea=totalresidencialarea*(1-unitareacover)        #unit circulation area, cost by area?
print("Total Unit Circulation Area",unitcirculationarea,"square feet")


studiocount=int(totalunitarea*studiosrate/studioSqFt)
print("Studio Unit Count",studiocount)

onebedroomcount=int(totalunitarea*onebedroomsrate/onebedroomSqFt)
print("One Bedroom Unit Count",onebedroomcount)

twobedroomcount=int(totalunitarea*twobedroomsrate/twobedroomSqFt)
print("Two Bedroom Unit Count",twobedroomcount)

threebedroomcount=int(totalunitarea*threebedroomrate/threeBedroomSqFt)
print("Three Bedroom Unit Count",threebedroomcount)

colivingcount=int(totalunitarea*colivingrate/colivingcostperunit)
print("Co-Living Unit Count",colivingcount)

totalunitcount=studiocount+onebedroomcount+twobedroomcount+threebedroomcount+colivingcount
print("New Development total unit count",totalunitcount)

increaseunitcount=totalunitcount-existingunitcount
print("Unit count increase number is",increaseunitcount)

###cost###
###total cost = landscape cost+ building cost and ?????###

###land cost
###other cost?
###maintain cost?

#building cost#
firstfloortotalcost=firstfloorusearea*firstfloorcostperSqf
secondfloortotalcost=secondfloorusearea*seconfloorcostperSqf
unitcirculationtotalcost=unitcirculationarea*unitcirculationcostperSqf
studiototalcost=studiocount*studiocostperunit
onebedroomcosttotalcost=onebedroomcount*onebedroomcostperunit
twobedroomtotalcost=twobedroomcount*twobedroomcostperunit
threebedroomtotalcost=threebedroomcount*threebedroomcostperunit
colivingtotalcost=colivingcount*colivingcostperunit
buildingtotalcost=firstfloortotalcost+secondfloortotalcost+unitcirculationtotalcost+studiototalcost+onebedroomcosttotalcost+twobedroomtotalcost+threebedroomtotalcost+colivingtotalcost
print("Buidling Total Cost",buildingtotalcost)


#benifit#

#Constants need to be defined by reserach

affordable_studiorent=500
affordable_onebedrent=600
affordable_twobedrent=700
affordable_threebedrent=800
affordable_colivingrent=900

market_studiorent=1500
market_onebedrent=2000
market_twobedrent=2500
market_threebedrent=3000
market_colivingrent=5000


#affordable housing rate = 80%#
affordablehousingrate=0.8
markethousingrate=1-affordablehousingrate
benifit=100000000000                   #this number equal land cost?

affordable_studiototalrent=affordable_studiorent*studiocount*affordablehousingrate*12
affordable_onebedtotalrent=affordable_onebedrent*onebedroomcount*affordablehousingrate*12
affordable_twobedtotalrent=affordable_twobedrent*twobedroomcount*affordablehousingrate*12
affordable_threebedtotalrent=affordable_threebedrent*threebedroomcount*affordablehousingrate*12
affordable_colivingtotalrent=affordable_colivingrent*colivingcount*affordablehousingrate*12

market_studiototalrent=affordable_studiorent*studiocount*markethousingrate*12
market_onebedtotalrent=affordable_onebedrent*onebedroomcount*markethousingrate*12
market_twobedtotalrent=affordable_twobedrent*twobedroomcount*markethousingrate*12
market_threebedtotalrent=affordable_threebedrent*threebedroomcount*markethousingrate*12
market_colivingtotalrent=affordable_colivingrent*colivingcount*markethousingrate*12

totalbenifit=benifit+affordable_studiototalrent+affordable_onebedtotalrent+affordable_twobedtotalrent+affordable_threebedtotalrent+affordable_colivingtotalrent+market_studiototalrent+market_onebedtotalrent+market_twobedtotalrent+market_threebedtotalrent+market_colivingtotalrent
print("Total benifit in 80% percentage affordable housing rate is",totalbenifit)