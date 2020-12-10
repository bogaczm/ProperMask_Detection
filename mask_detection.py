import cv2

image = cv2.imread('C:\\Users\\moko\\Desktop\\ProperMask_Detection\\NoMask_ae275d9e-34d5-11eb-a639-347df6021425.jpg')

img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)

if len(faces) != 0:
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('Oryginal', image)
cv2.imshow('Gray', img_gray)

cv2.waitKey(0)
