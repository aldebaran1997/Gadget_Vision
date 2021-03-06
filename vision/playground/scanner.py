#Import modules
import cv2
import numpy as np
import auto_canny as auto
import distortion

#Kernel for morphologyEx
kernel = np.ones((3,3), np.uint8)

#Calibration object (custom class)
Dist = distortion.distortion()

#Image border construction
def dp(img) :

    j, i = img.shape[:2]

    points = []
    point_x1 = []
    point_x2 = []
    point_y1 = []
    point_y2 = []

    #Border from up to down
    for x in range(i) :
        for y in range(j) :
            if img[y,x] == 255 :
                points.append((x,y))
                point_x1.append((x,y))
                break
            else :
                if y==j-1 :
                    points.append((x, 0))
                    point_x1.append((x, 0))
                    break

    #Border from down to up
    for x in range(i) :
        for y in range(j) :
            if img[j-1-y,x] == 255 :
                points.append((x,j-1-y))
                point_x2.append((x, j-1-y))
                break
            else :
                if y==j-1 :
                    points.append((x,j-1))
                    point_x2.append((x,j-1))
                    break

    #Border from left to right
    for y in range(j) :
        for x in range(i) :
            if img[y,x] == 255 :
                points.append((x,y))
                point_y1.append((x,y))
                break
            else :
                if x==i-1 :
                    points.append((0, y))
                    point_y1.append((0, y))
                    break

    #Border from right to left
    for y in range(j) :
        for x in range(i) :
            if img[y,i-1-x] == 255 :
                points.append((i-1-x,y))
                point_y2.append((i-1-x, y))
                break
            else :
                if x==i-1 :
                    points.append((i-1, y))
                    point_y2.append((i-1, y))
                    break

    return tuple([points,point_x1,point_x2,point_y1,point_y2])

#Webcam object
cam = cv2.VideoCapture(0)

while(cam.isOpened()) :

    #Input key
    key = cv2.waitKey(10)

    #Program exit
    if(key==27) :
        break
    
    #Get webcam screen
    ret, img = cam.read()

    #Calibrating webcam
    dst = Dist.Undistort(img)

    h, w = dst.shape[:2]

    #Grayscale image
    gray = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)

    #Canny image
    dst = auto.AutoCanny(gray)

    #Crop image
    dst = dst[15:415, 100:500]

    #Dilate to enhance image
    dst = cv2.morphologyEx(dst, cv2.MORPH_DILATE, kernel, iterations=1)
    
    #Construct blank image
    pic1 = dst.copy()
    pic1[:] = 0
    pic2 = dst.copy()
    pic2[:] = 0

    #Get border points
    points = dp(dst)

    #Visualize border image
    for (x,y) in points[0] :
        cv2.circle(pic1,(x,y),1,(255,255,255),-1)
    
    #Thickness of x and y
    len_x = []
    len_y = []

    #Press 's' to get and visualize thickness
    if(key==ord('s')) :
        
        #y-thickness (up-down)
        for (x,y) in points[1] :
            for (u,v) in points[2] :
                if x==u :
                    len_y.append(v-y)
        #x-thickness (right-left)
        for (x,y) in points[3] :
            for (u,v) in points[4] :
                if y==v :
                    len_x.append(u-x)
        #Visualize
        for j in range(len(points[2])) :
            for i in range(len(points[1])) :
                cv2.circle(pic2,(i,j),1,(np.sqrt(len_x[i]*len_y[j])/2,np.sqrt(len_x[i]*len_y[j])/2,np.sqrt(len_x[i]*len_y[j])/2),-1)
        cv2.imshow("Art of Goo",pic2)
        
    #Monitor
    cv2.imshow("Border",pic1)
    cv2.imshow("Canny",dst)

#Finalize
cam.release()
cv2.destroyAllWindows()
