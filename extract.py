from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

from pytube import YouTube
import cv2
import time


# Configure Selenium WebDriver
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox")
# service = Service('/path/to/chromedriver')

driver = webdriver.Chrome()


# Navigate to the YouTube shopping page
youtube_shopping_url = 'https://www.youtube.com/channel/UCkYQyvc_i9hXEo4xic9Hh2g'
driver.get(youtube_shopping_url)


time.sleep(5)


videos = driver.find_elements(By.CSS_SELECTOR, 'a#video-title')
video_info = []

for video in videos:
    title = video.get_attribute('title')
    link = video.get_attribute('href')
    video_info.append({'title': title, 'link': link})

# Print the extracted video info
# for info in video_info:
#     print(f"Title: {info['title']}\nLink: {info['link']}\n")

# Close the driver
driver.quit()


def download_video(url, output_path='.'):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path)

for info in video_info:
    download_video(info['link'])

# Step 3: Process Videos to Fetch Product Details
def process_video(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Example processing: Show the frame
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

for info in video_info:
    video_path = f"{info['title']}.mp4"
    process_video(video_path)