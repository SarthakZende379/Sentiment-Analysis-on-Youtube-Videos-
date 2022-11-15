
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

ids = ['nP6BRgrfmI4', 'M9ovHqv_k-g', 'hSINHJdLDdk']

for id in ids:
    video = YouTubeTranscriptApi.get_transcript(id)


    formatter = TextFormatter()
    text_file = formatter.format_transcript(video)
    text = str(text_file)

    with open('{}.txt'.format(id), 'w', encoding='utf-8') as text_file:
        text_file.write(text)
        
