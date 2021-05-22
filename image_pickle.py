import pickle
import cv2


img = cv2.imread('1_16.bmp')
cv2.imshow("Before",img)

pickled_img = pickle.dumps(img)
print(pickled_img)

unpickled_img = pickle.loads(pickled_img)
print(unpickled_img)

cv2.imshow("after",unpickled_img)
cv2.waitKey(0)
