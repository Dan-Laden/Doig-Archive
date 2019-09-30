#################################
# author@ Daniel Laden          #
# email@ dthomasladen@gmail.com #
#################################
print("Geojson-mmaker")
import time
start_time = time.time()


import sys #ref doc: https://docs.python.org/3.6/library/sys.html
import os #ref doc: https://docs.python.org/3.6/library/os.html
from geojson import Point, Feature, FeatureCollection, dump #ref: https://geojson.org/

#########################
#Start of main code

doig_locations = {}

for book in os.listdir("output"):
    direct = "output/"+book+"/Geolocations"
    for chapter in os.listdir(direct):
        source = direct + "/" + chapter
        f = open(source, 'r')
        geolocations = ""
        for line in f:
            geolocations = geolocations + line
        locations = geolocations.split("; ")
        for loc in locations:
            hit = loc.split("|")
            if hit != ['']:
                try:
                    doig_locations[hit[0]] += int(hit[1])
                except:
                    doig_locations[hit[0]] = int(hit[1])


print(doig_locations)

features = []

for loc in doig_locations:
    point = loc.split(" (")
    location = point[0]

    point = point[1].replace(")", "")
    point = point.split(",")
    latitude = float(point[0])
    longitude = float(point[1])

    point = Point((longitude, latitude))

    features.append(Feature(geometry=point, properties={"name": location, "hits": doig_locations[loc]}))

feature_collection = FeatureCollection(features)

with open('ivan_doig.geojson', 'w') as f:
   dump(feature_collection, f, indent=4, separators=(',', ': '))


#End of main code
#########################

seconds = round(time.time() - start_time)
minutes = 0
hours = 0
if seconds > 60:
    minutes = int(seconds/60)
    seconds = seconds - (minutes * 60)
if minutes > 60:
    hours = int(minutes/60)
    minutes = minutes - (hours * 60)
print("--- %s hours ---\n--- %s minutes ---\n--- %s seconds ---" % (hours, minutes, seconds))

#########################
#resources used for code so far
#
# http://sam.gleske.net/blog/engineering/2017/10/21/python-json-pretty-dump.html
# https://macwright.org/2015/03/23/geojson-second-bite.html
# https://gis.stackexchange.com/a/292255
# https://gist.github.com/wavded/1200773?short_path=99c1af9
# https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
# https://bytes.com/topic/python/answers/44454-using-wildcards
# https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python/3964689
#########################
