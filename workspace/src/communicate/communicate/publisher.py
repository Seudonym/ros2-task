import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from interfaces.msg import Num1, Num2

class Publisher(Node):
    def __init__(self):
        super().__init__('publisher')

        self.publisher0 = self.create_publisher(String, 'node1', 10)
        self.publisher1 = self.create_publisher(Num1, 'data_twos', 10)
        self.publisher2 = self.create_publisher(Num2, 'data_fives', 10)

        self.timer = self.create_timer(1, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg0 = String()
        msg1 = Num1()
        msg2 = Num2()
        
        msg0.data = "hello"
        msg1.num1 = self.i * 2
        msg2.num2 = self.i * 5

        self.publisher0.publish(msg0)
        self.publisher1.publish(msg1)
        self.publisher2.publish(msg2)

        self.get_logger().info(f'Publisher0: {msg0.data}')
        self.get_logger().info(f'Publisher1: {msg1.num1}')
        self.get_logger().info(f'Publisher2: {msg2.num2}')

        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    publisher = Publisher()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()