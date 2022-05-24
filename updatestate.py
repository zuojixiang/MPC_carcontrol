from std_msgs.msg import Float64
import time
import rospy
from math import *

rospy.init_node('listener1', anonymous=True)
pubupx = rospy.Publisher('upstatex', Float64,  queue_size=10)
pubupy = rospy.Publisher('upstatey', Float64,  queue_size=10)
pubupyaw = rospy.Publisher('upstateyaw', Float64,  queue_size=10)

dt = 0.5  # 时间间隔
Length = 1.0  # 车辆轴距
x = 50.0
y = 600.0
yaw = 0.0
v = 0.0
angle = 0.0

def callbackx(xx):
	global x
	x=xx.data	
def callbacky(yy):
	global y
	y=yy.data	
def callbackyaw(yyaw):
	global yaw
	yaw=yyaw.data	
def callbackv(vv):
	global v
	v=vv.data	
def callbackangle(aangle):
	global angle
	angle=aangle.data	
while(1):
    rospy.Subscriber('/chatterx', Float64, callbackx)
    rospy.Subscriber('/chattery', Float64, callbacky)
    rospy.Subscriber('/chatteryaw', Float64, callbackyaw)
    rospy.Subscriber('/chatterv', Float64, callbackv)
    rospy.Subscriber('/chatterangle', Float64, callbackangle)
    #更新车辆状态
    x += v * cos(yaw) * dt
    y += v * sin(yaw) * dt
    yaw += v / Length * tan(angle) * dt
    
    pubupx.publish(x)	# 发布数据
    #rospy.loginfo(x)	# 输出数据
    pubupy.publish(y)	
    #rospy.loginfo(y)	
    pubupyaw.publish(yaw)	
    #rospy.loginfo(yaw)	
    time.sleep(0.2)#延迟200ms发送
    

