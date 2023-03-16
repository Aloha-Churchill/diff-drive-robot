# ROS Client Library for Python
import rclpy
# Handles the creation of nodes
from rclpy.node import Node
# Handles string messages
from sensor_msgs.msg import LaserScan
 
class MinimalSubscriber(Node):
  """
  Create a subscriber node
  """
  def __init__(self):
    # Initiate the Node class's constructor and give it a name
    super().__init__('minimal_subscriber')
 
    # The node subscribes to messages of type std_msgs/String, 
    # over a topic named: /scan
    # The callback function is called as soon as a message is received.
    # The maximum number of queued messages is 10.
    self.subscription = self.create_subscription(
      LaserScan,
      'scan',
      self.listener_callback,
      10)
    self.subscription  # prevent unused variable warning

  def listener_callback(self, msg):
    #Display a message on the console every time a message is received on the scan topic

    #the scan msg has 720 elements in its array as the lidar scans 2 points per degree of rotation
    #therefore, if we want a FOV of 120deg, we want the first 60 elements in the array and the last 60 elements in the array
    #because the lidar scan starts when the lidar is pointing forwwards
    #so to cover the first 60 degrees of rotation, we need the first 120 elements in the array, and same for the last 60 deg
    first_slice = msg.ranges[0:121]
    last_slice = msg.ranges[600:721]
    #self.get_logger().info('I heard: "%s"' % msg.ranges)
    #print("Loop")
    if True in [x < 1 for x in first_slice]:
      print("Object right of center")
    if True in [x < 1 for x in last_slice]:
      print("Object left of center")
 
def main(args=None):
 
  # Initialize the rclpy library
  rclpy.init(args=args)
 
  # Create a subscriber
  minimal_subscriber = MinimalSubscriber()
 
  # Spin the node so the callback function is called.
  # Pull messages from any topics this node is subscribed to.
  rclpy.spin(minimal_subscriber)
 
  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  minimal_subscriber.destroy_node()
   
  # Shutdown the ROS client library for Python
  rclpy.shutdown()
 
if __name__ == '__main__':
  main()