import time
import datetime
import requests
from pydub import AudioSegment
from google.cloud import storage

def live_transcribe():
    
    #tracks the start time for the radio recording sequence
    starttime = time.time()


    def record(current_file, r, t_end, stream_file_name):
        curr_time = str(datetime.datetime.now())
        curr_time = curr_time.replace(".", "")
        curr_time = curr_time.replace(" ","")
        curr_time = curr_time.replace(":","_")
        stream_file_name = ('stream' + '.mp3')
        with open(stream_file_name, 'wb') as f:
            try:
                for block in r.iter_content(1024):
                    f.write(block)
                    if time.time() > t_end:
                        break
            except Exception as ex:
                pass
        return stream_file_name

    def changeFile(current_file):
        if current_file == 1:
            current_file = 2
        else:
            current_file = 1
        return current_file

    stream_url = 'http://relay.broadcastify.com/pm1vgh6kftnxr2c.mp3'

    current_file = 1
    r = requests.get(stream_url, stream=True)
    stream_file_name = ""
    
    # range(x) where x is the number of files to record
    # time.time() + x where x is the number in seconds for each recording (after the first recording)
    #for i in range(1):
    t_end = time.time() + 1
    thefile = record(current_file, r, t_end, stream_file_name)

    t_end = time.time() + 59
    thefile = record(current_file, r, t_end, stream_file_name)
    
    # Uncomment the line below to switch between two files called stream1.mp3 and stream2.mp3
    #current_file = changeFile(current_file)
    
    # Comment the line below to switch between two files called stream1.mp3 and stream2.mp3
    current_file += 1
    print(thefile)
    endtime = time.time()
    print(endtime - starttime)
    ###################################################
    startimet = time.time()
    print("converting file")
    song = AudioSegment.from_mp3(thefile)
    thefile = thefile.replace(".mp3", "")
    song.export(thefile + ".flac",format = "flac")
    print("done")
    thefile = thefile + ".flac"

    ###################################################

    def upload_blob(bucket_name, source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print('File {} uploaded to {}.'.format(
            source_file_name,
            destination_blob_name))

    bucket_name = "transcribe_ems"
    source_file_name = thefile
    destination_blob_name = thefile
    upload_blob(bucket_name, source_file_name, destination_blob_name)

    ###################################################

    def transcribe_gcs(gcs_uri, transcript):
        """Asynchronously transcribes the audio file specified by the gcs_uri."""
        from google.cloud import speech
        from google.cloud.speech import enums
        from google.cloud.speech import types
        client = speech.SpeechClient()

        transcript = "" 
        audio = types.RecognitionAudio(uri=gcs_uri)
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
            sample_rate_hertz=22050,
            language_code='en-US',
            model="video")

        operation = client.long_running_recognize(config, audio)

        print('Waiting for operation to complete...')
        response = operation.result(timeout=1000)

        # Each result is for a consecutive portion of the audio. Iterate through
        # them to get the transcripts for the entire audio file.
        for result in response.results:
            # The first alternative is the most likely one for this portion.
            print(u'Transcript: {}'.format(result.alternatives[0].transcript))
            print('Confidence: {}'.format(result.alternatives[0].confidence))
            transcript += result.alternatives[0].transcript + " "
        return transcript

    print("YOLO")
    transcript = ""
    transcript = transcribe_gcs('gs://transcribe_ems/' + thefile, transcript)
    print(transcript)
    f = open('filename.txt', 'a')
    f.write(transcript + " ")
    f.close()
    # upload files to gcs here: 
    endtime = time.time()
    print(endtime-starttime)
###################################################

while True:
    live_transcribe()
