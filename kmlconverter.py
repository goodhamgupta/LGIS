import csv
import simplekml
import geocoder
from xlsdictreader import XLSDictReader
from collections import defaultdict



def convert_file():
    mydict = defaultdict(list)
    with open('data.xlsx', 'r') as excelfile:
        dictReader = XLSDictReader(excelfile)    
        for row in dictReader:
            mycategory = row.pop("Name")
            mydict[mycategory].append(row)  # Will put a list for not-existing key
    mydict = dict(mydict) 
    kml =simplekml.Kml()
    for ctgy in mydict:
        fol=kml.newfolder(name=ctgy)
        for entry in mydict[ctgy]:
             # geocode addresses
             print "Niggatry!" ,entry

             '''
             g = geocoder.google(entry["Name"])
             pnt=fol.newpoint(name=entry["Name"], coords=[(g.lng,g.lat)], description=entry["Rating"])
             if entry["Icon"] != "":
                pnt.style.iconstyle.icon.href=entry["Icon"]
kml.save("data.kml")
'''