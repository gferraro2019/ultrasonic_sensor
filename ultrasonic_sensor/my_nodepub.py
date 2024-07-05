import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from gpiozero import DistanceSensor


class MyNode(Node):

    def __init__(self):
        super().__init__("my_node")
        self.publisher_ = self.create_publisher(String, "chatter", 10)
        timer_period = 0.003  # seconds
        self.get_logger().info("Starting:")
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.sensor = DistanceSensor(echo=27, trigger=17)

    def timer_callback(self):
        distance= -1.0
        try:
            distance = self.sensor.distance * 100  # Measure distance and convert from meters to centimeters
        except:
            self.get_logger().warn("No measure")

        msg = String()
        msg.data = f"distance {distance}"
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    # Destroy the node explicitly
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    print("starting")
    main()
