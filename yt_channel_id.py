import requests

api_key = "AIzaSyAmlThKq4RMPAbU7lZKwe34vWnyNkn_GrY"
video_id = "5-mBQZUjjU4"

url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part=snippet"

response = requests.get(url)
data = response.json()

channel_id = data["items"][0]["snippet"]["channelId"]

print(f"頻道ID: {channel_id}")
