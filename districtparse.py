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

# Sample Code

# Returns a list of counts used by the other two functions
counts = parseZips('Problem at 19102 please respond.')
print(counts)

# Returns a list of zip codes with counts greater than 0
print(getZips(counts))

# Returns the number of incidents for a given zip code
print(getZipCount(19102, counts))