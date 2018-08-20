import cv2
import numpy as np
import distortion
import auto_canny as auto

kernel = np.ones((3,3), np.uint8)

Dist = distortion.distortion()

def dp(gray) :

    j, i = gray.shape[:2]

    points = []
    point_x1 = []
    point_x2 = []
    point_y1 = []
    point_y2 = []

    for x in range(i) :
        for y in range(j) :
            if gray[y,x] == 255 :
                points.append((x,y))
                point_x1.append((x,y))
                break
            else :
                if y==j-1 :
                    points.append((x, 0))
                    point_x2.append((x, 0))
                    break

    for x in range(i) :
        for y in range(j) :
            if gray[j-1-y,x] == 255 :
                points.append((x,j-1-y))
                point_x2.append((x, j-1-y))
                break
            else :
                if y==j-1 :
                    points.append((x,j-1))
                    point_x1.append((x,j-1))
                    break

    for y in range(j) :
        for x in range(i) :
            if gray[y,x] == 255 :
                points.append((x,y))
                point_y1.append((x,y))
                break
            else :
                if x==i-1 :
                    points.append((0, y))
                    point_y2.append((0, y))
                    break

    for y in range(j) :
        for x in range(i) :
            if gray[y,i-1-x] == 255 :
                points.append((i-1-x,y))
                point_y2.append((i-1-x, y))
                break
            else :
                if x==i-1 :
                    points.append((i-1, y))
                    point_y1.append((i-1, y))
                    break

    return tuple([points,point_x1,point_x2,point_y1,point_y2])

cam = cv2.VideoCapture(0)

while(cam.isOpened()) :
    ret, img = cam.read()

    dst = Dist.Undistort(img)

    h, w = dst.shape[:2]

    gray = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)

    dst = auto.AutoCanny(gray)

    dst = dst[20:420, 100:500]

    dst = cv2.morphologyEx(dst, cv2.MORPH_DILATE, kernel, iterations=1)
#    print(dst.shape[:])
    pic = dst.copy()
    pic[:] = 0

    points = dp(dst)

    for (x,y) in points[0] :
        cv2.circle(pic,(x,y),1,(255,255,255),-1)

#    pic = cv2.morphologyEx(pic, cv2.MORPH_OPEN, kernel, iterations=1)

    len_x = []
    len_y = []

    key = cv2.waitKey(10)

    if(key==ord('s')) :
        for (x,y) in points[1] :
            for (u,v) in points[2] :
                if x==u :
                    len_y.append(v-y)
        for (x,y) in points[3] :
            for (u,v) in points[4] :
                if y==v :
                    len_x.append(u-x)
        print(len_x)

    if(key==27) :
        break
    cv2.imshow("scan",pic)
    cv2.imshow("canny",dst)

cam.release()

cv2.destroyAllWindows()