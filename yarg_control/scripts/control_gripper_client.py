from yarg_control.srv import YargControl, YargControlRequest
import sys
import rospy

def open_gripper_client(command):
    rospy.wait_for_service('open_gripper')
    try:
        open_gripper = rospy.ServiceProxy('open_gripper', YargControl)
        resp = open_gripper(command)
        return resp.success
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [command]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        command = int(sys.argv[1])
    else:
        print usage()
        sys.exit(1)
    if command == 0:
        print "Request STOP gripper"
    elif command == 1:
        print "Request OPEN gripper"
    elif command == 2:
        print "Request CLOSE gripper"
    else:
        print "Command not found"
        sys.exit(1)

    print "Request successfully executed= %r"%(open_gripper_client(command))
