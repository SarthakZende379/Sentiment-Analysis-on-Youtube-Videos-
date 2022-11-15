from importlib import reload
import os
import urllib
import sys
reload(sys)
#sys.setdefaultencoding('utf8')
from google import oauth2
import google.oauth2.credentials
import google_auth_oauthlib.flow



import oauth2client.tools

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyDrNxd38b7yuFQh5HVCd7KuXcz5_8xTiYU"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
  developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  videos = []

  # Add each result to the appropriate list, and then display the lists of videos
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],search_result["id"]["videoId"]))

  #Write results to file
  with open('video_list.txt', 'w', encoding="utf-8") as video_file:
    video_file.write("Videos: ")
    for video in videos:
      video_file.write("\n")
      video_file.write(video)
  video_file.close


if __name__ == "_main_":
  argparser.add_argument("--q", help="Search term", default="hate speech")        #default specifies the keywords to be searched 
  argparser.add_argument("--max-results", help="Max results", default=50)
  args = argparser.parse_args()

  try:
    youtube_search(args)
  except urllib.error.HTTPError as e:
    print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))