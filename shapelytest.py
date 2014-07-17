import json
from shapely.geometry import shape, Point

# load GeoJSON file containing sectors
#with open('gz_2010_us_050_00_5m.json' ) as f:
with open('cb_2013_us_county_20m.json' ) as f:
    js_str = f.read().replace('\n','')
    print js_str[12000:12073]
    js = json.loads(js_str.decode('latin1'))

# construct point based on lat/long returned by geocoder
point = Point(45.4519896, -122.7924463)
point = Point(-122.7924463,45.4519896)

# check each polygon to see if it contains the point

print js.keys()
#ne = js['objects'].keys()[0]
#print js['objects'][ne]['geometries']

for feature in js['features']:
    polygon = shape(feature['geometry'])
    if polygon.contains(point):
        print 'Found containing polygon:', feature

for feature in js['features']:
    polygon = shape(feature['geometry'])
    if polygon.contains(point):
        print 'Found containing polygon:', feature

for feature in js['features']:
    polygon = shape(feature['geometry'])
    if polygon.contains(point):
        print 'Found containing polygon:', feature

for feature in js['features']:
    polygon = shape(feature['geometry'])
    if polygon.contains(point):
        print 'Found containing polygon:', feature

for feature in js['features']:
    polygon = shape(feature['geometry'])
    if polygon.contains(point):
        print 'Found containing polygon:', feature

for feature in js['features']:
    polygon = shape(feature['geometry'])
    if polygon.contains(point):
        print 'Found containing polygon:', feature

for feature in js['features']:
    polygon = shape(feature['geometry'])
    if polygon.contains(point):
        print 'Found containing polygon:', feature

for feature in js['features']:
    polygon = shape(feature['geometry'])
    if polygon.contains(point):
        print 'Found containing polygon:', feature

for feature in js['features']:
    polygon = shape(feature['geometry'])
    if polygon.contains(point):
        print 'Found containing polygon:', feature

for feature in js['features']:
    polygon = shape(feature['geometry'])
    if polygon.contains(point):
        print 'Found containing polygon:', feature

for feature in js['features']:
    polygon = shape(feature['geometry'])
    if polygon.contains(point):
        print 'Found containing polygon:', feature
