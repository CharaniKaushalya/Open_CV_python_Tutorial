import cv2      #opencv ibrary

img = cv2.imread("open/46c7f2c4c3fe54a194f70ca4a7195871.jpg") #stroe image that want to display use opencv function  "imread"

cv2.imshow("Random Image",img)        #to show image in img variable

cv2.waitKey(0)              #0 Initialize image should be on screen untl cut
cv2.destroyAllWindows()