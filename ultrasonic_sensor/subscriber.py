import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class MySubscriber(Node):

    def __init__(self):
        super().__init__("my_subscriber")
        self.subscription = self.create_subscription(
            Float32, "chatter", self.listener_callback, 10
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%f"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    my_subscriber = MySubscriber()

    rclpy.spin(my_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    my_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
