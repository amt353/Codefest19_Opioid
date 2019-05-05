import googlemaps
import json
import webbrowser
from datetime import datetime

streets = [line.rstrip('\n') for line in open('streets.txt')]
zipcodes = [19142, 19128, 19118, 19140, 19148, 19102, 19152, 19154, 19145, 19120 , 19141 , 19149, 19136, 19114, 19115, 19146, 19130, 19107, 19122, 19106, 19143, 19112, 19103, 19133, 19124, 19153, 19131, 19104, 19121, 19144, 19150, 19123, 19125, 19111, 19151, 19139, 19126, 19134, 19137, 19127, 19129, 19132,19119, 19147,19138, 19135, 19116]

def parseZips(transcript):
    text = transcript.split()
    counts = [0] * len(zipcodes)
    for word in text:
        i = -1
        for zips in zipcodes:
            i += 1
            if str(zips) == word:
                counts[i] += 1
    return counts

def getZipCount(zipcode, counts):
    i = -1
    for zips in zipcodes:
        i += 1
        if zips == zipcode:
            return counts[i]
        
def getZips(counts):
    i = -1
    zips = []
    for num in counts:
        i += 1
        if num > 0:
            zips.append(zipcodes[i])
    return zips

def parseStreets(transcript):
    text = transcript.split()
    streetnames = []
    counts = [0] * len(streets)
    for word in text:
        i = -1
        for roads in streets:
            i += 1
            if roads == word:
                counts[i] += 1
                streetnames.append(streets[i])
    return counts, streetnames

def getMapZips(zips):
    gmaps = googlemaps.Client(key='AIzaSyAuhI_akYRWtJFWXmGmJDSRgzAQB_T7VZ8')
    url = 'https://maps.googleapis.com/maps/api/staticmap?center=Philadelphia,+PA&zoom=11&size=1920x1080&maptype=terrain'
    for zipcode in zips:
        # Geocoding an address
        geocode_result = gmaps.geocode('Philadelphia, PA ' + str(zipcode))

        geocode_result = str(geocode_result)
        geocode_result = geocode_result.replace("\'", "\"")
        wjdata = json.loads(str(geocode_result))

        lat = wjdata[0]['geometry']['location']['lat']
        lng = wjdata[0]['geometry']['location']['lng']

        url = url + '&markers=color:red%7C' + str(lat) + ',' + str(lng)
    
    url = url + '&key=AIzaSyAuhI_akYRWtJFWXmGmJDSRgzAQB_T7VZ8'
    webbrowser.open(url)

def getMapStreets(streetname):
    streetnames = streetname
    gmaps = googlemaps.Client(key='AIzaSyAuhI_akYRWtJFWXmGmJDSRgzAQB_T7VZ8')
    url = 'https://maps.googleapis.com/maps/api/staticmap?center=Philadelphia,+PA&zoom=11&size=1920x1080&maptype=terrain'
    for i in range(len(streetnames)):
        # Geocoding an address
        if len(streetnames) >= 2:
            geocode_result = gmaps.geocode(streetnames[0] + ' and ' + streetnames[1] + ' Philadelphia, PA')
            streetnames.pop(0)
            streetnames.pop(0)
            i += 1
        elif len(streetnames) == 1:
            geocode_result = gmaps.geocode(streetnames[0] + ' Philadelphia, PA')

        geocode_result = str(geocode_result)
        geocode_result = geocode_result.replace("\'", "\"")
        wjdata = json.loads(str(geocode_result))

        lat = wjdata[0]['geometry']['location']['lat']
        lng = wjdata[0]['geometry']['location']['lng']

        url = url + '&markers=color:red%7C' + str(lat) + ',' + str(lng)
    
    url = url + '&key=AIzaSyAuhI_akYRWtJFWXmGmJDSRgzAQB_T7VZ8'
    webbrowser.open(url)



# Sample Code

transcript = 'There is a man passed out on the corner of 5th and Market zipcode 19104 nearby Drexel University Copy that got a man drugged out here in the 19102 brought in a woman from 19152 bout an hour ago too'
#counts = parseZips(transcript)
#zips = getZips(counts)
#zips = [19104, 19102, 19142, 19128, 19118]
#getMapZips(zips)
#transcript = 'A man on 34th and Market is in pursuit'
counts, roadnames = parseStreets(transcript)
with open('log.txt', 'w') as f:
    for road in roadnames:
        f.write("%s\n" % road)
getMapStreets(roadnames)
