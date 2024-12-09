import cv2

video = cv2.VideoCapture(0)  #0 is ID for webCam


while True:
    success,img = video.read()
    cv2.imshow("sample_video",img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

cv2.destroyAllWindows()
