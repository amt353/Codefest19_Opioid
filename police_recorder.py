import time
import requests

def record(current_file, r, t_end):
    with open('stream' + str(current_file) + '.mp3', 'wb') as f:
        try:
            for block in r.iter_content(1024):
                f.write(block)
                if time.time() > t_end:
                    return
        except Exception as ex:
            pass

def changeFile(current_file):
    if current_file == 1:
        current_file = 2
    else:
        current_file = 1
    return current_file

stream_url = 'http://relay.broadcastify.com/1nzh0567c3yvbr2.mp3'

current_file = 1
r = requests.get(stream_url, stream=True)

# range(x) where x is the number of files to record
# time.time() + x where x is the number in seconds for each recording (after the first recording)
for i in range(1):
    t_end = time.time() + 5
    record(current_file, r, t_end)
    
    # Uncomment the line below to switch between two files called stream1.mp3 and stream2.mp3
    #current_file = changeFile(current_file)
    
    # Comment the line below to switch between two files called stream1.mp3 and stream2.mp3
    current_file += 1