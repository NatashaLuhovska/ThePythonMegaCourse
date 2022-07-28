import os
import cv2
print(os.listdir('sample_images'))

for img in os.listdir('sample_images'):
    img_new=cv2.imread(f"sample_images\{img}", 0)
    resized_image=cv2.resize(img_new, (100,100))
    cv2.imshow("Hey",resized_image)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cv2.imwrite(f"sample_images\{img[:-4]}_resized.jpg", resized_image)



#########################################

#import cv2
#import glob

#images=glob.glob("*.jpg")

#for image in images:
#    img=cv2.imread(image,0)
#    re=cv2.resize(img,(100,100))
#    cv2.imshow("Hey",re)
#    cv2.waitKey(500)
#    cv2.destroyAllWindows()
#    cv2.imwrite("resized_"+image,re)