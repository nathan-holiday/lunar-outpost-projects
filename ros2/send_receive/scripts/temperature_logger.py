#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from send_receive.srv import Service
import csv
import os
from datetime import datetime

class TemperatureLogger(Node):
    def __init__(self):
        super().__init__('temperature_logger')
        self.client = self.create_client(Service, 'get_temperature')
        
        # Wait for service
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for temperature service...')
        
        self.get_logger().info('Temperature logger started. Logging every 30 seconds.')
        
        # Create CSV file with header if it doesn't exist
        self.csv_file = 'temperature_log.csv'
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['timestamp', 'temperature_c'])
        
        # Call service every 30 seconds
        self.timer = self.create_timer(30.0, self.timer_callback)

    def timer_callback(self):
        request = Service.Request()
        future = self.client.call_async(request)
        future.add_done_callback(self.service_response_callback)

    def service_response_callback(self, future):
        try:
            response = future.result()
            if response.success:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                temp = response.temperature
                
                # Append to CSV
                with open(self.csv_file, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([timestamp, temp])
                
                self.get_logger().info(f'Logged: {temp}°C at {timestamp}')
            else:
                self.get_logger().warn(f'Service failed: {response.message}')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {str(e)}')


def main(args=None):
    rclpy.init(args=args)
    node = TemperatureLogger()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
