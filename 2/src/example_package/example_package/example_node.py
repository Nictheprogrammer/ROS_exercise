#!/usr/bin/python3
import os
import rclpy
from rclpy.node import Node

# Fill in something for msg type imports
# from duckietown_msgs.msg import SOMETHING
# from std_msgs.msg import SOMETHING
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class SkeletonNode(Node):
    def __init__(self):
        super().__init__('example_node')
        #Create publishers and subscribers in init, use callback
        self.pub= self.create_publisher(String, 'nicolas', 10)
        self.counter=0
        self.timer=self.create_timer(1.0, self.publish_msg)
    #Define callback functions here
    def publish msg(self):
        msg = String()
        msg.data = 'Hello World'
        self.pub.publish(msg)
        self.counter+=1


def main():
    print('In main')
    rclpy.init()
    node = SkeletonNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
