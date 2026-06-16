#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from w1thermsensor import W1ThermSensor, SensorNotReadyError, NoSensorFoundError

from send_receive.srv import Service


class TemperatureServiceServer(Node):
    def __init__(self):
        super().__init__('temperature_service_server')
        self.srv = self.create_service(
            Service, 
            'get_temperature',
            self.service_callback
        )
        self.get_logger().info('Temperature service ready (/get_temperature)')

    def service_callback(self, request, response):
        try:
            sensor = W1ThermSensor()
            temp_c = sensor.get_temperature()
            
            response.temperature = round(temp_c, 2)
            response.success = True
            response.message = "OK"
            self.get_logger().info(f'Temperature: {response.temperature}°C')

        except NoSensorFoundError:
            response.temperature = 0.0
            response.success = False
            response.message = "No DS18B20 sensor found"
            self.get_logger().error(response.message)

        except SensorNotReadyError:
            response.temperature = 0.0
            response.success = False
            response.message = "Sensor not ready yet"
            self.get_logger().warn(response.message)

        except Exception as e:
            response.temperature = 0.0
            response.success = False
            response.message = f"Unexpected error: {str(e)}"
            self.get_logger().error(response.message)

        return response


def main(args=None):
    rclpy.init(args=args)
    node = TemperatureServiceServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
