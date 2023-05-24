#!/usr/bin/python3


# 
# import random
# import rospy

import rospy
from xsens_awinda_ros_msgs.msg import LinkStateArray
from model_description import XSensAwindaModel
import odio_urdf as urdf

if __name__ == '__main__':

    rospy.init_node('urdf_model_generator', anonymous=True)

    # Get ROS params
    model_name = rospy.get_param("model_name", "human")
    link_state_topic = rospy.get_param("link_state_topic", "link_states")

    # Wait for link state message
    # rospy.loginfo("Waiting for message from \""+link_state_topic+"\" ROS topic...")
    # link_state_msg = rospy.wait_for_message(link_state_topic, LinkStateArray)
    # rospy.loginfo("Message from \""+link_state_topic+"\" ROS topic received.")

    hips_width = 0.5
    chest_width = 0.7
    arm_length = 0.5
    forearm_length = 0.4
    upperleg_length = 0.6
    leg_length = 0.5
    head_size = 0.2
    torso_height = 0.8
    link_size = 0.1

    # Define colors
    orange = urdf.Material(urdf.Color(rgba="0.059 0.475 0.443 1.0"), name="orange")
    yellow = urdf.Material(urdf.Color(rgba="0.961 0.918 0.078 1.0"), name="yellow")
    red = urdf.Material(urdf.Color(rgba="0.925 0.122 0.141 1.0"), name="red")
    purple = urdf.Material(urdf.Color(rgba="0.384 0.267 0.604 1.0"), name="purple")
    blue = urdf.Material(urdf.Color(rgba="0.176 0.404 0.694 1.0"), name="blue")
    green = urdf.Material(urdf.Color(rgba="0.255 0.71 0.29 1.0"), name="green")

    colors = [orange, yellow, red, purple, blue, green]
    # color = random.choice(colors)
    color = orange

    namespace = "model"

    xsens_awinda_model = XSensAwindaModel(namespace+"_", 
                                    namespace,
                                    color, 
                                    hips_width,
                                    torso_height,
                                    chest_width,
                                    head_size,
                                    arm_length,
                                    forearm_length,
                                    upperleg_length,
                                    leg_length,
                                    link_size)

    xsens_awinda_model.generate_model()

    rospy.set_param('robot_description', xsens_awinda_model.get_urdf())