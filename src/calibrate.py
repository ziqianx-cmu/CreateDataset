import cv2
import numpy as np
import glob

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

w = 9
h = 6

objp = np.zeros((w*h, 3), np.float32)
objp[:, :2] = np.mgrid[0:w, 0:h].T.reshape(-1, 2)
objp = objp*26.4  # 26.4mm

objpoints = []
imgpoints = []

images = glob.glob('../chessPlates/*.jpg')
i = 0
for fname in images:
    img = cv2.imread(fname)
    h1, w1 = img.shape[0], img.shape[1]
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    u, v = img.shape[:2]
    print(fname)
    ret, corners = cv2.findChessboardCorners(gray, (w, h), None)
    if ret:
        print("i:", i)
        i = i+1
        cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        objpoints.append(objp)
        imgpoints.append(corners)
        cv2.drawChessboardCorners(img, (w, h), corners, ret)
        cv2.namedWindow('findCorners', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('findCorners', 640, 480)
        cv2.imshow('findCorners', img)
        cv2.waitKey(200)
cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = \
    cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)


print("ret:", ret)
print("matrix:\n", mtx)  # [[fx, 0, cx],[0, fy, cy],[0, 0, 1]]
print("distortion:\n", dist)  # distortion: [k_1,k_2,p_1,p_2,k_3]
print("rvecs:\n", rvecs)
print("tvecs:\n", tvecs)
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (u, v), 0, (u, v))
print('newcameramtx', newcameramtx)