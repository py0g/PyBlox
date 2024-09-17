# pip install requests opencv pytube

import cv2
import requests
from pytube import YouTube

def frame_to_emojis(frame):
    height, width, _ = frame.shape
    emojis = ""
    for y in range(height):
        for x in range(width):
            b, g, r = frame[y, x]
            if r > 200 and g < 50 and b < 50:
                emojis += "🔴"  # Red
            elif r < 50 and g > 200 and b < 50:
                emojis += "🟢"  # Green
            elif r < 50 and g < 50 and b > 200:
                emojis += "🔵"  # Blue
            elif r > 200 and g > 200 and b < 50:
                emojis += "🟡"  # Yellow
            elif r < 50 and g > 200 and b > 200:
                emojis += "🟦"  # Cyan
            elif r > 200 and g < 50 and b > 200:
                emojis += "🟪"  # Magenta
            elif r > 200 and g > 200 and b > 200:
                emojis += "⚪"  # White
            elif r < 50 and g < 50 and b < 50:
                emojis += "⚫"  # Black
            elif r > 150 and g > 150 and b < 150:
                emojis += "🟠"  # Orange
            elif r > 150 and g < 150 and b < 50:
                emojis += "🟤"  # Brown
            elif r < 50 and g > 150 and b < 50:
                emojis += "🟩"  # Light Green
            elif r < 150 and g < 150 and b > 150:
                emojis += "🟦"  # Light Blue
            elif r > 100 and g < 50 and b < 100:
                emojis += "🟥"  # Dark Red
            elif r < 100 and g > 50 and b < 100:
                emojis += "🟫"  # Dark Green
            elif r < 100 and g < 100 and b > 100:
                emojis += "🟪"  # Dark Blue
            elif r < 150 and g > 150 and b < 50:
                emojis += "🟧"  # Olive
            else:
                emojis += "⚫"  # Black as a default
        emojis += "\n"
    return emojis

yt = YouTube('https://www.youtube.com/watch?v=VIDEO_ID')
stream = yt.streams.filter(file_extension='mp4').first()
stream.download(filename='video.mp4')

cap = cv2.VideoCapture('video.mp4')

roblox_server_url = 'http://localhost:3000/send_frame'

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (16, 16))
    emojis = frame_to_emojis(frame)

    response = requests.post(roblox_server_url, json={'frame': emojis})
    print(response.text)

cap.release()
