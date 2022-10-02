import json
from yt_extraction import get_audio_url, get_video_info
from api_comunication import save_transcript

def save_video_sentiments(url):
    video_infos = get_video_info(url)
    audio_url = get_audio_url(video_infos)
    title = video_infos['title']
    title = title.strip().replace(" ", "_")
    #title = "data/" + title
    save_transcript(audio_url, title, sentiment_analysis= True)

if __name__ == '__main__':
    save_video_sentiments('https://www.youtube.com/watch?v=fm0BKFADG14')#'https://www.youtube.com/watch?v=fa6mgRoDRak')