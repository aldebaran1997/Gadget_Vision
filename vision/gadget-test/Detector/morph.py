import cv2
import numpy as np
import auto_canny as auto
import imutils

class morph() :

    def __init__(self) :

        # kernel
        self.ksize = 3
        self.linek = np.zeros((2*(self.ksize)+1, 2*(self.ksize)+1), dtype=np.uint8)
        self.linek[self.ksize, ...] = 1
        self.kernel = np.ones((3,3),np.uint8)
        self.sharpk2 = np.array([[-1,-1,-1,-1,-1],[-1,2,2,2,-1],[-1,2,8,2,-1],[-1,2,2,2,-1],[-1,-1,-1,-1,-1]])/8
        self.iter = 1

    def MorphDetect(self, img) :
        # image gray, Blur, threshold
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#        cv2.imshow("gray",gray)
#        gray = cv2.morphologyEx(gray, cv2.MORPH_ERODE, self.kernel, iterations=2)
        #gray = cv2.filter2D(gray, -1, self.sharpk2)
        gray = cv2.medianBlur(gray, 5)
        gray = auto.AutoCanny(gray)
        gray = cv2.morphologyEx(gray, cv2.MORPH_DILATE, self.kernel, iterations=3)
        ret, gray = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
#        ret, gray = cv2.threshold(gray, 120, 255, cv2.THRESH_TOZERO)
        # morpohology
        u = gray.copy()
        v = gray.copy()
        w = gray.copy()
#        totalimg = gray.copy()
#        totalimg[ : , : ]=0
        v = np.transpose(v)
#        for angle in range(0, 180, 45):
#            # rotate the image and display it
#            rotated = imutils.rotate(w, angle=angle)
#            rotated = cv2.morphologyEx(rotated, cv2.MORPH_OPEN, self.linek, iterations=self.iter)
#            rotated = imutils.rotate(rotated, angle=-angle)
#            totalimg = totalimg | rotated
#            cv2.imshow("Angle=%d" % (angle), rotated)

        u = cv2.morphologyEx(u, cv2.MORPH_OPEN, self.linek, iterations=self.iter)
        v = cv2.morphologyEx(v, cv2.MORPH_OPEN, self.linek, iterations=self.iter)
        v = np.transpose(v)

        wgray = u|v
        #wgray = cv2.morphologyEx(wgray, cv2.MORPH_DILATE, self.kernel, iterations=self.iter)
#        cv2.imshow("totalimg", totalimg)
        wgray = cv2.resize(wgray,(300,300))
        w = cv2.resize(w, (300, 300))
        gray = cv2.resize(gray,(300, 300))
        cv2.imshow("wgray",wgray)
        result = ((wgray-gray), wgray , gray)
        #result = wgray

        return result
'''
import cv2
import numpy as np
import auto_canny as auto
import imutils

class morph() :

    def __init__(self) :

        self.ksize = 3
        self.iter = 1
        self.kernel = np.ones((3,3),np.uint8)
        self.linek = np.zeros((2*(self.ksize)+1, 2*(self.ksize)+1), dtype=np.uint8)
        self.linek[self.ksize, ...] = 1

    def MorphDetect(self, img) :

        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Grey",img)

#        ret, img = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY)
        img = auto.AutoCanny(img)

        totalimg = img.copy()
        totalimg[ : , : ]=0

        for angle in range(0, 180, 45):
            # rotate the image and display it
            rotated = imutils.rotate(img, angle=angle)
            rotated = cv2.morphologyEx(rotated, cv2.MORPH_OPEN, self.linek, iterations=self.iter)
            rotated = imutils.rotate(rotated, angle=-angle)
            totalimg = totalimg | rotated
            cv2.imshow("Angle=%d" % (angle), rotated)
#        cv2.imshow("Binary",img)

        img_h = img.copy()
        img_v = img.copy()
        img_v = np.transpose(img_v)

        img_h = cv2.morphologyEx(img_h, cv2.MORPH_OPEN, self.linek, iterations=self.iter)
        img_v = cv2.morphologyEx(img_v, cv2.MORPH_OPEN, self.linek, iterations=self.iter)
        img_v = np.transpose(img_v)

        img = cv2.addWeighted(img_h,1,img_v,1,0)

        return img
'''