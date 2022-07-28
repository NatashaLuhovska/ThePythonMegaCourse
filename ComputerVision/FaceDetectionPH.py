import cv2

face_cascade=cv2.CascadeClassifier("FilesImage\haarcascade_frontalface_default.xml")

img=cv2.imread("FilesImage\my_photo.jpg")
img=cv2.resize(img, (int(img.shape[1]/5),int(img.shape[0]/5)))
cv2.imshow("Gray", img)
cv2.waitKey(1000)
cv2.destroyAllWindows()

gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.05,
minNeighbors=5)

print(faces)   # поверне список з 4ох елементів
               # перші два значення координати вершини чотирикутника
               # інші дві це висота і ширина

for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)


cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

