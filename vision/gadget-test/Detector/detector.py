import cv2
import client
import morph
import hough
import distortion as dist
import auto_canny as auto

Trans = client.TrasnferClient()
Morph = morph.morph()
Hough = hough.hough(50,100)
Dist = dist.distortion()

p=0
q=0

# construct camera object
cam = cv2.VideoCapture(0)

while(cam.isOpened()) :
    ret, img = cam.read()

    #img = cv2.imread('001_crack.jpg')
    q += 1

    dst = Dist.Undistort(img)

    if(cv2.waitKey(1)==27) :
        break

    m_img = dst.copy()
    h_img = dst.copy()

    h_img = Hough.HoughDetect(h_img)
    totalimg, wgray, gray = Morph.MorphDetect(m_img)

#    m_img = cv2.resize(m_img,(300,300))
#    result = h_img-m_img
#    result = dst

#    cv2.imshow("wgray-gray",totalimg)
#    cv2.imshow("Wgray",wgray)
#    cv2.imshow("Hough",h_img)

    if q > 500 :
#        cv2.imwrite('/home/cae-lab/Desktop/result.png', result)
#        cv2.imwrite('/home/cae-lab/Desktop/result2.png', dst)
#        Trans.Transfer(filename='result.png')
#        Trans.Transfer(filename='result2.png')
        q=0
#        for i in range(len(result)) :
#            for j in range(len(result[i,:])) :
#                p += result[i,j]

#        if p > 1000 * 255 :
#            cv2.imwrite('/home/cae-lab/Desktop/result.png', result)
#            cv2.imwrite('/home/cae-lab/Desktop/result2.png', dst)
#            Trans.Transfer(filename='result.png')
#            Trans.Transfer(filename='result2.png')
#            p=0

cam.release()

cv2.destroyAllWindows()
'''
import cv2
import morph
import hough
import distortion as dist

Morph = morph.morph()
Hough = hough.hough()
Dist = dist.distortion()

# construct camera object
cam = cv2.VideoCapture(0)

while(cam.isOpened()) :

    if(cv2.waitKey(1)==27) :
        break

    ret, img = cam.read()

    img = Dist.Undistort(img)
    cv2.imshow("Original",img)

    img = Morph.MorphDetect(img)
    cv2.imshow("Morph",img)

    img = Hough.HoughDetect(img)
    cv2.imshow("Hough",img)

cam.release()
cv2.destroyAllWindows()
'''