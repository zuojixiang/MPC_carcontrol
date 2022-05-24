import cv2 as cv
import os
import rospy
import time
import numpy as np
from std_msgs.msg import Float64MultiArray, Int16
from cv_bridge import CvBridge , CvBridgeError
maxsize = (1080, 720)  # 定义图片放缩大小
img = cv.imread('1.png')
img = cv.resize(img, maxsize, cv.INTER_AREA)
os.remove('points.txt')
# 鼠标事件
def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        # 画圈（图像:img，坐标位置:xy，半径:1(就是一个点)，颜色:蓝，厚度：-1(就是实心)
        cv.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
        cv.putText(img, xy, (x, y), cv.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), thickness=1)
        cv.imshow("click some points with mouse to pass!", img)
        #写入txt
        x_str = str(x)
        y_str = str(y)
        f = open(r"points.txt", "a+")
        f.writelines(x_str + ' ' + y_str + '\n')
cv.namedWindow("click some points with mouse to pass!")
cv.resizeWindow("click some points with mouse to pass!", 800, 600) #设置窗口大小
cv.setMouseCallback("click some points with mouse to pass!", on_EVENT_LBUTTONDOWN)
cv.imshow("click some points with mouse to pass!", img)
#回车键退出
key=1
while (key!=13):
    key = cv.waitKey(1) & 0xFF
    break
cv.waitKey(0)
cv.destroyAllWindows()
data_list = np.loadtxt("points.txt")
n=np.shape(data_list)[0]
print(data_list)
rospy.init_node('talker', anonymous=True)
pub = rospy.Publisher('chatter', Float64MultiArray,  queue_size=10)
rate = rospy.Rate(10)
time.sleep(0.5)
for i in range(n):
		data = Float64MultiArray(data=data_list[i])	# 二维数组依次发送
		pub.publish(data)	# 发布数据
		rospy.loginfo(data)	# 输出数据
		rate.sleep()
