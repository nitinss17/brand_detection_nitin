import cv2
import os

dirs = '/home/nitin/Desktop/bigcity_assignment/github/data_norm/'
l = os.listdir(dirs)

for i in l:
    n = i.split('.')[0]
    e = i.split('.')[1]
    if e != 'xml' and e != 'txt' and e!= 'py':
        orig = cv2.imread(dirs+i)
        gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(dirs+n+'.jpg',gray)
