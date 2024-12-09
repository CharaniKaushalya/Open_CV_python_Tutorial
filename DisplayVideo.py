import cv2

video = cv2.VideoCapture("open/24.06.2024 Recording (1).mp4")  #load video into variavle use function "VideoCapture"

#use while loop because video have more than one layer rather than image
while True:     #while loop wil capture all frames or lauyers of video
    success,img = video.read()
    cv2.imshow("sample_video",img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

