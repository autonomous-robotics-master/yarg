from yarg_control.srv import YargControl, YargControlResponse
import rospy
import RPi.GPIO as GPIO
import time

def handle_open_gripper(req):
    servoPI = 17
    GPIO.setMode(GPIO.BCM)
    GPIO.setup(servoPIN. GPIO.OUT)

    p= GPIO.PWM(servoPIN, 50)
    p.start(2.5)

    if req.command == 0:
        print "Stopping gripper"
        p.stop()
        GPIO.cleanup()
    elif req.command == 1:
        print "Opening gripper"
        while True:
            p.ChangeDutyCycle(12.5)
            time.sleep(0.5)
     else:
         print "Closing gripper"
         while True:
            p.ChangeDutyCycle(2.5)
            time.sleep(0.5)

    print "Request completed"
    return YargControlResponse(True)

def open_gripper_server():
    rospy.init_node('open_gripper_server')
    s = rospy.Service('open_gripper', YargControl, handle_open_gripper)
    rospy.spin()

if __name__ == "__main__":
    open_gripper_server()
