import cv2
import  numpy as np

img=cv2.imread("img.jpg",0)
laplacian=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
laplacian=np.uint8(np.absolute(laplacian))
cv2.imshow("lap",laplacian)
cv2.imshow("img",img)
cv2.imwrite("D:\projects\python_pycharm\Laplacian\output.jpg",laplacian,None)
cv2.waitKey(0)
cv2.destroyWindow()