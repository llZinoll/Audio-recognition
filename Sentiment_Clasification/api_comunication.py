import requests
from api_secrets import API_KEY_ASSEMBLYAI
import json
import time
#Upload

aupload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcrpt_endpoint = 'https://api.assemblyai.com/v2/transcript'

headers = {'authorization': API_KEY_ASSEMBLYAI}

def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    upload_response = requests.post(aupload_endpoint,
                            headers=headers,
                            data=read_file(filename))

    audio_url = upload_response.json()['upload_url']
    return audio_url
#Trancribe
def transcribe(audio_url, sentiment_analysis):
    transcript_request = { "audio_url": audio_url,
                            'sentiment_analysis': sentiment_analysis }

    transcript_response = requests.post(transcrpt_endpoint, json=transcript_request, headers=headers)
    job_id =  transcript_response.json()['id']
    return job_id


#Poll
def poll(transcript_id):
    polling_endpoint = transcrpt_endpoint + "/" + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()

def get_transcription_result_url(audio_url, sentiment_analysis):
    transcript_id = transcribe(audio_url, sentiment_analysis)
    while True:
        data = poll(transcript_id)
        if data['status'] == 'completed':
            return data,None
        elif data['status'] == 'error':
            return data,data['error']

        print('Wainting 30 seconds')
        time.sleep(30)

#Save transcript
def save_transcript(audio_url, title, sentiment_analysis = False):
    data, error = get_transcription_result_url(audio_url, sentiment_analysis)

    if data:
        text_file = './Sentiment_Clasification/data/' + title + ".txt"

        with open(text_file, "w") as f:
            f.write(data['text'])
        
        if sentiment_analysis:
            filename = './Sentiment_Clasification/data/'+title + "_sentiments.json"
            with open(filename, 'w') as f:
                sentiments = data['sentiment_analysis_results']
                json.dump(sentiments, f, indent= 4)
        print('transcription save')
    elif error:
        print('Error', error)