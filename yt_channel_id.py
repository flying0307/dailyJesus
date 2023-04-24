import requests

api_key = "AIzaSyCOEsnzSTK11gzbP5SG_cgLCje5saWyO-A"
video_id = "FMBX9HITbhQ"

url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part=snippet"

response = requests.get(url)
data = response.json()

channel_id = data["items"][0]["snippet"]["channelId"]

print(f"頻道ID: {channel_id}")
