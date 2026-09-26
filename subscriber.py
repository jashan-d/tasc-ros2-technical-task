import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RoverControlSubscriber(Node):
    def __init__(self):
        #Initializes the node and name            
        super().__init__('rover_control_subscriber')
	#creates a subscriber that listens to the same topic the publisher is broadcasting on
        self.subscription = self.create_subscription(
            String,
            '/rover/front_distance_sensor',
            self.listener_callback,   #This function gets triggered each time a new message comes
            10
        )

    def listener_callback(self, msg):
	#This prints the sensor data to the terminal so the controller can "see" it.
        self.get_logger().info(f'Received by Controller: "{msg.data}"')

def main(args=None):
    #ROS 2 starts  
    rclpy.init(args=args)
    node = RoverControlSubscriber()
    try:   #node runs in a infinite loop listening for new messages
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass  #program can exit cleanly
    node.destroy_node()  #Node gets destroyed and ROS 2 is shut down
    rclpy.shutdown()

if __name__ == '__main__':
    main()
