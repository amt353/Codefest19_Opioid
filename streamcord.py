# from https://stackoverflow.com/questions/4247248/record-streaming-and-saving-internet-radio-in-python

import requests

stream_url = 'http://relay.broadcastify.com/pm1vgh6kftnxr2c.mp3'

r = requests.get(stream_url, stream=True)

with open('stream.mp3', 'wb') as f:
    try:
        for block in r.iter_content(1024):
            f.write(block)
    except KeyboardInterrupt:
        pass