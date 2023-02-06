import json
from yt_extractor import get_video_info, get_audio_url
from api_03 import save_transcript


def save_video_sentiments(url):
    video_info = get_video_info(url)
    url = get_audio_url(video_info)
    if url:
        title = video_info['title']
        title = title.strip().replace(" ", "_").replace("|", "_").replace("#", "_").replace(":", "_").replace(";", "_").replace("?", "_")
       
        title = "data/" + title
        save_transcript(url, title, sentiment_analysis=True)

if __name__ == "__main__":
    
    
   
    save_video_sentiments("https://www.youtube.com/watch?v=qe4CHWulnDs&ab_channel=WIRED")
