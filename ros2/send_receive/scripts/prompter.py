#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from send_receive.srv import Service


class TemperaturePrompter(Node):
    def __init__(self):
        super().__init__('temperature_prompter')
        self.client = self.create_client(Service, 'get_temperature')

        self.get_logger().info('Waiting for temperature service...')
        while not self.client.wait_for_service(timeout_sec=1.0):
            pass

        self.get_logger().info('Calling service to get temperature...')
        self.send_request()

    def send_request(self):
        request = Service.Request()           # empty request
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        response = future.result()
        if response is not None:
            if response.success:
                print(f"\nTemperature: {response.temperature}°C")
                print(f"Message: {response.message}\n")
            else:
                print(f"\nService failed: {response.message}\n")
        else:
            print("\nService call failed (no response)\n")


def main(args=None):
    rclpy.init(args=args)
    node = TemperaturePrompter()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
