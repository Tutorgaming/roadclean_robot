# Joystick to cmd_vel
import rospy

class JoystickToVelocities(object):
    """
    Class which get input from joystick
    and output as cmd_vel
    """

    def __init__(self):
        self.active = False
        self.already_stop = False

    def joy_callback(self, msg):
        """
        Callback when receiving joystick command
        calculate the conversion !
        """

        if self.active:
            # it is active - let the cmd_vel go
            self.already_stop = False
            self.publish_cmd_vel(0.0,0.0)
        else:
            if self.already_stop:
                rospy.loginfo("Do Nothing")
            else:
                # First time entering here
                self.already_stop = True
                # Consider sending a single empty cmd_vel here
                self.publish_cmd_vel(0.0,0.0)


    def publish_cmd_vel(self, linear_x, angular_z):
        """
        Publish the velocity to robot
        """
        pass


