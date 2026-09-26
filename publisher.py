import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class RoverSensorPublisher(Node):
    def __init__(self):
	#This initializes the node and name
        super().__init__('rover_sensor_publisher')
	#Creates a publisher that broadcasts the String messages to the topic (topic basically means the publisher and subscirber can communicate over a dedicated channel. like a data pipeline.)
	# 10 is the queue size
        self.publisher_ = self.create_publisher(String, '/rover/front_distance_sensor', 10)
	#This sets a timer to run timer_callback function every 1.0 seconds
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        # This simulates a distance sensor which reads in meters by picking a random number between 0.5 and 5.0
        simulated_distance = round(random.uniform(0.5, 5.0), 2)
	# Here it automatically flags the status as an obstacle if the distance drops to 1.5 meters or less
        status = "CLEAR" if simulated_distance > 1.5 else "OBSTACLE DETECTED"
	#This packages the distance adn status into a readable string
        msg.data = f"Distance: {simulated_distance} m | Status: {status}"
        
        # broadcasting the message to the topic
        self.publisher_.publish(msg)
        #This prints the data into the terminal so we can see visually if it is working
        self.get_logger().info(f'Publishing Sensor Data: "{msg.data}"')

def main(args=None):
    #Starts the ROS 2 
    rclpy.init(args=args)
    node = RoverSensorPublisher()
    try:
        #This keeps the node running in a infinite loop until manually stopped   
        rclpy.spin(node)
    except KeyboardInterrupt:
        #This allows the program to exit cleanly. pressing ctrl + C for example          
        pass
    #destroys the node and then shuts down the ROS 2         
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
