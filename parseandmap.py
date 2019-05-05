import googlemaps
import json
import webbrowser
from datetime import datetime

def parseZips(transcript):
    text = transcript.split()
    philly = [19142, 19128, 19118, 19140, 19148, 19102, 19152, 19154, 19145, 19120 , 19141 , 19149, 19136, 19114, 19115, 19146, 19130, 19107, 19122, 19106, 19143, 19112, 19103, 19133, 19124, 19153, 19131, 19104, 19121, 19144, 19150, 19123, 19125, 19111, 19151, 19139, 19126, 19134, 19137, 19127, 19129, 19132,19119, 19147,19138, 19135, 19116]
    counts = [0] * 47
    for word in text:
        i = -1
        for zips in philly:
            i += 1
            if str(zips) == word:
                counts[i] += 1
    return counts

def getZipCount(zipcode, counts):
    philly = [19142, 19128, 19118, 19140, 19148, 19102, 19152, 19154, 19145, 19120 , 19141 , 19149, 19136, 19114, 19115, 19146, 19130, 19107, 19122, 19106, 19143, 19112, 19103, 19133, 19124, 19153, 19131, 19104, 19121, 19144, 19150, 19123, 19125, 19111, 19151, 19139, 19126, 19134, 19137, 19127, 19129, 19132,19119, 19147,19138, 19135, 19116]
    i = -1
    for zips in philly:
        i += 1
        if zips == zipcode:
            return counts[i]
        
def getZips(counts):
    philly = [19142, 19128, 19118, 19140, 19148, 19102, 19152, 19154, 19145, 19120 , 19141 , 19149, 19136, 19114, 19115, 19146, 19130, 19107, 19122, 19106, 19143, 19112, 19103, 19133, 19124, 19153, 19131, 19104, 19121, 19144, 19150, 19123, 19125, 19111, 19151, 19139, 19126, 19134, 19137, 19127, 19129, 19132,19119, 19147,19138, 19135, 19116]
    i = -1
    zips = []
    for num in counts:
        i += 1
        if num > 0:
            zips.append(philly[i])
    return zips

def getMap(zips):
    gmaps = googlemaps.Client(key='AIzaSyAuhI_akYRWtJFWXmGmJDSRgzAQB_T7VZ8')
    url = 'https://maps.googleapis.com/maps/api/staticmap?center=Philadelphia,+PA&zoom=11&size=1920x1080&maptype=roadmap'
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
    print(url)
    webbrowser.open(url)




# Sample Code
transcript = 'There is a man passed out on the corner of 5th and Market zipcode 19104 nearby Drexel University Copy that got a man drugged out here in the 19102 brought in a woman from 19152 bout an hour ago too'
counts = parseZips(transcript)
zips = getZips(counts)
print(zips)
getMap(zips)