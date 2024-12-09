import cv2 as cv

# Use OpenCV's built-in path for the Haar cascade file
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")



# Load an image (update the path to your image)
image = cv.imread("open/faces.jpg")

# Convert to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image
cv.imshow("Face Detector", image)

cv.waitKey(0)
cv.destroyAllWindows()
